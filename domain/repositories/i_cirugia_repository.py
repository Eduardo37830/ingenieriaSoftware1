# domain/repositories/i_cita_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.cirugia import Cita

class ICirugiaRepository(ABC):
    @abstractmethod
    def save(self, cita: Cita) -> None:
        """Guarda o actualiza una cirugia."""
        pass

    @abstractmethod
    def find_by_id(self, cita_id: int) -> Cita:
        """Busca una cirugia por su ID."""
        pass

    @abstractmethod
    def find_all_by_paciente(self, paciente_id: int) -> List[Cita]:
        """Obtiene todas las cirugias de un paciente."""
        pass

    @abstractmethod
    def delete(self, cita_id: int) -> None:
        """Elimina una cirugia."""
        pass
