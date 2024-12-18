from domain.repositories.i_cirugia_repository import ICirugiaRepository
from application.dtos.cirugia_dto import CirugiaDTO
from application.exceptions.application_error import NotFoundError

class CirugiaApplicationService:
    def __init__(self, cirugia_repository: ICirugiaRepository):
        self.cirugia_repository = cirugia_repository

    def registrar_cirugia(self, cirugia_dto: CirugiaDTO) -> None:
        """Registra una nueva cirugía."""
        cirugia = cirugia_dto.to_entity()  # Convertimos el DTO a una entidad
        self.cirugia_repository.save(cirugia)

    def obtener_cirugia_por_id(self, cirugia_id: int) -> CirugiaDTO:
        """Obtiene una cirugía por su ID."""
        cirugia = self.cirugia_repository.find_by_id(cirugia_id)
        if not cirugia:
            raise NotFoundError(f"No se encontró una cirugía con el ID {cirugia_id}")
        return CirugiaDTO.from_entity(cirugia)  # Convertimos la entidad en un DTO

    def listar_cirugias_por_paciente(self, paciente_id: int) -> list[CirugiaDTO]:
        """Lista todas las cirugías de un paciente."""
        cirugias = self.cirugia_repository.find_all_by_paciente(paciente_id)
        return [CirugiaDTO.from_entity(c) for c in cirugias]  # Convertimos cada entidad en un DTO
