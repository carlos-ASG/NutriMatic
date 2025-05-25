from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SintomasSistemas(Base):
    __tablename__ = "sintomas_sistemas"
    ss_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    digestivo = Column(Text)
    cardiovascular = Column(Text)
    tegumentario = Column(Text)
    nervioso = Column(Text)
    urinario = Column(Text)
    reproductivo = Column(Text)