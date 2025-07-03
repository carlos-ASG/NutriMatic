from enum import Enum

class TipoEstadoCivil(Enum):
    SOLTERO = "Soltero/a"
    CASADO = "Casado/a"
    DIVORCIADO = "Divorciado/a"
    VIUDO = "Viudo/a"
    UNION_LIBRE = "Unión libre"
    OTRO = "Otro"