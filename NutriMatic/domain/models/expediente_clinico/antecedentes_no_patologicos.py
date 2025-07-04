import reflex as rx
from sqlmodel import Field, Column
from sqlalchemy import Enum as SAEnum
from typing import Optional
from uuid import UUID
from .enums.tipo_vivienda import TipoVivienda
from .enums.tipo_frecuencia_actividad import TipoFrecuenciaActividad
from .enums.tipo_grupo_sanguineo import TipoGrupoSanguineo

class AntecedenteNoPatologico(rx.Model, table=True):
    """
    Representa los antecedentes no patológicos de un paciente.
    Corresponde a la tabla 'antecedentes_no_patologicos'.
    """
    anp_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[UUID] = Field(default=None, foreign_key="paciente.paciente_id")
    tipo_vivienda: Optional[TipoVivienda] = Field(default=None, sa_column=Column(SAEnum(TipoVivienda, name="tipo_vivienda_enum", create_type=False)))
    tiene_agua: Optional[bool] = None
    abuso_sustancias: Optional[str] = None
    horas_sueño: Optional[int] = None
    numero_habitaciones: Optional[int] = None
    frecuencia_actividad_fisica: Optional[TipoFrecuenciaActividad] = Field(default=None, sa_column=Column(SAEnum(TipoFrecuenciaActividad, name="tipo_frecuencia_actividad", create_type=False)))
    grupo_sanguineo: Optional[TipoGrupoSanguineo] = Field(default=None, sa_column=Column(SAEnum(TipoGrupoSanguineo, name="tipo_grupo_sanguineo", create_type=False)))