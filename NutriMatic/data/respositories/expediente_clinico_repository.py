import reflex as rx
from typing import Dict, Any, Optional, List
from sqlmodel import select

from NutriMatic.domain.models.expediente_clinico.paciente import Paciente
from NutriMatic.domain.models.expediente_clinico.antecedentes_patologicos import AntecedentePersonalPatologico
from NutriMatic.domain.models.expediente_clinico.antecedentes_no_patologicos import AntecedenteNoPatologico
from NutriMatic.domain.models.expediente_clinico.antecedentes_heredofamiliares import AntecedenteHeredoFamiliar
from NutriMatic.domain.models.expediente_clinico.antecedentes_gineco_obstetricos import AntecedenteGinecoObstetrico
from NutriMatic.domain.models.expediente_clinico.indicadores_antropometricos import IndicadoresAntropometricos
from NutriMatic.domain.models.expediente_clinico.indicadores_bioquimicos import IndicadorBioquimico
from NutriMatic.domain.models.expediente_clinico.signos_vitales import SignosVitales
from NutriMatic.domain.models.expediente_clinico.exploracion_fisica import ExploracionFisica
from NutriMatic.domain.models.expediente_clinico.aparatos_y_sistemas import AparatosYSistemas
from NutriMatic.domain.models.expediente_clinico.habitos_de_alimentacion import HabitosAlimentacion
from NutriMatic.domain.models.expediente_clinico.recordatorio_24h import Recordatorio24h
from NutriMatic.domain.models.expediente_clinico.frecuencia_alimentaria import FrecuenciaAlimentaria
from NutriMatic.domain.models.expediente_clinico.diagnostico_nutricional import DiagnosticoNutricional
from NutriMatic.domain.models.expediente_clinico.recomendaciones_nutricionales import RecomendacionNutricional


