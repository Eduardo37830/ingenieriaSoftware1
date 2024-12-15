from ingenieriaSoftware1.domain.entities.personalMedico import PersonalMedico
from datetime import datetime
from typing import List


class CitaService:
    def __init__(self, personal_medico_repository, habitacion_repository):
        self.personal_medico_repository = personal_medico_repository
        self.habitacion_repository = habitacion_repository

    def verificarDisponibilidadPersonal(self, idPersonalMedico: int, fecha: datetime, hora: str) -> bool:
        # Aquí consultaríamos la disponibilidad del personal médico
        personal = self.personal_medico_repository.obtenerPorId(idPersonalMedico)
        return personal.consultarDisponibilidad(fecha, hora)

    def asignarHabitacion(self, idHabitacion: int, idCita: int):
        # Asignar habitación a la cita
        habitacion = self.habitacion_repository.obtenerPorId(idHabitacion)
        habitacion.asignarAcomodacion(idPaciente=idCita)
