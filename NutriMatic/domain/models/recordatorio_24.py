from sqlalchemy import Column, Integer, Date, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Recordatorio24(Base):
    __tablename__ = "recordatorio_24"
    recordatorio_24_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    fecha_recordatorio = Column(Date)
    desayuno = Column(Text)
    colaciones = Column(Text)
    comida = Column(Text)
    cena = Column(Text)
    frutas = Column(Text)
    verduras = Column(Text)
    cereal_sg = Column(Text)
    cereal_cg = Column(Text)
    leguminosas = Column(Text)
    aoa_muy_bajo = Column(Text)
    aoa_bajo = Column(Text)
    aoa_moderado = Column(Text)
    aoa_alto = Column(Text)
    leche = Column(Text)
    aceites_sp = Column(Text)
    aceites_cp = Column(Text)
    azucar = Column(Text)
    kcal_totales = Column(DECIMAL(10,2))