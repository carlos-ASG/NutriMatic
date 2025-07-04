import reflex as rx
from sqlmodel import Field
from typing import Optional
from uuid import UUID

class AntecedentePersonalPatologico(rx.Model, table=True):
    """
    Representa los antecedentes personales patológicos de un paciente.
    Corresponde a la tabla 'antecedentes_patologicos'.
    """
    app_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[UUID] = Field(default=None, foreign_key="paciente.paciente_id")
    cirugias_fracturas: Optional[str] = None
    medicamentos_actuales: Optional[str] = None
    transfusiones: Optional[bool]