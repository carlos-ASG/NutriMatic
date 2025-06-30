import reflex as rx
from NutriMatic.ui.components.header import header

def expediente_clinico_view() -> rx.Component:
    """Vista para el expediente clínico del paciente."""
    return rx.vstack(
        # --- Encabezado ---
        header(),
        
        # --- Contenedor Principal ---
        rx.container(
            
        ),
    )