from pydantic import BaseModel, Field
from typing import Dict, Any

class PacienteNutriologo(BaseModel):
    paciente_id: int = Field(..., description="ID del paciente, parte de la clave primaria compuesta")
    nutriologo_id: int = Field(..., description="ID del nutriólogo, parte de la clave primaria compuesta")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PacienteNutriologo":
        """
        Crea una instancia de PacienteNutriologo a partir de un diccionario.
        """
        return cls(**data)

    class Config:
        orm_mode = True
        # No hay enums en este modelo específico, pero use_enum_values
        # se puede mantener por consistencia si se desea.
        # use_enum_values = True