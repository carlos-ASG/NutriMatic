import reflex as rx
from NutriMatic.ui.components.header import header

def expediente_clinico_view() -> rx.Component:
    """Vista para el expediente clínico del paciente."""
    return rx.vstack(
        # --- Encabezado ---
        header(),
        
        # --- Contenedor Principal ---
        rx.container(
            rx.vstack(
                    rx.vstack(
                    rx.heading("Expediente Clínico", size="4", text_align="center"),
                    justify="center",
                    align="center",
                    width="100%",
                ),
            ),
            # --- ESTILOS DEL CONTENEDOR PRINCIPAL (LA TARJETA BLANCA) ---
            background_color="white",
            padding="2rem",
            border_radius="12px",
            border="1px solid #e0e0e0",
            box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
            margin_top="8rem",
            margin_x="auto",    #  Centra el contenedor horizontalmente.
            width="65%",       
            max_width="90%", # Aumentado para hacerlo más grande.
        ),
    )