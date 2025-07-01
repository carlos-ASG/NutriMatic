import reflex as rx
from sqlmodel import Field
from typing import Optional

class HabitosAlimentacion(rx.Model, table=True):
    """
    Representa los hábitos de alimentación de un paciente.
    Corresponde a la tabla 'habitos_alimentacion'.
    """
    ha_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: Optional[int] = Field(default=None, foreign_key="pacientes.paciente_id")
    num_comidas_casa_semana: Optional[int] = None
    num_comidas_fuera_semana: Optional[int] = None
    quien_prepara_alimentos_predominante: Optional[str] = None
    hora_mayor_apetito: Optional[str] = None  # tipo_hora_apetito ENUM en la BD
    apetito: Optional[str] = None             # tipo_apetito ENUM en la BD
    suplementos_descripcion: Optional[str] = None
    alergias_descripcion: Optional[str] = None
    intolerancias_descripcion: Optional[str] = None
    dietas_previas_existieron: Optional[bool] = None
    dietas_previas_descripcion: Optional[str] = None
    medicamentos_adelgazar_usados: Optional[bool] = None
    medicamentos_adelgazar_descripcion: Optional[str] = None
    alimentos_preferidos: Optional[str] = None
    alimentos_disgustan: Optional[str] = None
    consumo_agua_vasos_dia: Optional[int] = None
    notas_adicionales_habitos: Optional[str] = None