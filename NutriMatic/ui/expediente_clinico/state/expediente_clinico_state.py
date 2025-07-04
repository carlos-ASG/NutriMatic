import reflex as rx
from NutriMatic.domain.models.expediente_clinico import *
from NutriMatic.domain.models.expediente_clinico.paciente import Paciente
from NutriMatic.ui.expediente_clinico.components.ficha_identificacion import FichaIdentificacionState

class ExpedienteClinicoState(rx.State):
    """
    Estado para manejar la carga, edición y guardado de la Ficha de Identificación
    de un único paciente.
    """

    @rx.event
    async def handle_submit(self):
        """
        Orquesta el envío final.
        1. Recoge los diccionarios de cada sub-estado.
        2. Valida y "castea" los diccionarios a modelos rx.Model.
        3. Realiza una transacción de base de datos para guardar todo.
        """
        
        ficha_identificacion_data: Paciente = await self.get_var_value(FichaIdentificacionState.to_paciente_model)
        return rx.window_alert(f"Datos a guardar: {ficha_identificacion_data}")

