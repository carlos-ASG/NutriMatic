import reflex as rx


def index():
    return rx.vstack(
        rx.button(
            "Ir a Login",
            on_click=lambda: rx.redirect("/login"),
            size="3"
        ),
        align="center",
        justify="center",
        height="100vh"
    )