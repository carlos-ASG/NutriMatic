import reflex as rx
from sqlmodel import Field
from typing import Optional
from datetime import datetime

class ExploracionFisica(rx.Model, table=True):
    """
    Representa la exploración física de un paciente.
    Corresponde a la tabla 'exploracion_fisica'.
    """
    ef_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    fecha_exploracion: Optional[datetime] = Field(default_factory=datetime.now)
    aspecto_general: Optional[str] = None
    ojos: Optional[str] = None
    cuello: Optional[str] = None
    vias_urinarias: Optional[str] = None
    cabello: Optional[str] = None
    cara: Optional[str] = None
    torax: Optional[str] = None
    miembros_superiores: Optional[str] = None
    piel: Optional[str] = None
    boca: Optional[str] = None
    muscular: Optional[str] = None
    miembros_inferiores: Optional[str] = None
    uñas: Optional[str] = None
    dientes: Optional[str] = None
    sistema_nervioso: Optional[str] = None
    ojeras: Optional[str] = None