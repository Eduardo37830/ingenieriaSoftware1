# domain/repositories/i_personal_medico_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.personalMedico import PersonalMedico


class IPersonalMedicoRepository(ABC):
    @abstractmethod
    def save(self, personal: PersonalMedico) -> None:
        """Guarda o actualiza un personal médico."""
        pass

    @abstractmethod
    def find_by_id(self, personal_id: int) -> PersonalMedico:
        """Busca un personal médico por su ID."""
        pass

    @abstractmethod
    def find_available(self, start_time: str, end_time: str) -> List[PersonalMedico]:
        """Obtiene personal médico disponible en un rango de horarios."""
        pass

    @abstractmethod
    def find_all(self) -> List[PersonalMedico]:
        """Obtiene todos los pacientes."""
        pass

    @abstractmethod
    def delete(self, personal_id):
        pass
