import reflex as rx
from NutriMatic.ui.expediente_clinico.components.input_field import input_field, select_field, form_section, fecha_input
from NutriMatic.domain.models.expediente_clinico import *
from NutriMatic.ui.expediente_clinico.state.expediente_clinico_state import PacienteState
from NutriMatic.domain.models.expediente_clinico.enums.tipo_estado_civil import TipoEstadoCivil
from NutriMatic.domain.models.expediente_clinico.enums.tipo_genero import TipoGenero


def ficha_identificacion() -> rx.Component:
    return rx.vstack(

    )