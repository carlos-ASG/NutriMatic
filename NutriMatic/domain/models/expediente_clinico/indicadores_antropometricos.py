import reflex as rx
from sqlmodel import Field
from typing import Optional

class IndicadoresAntropometricos(rx.Model, table=True):
    """
    Representa las mediciones antropométricas de un paciente.
    Corresponde a la tabla 'mediciones_antropometricas'.
    """
    ma_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    peso_actual: Optional[float] = None
    peso_habitual: Optional[float] = None
    talla: Optional[float] = None
    imc: Optional[float] = None
    circ_brazo_relajado: Optional[float] = None
    circ_brazo_contraido: Optional[float] = None
    pliegue_triceps: Optional[float] = None
    circ_muslo: Optional[float] = None
    circ_cadera: Optional[float] = None
    circ_abdominal: Optional[float] = None
    circ_muñeca: Optional[float] = None
    circ_pantorrilla: Optional[float] = None
    diametro_humero: Optional[float] = None
    diametro_femur: Optional[float] = None
    circ_antebrazo: Optional[float] = None
    objetivo: Optional[str] = None  # tipo_objetivo ENUM en la BD