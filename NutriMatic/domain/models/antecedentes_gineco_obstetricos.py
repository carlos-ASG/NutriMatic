from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AntecedenteGinecoObstetrico(Base):
    __tablename__ = "antecedentes_gineco_obstetricos"
    ago_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    embarazos = Column(Integer)
    partos = Column(Integer)
    ultima_menstruacion = Column(Date)
    semanas_gestacion = Column(Integer)
    periodo_postparto = Column(Text)
    edad_menarquia = Column(Integer)
    anticonceptivos = Column(Text)