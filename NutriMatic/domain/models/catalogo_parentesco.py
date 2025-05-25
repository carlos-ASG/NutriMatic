from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CatalogoParentesco(Base):
    __tablename__ = "catalogo_parentescos"
    parentesco_id = Column(Integer, primary_key=True)
    nombre_parentesco = Column(String(50), unique=True, nullable=False)