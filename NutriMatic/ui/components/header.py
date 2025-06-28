import reflex as rx

def header() -> rx.Component:
    """Header component for the NutriMatic application."""
    return rx.hstack(
        rx.hstack(
            rx.image( src="/NutriMatic_Only_Logo.png", width="50px",border_radius="50px" ),
            rx.heading("NutriMatic",size="6"),
            align="center", 
            spacing="4"
            ),rx.hstack(
                rx.link(
                    rx.text("Inicio", size="4"),
                    color="black",
                    text_decoration="none",
                    _hover={ "text_decoration": "underline"}
                ),
                rx.link(
                    rx.text("Desempeño", size="4"),
                    color="black",
                    text_decoration="none",
                    _hover={ "text_decoration": "underline"}  
                ),
                align="center",
                spacing="8", # Espacio entre los dos textos
            ),rx.icon(
                tag="menu", 
                size=36, 
                color="black",
                cursor="pointer",
                
            ),
            justify="between", # Distribuye el espacio entre los 3 grupos de elementos.
            align="center",          # Alinea verticalmente los elementos al centro.
            width="100%",            # Ocupa todo el ancho de la página.
            padding="1rem",          # Relleno interno para que no esté pegado a los bordes.
            border_bottom="1px solid #eaeaea", # Una línea sutil para separar el header.
            position="fixed",        # Fija el header en la parte superior.
            top="0px",
            background_color=" #40c6dc",
            z_index="9"            # Asegura que esté por encima de otro contenido. 
    ),
    