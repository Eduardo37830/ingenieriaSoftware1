from datetime import datetime


class Appointment:
    def __init__(self, id, reasonForConsultation, appointmentDateTime, patient_id, medicalStaff_id, totalFee, room_id=None):
        """
        Clase para representar una cita médica.
        :param id: Identificador único de la cita.
        :param reasonForConsultation: Motivo de la consulta.
        :param appointmentDateTime: Fecha y hora de la consulta (datetime).
        :param patient_id: ID del paciente asociado.
        :param medicalStaff_id: ID del personal médico asignado.
        :param totalFee: Monto total a pagar por la consulta.
        :param room_id: ID de la habitación asociada (opcional).
        """
        self.id = id
        self.reasonForConsultation = reasonForConsultation
        self.appointmentDateTime = appointmentDateTime
        self.totalFee = totalFee
        self.patient_id = patient_id
        self.medicalStaff_id = medicalStaff_id
        self.room_id = room_id

    def verificarConflicto(self, otra_cita):
        """
        Verifica si existe un conflicto de horarios con otra cita.
        :param otra_cita: Instancia de otra cita con la que se comparará.
        :return: True si hay conflicto, False en caso contrario.
        """
        # Verificar si el mismo paciente o personal médico está involucrado en ambas citas
        if self.patient_id == otra_cita.patient_id or self.medicalStaff_id == otra_cita.medicalStaff_id:
            # Comparar fechas y horas exactas de las citas
            if self.appointmentDateTime == otra_cita.appointmentDateTime:
                return True  # Conflicto detectado

        return False  # No hay conflicto

    def __str__(self):
        """
        Representación en texto de una cita médica.
        """
        return (
            f"Cita ID: {self.id}\n"
            f"Motivo: {self.reasonForConsultation}\n"
            f"Fecha y Hora: {self.appointmentDateTime}\n"
            f"Paciente ID: {self.patient_id}\n"
            f"Médico ID: {self.medicalStaff_id}\n"
            f"Habitación ID: {self.room_id}\n"
            f"Total a Pagar: {self.totalFee}\n"
        )
