from datetime import datetime, date, time

class Cita:
    def __init__(self, id, motivoConsulta, fechaConsulta, horaConsulta, paciente_id, personalMedico_id, costoTotal, habitacion_id=None):
        """
        Clase para representar una cita médica.
        :param id: Identificador único de la cita.
        :param motivoConsulta: Motivo de la consulta.
        :param fechaConsulta: Fecha de la consulta (YYYY-MM-DD).
        :param horaConsulta: Hora de la consulta (HH:MM:SS).
        :param paciente_id: ID del paciente asociado.
        :param personalMedico_id: ID del personal médico asignado.
        :param costoTotal: Monto total a pagar por la consulta.
        :param habitacion_id: ID de la habitación asociada (opcional).
        """
        self.id = id
        self.motivoConsulta = motivoConsulta
        self.fechaConsulta = datetime.strptime(fechaConsulta, "%Y-%m-%d").date() if isinstance(fechaConsulta, str) else fechaConsulta
        self.horaConsulta = datetime.strptime(horaConsulta, "%H:%M:%S").time() if isinstance(horaConsulta, str) else horaConsulta
        self.paciente_id = paciente_id
        self.personalMedico_id = personalMedico_id
        self.costoTotal = costoTotal
        self.habitacion_id = habitacion_id

    def verificarConflicto(self, otra_cita):
        """
        Verifica si existe un conflicto de horarios con otra cita.
        :param otra_cita: Instancia de otra cita con la que se comparará.
        :return: True si hay conflicto, False en caso contrario.
        """
        if self.paciente_id == otra_cita.paciente_id or self.personalMedico_id == otra_cita.personalMedico_id:
            if self.fechaConsulta == otra_cita.fechaConsulta and self.horaConsulta == otra_cita.horaConsulta:
                return True
        return False

    def __str__(self):
        """
        Representación en texto de una cita médica.
        """
        return (
            f"Cita ID: {self.id}\n"
            f"Motivo: {self.motivoConsulta}\n"
            f"Fecha: {self.fechaConsulta}\n"
            f"Hora: {self.horaConsulta}\n"
            f"Paciente ID: {self.paciente_id}\n"
            f"Médico ID: {self.personalMedico_id}\n"
            f"Habitación ID: {self.habitacion_id or 'N/A'}\n"
            f"Total a Pagar: {self.costoTotal}\n"
        )
