import reflex as rx
from sqlmodel import Field
from datetime import date
from typing import Optional

class Paciente(rx.Model, table=True):
    """
    Representa un paciente en la base de datos.
    Corresponde a la tabla 'pacientes'.
    """
    paciente_id: Optional[int] = Field(default=None, primary_key=True)
    nombre_completo: str
    fecha_nacimiento: Optional[date] = None
    genero: Optional[str] = None   # tipo_genero ENUM en la BD
    estado_civil: Optional[str] = None  # tipo_estado_civil ENUM en la BD
    ocupacion: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    nivel_educativo: Optional[str] = None
    fecha_creacion: Optional[date] = Field(default_factory=date.today)
    fecha_actualizacion: Optional[date] = Field(default_factory=date.today)