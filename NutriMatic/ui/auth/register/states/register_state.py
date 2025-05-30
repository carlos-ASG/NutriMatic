import reflex as rx
from NutriMatic.data.respositories.auth_repository import AuthRepository

class RegisterState(rx.State):
    email: str = ""
    password: str = ""
    confirm_password: str = ""
    error_message: str = ""

    @rx.var
    def is_password_valid(self) -> bool:
        return self.password == self.confirm_password and len(self.password) >= 6

    @rx.event
    def register(self):
        if not self.is_password_valid:
            self.error_message = "Passwords do not match or are too short."
            return

        try:
            response = AuthRepository.sing_up(self.email, self.password)
            print(response)
            if response:
                self.error_message = response["error"]["message"]
            else:
                self.error_message = ""
                # Redirigir al usuario a la página de login después del registro exitoso
                return rx.redirect("/login")
        except Exception as e:
            self.error_message = str(e)