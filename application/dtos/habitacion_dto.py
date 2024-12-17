from domain.entities.habitacion import Habitacion

class HabitacionDTO:
    def __init__(self, id: int, disponibilidad: bool, tipo_habitacion: str, capacidad: int, cita_asignada: int = None):
        self.id = id
        self.disponibilidad = disponibilidad
        self.tipo_habitacion = tipo_habitacion
        self.capacidad = capacidad
        self.cita_asignada = cita_asignada

    def __repr__(self):
        return (f"HabitacionDTO(id={self.id}, disponibilidad={self.disponibilidad}, tipo_habitacion='{self.tipo_habitacion}', "
                f"capacidad={self.capacidad}, cita_asignada={self.cita_asignada})")

    @staticmethod
    def from_entity(habitacion: Habitacion) -> 'HabitacionDTO':
        """Convierte una entidad Habitacion a HabitacionDTO."""
        return HabitacionDTO(
            id=habitacion.id,
            disponibilidad=habitacion.disponibilidad,
            tipo_habitacion=habitacion.tipo_habitacion,
            capacidad=habitacion.capacidad,
            cita_asignada=habitacion.cita_asignada
        )

    def to_entity(self) -> Habitacion:
        """Convierte un HabitacionDTO a entidad Habitacion."""
        return Habitacion(
            id=self.id,
            disponibilidad=self.disponibilidad,
            tipo_habitacion=self.tipo_habitacion,
            capacidad=self.capacidad
        )
