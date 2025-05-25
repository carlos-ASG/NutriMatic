from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CatalogoCondicionMedica(Base):
    __tablename__ = "catalogo_condiciones_medicas"
    condicion_id = Column(Integer, primary_key=True)
    nombre_condicion = Column(String(150), unique=True, nullable=False)
    descripcion = Column(Text)
    categoria = Column(String(50))