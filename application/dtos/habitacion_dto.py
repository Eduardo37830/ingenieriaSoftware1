from domain.entities.habitacion import Habitacion

class HabitacionDTO:
    def __init__(self, id: int, disponibilidad: bool, tipo_habitacion: str, capacidad: int, cita_asignada: int = None):
        """
        Constructor del DTO de Habitacion.
        :param id: Identificador único de la habitación.
        :param disponibilidad: Indica si la habitación está disponible (bool).
        :param tipo_habitacion: Tipo de habitación (por ejemplo, "Individual", "Doble").
        :param capacidad: Capacidad de la habitación (número de personas que puede acomodar).
        :param cita_asignada: ID de la cita asignada a esta habitación (opcional).
        """
        self.id = id
        self.disponibilidad = disponibilidad
        self.tipo_habitacion = tipo_habitacion
        self.capacidad = capacidad
        self.cita_asignada = cita_asignada

    def __repr__(self):
        """Representación en formato string del DTO para facilitar la depuración."""
        return (f"HabitacionDTO(id={self.id}, disponibilidad={self.disponibilidad}, "
                f"tipo_habitacion='{self.tipo_habitacion}', capacidad={self.capacidad}, "
                f"cita_asignada={self.cita_asignada})")

    @staticmethod
    def from_entity(habitacion: Habitacion) -> 'HabitacionDTO':
        """
        Convierte una entidad Habitacion en un HabitacionDTO.
        :param habitacion: Instancia de la entidad Habitacion.
        :return: Instancia de HabitacionDTO.
        """
        return HabitacionDTO(
            id=habitacion.id,
            disponibilidad=habitacion.disponibilidad,
            tipo_habitacion=habitacion.tipo_habitacion,
            capacidad=habitacion.capacidad,
            cita_asignada=habitacion.cita_asignada  # Aquí se puede pasar directamente
        )

    def to_entity(self) -> Habitacion:
        """
        Convierte un HabitacionDTO en una entidad Habitacion.
        :return: Instancia de Habitacion.
        """
        return Habitacion(
            id=self.id,
            disponibilidad=self.disponibilidad,
            tipo_habitacion=self.tipo_habitacion,
            capacidad=self.capacidad
        )

    def to_dict(self) -> dict:
        """Convierte el DTO a un diccionario para su serialización en API u otros usos."""
        return {
            "id": self.id,
            "disponibilidad": self.disponibilidad,
            "tipo_habitacion": self.tipo_habitacion,
            "capacidad": self.capacidad,
            "cita_asignada": self.cita_asignada
        }
