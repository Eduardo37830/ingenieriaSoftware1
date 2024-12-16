from datetime import datetime
from paciente import Paciente
from personalMedico import PersonalMedico

class Cita:
    def __init__(self, id: int, motivoConsulta: str, fechaHoraConsulta: datetime, paciente: Paciente, personalMedico: PersonalMedico, totalAPagar: float):
        self.id = id
        self.motivoConsulta = motivoConsulta
        self.fechaHoraConsulta = fechaHoraConsulta
        self.paciente = paciente
        self.personalMedico = personalMedico
        self.totalAPagar = totalAPagar

    def verificarConflicto(self, otraCita: 'Cita') -> bool:
        return self.fechaHoraConsulta == otraCita.fechaHoraConsulta