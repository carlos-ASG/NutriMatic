from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class LoginPacientes(Base):
    __tablename__ = "login_pacientes"
    login_paciente_id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    verificado = Column(Boolean, default=False)