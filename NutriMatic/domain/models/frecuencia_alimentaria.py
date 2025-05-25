from sqlalchemy import Column, Integer, Enum, ForeignKey
from NutriMatic.domain.models.data_enums import TipoGrupoAlimento, TipoFrecuenciaConsumo
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FrecuenciaAlimentaria(Base):
    __tablename__ = "frecuencia_alimentaria"
    fa_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    grupo_alimento = Column(Enum(TipoGrupoAlimento, name="tipo_grupo_alimento"))
    frecuencia = Column(Enum(TipoFrecuenciaConsumo, name="tipo_frecuencia_consumo"))