import reflex as rx

def nutri_home_view() -> rx.Component:
    """Vista para la página principal del nutriólogo."""
    return rx.container(
        rx.heading("Nutri Home", size="9", text_align="center", margin_top="2em"),
    )