import reflex as rx
from sqlmodel import Field
from typing import Optional

class AparatosYSistemas(rx.Model, table=True):
    """
    Representa los síntomas por aparatos y sistemas de un paciente.
    Corresponde a la tabla 'sintomas_sistemas'.
    """
    ss_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    digestivo: Optional[str] = None
    cardiovascular: Optional[str] = None
    tegumentario: Optional[str] = None
    nervioso: Optional[str] = None
    urinario: Optional[str] = None
    reproductivo: Optional[str] = None