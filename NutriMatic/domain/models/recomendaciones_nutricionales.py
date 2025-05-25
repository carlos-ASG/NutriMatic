from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RecomendacionesNutricionales(Base):
    __tablename__ = "recomendaciones_nutricionales"
    rn_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    recomendacion = Column(Text)
    fecha_recomendacion = Column(Date)