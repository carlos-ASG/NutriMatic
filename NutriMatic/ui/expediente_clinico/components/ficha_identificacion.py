import reflex as rx
from NutriMatic.ui.expediente_clinico.components.input_field import input_field, select_field, form_section
from NutriMatic.domain.models.expediente_clinico import *
from NutriMatic.ui.expediente_clinico.state.expediente_clinico_state import PacienteState

def ficha_identificacion() -> rx.Component:
    """
    Componente de UI para el formulario de la Ficha de Identificación.
    No contiene lógica, solo se conecta al PacienteState.
    """
    return form_section(
        title="FICHA DE IDENTIFICACIÓN",
        date=rx.cond(
            PacienteState.paciente.fecha_creacion,
            PacienteState.paciente.fecha_creacion.to_string(), # Muestra la fecha si existe
            "Nueva Ficha"
        ),
        children=[
            input_field(
                "Nombre Completo",
                "Nombres y Apellidos",
                PacienteState.paciente.nombre_completo,
                lambda v: PacienteState.set_field("nombre_completo", v)
            ),
            
            select_field(
                "Género",
                "Seleccionar...",
                [g.value for g in TipoGenero],
                PacienteState.paciente.genero,
                lambda v: PacienteState.set_field("genero", v)
            ),
            select_field(
                "Estado Civil",
                "Seleccionar...",
                [e.c.value for e in TipoEstadoCivil],
                PacienteState.paciente.estado_civil,
                lambda v: PacienteState.set_field("estado_civil", v)
            ),
            input_field("Ocupación", "", PacienteState.paciente.ocupacion, lambda v: PacienteState.set_field("ocupacion", v)),
            input_field("Teléfono", "", PacienteState.paciente.telefono, lambda v: PacienteState.set_field("telefono", v)),
            input_field("Dirección", "", PacienteState.paciente.direccion, lambda v: PacienteState.set_field("direccion", v)),
            input_field("Nivel Educativo", "", PacienteState.paciente.nivel_educativo, lambda v: PacienteState.set_field("nivel_educativo", v)),

            # Botón de Guardar
            rx.box(
                rx.button("Guardar Paciente", on_click=PacienteState.save_paciente, size="3"),
                grid_column="span 2",
                style={"text_align": "right", "padding_top": "1rem"},
            ),
        ]
    )