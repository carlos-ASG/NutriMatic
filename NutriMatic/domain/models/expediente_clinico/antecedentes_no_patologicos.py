import reflex as rx
from sqlmodel import Field
from typing import Optional

class AntecedenteNoPatologico(rx.Model, table=True):
    """
    Representa los antecedentes no patológicos de un paciente.
    Corresponde a la tabla 'antecedentes_no_patologicos'.
    """
    anp_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    tipo_vivienda: Optional[str] = None  # tipo_vivienda_enum en la BD
    tiene_agua: Optional[bool] = None
    abuso_sustancias: Optional[str] = None
    horas_sueño: Optional[int] = None
    numero_habitaciones: Optional[int] = None
    frecuencia_actividad_fisica: Optional[str] = None  # tipo_frecuencia_actividad en la BD
    grupo_sanguineo: Optional[str] = None  # tipo_grupo_sanguineo en la BD