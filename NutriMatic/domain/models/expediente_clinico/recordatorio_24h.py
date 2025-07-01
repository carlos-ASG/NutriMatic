import reflex as rx
from sqlmodel import Field
from typing import Optional
from datetime import date

class Recordatorio24h(rx.Model, table=True):
    """
    Representa el recordatorio de 24 horas de un paciente.
    Corresponde a la tabla 'recordatorio_24'.
    """
    recordatorio_24_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    fecha_recordatorio: Optional[date] = Field(default_factory=date.today)
    desayuno: Optional[str] = None
    colaciones: Optional[str] = None
    comida: Optional[str] = None
    cena: Optional[str] = None
    frutas: Optional[str] = None
    verduras: Optional[str] = None
    cereal_sg: Optional[str] = None
    cereal_cg: Optional[str] = None
    leguminosas: Optional[str] = None
    aoa_muy_bajo: Optional[str] = None
    aoa_bajo: Optional[str] = None
    aoa_moderado: Optional[str] = None
    aoa_alto: Optional[str] = None
    leche: Optional[str] = None
    aceites_sp: Optional[str] = None
    aceites_cp: Optional[str] = None
    azucar: Optional[str] = None
    kcal_totales: Optional[float] = None