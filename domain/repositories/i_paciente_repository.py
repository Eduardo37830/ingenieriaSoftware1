# domain/repositories/i_paciente_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.paciente import Paciente

class IPacienteRepository(ABC):
    @abstractmethod
    def save(self, paciente: Paciente) -> None:
        """Guarda o actualiza un paciente."""
        pass

    @abstractmethod
    def find_by_id(self, paciente_id: int) -> Paciente:
        """Busca un paciente por su ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[Paciente]:
        """Obtiene todos los pacientes."""
        pass
