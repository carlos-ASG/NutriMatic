import reflex as rx
from sqlmodel import Field
from typing import Optional
from datetime import date
from uuid import UUID

class AntecedenteGinecoObstetrico(rx.Model, table=True):
    """
    Representa los antecedentes gineco-obstétricos de un paciente.
    Corresponde a la tabla 'antecedentes_gineco_obstetricos'.
    """
    ago_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[UUID] = Field(default=None, foreign_key="paciente.paciente_id")
    embarazos: Optional[int] = None
    partos: Optional[int] = None
    ultima_menstruacion: Optional[date] = None
    semanas_gestacion: Optional[int] = None
    periodo_postparto: Optional[str] = None
    edad_menarquia: Optional[int] = None
    anticonceptivos: Optional[str] = None  # tipo_anticonceptivos ENUM en la BD