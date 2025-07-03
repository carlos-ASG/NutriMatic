import reflex as rx
from typing import List

# --- Componente reutilizable para un campo de texto ---
def input_field(label: str, placeholder: str, value: rx.Var, on_change: callable) -> rx.Component:
    """Crea un campo de entrada con una etiqueta y lo conecta al estado."""
    return rx.vstack(
        rx.text(label, size="2", weight="bold", color="#333"),
        rx.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            width="100%",
        ),
        align_items="start",
        spacing="1",
        width="100%",
    )

# --- Componente reutilizable para un menú desplegable ---
def select_field(label: str, placeholder: str, options: list[str], value: rx.Var, on_change: callable) -> rx.Component:
    """Crea un menú de selección con una etiqueta y lo conecta al estado."""
    return rx.vstack(
        rx.text(label, size="2", weight="bold", color="#333"),
        rx.select.root(
            rx.select.trigger(
                rx.select.value(placeholder=placeholder),
                width="100%",
            ),
            rx.select.content(
                rx.foreach(
                    options,
                    lambda option: rx.select.item(option, value=option)
                )
            ),
            value=value,
            on_change=on_change,
            width="100%",
        ),
        align_items="start",
        spacing="1",
        width="100%",
    )

# --- Componente reutilizable para una sección del formulario ---
def form_section(title: str, date: str, children: list[rx.Component]) -> rx.Component:
    """Crea una sección completa del formulario con título y contenido en una grilla."""
    return rx.vstack(
        rx.hstack(
            rx.heading(title, size="3", color="white", weight="bold"),
            rx.text(date, size="2", color="white"),
            justify="between",
            align="center",
            background_color="#40c6dc",
            padding="0.5rem 1rem",
            border_top_radius="8px",
        ),
        rx.grid(
            *children,
            columns=["1", "2"],
            spacing="4",
            width="100%",
            padding="1.5rem",
            background_color="#f8f9fa",
            border_bottom_radius="8px",
        ),
        width="100%",
        align_items="stretch",
        spacing="0",
        border="1px solid #ddd",
        border_radius="8px",
        box_shadow="0 1px 2px rgba(0,0,0,0.05)",
    )