from ingenieriaSoftware1.domain.repositories.i_historial_medico_repository import HistorialMedicoRepository
from ingenieriaSoftware1.application.dtos.historial_medico_dto import HistorialMedicoDTO
from ingenieriaSoftware1.application.exceptions.application_error import NotFoundError

class HistorialMedicoApplicationService:
    def __init__(self, historial_medico_repository: HistorialMedicoRepository):
        self.historial_medico_repository = historial_medico_repository

    def registrar_historial_medico(self, historial_medico_dto: HistorialMedicoDTO) -> None:
        """Registra una nueva entrada en el historial médico."""
        historial_medico = historial_medico_dto.to_entity()
        self.historial_medico_repository.save(historial_medico)

    def obtener_historial_medico_por_paciente(self, paciente_id: int) -> list[HistorialMedicoDTO]:
        """Obtiene todos los historiales médicos de un paciente."""
        historiales = self.historial_medico_repository.find_all_by_paciente(paciente_id)
        return [HistorialMedicoDTO.from_entity(h) for h in historiales]

    def obtener_historial_medico_por_id(self, historial_id: int) -> HistorialMedicoDTO:
        """Obtiene una entrada específica del historial médico por su ID."""
        historial = self.historial_medico_repository.find_by_id(historial_id)
        if not historial:
            raise NotFoundError(f"No se encontró el historial médico con el ID {historial_id}")
        return HistorialMedicoDTO.from_entity(historial)
