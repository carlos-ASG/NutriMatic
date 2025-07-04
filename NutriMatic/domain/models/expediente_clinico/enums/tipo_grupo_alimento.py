from enum import Enum

class TipoGrupoAlimento(Enum):
    FRUTAS = "Frutas"
    VERDURAS = "Verduras"
    CEREALES_SG = "Cereales s/g"
    CEREALES_CG = "Cereales c/g"
    LEGUMINOSAS = "Leguminosas"
    AOA_MUY_BAJO = "AOA Muy Bajo"
    AOA_BAJO = "AOA Bajo"
    AOA_MODERADO = "AOA Moderado"
    AOA_ALTO = "AOA Alto"
    LECHE = "Leche"
    ACEITES_SP = "Aceites s/p"
    ACEITES_CP = "Aceites c/p"
    AZUCARES = "Azúcares"
    BEBIDAS_ALCOHOLICAS = "Bebidas Alcohólicas"
    BEBIDAS_AZUCARADAS = "Bebidas Azucaradas"
    AGUA_NATURAL = "Agua Natural"
    OTROS = "Otros"