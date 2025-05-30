from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Dict, Any
from data_enums import TipoGenero, TipoEstadoCivil
class Paciente(BaseModel):
    paciente_id: Optional[int] = Field(None, description="ID único del paciente")
    nombre_completo: str = Field(..., max_length=100, description="Nombre completo del paciente")
    fecha_nacimiento: Optional[date] = Field(None, description="Fecha de nacimiento del paciente")
    genero: Optional[TipoGenero] = Field(None, description="Género del paciente")
    estado_civil: Optional[TipoEstadoCivil] = Field(None, description="Estado civil del paciente")
    ocupacion: Optional[str] = Field(None, max_length=50, description="Ocupación del paciente")
    telefono: Optional[str] = Field(None, max_length=15, description="Teléfono del paciente")
    direccion: Optional[str] = Field(None, max_length=200, description="Dirección del paciente")
    nivel_educativo: Optional[str] = Field(None, max_length=50, description="Nivel educativo del paciente")
    fecha_creacion: Optional[date] = Field(None, description="Fecha de creación del registro")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Paciente":
        """
        Crea una instancia de Paciente a partir de un diccionario.
        """
        return cls(**data)

    class Config:
        orm_mode = True
        use_enum_values = True # Útil si los datos del dict vienen como valores de enum (ej. "Masculino")

