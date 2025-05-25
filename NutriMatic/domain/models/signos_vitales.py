from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SignosVitales(Base):
    __tablename__ = "signos_vitales"
    sv_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    frecuencia_cardiaca = Column(Integer)
    frecuencia_respiratoria = Column(Integer)
    presion_sistolica = Column(Integer)
    presion_diastolica = Column(Integer)
    temperatura = Column(DECIMAL(4,1))
    fecha_medicion = Column(DateTime)