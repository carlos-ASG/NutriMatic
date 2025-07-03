from enum import Enum

class TipoFrecuenciaActividad(Enum):
    SEDENTARIO = "Sedentario"
    LIGERA = "Ligera (1-2 días/sem)"
    MODERADA = "Moderada (3-5 días/sem)"
    INTENSA = "Intensa (6-7 días/sem)"
    MUY_INTENSA = "Muy intensa"