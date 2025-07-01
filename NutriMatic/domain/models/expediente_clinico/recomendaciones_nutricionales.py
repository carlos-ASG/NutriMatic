import reflex as rx
from sqlmodel import Field
from typing import Optional
from datetime import date

class RecomendacionNutricional(rx.Model, table=True):
    """
    Representa una recomendación nutricional de un paciente.
    Corresponde a la tabla 'recomendaciones_nutricionales'.
    """
    rn_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    recomendacion: Optional[str] = None
    #fecha_recomendacion: Optional[date] = Field(default_factory=date.today)