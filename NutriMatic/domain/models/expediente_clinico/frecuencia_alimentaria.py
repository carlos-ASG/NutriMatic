import reflex as rx
from sqlmodel import Field
from typing import Optional

class FrecuenciaAlimentaria(rx.Model, table=True):
    """
    Representa la frecuencia alimentaria de un paciente.
    Corresponde a la tabla 'frecuencia_alimentaria'.
    """
    fa_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    grupo_alimento: Optional[str] = None  # tipo_grupo_alimento ENUM en la BD
    frecuencia: Optional[str] = None      # tipo_frecuencia_consumo ENUM en la BD