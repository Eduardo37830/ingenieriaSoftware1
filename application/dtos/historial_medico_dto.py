from ingenieriaSoftware1.domain.entities.historial_medico import HistorialMedico

class HistorialMedicoDTO:
    def __init__(self, fecha, diagnostico, tratamiento, observaciones, medico_id, paciente_id):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.observaciones = observaciones
        self.medico_id = medico_id
        self.paciente_id = paciente_id

    def __repr__(self):
        return (f"HistorialMedicoDTO(fecha={self.fecha}, diagnostico='{self.diagnostico}', "
                f"tratamiento='{self.tratamiento}', observaciones='{self.observaciones}', "
                f"medico_id={self.medico_id}, paciente_id={self.paciente_id})")

    @staticmethod
    def from_entity(historial_medico: HistorialMedico) -> 'HistorialMedicoDTO':
        """Convierte una entidad HistorialMedico a HistorialMedicoDTO."""
        return HistorialMedicoDTO(
            fecha=historial_medico.fecha,
            diagnostico=historial_medico.diagnostico,
            tratamiento=historial_medico.tratamiento,
            observaciones=historial_medico.observaciones,
            medico_id=historial_medico.medico_id,
            paciente_id=historial_medico.paciente_id
        )

    def to_entity(self) -> HistorialMedico:
        """Convierte un HistorialMedicoDTO a entidad HistorialMedico."""
        return HistorialMedico(
            fecha=self.fecha,
            diagnostico=self.diagnostico,
            tratamiento=self.tratamiento,
            observaciones=self.observaciones,
            medico_id=self.medico_id,
            paciente_id=self.paciente_id
        )
