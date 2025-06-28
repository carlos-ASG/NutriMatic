-- Creación de Tipos ENUM
CREATE TYPE tipo_genero AS ENUM (
    'Masculino',
    'Femenino'
);

CREATE TYPE tipo_estado_civil AS ENUM (
    'Soltero/a',
    'Casado/a',
    'Divorciado/a',
    'Viudo/a',
    'Unión libre',
    'Otro'
);

CREATE TYPE tipo_frecuencia_actividad AS ENUM (
    'Sedentario',
    'Ligera (1-2 días/sem)',
    'Moderada (3-5 días/sem)',
    'Intensa (6-7 días/sem)',
    'Muy intensa (Atleta)'
);

CREATE TYPE tipo_grupo_sanguineo AS ENUM (
    'A+',
    'A-',
    'B+',
    'B-',
    'AB+',
    'AB-',
    'O+',
    'O-',
    'Desconocido'
);

CREATE TYPE tipo_apetito AS ENUM (
    'Bueno',
    'Regular',
    'Malo',
    'Aumentado',
    'Disminuido'
);

CREATE TYPE tipo_vivienda_enum AS ENUM (
    'Rentada',
    'Propia'
);

CREATE TYPE tipo_grupo_alimento AS ENUM (
    'Frutas',
    'Verduras',
    'Cereales s/g',
    'Cereales c/g',
    'Leguminosas',
    'AOA Muy Bajo',
    'AOA Bajo',
    'AOA Moderado',
    'AOA Alto',
    'Leche',
    'Aceites s/p',
    'Aceites c/p',
    'Azúcares',
    'Bebidas Alcohólicas',
    'Bebidas Azucaradas',
    'Agua Natural',
    'Otros'
);

CREATE TYPE tipo_frecuencia_consumo AS ENUM (
    'Diaria (varias veces)',
    'Diaria (una vez)',
    'Semanal (4-6 veces)',
    'Semanal (1-3 veces)',
    'Quincenal',
    'Mensual',
    'Ocasional',
    'Nunca'
);

CREATE TYPE tipo_hora_apetito AS ENUM (
    'Mañana',
    'Mediodía',
    'Tarde',
    'Noche',
    'Indiferente',
    'Variable'
);

-- Tablas

CREATE TABLE pacientes (
    paciente_id SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    genero tipo_genero,
    estado_civil tipo_estado_civil,
    ocupacion VARCHAR(50),
    telefono VARCHAR(15),
    direccion VARCHAR(200),
    nivel_educativo VARCHAR(50),
    fecha_creacion DATE DEFAULT CURRENT_DATE
);

CREATE TABLE catalogo_condiciones_medicas (
    condicion_id SERIAL PRIMARY KEY,
    nombre_condicion VARCHAR(150) NOT NULL UNIQUE,
    descripcion TEXT NULL,
    categoria VARCHAR(50) NULL
);

