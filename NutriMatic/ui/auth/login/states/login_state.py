import reflex as rx
from NutriMatic.data.respositories.auth_repository import sign_in

class LoginState(rx.State):
    """State for the login form."""
    email: str = ""
    password: str = ""
    error_message: str = ""
    is_loading: bool = False

    async def handle_login(self):
        """Handle the login form submission."""
        self.is_loading = True
        self.error_message = ""
        try:
            response = await sign_in(email=self.email, password=self.password)
            if response.user:
                # Successful login, redirect to the main page
                return rx.redirect("/")
        except Exception as e:
            self.error_message = f"Login failed: {e}"
        finally:
            self.is_loading = False