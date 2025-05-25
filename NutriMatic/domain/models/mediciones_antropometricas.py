from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MedicionesAntropometricas(Base):
    __tablename__ = "mediciones_antropometricas"
    ma_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    peso_actual = Column(DECIMAL(5,2))
    peso_habitual = Column(DECIMAL(5,2))
    talla = Column(DECIMAL(3,2))
    imc = Column(DECIMAL(4,2))
    circ_brazo_relajado = Column(DECIMAL(4,2))
    circ_brazo_contraido = Column(DECIMAL(4,2))
    pliegue_triceps = Column(DECIMAL(4,2))
    circ_muslo = Column(DECIMAL(4,2))
    circ_cadera = Column(DECIMAL(4,2))
    circ_abdominal = Column(DECIMAL(4,2))
    circ_muñeca = Column(DECIMAL(4,2))
    circ_pantorrilla = Column(DECIMAL(4,2))
    diametro_humero = Column(DECIMAL(4,2))
    diametro_femur = Column(DECIMAL(4,2))
    circ_antebrazo = Column(DECIMAL(4,2))
    objetivo = Column(String(50))