from domain.repositories.i_equipoMedico_repository import IequipoMedicoRepository
from application.dtos.equipo_medico_dto import EquipoMedicoDTO
from application.exceptions.application_error import NotFoundError

class EquipoMedicoApplicationService:
    def __init__(self, equipo_medico_repository: IequipoMedicoRepository):
        self.equipo_medico_repository = equipo_medico_repository

    def registrar_equipo_medico(self, equipo_medico_dto: EquipoMedicoDTO) -> None:
        """Registra un nuevo equipo médico."""
        equipo_medico = equipo_medico_dto.to_entity()  # Convertir el DTO en una entidad
        self.equipo_medico_repository.save(equipo_medico)

    def obtener_equipo_medico_por_id(self, equipo_medico_id: int) -> EquipoMedicoDTO:
        """Obtiene un equipo médico por su ID."""
        equipo_medico = self.equipo_medico_repository.find_by_id(equipo_medico_id)
        if not equipo_medico:
            raise NotFoundError(f"No se encontró un equipo médico con el ID {equipo_medico_id}")
        return EquipoMedicoDTO.from_entity(equipo_medico)  # Convertir la entidad en un DTO

    def obtener_todos_los_equipos(self) -> list[EquipoMedicoDTO]:
        """Obtiene todos los equipos médicos."""
        equipos = self.equipo_medico_repository.find_all()
        return [EquipoMedicoDTO.from_entity(e) for e in equipos]  # Convertir todas las entidades a DTO

    def verificar_disponibilidad(self, equipo_medico_id: int) -> bool:
        """Verifica la disponibilidad de un equipo médico."""
        equipo_medico = self.equipo_medico_repository.find_by_id(equipo_medico_id)
        if not equipo_medico:
            raise NotFoundError(f"No se encontró un equipo médico con el ID {equipo_medico_id}")
        return equipo_medico.disponibilidad
