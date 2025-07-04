import reflex as rx
from NutriMatic.ui.auth.state.auth_state import AuthState

def signup_view() -> rx.Component:
    return rx.vstack(  # Contenedor principal para centrar
        rx.card(
            rx.vstack(
                rx.flex(
                    rx.heading(
                        "Registro de sesión",
                        size="6",
                        as_="h2",
                        width="100%",
                    ), rx.vstack(
                        #Imagen de logo
                    ),
                    rx.hstack(
                        rx.text(
                            "Ya tienes una cuenta?",
                            size="3",
                            text_align="left",
                        ),
                        rx.link("Inicio de sesión", href='/login', size="3"),
                        spacing="2",
                        opacity="0.8",
                        width="100%",
                    ),
                    justify="start",
                    direction="column",
                    spacing="4",
                    width="100%",
                ),
                rx.cond(
                    AuthState.error_message != "",
                    rx.callout(
                        AuthState.error_message,
                        icon="triangle_alert",
                        color_scheme="red",
                        role="alert",
                        width="100%",
                    )
                ),
                rx.vstack(
                    rx.text(
                        "Nombres",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="Luis Angel",
                        type="text",
                        size="3",
                        width="100%",
                        required=True,
                        aria_label="Nombres",
                        aria_required=True,
                        on_change=AuthState.set_nombre, # type: ignore
                    ),
                    spacing="2",
                    justify="start",
                    width="100%",
                ), rx.vstack(
                    rx.text(
                        "Apellidos",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="Rodriguez Cobian",
                        type="text",
                        size="3",
                        width="100%",
                        required=True,
                        aria_label="Apellidos",
                        aria_required=True,
                        on_change=AuthState.set_apellido, # type: ignore
                    ),
                    spacing="2",
                    justify="start",
                    width="100%",
                ),  rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Email",
                            size="3",
                            weight="medium",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("mail")),
                        placeholder="user@gmail.com",
                        type="email",
                        required=True,
                        aria_label="Email",
                        aria_required=True,
                        size="3",
                        width="100%",
                        on_change=AuthState.set_email, # type: ignore
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                        on_change=AuthState.set_password, # type: ignore
                    ),
                    spacing="2",
                    width="100%",
                ), 
                rx.button(
                    "Signup", 
                    size="3", 
                    width="100%", 
                    on_click=AuthState.handle_signup,  # type: ignore
                    loading=AuthState.loading
                ),
                rx.hstack(
                    rx.divider(margin="0"),
                    rx.text(
                        "Or continue with",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    rx.divider(margin="0"),
                    align="center",
                    width="100%",
                ),
                rx.center(
                    rx.icon_button(
                        rx.icon(tag="github"),
                        variant="soft",
                        size="3",
                    ),
                    rx.icon_button(
                        rx.icon(tag="facebook"),
                        variant="soft",
                        size="3",
                    ),
                    rx.icon_button(
                        rx.icon(tag="twitter"),
                        variant="soft",
                        size="3",
                    ),
                    spacing="4",
                    direction="row",
                    width="100%",
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
        height="120vh",  # Ajustado para mejor visualización
        width="100%", # Ocupa todo el ancho de la ventana
        background="linear-gradient(to bottom, #ade7ab  0%, #40c6dc 100%)"
    )