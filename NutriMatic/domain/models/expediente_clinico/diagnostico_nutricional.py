import reflex as rx
from sqlmodel import Field
from typing import Optional
from datetime import date

class DiagnosticoNutricional(rx.Model, table=True):
    """
    Representa el diagnóstico nutricional de un paciente.
    Corresponde a la tabla 'diagnostico_nutricional'.
    """
    dn_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    diagnostico: Optional[str] = None
    #fecha_diagnostico: Optional[date] = Field(default_factory=date.today)