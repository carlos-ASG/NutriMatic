from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HistoriaClinica(Base):
    __tablename__ = "historia_clinica"
    hc_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    nutriologo_id = Column(Integer, ForeignKey("nutriologo.nutriologo_id"))
    fecha_historia = Column(Date)