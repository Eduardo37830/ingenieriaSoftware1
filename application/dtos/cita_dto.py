from datetime import datetime, time
from typing import Optional
from domain.entities.cita import Cita

class CitaDTO:
    def __init__(self, id, motivoConsulta: str = "", fechaConsulta: datetime = None,
                 horaConsulta: time = "", paciente_id: int = None, personalMedico_id: int = None,
                 costoTotal: float = 0.0, habitacion_id: Optional[int] = None):
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
        hora_consulta = (
            datetime.strptime(cita.horaConsulta, "%H:%M").time()
            if isinstance(cita.horaConsulta, str) else
            cita.horaConsulta  # Si ya es un objeto time
        )

        return CitaDTO(
            id=cita.id,
            motivoConsulta=cita.motivoConsulta,
            fechaConsulta=cita.fechaConsulta,
            horaConsulta=hora_consulta,  # Usamos el objeto time procesado
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
            horaConsulta=self.horaConsulta, # Combinamos fecha y hora
            paciente_id=self.paciente_id,
            personalMedico_id=self.personalMedico_id,
            costoTotal=self.costoTotal,
            habitacion_id=self.habitacion_id
        )

    def to_dict(self):
        """Convierte el DTO a un diccionario."""
        return {
            "id": self.id,
            "paciente_id": self.paciente_id,
            "personalMedico_id": self.personalMedico_id,
            "motivoConsulta": self.motivoConsulta,
            "fechaConsulta": self.fechaConsulta.strftime("%Y-%m-%d") if isinstance(self.fechaConsulta,
                                                                                   datetime) else self.fechaConsulta,
            "horaConsulta": (
                self.horaConsulta.strftime("%H:%M") if isinstance(self.horaConsulta, time)
                else self.horaConsulta
            ),

            "habitacion_id": self.habitacion_id,
            "costoTotal": self.costoTotal,

        }


