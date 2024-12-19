from typing import Optional
from domain.entities.equipoMedico import EquipoMedico

class EquipoMedicoDTO:
    def __init__(self, id: Optional[int] = None, tipo_equipo: str = "", funcionalidad: Optional[str] = None,
                 disponibilidad: bool = True):
        """
        Constructor para el DTO de EquipoMedico.
        :param id: Identificador único del equipo médico.
        :param tipo_equipo: Tipo de equipo médico (ejemplo: "Radiografía").
        :param funcionalidad: Descripción de la funcionalidad del equipo (opcional).
        :param disponibilidad: Indica si el equipo está disponible o no (por defecto es True).
        """
        self.id = id
        self.tipo_equipo = tipo_equipo
        self.funcionalidad = funcionalidad
        self.disponibilidad = disponibilidad

    def __repr__(self):
        """Representación del objeto en formato string para depuración."""
        return (f"EquipoMedicoDTO(id={self.id}, tipo_equipo='{self.tipo_equipo}', funcionalidad={self.funcionalidad}, "
                f"disponibilidad={self.disponibilidad})")

    @staticmethod
    def from_entity(equipo_medico: EquipoMedico) -> 'EquipoMedicoDTO':
        """Convierte una entidad EquipoMedico en un DTO de EquipoMedico."""
        return EquipoMedicoDTO(
            id=equipo_medico.id,
            tipo_equipo=equipo_medico.tipo_equipo,
            funcionalidad=equipo_medico.funcionalidad,
            disponibilidad=equipo_medico.disponibilidad
        )

    def to_entity(self) -> EquipoMedico:
        """Convierte un DTO de EquipoMedico en una entidad EquipoMedico."""
        return EquipoMedico(
            id=self.id,
            tipo_equipo=self.tipo_equipo,
            funcionalidad=self.funcionalidad,
            disponibilidad=self.disponibilidad
        )

    def to_dict(self) -> dict:
        """Convierte el DTO a un diccionario para serialización, ideal para enviar en una API."""
        return {
            "id": self.id,
            "tipo_equipo": self.tipo_equipo,
            "funcionalidad": self.funcionalidad,
            "disponibilidad": self.disponibilidad
        }
