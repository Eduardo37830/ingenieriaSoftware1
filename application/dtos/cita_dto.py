from datetime import datetime
from typing import Optional
from domain.entities.cita import Cita

class CitaDTO:
    def __init__(self, id: Optional[int] = None, motivoConsulta: str = "", fechaConsulta: datetime = None,
                 horaConsulta: datetime = None, paciente_id: int = None, personalMedico_id: int = None,
                 costoTotal: float = 0.0, habitacion_id: Optional[int] = None):
        self.usuario_id = None
        self.id = id
        self.motivoConsulta = motivoConsulta
        self.fechaConsulta = fechaConsulta
        self.horaConsulta = horaConsulta
        self.costoTotal = costoTotal
        self.paciente_id = paciente_id
        self.personalMedico_id = personalMedico_id
        self.habitacion_id = habitacion_id

    def __repr__(self):
        return (f"CitaDTO(id={self.id}, motivoConsulta='{self.motivoConsulta}', fechaConsulta={self.fechaConsulta}, "
                f"horaConsulta={self.horaConsulta}, paciente_id={self.paciente_id}, "
                f"personalMedico_id={self.personalMedico_id}, costoTotal={self.costoTotal}, habitacion_id={self.habitacion_id})")

    @staticmethod
    def from_entity(cita: Cita) -> 'CitaDTO':
        """Convierte una entidad Cita en un CitaDTO."""
        return CitaDTO(
            id=cita.id,
            motivoConsulta=cita.motivoConsulta,
            fechaConsulta=cita.fechaConsulta,
            horaConsulta=cita.horaConsulta,
            paciente_id=cita.paciente_id,
            personalMedico_id=cita.personalMedico_id,
            costoTotal=cita.costoTotal,
            habitacion_id=cita.habitacion_id
        )

    def to_entity(self) -> Cita:
        """Convierte un CitaDTO en una entidad Cita."""
        return Cita(
            id=self.id,
            motivoConsulta=self.motivoConsulta,
            fechaConsulta=self.fechaConsulta,
            horaConsulta=self.horaConsulta,
            paciente_id=self.paciente_id,
            personalMedico_id=self.personalMedico_id,
            costoTotal=self.costoTotal,
            habitacion_id=self.habitacion_id
        )
