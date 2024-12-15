from ingenieriaSoftware1.domain.entities.paciente import Paciente
from ingenieriaSoftware1.domain.entities.cita import Cita
from typing import List


class PacienteService:
    def __init__(self, cita_repository):
        self.cita_repository = cita_repository

    def agendarCita(self, paciente: Paciente, cita: Cita):
        # Validar disponibilidad del personal médico y otras reglas
        self.cita_repository.guardar(cita)

    def cancelarCita(self, cita: Cita):
        # Eliminar cita de la base de datos o repositorio
        self.cita_repository.eliminar(cita.id)

    def consultarCitas(self, idPaciente: int) -> List[Cita]:
        return self.cita_repository.obtenerPorPaciente(idPaciente)
