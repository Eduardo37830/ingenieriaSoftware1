class HistorialMedico:
    def __init__(self, fecha, diagnostico, tratamiento, observaciones, medico_id,paciente_id, id):
        """
        Clase para representar una entrada en el historial médico de un paciente.
        :param fecha: Fecha de la consulta médica.
        :param diagnostico: Descripción del diagnóstico.
        :param tratamiento: Detalles del tratamiento.
        :param observaciones: Notas adicionales sobre la condición del paciente.
        :param medico: Nombre del médico o identificador del personal médico.
        """
        self.id = id
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.observaciones = observaciones
        self.medico_id = medico_id  # Relacion con PersonalMedico por id
        self.paciente_id = paciente_id  # Relacion con Paciente por id

    def __str__(self):
        """
        Representación en texto de la entrada del historial médico.
        """
        return (
            f"Fecha: {self.fecha}\n"
            f"Diagnóstico: {self.diagnostico}\n"
            f"Tratamiento: {self.tratamiento}\n"
            f"Observaciones: {self.observaciones}\n"
            f"Médico: {self.medico_id}\n"
        )
