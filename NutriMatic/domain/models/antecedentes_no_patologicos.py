from NutriMatic.domain.models.data_enums import TipoVivienda, TipoFrecuenciaActividad, TipoGrupoSanguineo

class AntecedenteNoPatologico:
    def __init__(self, anp_id: int, paciente_id: int, tipo_vivienda: TipoVivienda = None,
                 tiene_agua: bool = None, abuso_sustancias: str = None, horas_sueño: int = None,
                 numero_habitaciones: int = None, frecuencia_actividad_fisica: TipoFrecuenciaActividad = None,
                 grupo_sanguineo: TipoGrupoSanguineo = None):
        self.anp_id = anp_id
        self.paciente_id = paciente_id
        self.tipo_vivienda = tipo_vivienda
        self.tiene_agua = tiene_agua
        self.abuso_sustancias = abuso_sustancias
        self.horas_sueño = horas_sueño
        self.numero_habitaciones = numero_habitaciones
        self.frecuencia_actividad_fisica = frecuencia_actividad_fisica
        self.grupo_sanguineo = grupo_sanguineo

    @classmethod
    def from_dict(cls, data: dict):
        # Helper para convertir string a Enum si es necesario
        tipo_vivienda_data = data.get('tipo_vivienda')
        if isinstance(tipo_vivienda_data, str):
            try:
                tipo_vivienda_obj = TipoVivienda(tipo_vivienda_data)
            except ValueError:
                tipo_vivienda_obj = None
        elif isinstance(tipo_vivienda_data, TipoVivienda):
            tipo_vivienda_obj = tipo_vivienda_data
        else:
            tipo_vivienda_obj = None

        frecuencia_actividad_data = data.get('frecuencia_actividad_fisica')
        if isinstance(frecuencia_actividad_data, str):
            try:
                frecuencia_actividad_obj = TipoFrecuenciaActividad(frecuencia_actividad_data)
            except ValueError:
                frecuencia_actividad_obj = None
        elif isinstance(frecuencia_actividad_data, TipoFrecuenciaActividad):
            frecuencia_actividad_obj = frecuencia_actividad_data
        else:
            frecuencia_actividad_obj = None

        grupo_sanguineo_data = data.get('grupo_sanguineo')
        if isinstance(grupo_sanguineo_data, str):
            try:
                grupo_sanguineo_obj = TipoGrupoSanguineo(grupo_sanguineo_data)
            except ValueError:
                grupo_sanguineo_obj = None
        elif isinstance(grupo_sanguineo_data, TipoGrupoSanguineo):
            grupo_sanguineo_obj = grupo_sanguineo_data
        else:
            grupo_sanguineo_obj = None

        return cls(
            anp_id=data.get('anp_id'),
            paciente_id=data.get('paciente_id'),
            tipo_vivienda=tipo_vivienda_obj,
            tiene_agua=data.get('tiene_agua'),
            abuso_sustancias=data.get('abuso_sustancias'),
            horas_sueño=data.get('horas_sueño'),
            numero_habitaciones=data.get('numero_habitaciones'),
            frecuencia_actividad_fisica=frecuencia_actividad_obj,
            grupo_sanguineo=grupo_sanguineo_obj
        )