from application.dtos.paciente_dto import PacienteDTO
from domain.repositories.i_paciente_repository import IPacienteRepository
from application.exceptions.application_error import NotFoundError

class PacienteApplicationService:
    def __init__(self, paciente_repository: IPacienteRepository):
        self.paciente_repository = paciente_repository

    def registrar_paciente(self, paciente_dto: PacienteDTO) -> None:
        """Registra un nuevo paciente."""
        paciente = paciente_dto.to_entity()  # Convierte el DTO a entidad
        self.paciente_repository.save(paciente)

    def obtener_paciente_por_id(self, paciente_id: int) -> PacienteDTO:
        """Obtiene un paciente por su ID."""
        paciente = self.paciente_repository.find_by_id(paciente_id)
        if not paciente:
            raise NotFoundError(f"No se encontró un paciente con el ID {paciente_id}")
        return PacienteDTO.from_entity(paciente)

    def actualizar_paciente(self, paciente_id: int, paciente_dto: PacienteDTO) -> None:
        """Actualiza los datos de un paciente."""
        paciente = self.paciente_repository.find_by_id(paciente_id)
        if not paciente:
            raise NotFoundError(f"No se encontró un paciente con el ID {paciente_id}")
        paciente_actualizado = paciente_dto.to_entity()
        self.paciente_repository.update(paciente_actualizado)

    def eliminar_paciente(self, paciente_id: int) -> None:
        """Elimina un paciente."""
        paciente = self.paciente_repository.find_by_id(paciente_id)
        if not paciente:
            raise NotFoundError(f"No se encontró un paciente con el ID {paciente_id}")
        self.paciente_repository.delete(paciente_id)

    def agregar_historial_medico(self, paciente_id: int, historial_medico) -> None:
        """Agrega un historial médico al paciente."""
        paciente = self.paciente_repository.find_by_id(paciente_id)
        if not paciente:
            raise NotFoundError(f"No se encontró un paciente con el ID {paciente_id}")
        paciente.agregarHistorial(historial_medico)
        self.paciente_repository.update(paciente)

    def listar_historial_medico(self, paciente_id: int) -> str:
        """Lista el historial médico completo del paciente."""
        paciente = self.paciente_repository.find_by_id(paciente_id)
        if not paciente:
            raise NotFoundError(f"No se encontró un paciente con el ID {paciente_id}")
        return paciente.mostrarHistorial()

    def agregar_cita(self, paciente_id: int, cita) -> None:
        """Agrega una cita al paciente."""
        paciente = self.paciente_repository.find_by_id(paciente_id)
        if not paciente:
            raise NotFoundError(f"No se encontró un paciente con el ID {paciente_id}")
        paciente.agregarCita(cita)
        self.paciente_repository.update(paciente)

    def listar_citas(self, paciente_id: int) -> str:
        """Lista todas las citas del paciente."""
        paciente = self.paciente_repository.find_by_id(paciente_id)
        if not paciente:
            raise NotFoundError(f"No se encontró un paciente con el ID {paciente_id}")
        return "\n".join(str(cita) for cita in paciente.citas)

    def agregar_formula(self, paciente_id: int, formula) -> None:
        """Agrega una fórmula al paciente."""
        paciente = self.paciente_repository.find_by_id(paciente_id)
        if not paciente:
            raise NotFoundError(f"No se encontró un paciente con el ID {paciente_id}")
        paciente.formulas.append(formula)
        self.paciente_repository.update(paciente)
