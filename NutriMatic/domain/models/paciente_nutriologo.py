from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PacienteNutriologo(Base):
    __tablename__ = "paciente_nutriologo"
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"), primary_key=True)
    nutriologo_id = Column(Integer, ForeignKey("nutriologo.nutriologo_id"), primary_key=True)