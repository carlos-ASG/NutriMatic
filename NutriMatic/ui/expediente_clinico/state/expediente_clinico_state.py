import reflex as rx
from NutriMatic.domain.models.expediente_clinico import *
from NutriMatic.domain.models.expediente_clinico.paciente import Paciente

class PacienteState(rx.State):
    """
    Estado para manejar la carga, edición y guardado de la Ficha de Identificación
    de un único paciente.
    """
    paciente: Paciente = Paciente()

    # Evento para cargar los datos de un paciente desde la BD
    async def load_paciente(self, paciente_id: int):
        async with rx.session() as session:
            paciente_db = await session.get(Paciente, paciente_id)
            if paciente_db:
                yield self.set_paciente(paciente_db)
            else:
                print(f"No se encontró al paciente con ID: {paciente_id}")
                yield self.set_paciente(Paciente())

    # Evento para guardar los cambios en la BD
    async def save_paciente(self):
        """Guarda el objeto paciente actual en la base de datos."""
        async with rx.session() as session:
            # Añade el objeto paciente del estado a la sesión de la BD
            session.add(self.paciente)
            await session.commit()
            # Refresca el objeto para asegurar que tenemos los datos más recientes
            await session.refresh(self.paciente)
        
        print(f"¡Paciente '{self.paciente.nombre_completo}' guardado con éxito!")


    # Un evento genérico para actualizar los campos del formulario
    def set_field(self, field_name: str, value: str):
        """Actualiza un campo del objeto paciente en el estado."""
        # setattr es una función de Python que nos permite modificar un atributo por su nombre
        setattr(self.paciente, field_name, value)
