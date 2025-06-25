from dataclasses import dataclass
from NutriMatic.config.supabase_conection import supabase



async def sign_up(email: str, password: str, data: any) -> dict:
    response = supabase.auth.sign_up({
        "email": email,
        "password": password,
        "data": data
    })
    return response

async def sign_in(email: str, password: str) -> dict:
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
        })
    return response

async def logout(self) -> dict:
    """
    Log out the current user.
    """
    response = supabase.auth.sign_out()
    return response