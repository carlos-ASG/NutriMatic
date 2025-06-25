import reflex as rx
from supabase import create_client, Client, AuthSession
from NutriMatic.data.respositories.auth_repository import *
from typing import Optional

# Obtenemos la configuración de rxconfig
from rxconfig import config

class AuthState(rx.State):
    """Maneja la autenticación del usuario con Supabase."""
    
    session: Optional[AuthSession] = None
    
    # Inputs del formulario de login
    email: str = ""
    password: str = ""
    loading: bool = False

    def on_load(self):
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
            self.session = None

    @rx.var
    def supabase_client(self) -> Client:
        """Inicializa y devuelve el cliente de Supabase."""
        return create_client(config.supabase_url, config.supabase_key)
        
    @rx.var
    def is_authenticated(self) -> bool:
        """Verifica si el usuario está autenticado."""
        return self.session is not None and self.session.user is not None

    async def handle_login(self):
        """Maneja el inicio de sesión."""
        self.loading = True
        try:
            response = self.supabase_client.auth.sign_in_with_password({
                "email": self.email,
                "password": self.password,
            })
            # La sesión se guarda en las cookies del navegador automáticamente
            # por el cliente de Supabase.
            self.session = response.session
            return rx.redirect("/dashboard")
        except Exception as e:
            print(f"Error en login: {e}") # Opcional: manejar errores en la UI
            self.password = ""
        finally:
            self.loading = False
            
    def handle_logout(self):
        """Maneja el cierre de sesión."""
        self.supabase_client.auth.sign_out()
        self.session = None
        return rx.redirect("/")