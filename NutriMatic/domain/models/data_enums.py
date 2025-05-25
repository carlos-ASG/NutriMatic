import enum

class TipoGenero(enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"

class TipoEstadoCivil(enum.Enum):
    Soltero = "Soltero/a"
    Casado = "Casado/a"
    Divorciado = "Divorciado/a"
    Viudo = "Viudo/a"
    UnionLibre = "Unión libre"
    Otro = "Otro"

class TipoFrecuenciaActividad(enum.Enum):
    Sedentario = "Sedentario"
    Ligera = "Ligera (1-2 días/sem)"
    Moderada = "Moderada (3-5 días/sem)"
    Intensa = "Intensa (6-7 días/sem)"
    MuyIntensa = "Muy intensa (Atleta)"

class TipoGrupoSanguineo(enum.Enum):
    A_pos = "A+"
    A_neg = "A-"
    B_pos = "B+"
    B_neg = "B-"
    AB_pos = "AB+"
    AB_neg = "AB-"
    O_pos = "O+"
    O_neg = "O-"
    Desconocido = "Desconocido"

class TipoApetito(enum.Enum):
    Bueno = "Bueno"
    Regular = "Regular"
    Malo = "Malo"
    Aumentado = "Aumentado"
    Disminuido = "Disminuido"

class TipoVivienda(enum.Enum):
    Rentada = "Rentada"
    Propia = "Propia"

class TipoGrupoAlimento(enum.Enum):
    Frutas = "Frutas"
    Verduras = "Verduras"
    CerealesSG = "Cereales s/g"
    CerealesCG = "Cereales c/g"
    Leguminosas = "Leguminosas"
    AOAMuyBajo = "AOA Muy Bajo"
    AOABajo = "AOA Bajo"
    AOAModerado = "AOA Moderado"
    AOAAlto = "AOA Alto"
    Leche = "Leche"
    AceitesSP = "Aceites s/p"
    AceitesCP = "Aceites c/p"
    Azucares = "Azúcares"
    BebidasAlcoholicas = "Bebidas Alcohólicas"
    BebidasAzucaradas = "Bebidas Azucaradas"
    AguaNatural = "Agua Natural"
    Otros = "Otros"

class TipoFrecuenciaConsumo(enum.Enum):
    DiariaVarias = "Diaria (varias veces)"
    DiariaUna = "Diaria (una vez)"
    Semanal46 = "Semanal (4-6 veces)"
    Semanal13 = "Semanal (1-3 veces)"
    Quincenal = "Quincenal"
    Mensual = "Mensual"
    Ocasional = "Ocasional"
    Nunca = "Nunca"

class TipoHoraApetito(enum.Enum):
    Manana = "Mañana"
    Mediodia = "Mediodía"
    Tarde = "Tarde"
    Noche = "Noche"
    Indiferente = "Indiferente"
    Variable = "Variable"