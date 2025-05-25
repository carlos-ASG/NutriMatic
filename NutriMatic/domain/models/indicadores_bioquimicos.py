from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IndicadoresBioquimicos(Base):
    __tablename__ = "indicadores_bioquimicos"
    ib_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    nombre_indicador = Column(String(50))
    valor = Column(Text)
    fecha_medicion = Column(Date)