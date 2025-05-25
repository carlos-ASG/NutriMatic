from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, Enum
from NutriMatic.domain.models.data_enums import TipoVivienda, TipoFrecuenciaActividad, TipoGrupoSanguineo
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AntecedenteNoPatologico(Base):
    __tablename__ = "antecedentes_no_patologicos"
    anp_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    tipo_vivienda = Column(Enum(TipoVivienda, name="tipo_vivienda_enum"))
    tiene_agua = Column(Boolean)
    abuso_sustancias = Column(Text)
    horas_sueño = Column(Integer)
    numero_habitaciones = Column(Integer)
    frecuencia_actividad_fisica = Column(Enum(TipoFrecuenciaActividad, name="tipo_frecuencia_actividad"))
    grupo_sanguineo = Column(Enum(TipoGrupoSanguineo, name="tipo_grupo_sanguineo"))