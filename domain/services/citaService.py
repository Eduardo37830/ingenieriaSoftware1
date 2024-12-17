from domain.entities.personalMedico import PersonalMedico
from datetime import datetime
from typing import List


class CitaService:
    def __init__(self, personal_medico_repository, habitacion_repository):
        self.personal_medico_repository = personal_medico_repository
        self.habitacion_repository = habitacion_repository

    def verificarDisponibilidadPersonal(self, idPersonalMedico: int, fecha: datetime, hora: str) -> bool:
        personal = self.personal_medico_repository.obtenerPorId(idPersonalMedico)
        if not personal:
            raise ValueError(f"El personal médico con ID {idPersonalMedico} no existe.")
        return personal.consultarDisponibilidad(fecha, hora)

    def asignarHabitacion(self, idHabitacion: int, idCita: int):
        habitacion = self.habitacion_repository.obtenerPorId(idHabitacion)
        if not habitacion:
            raise ValueError(f"La habitación con ID {idHabitacion} no existe.")
        if not habitacion.estaDisponible():
            raise ValueError(f"La habitación con ID {idHabitacion} no está disponible.")
        habitacion.asignarAcomodacion(idCita=idCita)