CREATE TABLE catalogo_parentescos (
    parentesco_id SERIAL PRIMARY KEY,
    nombre_parentesco VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE paciente_antecedentes_familiares (
    pac_ant_fam_id SERIAL PRIMARY KEY,
    paciente_id INTEGER NOT NULL REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    condicion_id INTEGER NOT NULL REFERENCES catalogo_condiciones_medicas(condicion_id) ON DELETE RESTRICT,
    parentesco_id INTEGER NOT NULL REFERENCES catalogo_parentescos(parentesco_id) ON DELETE RESTRICT,
    comentarios TEXT NULL,
    fecha_registro DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT uq_paciente_condicion_parentesco UNIQUE (paciente_id, condicion_id, parentesco_id)
);

CREATE TABLE antecedentes_no_patologicos (
    anp_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    tipo_vivienda tipo_vivienda_enum,
    tiene_agua BOOLEAN,
    abuso_sustancias TEXT,
    horas_sueño INTEGER,
    numero_habitaciones INTEGER,
    frecuencia_actividad_fisica tipo_frecuencia_actividad,
    grupo_sanguineo tipo_grupo_sanguineo
);

CREATE TABLE antecedentes_gineco_obstetricos (
    ago_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    embarazos INTEGER,
    partos INTEGER,
    ultima_menstruacion DATE,
    semanas_gestacion INTEGER,
    periodo_postparto TEXT,
    edad_menarquia INTEGER,
    anticonceptivos TEXT
);

CREATE TABLE catalogo_patologias (
    patologia_id SERIAL PRIMARY KEY,
    nombre_patologia VARCHAR(150) NOT NULL UNIQUE,
    codigo_cie10 VARCHAR(10) NULL UNIQUE,
    descripcion TEXT NULL,
    categoria VARCHAR(50) NULL
);

CREATE TABLE paciente_patologias_asignadas (
    paciente_id INTEGER NOT NULL REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    patologia_id INTEGER NOT NULL REFERENCES catalogo_patologias(patologia_id) ON DELETE RESTRICT,
    PRIMARY KEY (paciente_id, patologia_id)
);

CREATE TABLE antecedentes_patologicos (
    app_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    cirugias_fracturas TEXT,
    medicamentos_actuales TEXT,
    transfusiones BOOLEAN
);

CREATE TABLE sintomas_sistemas (
    ss_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    digestivo TEXT,
    cardiovascular TEXT,
    tegumentario TEXT,
    nervioso TEXT,
    urinario TEXT,
    reproductivo TEXT
);

CREATE TABLE signos_vitales (
    sv_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    frecuencia_cardiaca INTEGER,
    frecuencia_respiratoria INTEGER,
    presion_sistolica INTEGER,
    presion_diastolica INTEGER,
    temperatura DECIMAL(4,1),
    fecha_medicion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE exploracion_fisica (
    ef_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    fecha_exploracion TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    aspecto_general VARCHAR(50),
    ojos VARCHAR(50),
    cuello VARCHAR(50),
    vias_urinarias VARCHAR(50),
    cabello VARCHAR(50),
    cara VARCHAR(50),
    torax VARCHAR(50),
    miembros_superiores VARCHAR(50),
    piel VARCHAR(50),
    boca VARCHAR(50),
    muscular VARCHAR(50),
    miembros_inferiores VARCHAR(50),
    uñas VARCHAR(50),
    dientes VARCHAR(50),
    sistema_nervioso VARCHAR(50),
    ojeras VARCHAR(50)
);

CREATE TABLE mediciones_antropometricas (
    ma_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    peso_actual DECIMAL(5,2),
    peso_habitual DECIMAL(5,2),
    talla DECIMAL(3,2),
    imc DECIMAL(4,2),
    circ_brazo_relajado DECIMAL(4,2),
    circ_brazo_contraido DECIMAL(4,2),
    pliegue_triceps DECIMAL(4,2),
    circ_muslo DECIMAL(4,2),
    circ_cadera DECIMAL(4,2),
    circ_abdominal DECIMAL(4,2),
    circ_muñeca DECIMAL(4,2),
    circ_pantorrilla DECIMAL(4,2),
    diametro_humero DECIMAL(4,2),
    diametro_femur DECIMAL(4,2),
    circ_antebrazo DECIMAL(4,2),
    objetivo VARCHAR(50)
);

CREATE TABLE indicadores_bioquimicos (
    ib_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    nombre_indicador VARCHAR(50),
    valor TEXT,
    fecha_medicion DATE DEFAULT CURRENT_DATE
);

CREATE TABLE diagnostico_nutricional (
    dn_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    diagnostico TEXT,
    fecha_diagnostico DATE DEFAULT CURRENT_DATE
);

CREATE TABLE recomendaciones_nutricionales (
    rn_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    recomendacion TEXT,
    fecha_recomendacion DATE DEFAULT CURRENT_DATE
);

-- MODIFICADO: La tabla 'nutriologo' usa una PK 'nutriologo_id' para ser más descriptiva.
CREATE TABLE nutriologo (
    nutriologo_id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL
);

CREATE TABLE paciente_nutriologo (
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    nutriologo_id UUID REFERENCES nutriologo(nutriologo_id) ON DELETE CASCADE, -- CORREGIDO
    PRIMARY KEY (paciente_id, nutriologo_id)
);

CREATE TABLE historia_clinica (
    hc_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    nutriologo_id UUID REFERENCES nutriologo(nutriologo_id) ON DELETE SET NULL, -- CORREGIDO
    fecha_historia DATE DEFAULT CURRENT_DATE
);

CREATE TABLE frecuencia_alimentaria (
    fa_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    grupo_alimento tipo_grupo_alimento,
    frecuencia tipo_frecuencia_consumo
);

CREATE TABLE recordatorio_24 (
    recordatorio_24_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    fecha_recordatorio DATE DEFAULT CURRENT_DATE,
    desayuno TEXT,
    colaciones TEXT,
    comida TEXT,
    cena TEXT,
    frutas TEXT,
    verduras TEXT,
    cereal_sg TEXT,
    cereal_cg TEXT,
    leguminosas TEXT,
    aoa_muy_bajo TEXT,
    aoa_bajo TEXT,
    aoa_moderado TEXT,
    aoa_alto TEXT,
    leche TEXT,
    aceites_sp TEXT,
    aceites_cp TEXT,
    azucar TEXT,
    kcal_totales DECIMAL(10,2)
);

-- Tabla habitos_alimentacion (MODIFICADA)
CREATE TABLE habitos_alimentacion (
    ha_id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    num_comidas_casa_semana INTEGER NULL,
    num_comidas_fuera_semana INTEGER NULL,
    quien_prepara_alimentos_predominante VARCHAR(100) NULL, -- Podría ser un ENUM si la lista es fija
    hora_mayor_apetito tipo_hora_apetito,
    apetito tipo_apetito,
    suplementos_descripcion TEXT NULL,
    alergias_descripcion TEXT NULL,
    intolerancias_descripcion TEXT NULL,
    dietas_previas_existieron BOOLEAN NULL,
    dietas_previas_descripcion TEXT NULL,
    medicamentos_adelgazar_usados BOOLEAN NULL,
    medicamentos_adelgazar_descripcion TEXT NULL,
    alimentos_preferidos TEXT,
    alimentos_disgustan TEXT,
    consumo_agua_vasos_dia INTEGER NULL,
    notas_adicionales_habitos TEXT NULL -- Campo general para otras notas
);

-- ELIMINADO: Esta tabla ya no es necesaria, la autenticación se maneja con auth.users
-- y el perfil con la tabla 'nutriologo' vinculada;
/*
CREATE TABLE login_pacientes (
    login_paciente_id SERIAL PRIMARY KEY,
    paciente_id INTEGER NOT NULL UNIQUE REFERENCES pacientes(paciente_id) ON DELETE CASCADE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    verificado BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE login_nutriologos (
    login_nutriologo_id SERIAL PRIMARY KEY,
    nutriologo_id INTEGER NOT NULL UNIQUE REFERENCES nutriologo(nutriologo_id) ON DELETE CASCADE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    verificado BOOLEAN NOT NULL DEFAULT FALSE
);
*/

CREATE TABLE catalogo_grupos_alimentos (
    grupo_alimento_id SERIAL PRIMARY KEY,
    nombre_grupo VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT NULL
);

CREATE TABLE Alimentos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    grupo_alimento_id INTEGER REFERENCES catalogo_grupos_alimentos(grupo_alimento_id),
    cantidad_sugerida VARCHAR(50),
    unidad VARCHAR(50),
    peso_bruto DECIMAL(10,2),
    peso_neto DECIMAL(10,2),
    energia DECIMAL(10,2),
    proteina DECIMAL(10,2),
    hidratos_de_carbono DECIMAL(10,2),
    ag_saturados DECIMAL(10,3),
    ag_monoinsaturados DECIMAL(10,3),
    ag_poliinsaturados DECIMAL(10,3),
    colesterol DECIMAL(10,3),
    azucar DECIMAL(10,2),
    fibra DECIMAL(10,2),
    vitamina_a DECIMAL(10,3),
    acido_ascorbico DECIMAL(10,3),
    calcio DECIMAL(10,3),
    hierro DECIMAL(10,3),
    potasio DECIMAL(10,3),
    sodio DECIMAL(10,3),
    fosforo DECIMAL(10,3),
    etanol DECIMAL(10,2),
    indice_glucemico DECIMAL(5,1) NULL,
    carga_glicemica DECIMAL(5,1) NULL
);

-- Inserciones de ejemplo para catálogos
INSERT INTO catalogo_condiciones_medicas (nombre_condicion, categoria) VALUES
('Diabetes Mellitus Tipo 1', 'Endocrina'),
('Diabetes Mellitus Tipo 2', 'Endocrina'),
('Hipertensión Arterial', 'Cardiovascular'),
('Dislipidemia (Colesterol Alto)', 'Cardiovascular'),
('Obesidad', 'Metabólica'),
('Cáncer de Mama', 'Oncológica'),
('Otra Condición (especificar)', 'General')
ON CONFLICT (nombre_condicion) DO NOTHING;

INSERT INTO catalogo_parentescos (nombre_parentesco) VALUES
('Padre'), ('Madre'), ('Hermano/a'), ('Hijo/a'), ('Abuelo Paterno'), ('Abuela Paterna'),
('Abuelo Materno'), ('Abuela Materna'), ('Tío Paterno'), ('Tía Paterna'), ('Tío Materno'),
('Tía Materna'), ('Primo/a Hermano/a Paterno/a'), ('Primo/a Hermano/a Materno/a'), ('Otro (especificar)')
ON CONFLICT (nombre_parentesco) DO NOTHING;

INSERT INTO catalogo_grupos_alimentos (nombre_grupo) VALUES
('verduras'), ('frutas'), ('cereales sin grasa'), ('cereales con grasa'), ('leguminosas'),
('origen animal muy baja en grasa'), ('origen animal baja en grasa'), ('origen animal moderado en grasa'),
('origen animal alto en grasa'), ('leches descremada'), ('leche semi descremada'), ('leche entera'),
('leche con azúcar'), ('grasas sin proteína'), ('grasas con proteína'), ('azucares sin grasa'),
('azucares con grasa'), ('libres en energía'), ('bebidas alcohólicas')
ON CONFLICT (nombre_grupo) DO NOTHING;

INSERT INTO catalogo_patologias (nombre_patologia, codigo_cie10, categoria) VALUES
('Diabetes Mellitus Tipo 1', 'E10', 'Endocrina'),
('Diabetes Mellitus Tipo 2', 'E11', 'Endocrina'),
('Hipertensión Arterial Esencial', 'I10', 'Cardiovascular'),
('Dislipidemia Mixta', 'E78.2', 'Metabólica'),
('Obesidad debida a exceso de calorías', 'E66.0', 'Metabólica'),
('Anemia por deficiencia de hierro', 'D50', 'Hematológica'),
('Hipotiroidismo no especificado', 'E03.9', 'Endocrina'),
('Asma no especificada', 'J45.9', 'Respiratoria'),
('Enfermedad por Reflujo Gastroesofágico', 'K21', 'Gastroenterológica'),
('Cáncer (no especificado)', NULL, 'Oncológica'),
('Enfermedad Renal (no especificada)', NULL, 'Nefrológica')
ON CONFLICT (nombre_patologia) DO NOTHING;