from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class Nutriologo(BaseModel):
    nutriologo_id: Optional[int] = Field(None, description="ID único del nutriólogo")
    nombre: str = Field(..., max_length=100, description="Nombre del nutriólogo")
    apellido: str = Field(..., max_length=100, description="Apellido del nutriólogo")
    celular: Optional[str] = Field(None, max_length=20, description="Número de celular del nutriólogo")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Nutriologo":
        """
        Crea una instancia de Nutriologo a partir de un diccionario.
        """
        return cls(**data)

    class Config:
        orm_mode = True
        use_enum_values = True # Aunque no hay enums aquí, es bueno para consistencia