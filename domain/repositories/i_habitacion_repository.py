# domain/repositories/i_habitacion_repository.py
from abc import ABC, abstractmethod
from typing import List
from ingenieriaSoftware1.domain.entities.habitacion import Habitacion

class IhabitacionRepository(ABC):
    @abstractmethod
    def save(self, habitacion: Habitacion) -> None:
        """Guarda o actualiza una habitacion."""
        pass

    @abstractmethod
    def find_by_id(self, habitacion_id: int) -> Habitacion:
        """Busca una habitacion por su ID."""
        pass

    @abstractmethod
    def find_all_by_paciente(self, paciente_id: int) -> List[Habitacion]:
        """Obtiene todas las habitacions de un paciente."""
        pass

    @abstractmethod
    def delete(self, habitacion_id: int) -> None:
        """Elimina una habitacion."""
        pass
