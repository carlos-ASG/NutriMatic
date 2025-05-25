from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CatalogoPatologia(Base):
    __tablename__ = "catalogo_patologias"
    patologia_id = Column(Integer, primary_key=True)
    nombre_patologia = Column(String(150), unique=True, nullable=False)
    codigo_cie10 = Column(String(10), unique=True)
    descripcion = Column(Text)
    categoria = Column(String(50))