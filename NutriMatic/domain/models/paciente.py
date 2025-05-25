from sqlalchemy import Column, Integer, String, Date, Enum
from NutriMatic.domain.models.data_enums import TipoGenero, TipoEstadoCivil
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = "pacientes"
    paciente_id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date)
    genero = Column(Enum(TipoGenero, name="tipo_genero"))
    estado_civil = Column(Enum(TipoEstadoCivil, name="tipo_estado_civil"))
    ocupacion = Column(String(50))
    telefono = Column(String(15))
    direccion = Column(String(200))
    nivel_educativo = Column(String(50))
    fecha_creacion = Column(Date)