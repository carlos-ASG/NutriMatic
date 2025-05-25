from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Alimentos(Base):
    __tablename__ = "Alimentos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    grupo_alimento_id = Column(Integer, ForeignKey("catalogo_grupos_alimentos.grupo_alimento_id"))
    cantidad_sugerida = Column(String(50))
    unidad = Column(String(50))
    peso_bruto = Column(DECIMAL(10,2))
    peso_neto = Column(DECIMAL(10,2))
    energia = Column(DECIMAL(10,2))
    proteina = Column(DECIMAL(10,2))
    hidratos_de_carbono = Column(DECIMAL(10,2))
    ag_saturados = Column(DECIMAL(10,3))
    ag_monoinsaturados = Column(DECIMAL(10,3))
    ag_poliinsaturados = Column(DECIMAL(10,3))
    colesterol = Column(DECIMAL(10,3))
    azucar = Column(DECIMAL(10,2))
    fibra = Column(DECIMAL(10,2))
    vitamina_a = Column(DECIMAL(10,3))
    acido_ascorbico = Column(DECIMAL(10,3))
    calcio = Column(DECIMAL(10,3))
    hierro = Column(DECIMAL(10,3))
    potasio = Column(DECIMAL(10,3))
    sodio = Column(DECIMAL(10,3))
    fosforo = Column(DECIMAL(10,3))
    etanol = Column(DECIMAL(10,2))
    indice_glucemico = Column(DECIMAL(5,1))
    carga_glicemica = Column(DECIMAL(5,1))