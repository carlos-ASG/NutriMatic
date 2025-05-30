

class Alimentos():

    def __init__(self, id: int, nombre: str, grupo_alimento_id: int, cantidad_sugerida: str,
                 unidad: str, peso_bruto: float, peso_neto: float, energia: float,
                 proteina: float, hidratos_de_carbono: float, ag_saturados: float,
                 ag_monoinsaturados: float, ag_poliinsaturados: float, colesterol: float,
                 azucar: float, fibra: float, vitamina_a: float, acido_ascorbico: float,
                 calcio: float, hierro: float, potasio: float, sodio: float, fosforo: float,
                 etanol: float, indice_glucemico: float, carga_glicemica: float):
        self.id = id
        self.nombre = nombre
        self.grupo_alimento_id = grupo_alimento_id
        self.cantidad_sugerida = cantidad_sugerida
        self.unidad = unidad
        self.peso_bruto = peso_bruto
        self.peso_neto = peso_neto
        self.energia = energia
        self.proteina = proteina
        self.hidratos_de_carbono = hidratos_de_carbono
        self.ag_saturados = ag_saturados
        self.ag_monoinsaturados = ag_monoinsaturados
        self.ag_poliinsaturados = ag_poliinsaturados
        self.colesterol = colesterol
        self.azucar = azucar
        self.fibra = fibra
        self.vitamina_a = vitamina_a
        self.acido_ascorbico = acido_ascorbico
        self.calcio = calcio
        self.hierro = hierro
        self.potasio = potasio
        self.sodio = sodio
        self.fosforo = fosforo
        self.etanol = etanol
        self.indice_glucemico = indice_glucemico
        self.carga_glicemica = carga_glicemica

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            nombre=data.get('nombre'),
            grupo_alimento_id=data.get('grupo_alimento_id'),
            cantidad_sugerida=data.get('cantidad_sugerida'),
            unidad=data.get('unidad'),
            peso_bruto=float(data.get('peso_bruto', 0.0)),
            peso_neto=float(data.get('peso_neto', 0.0)),
            energia=float(data.get('energia', 0.0)),
            proteina=float(data.get('proteina', 0.0)),
            hidratos_de_carbono=float(data.get('hidratos_de_carbono', 0.0)),
            ag_saturados=float(data.get('ag_saturados', 0.0)),
            ag_monoinsaturados=float(data.get('ag_monoinsaturados', 0.0)),
            ag_poliinsaturados=float(data.get('ag_poliinsaturados', 0.0)),
            colesterol=float(data.get('colesterol', 0.0)),
            azucar=float(data.get('azucar', 0.0)),
            fibra=float(data.get('fibra', 0.0)),
            vitamina_a=float(data.get('vitamina_a', 0.0)),
            acido_ascorbico=float(data.get('acido_ascorbico', 0.0)),
            calcio=float(data.get('calcio', 0.0)),
            hierro=float(data.get('hierro', 0.0)),
            potasio=float(data.get('potasio', 0.0)),
            sodio=float(data.get('sodio', 0.0)),
            fosforo=float(data.get('fosforo', 0.0)),
            etanol=float(data.get('etanol', 0.0)),
            indice_glucemico=float(data.get('indice_glucemico', 0.0)),
            carga_glicemica=float(data.get('carga_glicemica', 0.0))
        )