import reflex as rx
from sqlmodel import Field
from datetime import date
from typing import Optional

class AntecedenteHeredoFamiliar(rx.Model, table=True):
    """
    Representa un antecedente heredofamiliar de un paciente.
    Corresponde a la tabla 'paciente_antecedentes_familiares'.
    """
    pac_ant_fam_id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: int  # FK a pacientes.paciente_id
    condicion_id: int  # FK a catalogo_condiciones_medicas.condicion_id
    parentesco_id: int  # FK a catalogo_parentescos.parentesco_id
    comentarios: Optional[str] = None
    fecha_registro: Optional[date] = Field(default_factory=date.today)