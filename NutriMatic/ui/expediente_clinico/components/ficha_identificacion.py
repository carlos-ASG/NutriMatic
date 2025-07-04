from datetime import date, datetime
import reflex as rx
from NutriMatic.ui.expediente_clinico.components.custom_inputs import input_field, select_field, form_section, fecha_input
from NutriMatic.domain.models.expediente_clinico.paciente import Paciente


class FichaIdentificacionState(rx.State):
    """
    Estado para manejar la información de la ficha de identificación del paciente.
    """
    nombre_completo: str
    fecha_nacimiento: str
    genero: str  # tipo_genero ENUM en la BD
    estado_civil: str# tipo_estado_civil ENUM en la BD
    ocupacion: str
    telefono: str
    direccion: str
    nivel_educativo: str

    @rx.var
    def to_paciente_model(self) -> Paciente:
        """Convierte los atributos del estado a un objeto Paciente."""
        fecha_nacimiento_obj = None
        if self.fecha_nacimiento:
            try:
                fecha_nacimiento_obj = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d").date()
            except ValueError:
                # Manejar el caso de que la fecha no esté en el formato esperado
                fecha_nacimiento_obj = None

        return Paciente(
            nombre_completo=self.nombre_completo,
            fecha_nacimiento=fecha_nacimiento_obj,
            genero=self.genero,
            estado_civil=self.estado_civil,
            ocupacion=self.ocupacion,
            telefono=self.telefono,
            direccion=self.direccion,
            nivel_educativo=self.nivel_educativo,
        )

def ficha_identificacion() -> rx.Component:
    return rx.vstack(
        form_section(
            title="Ficha de Identificacion",
            date= "hoy",
            children=[
                input_field(
                    label="Nombre completo",
                    placeholder="Ingrese los nombres del paciente",
                    on_change=FichaIdentificacionState.set_nombre_completo # type: ignore
                )
            ]
        )
    )