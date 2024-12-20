from datetime import datetime
from typing import Optional
from domain.entities.cirugia import Cirugia

class CirugiaDTO:
    def __init__(self, id: Optional[int] = None, fecha_cirugia: Optional[datetime] = None, tipo_cirugia: str = "",
                 id_paciente: Optional[int] = None, id_habitacion: Optional[int] = None, hora_cirugia: str = ""):
        """
        Constructor del DTO de Cirugia.
        :param id: Identificador único de la cirugía (opcional).
        :param fecha_cirugia: Fecha y hora de la cirugía (opcional, tipo datetime).
        :param tipo_cirugia: Tipo de cirugía realizada.
        :param id_paciente: ID del paciente asociado.
        :param id_habitacion: ID de la habitación asignada (opcional).
        :param hora_cirugia: Hora específica de la cirugía (formato string).
        """
        self.id = id
        self.fecha_cirugia = fecha_cirugia
        self.tipo_cirugia = tipo_cirugia
        self.id_paciente = id_paciente
        self.id_habitacion = id_habitacion
        self.hora_cirugia = hora_cirugia

    def __repr__(self):
        """Representación en string del DTO de Cirugia."""
        return (f"CirugiaDTO(id={self.id}, fecha_cirugia={self.fecha_cirugia}, tipo_cirugia='{self.tipo_cirugia}', "
                f"id_paciente={self.id_paciente}, id_habitacion={self.id_habitacion}, hora_cirugia='{self.hora_cirugia}')")

    @staticmethod
    def from_entity(cirugia: Cirugia) -> 'CirugiaDTO':
        """
        Convierte una entidad Cirugia en un DTO de Cirugia.
        :param cirugia: Entidad Cirugia.
        :return: CirugiaDTO.
        """
        return CirugiaDTO(
            id=cirugia.id,
            fecha_cirugia=cirugia.fecha_cirugia,
            tipo_cirugia=cirugia.tipo_cirugia,
            id_paciente=cirugia.id_paciente,
            id_habitacion=cirugia.id_habitacion,
            hora_cirugia=cirugia.hora_cirugia
        )

    def to_entity(self) -> Cirugia:
        """
        Convierte un DTO de Cirugia en una entidad Cirugia.
        :return: Entidad Cirugia.
        """
        return Cirugia(
            id=self.id,
            fecha_cirugia=self.fecha_cirugia,
            tipo_cirugia=self.tipo_cirugia,
            id_paciente=self.id_paciente,
            id_habitacion=self.id_habitacion,
            hora_cirugia=self.hora_cirugia
        )

    def to_dict(self):
        """Convierte el DTO en un diccionario para serialización, ideal para APIs."""
        return {
            "id": self.id,
            "fecha_cirugia": self.fecha_cirugia.strftime("%Y-%m-%d") if self.fecha_cirugia else None,
            "hora_cirugia": self.hora_cirugia,
            "tipo_cirugia": self.tipo_cirugia,
            "id_paciente": self.id_paciente,
            "id_habitacion": self.id_habitacion,
        }
