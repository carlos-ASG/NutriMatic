import reflex as rx
from uuid import UUID
from sqlmodel import Field

class Nutriologo(rx.Model, table=True):
    """
    Representa el perfil de un nutriólogo en la base de datos.
    La llave primaria 'nutriologo_id' se corresponde con el id del usuario
    en la tabla auth.users de Supabase.
    """
    nutriologo_id: UUID = Field(primary_key=True)
    nombre: str
    apellido: str