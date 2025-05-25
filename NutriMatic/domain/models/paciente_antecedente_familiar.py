from sqlalchemy import Column, Integer, Text, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PacienteAntecedenteFamiliar(Base):
    __tablename__ = "paciente_antecedentes_familiares"
    pac_ant_fam_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"), nullable=False)
    condicion_id = Column(Integer, ForeignKey("catalogo_condiciones_medicas.condicion_id"), nullable=False)
    parentesco_id = Column(Integer, ForeignKey("catalogo_parentescos.parentesco_id"), nullable=False)
    comentarios = Column(Text)
    fecha_registro = Column(Date)
    __table_args__ = (UniqueConstraint('paciente_id', 'condicion_id', 'parentesco_id', name='uq_paciente_condicion_parentesco'),)