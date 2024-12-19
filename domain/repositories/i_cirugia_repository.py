from abc import ABC, abstractmethod
from typing import List
from domain.entities.cirugia import Cirugia

class ICirugiaRepository(ABC):
    @abstractmethod
    def save(self, cirugia: Cirugia) -> None:
        """Guarda o actualiza una cirugía."""
        pass

    @abstractmethod
    def find_by_id(self, cirugia_id: int) -> Cirugia:
        """Busca una cirugía por su ID."""
        pass

    @abstractmethod
    def find_all_by_paciente(self, paciente_id: int) -> List[Cirugia]:
        """Obtiene todas las cirugías de un paciente."""
        pass

    @abstractmethod
    def delete(self, cirugia_id: int) -> None:
        """Elimina una cirugía por su ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[Cirugia]:
        """Obtiene todas las cirugías registradas."""
        pass
