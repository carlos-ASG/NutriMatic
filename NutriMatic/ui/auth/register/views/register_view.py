import reflex as rx
from NutriMatic.ui.auth.register.states.register_state import RegisterState
from NutriMatic.ui.auth.register.states.register_state import RegisterState

def register_view() -> rx.Component:
    return rx.vstack(  # Contenedor principal para centrar
        rx.card(
            rx.vstack(
                rx.flex(
                    rx.heading(
                        "Register your account",
                        size="6",
                        as_="h2",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.text(
                            "Already have an account?",
                            size="3",
                            text_align="left",
                        ),
                        rx.link("Log in", href="/login", size="3"),  # Cambiado a "Log in"
                        spacing="2",
                        opacity="0.8",
                        width="100%",
                    ),
                    justify="start",
                    direction="column",
                    spacing="4",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="user@reflex.dev",
                        type="email",
                        size="3",
                        width="100%",
                        on_change=RegisterState.set_email,
                    ),
                    spacing="2",
                    justify="start",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                        on_change=RegisterState.set_password,
                    ),
                    rx.input(
                        placeholder="Confirm your password",
                        type="password",
                        size="3",
                        width="100%",
                        on_change=RegisterState.set_confirm_password,
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.text(RegisterState.error_message, color="red", size="3"),
                rx.button(
                    "Sign up",
                    size="3",
                    width="100%",
                    on_click=RegisterState.register,
                ),
                spacing="6",
                width="100%",
            ),
            size="4",
            max_width="28em",
            width="100%",
        ),
        align="center",  # Centra horizontalmente
        justify="center",  # Centra verticalmente
        height="100vh",  # Ocupa toda la altura de la ventana
        width="100%" # Ocupa todo el ancho de la ventana
    )