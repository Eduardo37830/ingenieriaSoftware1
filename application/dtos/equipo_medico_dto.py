from typing import Optional
from ingenieriaSoftware1.domain.entities.equipo_medico import EquipoMedico

class EquipoMedicoDTO:
    def __init__(self, id: Optional[int] = None, tipo_equipo: str = "", funcionalidad: Optional[str] = None,
                 disponibilidad: bool = True):
        self.id = id
        self.tipo_equipo = tipo_equipo
        self.funcionalidad = funcionalidad
        self.disponibilidad = disponibilidad

    def __repr__(self):
        return (f"EquipoMedicoDTO(id={self.id}, tipo_equipo='{self.tipo_equipo}', funcionalidad={self.funcionalidad}, "
                f"disponibilidad={self.disponibilidad})")

    @staticmethod
    def from_entity(equipo_medico: EquipoMedico) -> 'EquipoMedicoDTO':
        """Convierte una entidad EquipoMedico en un EquipoMedicoDTO."""
        return EquipoMedicoDTO(
            id=equipo_medico.id,
            tipo_equipo=equipo_medico.tipo_equipo,
            funcionalidad=equipo_medico.funcionalidad,
            disponibilidad=equipo_medico.disponibilidad
        )

    def to_entity(self) -> EquipoMedico:
        """Convierte un EquipoMedicoDTO en una entidad EquipoMedico."""
        return EquipoMedico(
            id=self.id,
            tipo_equipo=self.tipo_equipo,
            funcionalidad=self.funcionalidad,
            disponibilidad=self.disponibilidad
        )
