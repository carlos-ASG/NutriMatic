from enum import Enum

class TipoFrecuenciaConsumo(Enum):
    DIARIA_VARIAS_VECES = "Diaria (varias veces)"
    DIARIA_UNA_VEZ = "Diaria (una vez)"
    SEMANAL_4_6_VECES = "Semanal (4-6 veces)"
    SEMANAL_1_3_VECES = "Semanal (1-3 veces)"
    QUINCENAL = "Quincenal"
    MENSUAL = "Mensual"
    OCASIONAL = "Ocasional"
    NUNCA = "Nunca"