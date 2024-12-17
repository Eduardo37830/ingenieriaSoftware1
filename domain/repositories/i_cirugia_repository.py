# domain/repositories/i_cirugia_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.cirugia import Cirugia

class ICirugiaRepository(ABC):
    @abstractmethod
    def save(self, cirugia: Cirugia) -> None:
        """Guarda o actualiza una cirugia.py."""
        pass

    @abstractmethod
    def find_by_id(self, cirugia_id: int) -> Cirugia:
        """Busca una cirugia.py por su ID."""
        pass

    @abstractmethod
    def find_all_by_paciente(self, paciente_id: int) -> List[Cirugia]:
        """Obtiene todas las cirugias de un paciente."""
        pass

    @abstractmethod
    def delete(self, cirugia_id: int) -> None:
        """Elimina una cirugia.py."""
        pass
