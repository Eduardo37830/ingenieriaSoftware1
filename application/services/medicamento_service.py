from domain.repositories.i_medicamento_repository import IMedicamentoRepository
from application.dtos.medicamento_dto import MedicamentoDTO
from application.exceptions.application_error import NotFoundError

class MedicamentoApplicationService:
    def __init__(self, medicamento_repository: IMedicamentoRepository):
        self.medicamento_repository = medicamento_repository

    def registrar_medicamento(self, medicamento_dto: MedicamentoDTO) -> None:
        """Registra un nuevo medicamento en el sistema."""
        medicamento = medicamento_dto.to_entity()
        self.medicamento_repository.save(medicamento)

    def obtener_medicamento_por_id(self, medicamento_id: int) -> MedicamentoDTO:
        """Obtiene un medicamento por su ID."""
        medicamento = self.medicamento_repository.find_by_id(medicamento_id)
        if not medicamento:
            raise NotFoundError(f"No se encontró el medicamento con el ID {medicamento_id}")
        return MedicamentoDTO.from_entity(medicamento)

    def listar_medicamentos(self) -> list[MedicamentoDTO]:
        """Lista todos los medicamentos registrados en el sistema."""
        medicamentos = self.medicamento_repository.find_all()
        return [MedicamentoDTO.from_entity(m) for m in medicamentos]

    def actualizar_cantidad_medicamento(self, medicamento_id: int, cantidad: int) -> None:
        """Actualiza la cantidad de un medicamento en inventario."""
        medicamento = self.medicamento_repository.find_by_id(medicamento_id)
        if not medicamento:
            raise NotFoundError(f"No se encontró el medicamento con el ID {medicamento_id}")
        medicamento.actualizarCantidad(cantidad)
        self.medicamento_repository.save(medicamento)
