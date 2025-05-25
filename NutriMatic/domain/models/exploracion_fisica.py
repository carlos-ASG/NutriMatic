from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ExploracionFisica(Base):
    __tablename__ = "exploracion_fisica"
    ef_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    fecha_exploracion = Column(DateTime)
    aspecto_general = Column(String(50))
    ojos = Column(String(50))
    cuello = Column(String(50))
    vias_urinarias = Column(String(50))
    cabello = Column(String(50))
    cara = Column(String(50))
    torax = Column(String(50))
    miembros_superiores = Column(String(50))
    piel = Column(String(50))
    boca = Column(String(50))
    muscular = Column(String(50))
    miembros_inferiores = Column(String(50))
    uñas = Column(String(50))
    dientes = Column(String(50))
    sistema_nervioso = Column(String(50))
    ojeras = Column(String(50))