import reflex as rx

def nutri_home_view() -> rx.Component:
    """Vista para la página principal del nutriólogo."""
    return rx.vstack(
        rx.hstack(
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
        ),rx.container(
            rx.vstack(
                # --- Sección Superior: Buscador y Botón ---
                rx.hstack(
                    rx.input(
                        rx.input.slot(rx.icon("search")),
                        placeholder="Search...",
                        icon="search",
                        radius="full",
                        width="300px"
                    ),
                    rx.button(
                        "Agregar Paciente",
                        size="3",
                        border_radius="10px",
                        style={"cursor": "pointer", "color": "black"}
                    ),
                    justify="center",
                    spacing="9",
                    margin_x="auto", # Centra el buscador y botón
                    align="center",
                    width="100%"
                ),
                # --- Sección Inferior: Lista de Pacientes ---
                rx.vstack(
                    # Fila de ejemplo
                    rx.link(
                        rx.hstack(
                            rx.text("Luis Angel Rodriguez Cobian", weight="bold", href="#"),
                            # Para que se parezca a la imagen, quité el icono de 3 puntos por ahora
                            justify="between",
                            align="center",
                            width="100%",
                            background_color="#ade7ab",
                            border_radius="8px",
                        ),
                        # Usamos un f-string para crear una URL dinámica para cada paciente
                        #href=f"/pacientes/{patient_id}",
                        width="100%",
                        border_radius="8px",
                        background_color="#ade7ab",
                        padding="0.75rem 1rem",
                        text_decoration="none", # Quita el subrayado
                        color="inherit", 
                        transition="all 0.2s ease-in-out",
                        _hover={
                            "color": "inherit",
                            "transform": "translateY(-1px)",
                            "box_shadow": f"5px 5px 5px rgba(57, 255, 20, 0.7)",
                        }, # Cambia el color al pasar el mouse
                    ),
                    # Aquí puedes agregar más filas de pacientes en el futuro
                    #*[patient_row(f"Paciente de Ejemplo {i + 1}") for i in range(15)],
                    max_height="500px",
                    overflow_y="auto", #para tenga scroll si hay muchos pacientes
                    padding_right="0.5rem", # Espacio para el scroll
                    spacing="4",
                    width="80%", # Ancho de la lista de pacientes
                    margin_x="auto", # Centra la lista de pacientes
                ),
                # --- Espacio entre el buscador y la lista de pacientes ---
                spacing="6",
                width="100%"
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
    ),