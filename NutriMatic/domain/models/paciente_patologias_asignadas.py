from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PacientePatologiaAsignada(Base):
    __tablename__ = "paciente_patologias_asignadas"
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"), primary_key=True)
    patologia_id = Column(Integer, ForeignKey("catalogo_patologias.patologia_id"), primary_key=True)