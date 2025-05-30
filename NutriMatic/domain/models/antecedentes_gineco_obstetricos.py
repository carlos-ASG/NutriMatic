from datetime import date


class AntecedenteGinecoObstetrico:

    def __init__(self, ago_id: int, paciente_id: int, embarazos: int = None,
                 partos: int = None, ultima_menstruacion: date = None,
                 semanas_gestacion: int = None, periodo_postparto: str = None,
                 edad_menarquia: int = None, anticonceptivos: str = None):
        self.ago_id = ago_id
        self.paciente_id = paciente_id
        self.embarazos = embarazos
        self.partos = partos
        self.ultima_menstruacion = ultima_menstruacion
        self.semanas_gestacion = semanas_gestacion
        self.periodo_postparto = periodo_postparto
        self.edad_menarquia = edad_menarquia
        self.anticonceptivos = anticonceptivos

    @classmethod
    def from_dict(cls, data: dict):
        # Helper para convertir string a date si es necesario
        ultima_menstruacion_data = data.get('ultima_menstruacion')
        if isinstance(ultima_menstruacion_data, str):
            try:
                ultima_menstruacion_obj = date.fromisoformat(ultima_menstruacion_data)
            except ValueError:
                ultima_menstruacion_obj = None # O manejar el error como prefieras
        elif isinstance(ultima_menstruacion_data, date):
            ultima_menstruacion_obj = ultima_menstruacion_data
        else:
            ultima_menstruacion_obj = None

        return cls(
            ago_id=data.get('ago_id'),
            paciente_id=data.get('paciente_id'),
            embarazos=data.get('embarazos'),
            partos=data.get('partos'),
            ultima_menstruacion=ultima_menstruacion_obj,
            semanas_gestacion=data.get('semanas_gestacion'),
            periodo_postparto=data.get('periodo_postparto'),
            edad_menarquia=data.get('edad_menarquia'),
            anticonceptivos=data.get('anticonceptivos')
        )