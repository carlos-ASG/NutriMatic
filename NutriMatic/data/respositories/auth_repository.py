from NutriMatic.config import supabase

class AuthRepository:
    
    def sign_in_with_password(email: str, password:str):
        response = supabase.auth.sign_in_with_password(
                    {
                        "email": email, 
                        "password": password,
                    }
                )
        return response
    
    def sing_up(email: str, password:str):
        response = supabase.auth.sign_up(
                {
                    "email": email, 
                    "password": password,
                }
            )
        return response