class ExpedienteClinicoRepository:
    """
    Repositorio para gestionar las operaciones CRUD de todo el expediente clínico.
    """

    def create_expediente_completo(self, paciente: Paciente) -> Paciente:
        """
        Crea un nuevo paciente y todos los registros asociados a su expediente clínico.
        """
        with rx.session() as session:
            # 1. Guardar el paciente para obtener su ID
            session.add(paciente)
            session.commit()
            session.refresh(paciente)
            
            paciente_id = paciente.paciente_id

            # 2. Crear instancias de todos los modelos relacionados con el ID del paciente
            modelos_a_crear = [
                AntecedentePersonalPatologico(paciente_id=paciente_id, transfusiones=None),
                AntecedenteNoPatologico(paciente_id=paciente_id),
                AntecedenteGinecoObstetrico(paciente_id=paciente_id),
                IndicadoresAntropometricos(paciente_id=paciente_id),
                SignosVitales(paciente_id=paciente_id),
                ExploracionFisica(paciente_id=paciente_id),
                AparatosYSistemas(paciente_id=paciente_id),
                HabitosAlimentacion(paciente_id=paciente_id),
                Recordatorio24h(paciente_id=paciente_id),
                # Los modelos con registros múltiples (como antecedentes heredofamiliares)
                # se añadirán por separado cuando se tenga la información.
            ]
            
            session.add_all(modelos_a_crear)
            session.commit()
            
            return paciente

    def get_expediente_by_paciente_id(self, paciente_id: int) -> Optional[Dict[str, Any]]:
        """
        Obtiene el expediente completo de un paciente por su ID.
        """
        with rx.session() as session:
            paciente = session.get(Paciente, paciente_id)
            if not paciente:
                return None

            expediente: Dict[str, Any] = {"paciente": paciente}
            
            # Cargar cada parte del expediente que es una relación uno a uno
            expediente["antecedentes_patologicos"] = session.exec(select(AntecedentePersonalPatologico).where(AntecedentePersonalPatologico.paciente_id == paciente_id)).first()
            expediente["antecedentes_no_patologicos"] = session.exec(select(AntecedenteNoPatologico).where(AntecedenteNoPatologico.paciente_id == paciente_id)).first()
            expediente["antecedentes_gineco_obstetricos"] = session.exec(select(AntecedenteGinecoObstetrico).where(AntecedenteGinecoObstetrico.paciente_id == paciente_id)).first()
            expediente["indicadores_antropometricos"] = session.exec(select(IndicadoresAntropometricos).where(IndicadoresAntropometricos.paciente_id == paciente_id)).first()
            expediente["signos_vitales"] = session.exec(select(SignosVitales).where(SignosVitales.paciente_id == paciente_id)).first()
            expediente["exploracion_fisica"] = session.exec(select(ExploracionFisica).where(ExploracionFisica.paciente_id == paciente_id)).first()
            expediente["aparatos_y_sistemas"] = session.exec(select(AparatosYSistemas).where(AparatosYSistemas.paciente_id == paciente_id)).first()
            expediente["habitos_de_alimentacion"] = session.exec(select(HabitosAlimentacion).where(HabitosAlimentacion.paciente_id == paciente_id)).first()
            expediente["recordatorio_24h"] = session.exec(select(Recordatorio24h).where(Recordatorio24h.paciente_id == paciente_id)).first()

            # Cargar las secciones que pueden tener múltiples registros (uno a muchos)
            expediente["antecedentes_heredofamiliares"] = session.exec(select(AntecedenteHeredoFamiliar).where(AntecedenteHeredoFamiliar.paciente_id == paciente_id)).all()
            expediente["indicadores_bioquimicos"] = session.exec(select(IndicadorBioquimico).where(IndicadorBioquimico.paciente_id == paciente_id)).all()
            expediente["frecuencia_alimentaria"] = session.exec(select(FrecuenciaAlimentaria).where(FrecuenciaAlimentaria.paciente_id == paciente_id)).all()
            expediente["diagnostico_nutricional"] = session.exec(select(DiagnosticoNutricional).where(DiagnosticoNutricional.paciente_id == paciente_id)).all()
            expediente["recomendaciones_nutricionales"] = session.exec(select(RecomendacionNutricional).where(RecomendacionNutricional.paciente_id == paciente_id)).all()

            return expediente

    def update_seccion_expediente(self, seccion: rx.Model) -> rx.Model:
        """
        Actualiza una sección específica del expediente clínico en la base de datos.

        Args:
            seccion (rx.Model): Instancia del modelo de la sección del expediente clínico a actualizar.

        Returns:
            rx.Model: La instancia actualizada de la sección del expediente clínico.
        """
        with rx.session() as session:
            session.add(seccion)
            session.commit()
            session.refresh(seccion)
            return seccion

    def update_multiples_secciones(self, secciones: List[rx.Model]) -> List[rx.Model]:
        """
        Actualiza una lista de secciones del expediente clínico en una sola transacción.

        Args:
            secciones (List[rx.Model]): Lista de instancias de modelos a actualizar.

        Returns:
            List[rx.Model]: La lista de instancias actualizadas.
        """
        with rx.session() as session:
            session.add_all(secciones)
            session.commit()
            for seccion in secciones:
                session.refresh(seccion)
            return secciones

    def delete_expediente_completo(self, paciente_id: int) -> bool:
        """
        Elimina un paciente y todos sus registros asociados del expediente.
        """
        with rx.session() as session:
            paciente = session.get(Paciente, paciente_id)
            if not paciente:
                return False

            # Eliminar todos los registros hijos antes que el padre (Paciente)
            modelos_a_eliminar = [
                AntecedentePersonalPatologico, AntecedenteNoPatologico, AntecedenteGinecoObstetrico,
                IndicadoresAntropometricos, SignosVitales, ExploracionFisica, AparatosYSistemas,
                HabitosAlimentacion, Recordatorio24h, AntecedenteHeredoFamiliar, IndicadorBioquimico,
                FrecuenciaAlimentaria, DiagnosticoNutricional, RecomendacionNutricional
            ]

            for model in modelos_a_eliminar:
                statement = select(model).where(model.paciente_id == paciente_id)
                results = session.exec(statement).all()
                for row in results:
                    session.delete(row)
            
            session.delete(paciente)
            session.commit()
            return True