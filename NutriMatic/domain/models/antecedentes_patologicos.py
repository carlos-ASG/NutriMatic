from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AntecedentePatologico(Base):
    __tablename__ = "antecedentes_patologicos"
    app_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    cirugias_fracturas = Column(Text)
    medicamentos_actuales = Column(Text)
    transfusiones = Column(Boolean)