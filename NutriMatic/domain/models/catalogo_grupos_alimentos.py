from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CatalogoGruposAlimentos(Base):
    __tablename__ = "catalogo_grupos_alimentos"
    grupo_alimento_id = Column(Integer, primary_key=True)
    nombre_grupo = Column(String(100), unique=True, nullable=False)
    descripcion = Column(Text)