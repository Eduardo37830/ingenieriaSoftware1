from domain.repositories.i_habitacion_repository import IhabitacionRepository
from application.dtos.habitacion_dto import HabitacionDTO
from application.exceptions.application_error import NotFoundError

class HabitacionApplicationService:
    def __init__(self, habitacion_repository: IhabitacionRepository):
        self.habitacion_repository = habitacion_repository

    def asignar_habitacion_a_cita(self, habitacion_id: int, cita_id: int) -> str:
        """Asigna una habitación a una cita si está disponible."""
        habitacion = self.habitacion_repository.find_by_id(habitacion_id)
        if not habitacion:
            raise NotFoundError(f"No se encontró una habitación con el ID {habitacion_id}")
        return habitacion.asignar_acomodacion(cita_id)

    def liberar_habitacion(self, habitacion_id: int) -> str:
        """Libera una habitación, haciendo que esté nuevamente disponible."""
        habitacion = self.habitacion_repository.find_by_id(habitacion_id)
        if not habitacion:
            raise NotFoundError(f"No se encontró una habitación con el ID {habitacion_id}")
        return habitacion.liberar_acomodacion()

    def obtener_habitacion_por_id(self, habitacion_id: int) -> HabitacionDTO:
        """Obtiene una habitación por su ID."""
        habitacion = self.habitacion_repository.find_by_id(habitacion_id)
        if not habitacion:
            raise NotFoundError(f"No se encontró una habitación con el ID {habitacion_id}")
        return HabitacionDTO.from_entity(habitacion)  # Convertir la entidad en DTO
