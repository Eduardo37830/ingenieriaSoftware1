from ingenieriaSoftware1.domain.repositories.i_cita_repository import ICitaRepository
from ingenieriaSoftware1.application.dtos.cita_dto import CitaDTO
from ingenieriaSoftware1.application.exceptions.application_error import NotFoundError

class CitaApplicationService:
    def __init__(self, cita_repository: ICitaRepository):
        self.cita_repository = cita_repository

    def registrar_cita(self, cita_dto: CitaDTO) -> None:
        """Registra una nueva cita médica."""
        cita = cita_dto.to_entity()  # Convertir el DTO en una entidad
        self.cita_repository.save(cita)

    def obtener_cita_por_id(self, cita_id: int) -> CitaDTO:
        """Obtiene una cita por su ID."""
        cita = self.cita_repository.find_by_id(cita_id)
        if not cita:
            raise NotFoundError(f"No se encontró una cita con el ID {cita_id}")
        return CitaDTO.from_entity(cita)  # Convertir la entidad en un DTO

    def verificar_conflicto(self, cita_dto: CitaDTO) -> bool:
        """Verifica si la nueva cita entra en conflicto con alguna existente."""
        cita = cita_dto.to_entity()
        todas_las_citas = self.cita_repository.find_all()
        for otra_cita in todas_las_citas:
            if cita.verificarConflicto(otra_cita):  # Llamada al método verificarConflicto
                return True
        return False

    def save_cita(self, cita_dto):
        pass

    def get_cita_by_id(self, param):
        pass
