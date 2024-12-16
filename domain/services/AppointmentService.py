from ingenieriaSoftware1.domain.entities.cita import Cita
from ingenieriaSoftware1.domain.repositories.i_cita_repository import ICitaRepository

class AppointmentService:
    def __init__(self, cita_repository: ICitaRepository):
        # Inicializa el servicio con un repositorio de citas.
        self.cita_repository = cita_repository

    def verify_staff_availability(self, staff_id: int, date: str, time: str) -> bool:
        """Verifica la disponibilidad del personal médico para una cita."""
        # Lógica para verificar la disponibilidad
        # Se debe implementar en colaboración con el dominio.
        staff = self.staff_repository.find_by_id(staff_id)
        return staff.is_available(date, time)

    def assign_room(self, room_id: int, appointment_id: int) -> None:
        """Asigna una habitación a una cita específica."""
        appointment = self.cita_repository.find_by_id(appointment_id)
        if appointment.room_id:
            raise ValueError("La cita ya tiene una habitación asignada.")
        appointment.assign_room(room_id)
        self.cita_repository.save(appointment)
