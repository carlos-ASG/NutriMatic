from sqlalchemy import Column, Integer, Text, Boolean, String, Enum, ForeignKey
from NutriMatic.domain.models.data_enums import TipoHoraApetito, TipoApetito
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HabitosAlimentacion(Base):
    __tablename__ = "habitos_alimentacion"
    ha_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    num_comidas_casa_semana = Column(Integer)
    num_comidas_fuera_semana = Column(Integer)
    quien_prepara_alimentos_predominante = Column(String(100))
    hora_mayor_apetito = Column(Enum(TipoHoraApetito, name="tipo_hora_apetito"))
    apetito = Column(Enum(TipoApetito, name="tipo_apetito"))
    suplementos_descripcion = Column(Text)
    alergias_descripcion = Column(Text)
    intolerancias_descripcion = Column(Text)
    dietas_previas_existieron = Column(Boolean)
    dietas_previas_descripcion = Column(Text)
    medicamentos_adelgazar_usados = Column(Boolean)
    medicamentos_adelgazar_descripcion = Column(Text)
    alimentos_preferidos = Column(Text)
    alimentos_disgustan = Column(Text)
    consumo_agua_vasos_dia = Column(Integer)
    notas_adicionales_habitos = Column(Text)