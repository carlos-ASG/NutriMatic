import reflex as rx
from sqlmodel import Field
from typing import Optional
from datetime import datetime

class SignosVitales(rx.Model, table=True):
    """
    Representa los signos vitales de un paciente.
    Corresponde a la tabla 'signos_vitales'.
    """
    sv_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    frecuencia_cardiaca: Optional[int] = None
    frecuencia_respiratoria: Optional[int] = None
    presion_sistolica: Optional[int] = None
    presion_diastolica: Optional[int] = None
    temperatura: Optional[float] = None
    fecha_medicion: Optional[datetime] = Field(default_factory=datetime.now)