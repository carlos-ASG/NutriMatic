import reflex as rx
from sqlmodel import Field, Column
from sqlalchemy import Enum as SAEnum
from datetime import date
from typing import Optional
from uuid import UUID
from .enums.tipo_genero import TipoGenero
from .enums.tipo_estado_civil import TipoEstadoCivil

class Paciente(rx.Model, table=True):
    """
    Representa un paciente en la base de datos.
    La llave primaria 'paciente_id' se corresponde con el id del usuario
    en la tabla auth.users de Supabase.
    """
    paciente_id: UUID = Field(primary_key=True)
    nombre_completo: str
    fecha_nacimiento: Optional[date] = None
    genero: Optional[TipoGenero] = Field(default=None, sa_column=Column(SAEnum(TipoGenero, name="tipo_genero", create_type=False)))
    estado_civil: Optional[TipoEstadoCivil] = Field(default=None, sa_column=Column(SAEnum(TipoEstadoCivil, name="tipo_estado_civil", create_type=False)))
    ocupacion: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    nivel_educativo: Optional[str] = None
    fecha_creacion: Optional[date] = Field(default_factory=date.today)
    fecha_actualizacion: Optional[date] = Field(default_factory=date.today)