from gotrue import User
import reflex as rx
from NutriMatic.data.respositories.auth_repository import AuthRepository
from typing import Optional, Dict, Any
from NutriMatic.data.respositories.nutriologo_repository import NutriologoRepository
from NutriMatic.domain.models.nutriologo.nutriologo import Nutriologo

# Obtenemos la configuración de rxconfig
from rxconfig import config

class AuthState(rx.State):
    # No almacenes el objeto de sesión completo, ya que no es serializable.
    # En su lugar, almacena la información del usuario como un diccionario.
    user: dict | None = None
    nutriologo: Optional[Nutriologo] = None  # Nutriologo asociado al usuario, si aplica
    
    # Inputs para los formularios
    nombre: str = ""
    apellido: str = ""
    email: str = ""
    password: str = ""
    loading: bool = False
    error_message: str = ""

    def _clear_fields_and_error(self):
        """Resets input fields and error message."""
        self.email = ""
        self.password = ""
        self.nombre = ""
        self.apellido = ""
        self.error_message = ""



    @rx.var
    def is_authenticated(self) -> bool:
        """Verifica si el usuario está autenticado."""
        return self.user is not None

    async def check_auth(self):
        """
        Verifica si el usuario está autenticado al cargar una página protegida.
        Si no hay un usuario en el estado, intenta obtener la sesión.
        Si no hay sesión, redirige a la página de login.
        """
        if not self.is_authenticated:
            auth_repo = AuthRepository()
            try:
                response = await auth_repo.get_session()
                if response and response.user:
                    self.user = response.user.model_dump()
                    
                else:
                    # La redirección debe ser un evento que se retorna
                    return rx.redirect("/login")
            except Exception:
                return rx.redirect("/login")

    @rx.event
    async def handle_login(self):
        """Maneja el inicio de sesión."""
        self.loading = True
        self.error_message = ""  # Clear previous errors
        auth_repo = AuthRepository()  # Instancia el repositorio aquí.
        nutri_repo = NutriologoRepository()  # Instancia el repositorio de nutriologos aquí.
        try:
            response = await auth_repo.sign_in(
                email=self.email,
                password=self.password
            )
            # La sesión se guarda en las cookies del navegador automáticamente
            # por el cliente de Supabase.
            if response.session and response.session.user:
                self.user = response.session.user.model_dump()
                self._clear_fields_and_error()
                nutriologo = nutri_repo.get_nutriologo_by_uuid(self.user['id'])
                print(f"Nutriologo encontrado: {nutriologo}")
                return rx.redirect("/nutri-home")
        except Exception as e:
            self.error_message = "Credenciales inválidas. Por favor, inténtalo de nuevo."
            print(f"Error en login: {e}") # Opcional: manejar errores en la UI
            self.password = ""
        finally:
            self.loading = False

    @rx.event
    async def handle_signup(self):
        """
        Maneja el registro de un nuevo usuario.
        Si es exitoso, redirige a la página de login sin iniciar sesión.
        """
        self.loading = True
        self.error_message = ""  # Clear previous errors
        auth_repo = AuthRepository()
        try:
            # 1. Crear una instancia del modelo Nutriologo con los datos del formulario.
            nutriologo_data = Nutriologo(
                nombre=self.nombre,
                apellido=self.apellido
            )

            # 2. Llamar al método sign_up del repositorio.
            response = await auth_repo.sign_up(
                email=self.email,
                password=self.password,
                nutriologo=nutriologo_data
            )

            # 3. Si el usuario se creó (response.user no es None), redirigir a login.
            # No se guarda la sesión ni el usuario en el estado.
            if response.user:
                print("Registro exitoso. Por favor, inicie sesión.")
                self._clear_fields_and_error()
                return rx.redirect("/login")
            # Si response.user es None, la excepción probablemente ya se manejó
            # o se puede añadir un mensaje de error genérico aquí.

        except Exception as e:
            self.error_message = "No se pudo completar el registro. Verifica tus datos."
            # Idealmente, mostrar un error en la UI.
            print(f"Error en signup: {e}")
        finally:
            self.loading = False
    
    @rx.event
    async def handle_logout(self):
        """Maneja el cierre de sesión."""
        auth_repo = AuthRepository()  # Instancia el repositorio aquí.
        await auth_repo.logout()
        self.user = None
        return rx.redirect("/")
    
    @classmethod
    def from_supabase_user(cls, user: User):
        """
        Crea una instancia de AuthState a partir de un objeto User de Supabase.
        Esto es útil para restaurar el estado de autenticación en el cliente.
        """
        state = cls()
        state.user = user.model_dump()  # Almacena la información del usuario como un diccionario
        return state