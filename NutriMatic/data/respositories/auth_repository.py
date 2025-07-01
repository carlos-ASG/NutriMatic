from gotrue import AuthResponse
from supabase import Client
from NutriMatic.config.supabase_conection import supabase
from NutriMatic.domain.models.nutriologo.nutriologo import Nutriologo
import reflex as rx
from uuid import UUID

class AuthRepository:
    def __init__(self, supabase: Client = supabase):
        self.supabase = supabase

    async def sign_up(self,email: str, password: str, nutriologo: Nutriologo) -> AuthResponse:
        response = self.supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        # Si el registro en Supabase Auth es exitoso, creamos el perfil.
        if response.user:
            try:
                # Asignamos el UUID del usuario de Supabase al 'nutriologo_id' de nuestro modelo.
                nutriologo.nutriologo_id = UUID(response.user.id)
                
                # Usamos la sesión de Reflex para guardar el nuevo perfil en la BD.
                with rx.session() as session:
                    session.add(nutriologo)
                    session.commit()
            except Exception as e:
                # Opcional: Manejo de errores. Si esto falla, tenemos un usuario en
                # Supabase Auth sin un perfil en nuestra tabla.
                print(f"Error al insertar el perfil del nutriólogo: {e}")
                # Aquí se podría agregar lógica para eliminar el usuario de Supabase Auth
                # y mantener la consistencia. Por ahora, solo lo registramos.

        return response

    async def sign_in(self,email: str, password: str) -> AuthResponse:
        response = self.supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
            })
        return response

    async def logout(self) -> None:
        self.supabase.auth.sign_out()
