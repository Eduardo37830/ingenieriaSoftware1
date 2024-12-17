from datetime import datetime
from typing import Optional
from domain.entities.cirugia import Cirugia

class CirugiaDTO:
    def __init__(self, id: Optional[int] = None, fecha_cirugia: datetime = None, tipo_cirugia: str = "",
                 id_paciente: int = None, id_habitacion: int = None, hora_cirugia: datetime = None):
        self.id = id
        self.fecha_cirugia = fecha_cirugia
        self.tipo_cirugia = tipo_cirugia
        self.id_paciente = id_paciente
        self.id_habitacion = id_habitacion
        self.hora_cirugia = hora_cirugia

    def __repr__(self):
        return (f"CirugiaDTO(id={self.id}, fecha_cirugia={self.fecha_cirugia}, tipo_cirugia='{self.tipo_cirugia}', "
                f"id_paciente={self.id_paciente}, id_habitacion={self.id_habitacion}, hora_cirugia={self.hora_cirugia})")

    @staticmethod
    def from_entity(cirugia) -> 'CirugiaDTO':
        """Convierte una entidad Cirugia en un CirugiaDTO."""
        return CirugiaDTO(
            id=cirugia.id,
            fecha_cirugia=cirugia.fecha_cirugia,
            tipo_cirugia=cirugia.tipo_cirugia,
            id_paciente=cirugia.id_paciente,
            id_habitacion=cirugia.id_habitacion,
            hora_cirugia=cirugia.hora_cirugia
        )

    def to_entity(self) -> Cirugia:
        """Convierte un CirugiaDTO en una entidad Cirugia."""
        return Cirugia(
            id=self.id,
            fecha_cirugia=self.fecha_cirugia,
            tipo_cirugia=self.tipo_cirugia,
            id_paciente=self.id_paciente,
            id_habitacion=self.id_habitacion,
            hora_cirugia=self.hora_cirugia
        )
