import reflex as rx
from sqlmodel import Field, Column
from sqlalchemy import Enum as SAEnum
from typing import Optional
from uuid import UUID
from .enums.tipo_grupo_alimento import TipoGrupoAlimento
from .enums.tipo_frecuencia_consumo import TipoFrecuenciaConsumo

class FrecuenciaAlimentaria(rx.Model, table=True):
    """
    Representa la frecuencia alimentaria de un paciente.
    Corresponde a la tabla 'frecuencia_alimentaria'.
    """
    fa_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[UUID] = Field(default=None, foreign_key="paciente.paciente_id")
    grupo_alimento: Optional[TipoGrupoAlimento] = Field(default=None, sa_column=Column(SAEnum(TipoGrupoAlimento, name="tipo_grupo_alimento", create_type=False)))
    frecuencia: Optional[TipoFrecuenciaConsumo] = Field(default=None, sa_column=Column(SAEnum(TipoFrecuenciaConsumo, name="tipo_frecuencia_consumo", create_type=False)))