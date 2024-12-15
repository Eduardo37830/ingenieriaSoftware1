class HistorialMedico:
    def __init__(self, date, diagnosis, treatment, observations, doctor):
        """
        Clase para representar una entrada en el historial médico de un paciente.
        :param date: Fecha de la consulta médica.
        :param diagnosis: Descripción del diagnóstico.
        :param treatment: Detalles del tratamiento.
        :param observations: Notas adicionales sobre la condición del paciente.
        :param doctor: Nombre del médico o identificador del personal médico.
        """
        self.date = date
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.observations = observations
        self.doctor = doctor

    def __str__(self):
        """
        Representación en texto de la entrada del historial médico.
        """
        return (
            f"Fecha: {self.date}\n"
            f"Diagnóstico: {self.diagnosis}\n"
            f"Tratamiento: {self.treatment}\n"
            f"Observaciones: {self.observations}\n"
            f"Médico: {self.doctor}\n"
        )
