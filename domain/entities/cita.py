from datetime import datetime, date, time
from typing import Optional


class Cita:
    def __init__(self, id: int, motivoConsulta: str, fechaConsulta: datetime, horaConsulta: time,
                 paciente_id: int, personalMedico_id: int, costoTotal: float, habitacion_id: Optional[int] = None):
        """
        Clase para representar una cita médica.
        :param id: Identificador único de la cita.
        :param motivoConsulta: Motivo de la consulta.
        :param fechaConsulta: Fecha de la consulta (datetime).
        :param horaConsulta: Hora de la consulta (datetime).
        :param paciente_id: ID del paciente asociado.
        :param personalMedico_id: ID del personal médico asignado.
        :param costoTotal: Monto total a pagar por la consulta.
        :param habitacion_id: ID de la habitación asociada (opcional).
        """
        self.id = id
        self.motivoConsulta = motivoConsulta
        self.fechaConsulta = fechaConsulta.date() if isinstance(fechaConsulta, datetime) else fechaConsulta
        self.horaConsulta = horaConsulta if isinstance(horaConsulta, time) else horaConsulta
        self.paciente_id = paciente_id
        self.personalMedico_id = personalMedico_id
        self.costoTotal = costoTotal
        self.habitacion_id = habitacion_id

    def verificarConflicto(self, otra_cita) -> bool:
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

    def __repr__(self):
        """
        Representación de la cita para propósitos de depuración y listas.
        """
        return (f"Cita(id={self.id}, motivoConsulta='{self.motivoConsulta}', fechaConsulta={self.fechaConsulta}, "
                f"horaConsulta={self.horaConsulta}, paciente_id={self.paciente_id}, personalMedico_id={self.personalMedico_id}, "
                f"costoTotal={self.costoTotal}, habitacion_id={self.habitacion_id})")
