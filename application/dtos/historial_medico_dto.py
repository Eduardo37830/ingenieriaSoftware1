from domain.entities.historialMedico import HistorialMedico

class HistorialMedicoDTO:
    def __init__(self, fecha, diagnostico, tratamiento, observaciones, medico_id, paciente_id):
        """
        Constructor del DTO de HistorialMedico.
        :param fecha: Fecha del historial médico.
        :param diagnostico: Diagnóstico realizado al paciente.
        :param tratamiento: Tratamiento prescrito.
        :param observaciones: Observaciones adicionales del médico.
        :param medico_id: ID del médico que atendió al paciente.
        :param paciente_id: ID del paciente asociado al historial médico.
        """
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.observaciones = observaciones
        self.medico_id = medico_id
        self.paciente_id = paciente_id

    def __repr__(self):
        """Representación en formato de cadena del DTO para facilitar la depuración."""
        return (f"HistorialMedicoDTO(fecha={self.fecha}, diagnostico='{self.diagnostico}', "
                f"tratamiento='{self.tratamiento}', observaciones='{self.observaciones}', "
                f"medico_id={self.medico_id}, paciente_id={self.paciente_id})")

    @staticmethod
    def from_entity(historial_medico: HistorialMedico) -> 'HistorialMedicoDTO':
        """
        Convierte una entidad HistorialMedico en un HistorialMedicoDTO.
        :param historial_medico: Instancia de la entidad HistorialMedico.
        :return: Instancia de HistorialMedicoDTO.
        """
        return HistorialMedicoDTO(
            fecha=historial_medico.fecha,
            diagnostico=historial_medico.diagnostico,
            tratamiento=historial_medico.tratamiento,
            observaciones=historial_medico.observaciones,
            medico_id=historial_medico.medico_id,
            paciente_id=historial_medico.paciente_id
        )

    def to_entity(self) -> HistorialMedico:
        """
        Convierte un HistorialMedicoDTO en una entidad HistorialMedico.
        :return: Instancia de HistorialMedico.
        """
        return HistorialMedico(
            fecha=self.fecha,
            diagnostico=self.diagnostico,
            tratamiento=self.tratamiento,
            observaciones=self.observaciones,
            medico_id=self.medico_id,
            paciente_id=self.paciente_id
        )

    def to_dict(self):
        """Convierte el DTO a un diccionario para su serialización en API u otros usos."""
        return {
            "fecha": self.fecha.strftime("%Y-%m-%d"),  # Formato de fecha (puedes ajustar según el formato necesario)
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento,
            "observaciones": self.observaciones,
            "medico_id": self.medico_id,
            "paciente_id": self.paciente_id
        }
