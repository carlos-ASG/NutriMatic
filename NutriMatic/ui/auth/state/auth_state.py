from gotrue import User
import reflex as rx
from NutriMatic.data.respositories.auth_repository import AuthRepository
from typing import Optional, Dict, Any
from NutriMatic.domain.models.nutriologo import Nutriologo

# Obtenemos la configuración de rxconfig
from rxconfig import config

class AuthState(rx.State):
    # No almacenes el objeto de sesión completo, ya que no es serializable.
    # En su lugar, almacena la información del usuario como un diccionario.
    user: Optional[Dict[str, Any]] = None
    
    # Inputs para los formularios
    nombre: str = ""
    apellido: str = ""
    email: str = ""
    password: str = ""
    loading: bool = False

    '''def on_load(self):
        """
        Este evento se ejecuta en cada carga de página.
        Verifica la sesión del usuario a partir de las cookies.
        """
        # Obtenemos el token de la cookie que Supabase guarda en el navegador
        token = self.router.page.cookies.get("sb-access-token")
        if token:
            try:
                # Validamos el token y actualizamos la sesión en el estado del backend
                self.session = self.supabase_client.auth.get_session()
            except Exception:
                # Si el token es inválido o expiró, reseteamos la sesión
                self.session = None
        else:
            self.session = None'''


    @rx.var
    def is_authenticated(self) -> bool:
        """Verifica si el usuario está autenticado."""
        return self.user is not None

    async def handle_login(self):
        """Maneja el inicio de sesión."""
        self.loading = True
        auth_repo = AuthRepository()  # Instancia el repositorio aquí.
        try:
            response = await auth_repo.sign_in(
                email=self.email,
                password=self.password
            )
            # La sesión se guarda en las cookies del navegador automáticamente
            # por el cliente de Supabase.
            if response.session and response.session.user:
                self.user = response.session.user.model_dump()
                return rx.redirect("/nutri-home")
        except Exception as e:
            print(f"Error en login: {e}") # Opcional: manejar errores en la UI
            self.password = ""
        finally:
            self.loading = False

    async def handle_signup(self):
        """
        Maneja el registro de un nuevo usuario.
        Si es exitoso, redirige a la página de login sin iniciar sesión.
        """
        self.loading = True
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
                return rx.redirect("/login")
            # Si response.user es None, la excepción probablemente ya se manejó
            # o se puede añadir un mensaje de error genérico aquí.

        except Exception as e:
            # Idealmente, mostrar un error en la UI.
            print(f"Error en signup: {e}")
        finally:
            self.loading = False
            
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