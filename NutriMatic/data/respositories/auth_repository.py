from gotrue import AuthResponse
from supabase import Client
from NutriMatic.config.supabase_conection import supabase

class AuthRepository:
    def __init__(self, supabase: Client = supabase):
        self.supabase = supabase

    async def sign_up(self,email: str, password: str) -> AuthResponse:
        response = self.supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        return response

    async def sign_in(self,email: str, password: str) -> AuthResponse:
        response = self.supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
            })
        return response

    async def logout(self) -> None:
        self.supabase.auth.sign_out()