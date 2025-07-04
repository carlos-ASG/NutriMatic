import reflex as rx
from typing import Optional
from uuid import UUID
from NutriMatic.domain.models.nutriologo.nutriologo import Nutriologo

class NutriologoRepository:
    """
    Repositorio para gestionar las operaciones de la base de datos
    relacionadas con el modelo Nutriologo.
    """

    def get_nutriologo_by_uuid(self, uuid_str: str) -> Optional[Nutriologo]:
        """
        Obtiene un nutriólogo de la base de datos por su UUID.

        Args:
            uuid_str: El UUID del nutriólogo en formato de cadena.

        Returns:
            Un objeto Nutriologo si se encuentra, de lo contrario None.
        """
        try:
            nutriologo_uuid = UUID(uuid_str)
            with rx.session() as session:
                return session.get(Nutriologo, nutriologo_uuid)
        except (ValueError, TypeError):
            # Retorna None si el string no es un UUID válido.
            return