from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DiagnosticoNutricional(Base):
    __tablename__ = "diagnostico_nutricional"
    dn_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    diagnostico = Column(Text)
    fecha_diagnostico = Column(Date)