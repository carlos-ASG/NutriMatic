import reflex as rx
from NutriMatic.ui.auth.state.auth_state import AuthState
from typing import Callable

def require_auth(page: Callable[[], rx.Component]) -> Callable[[], rx.Component]:
    """
    Un componente de orden superior que muestra la página solo si el usuario está autenticado.
    De lo contrario, muestra un spinner mientras se verifica la autenticación.
    La lógica de redirección se maneja en `AuthState.check_auth`.
    """
    def protected_page() -> rx.Component:
        return rx.fragment(
            rx.cond(
                AuthState.is_authenticated,
                page(),
                rx.center(
                    rx.spinner(size="3"),
                    height="100vh"
                )
            )
        )
    return protected_page