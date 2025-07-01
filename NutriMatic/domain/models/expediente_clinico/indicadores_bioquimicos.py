import reflex as rx
from sqlmodel import Field
from typing import Optional
from datetime import date

class IndicadorBioquimico(rx.Model, table=True):
    """
    Representa un indicador bioquímico de un paciente.
    Corresponde a la tabla 'indicadores_bioquimicos'.
    """
    ib_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    nombre_indicador: Optional[str] = None
    valor: Optional[str] = None
    #fecha_medicion: Optional[date] = Field(default_factory=date.today)