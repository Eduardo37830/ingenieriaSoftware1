# domain/repositories/i_medicamento_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.medicamento import Medicamento

class IMedicamentoRepository(ABC):
    @abstractmethod
    def save(self, medicamento: Medicamento) -> None:
        """Guarda o actualiza un medicamento."""
        pass

    @abstractmethod
    def find_by_id(self, medicamento_id: int) -> Medicamento:
        """Busca un medicamento por su ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[Medicamento]:
        """Obtiene todos los medicamentos."""
        pass

    @abstractmethod
    def find_low_stock(self, threshold: int) -> List[Medicamento]:
        """Obtiene medicamentos con stock por debajo del umbral."""
        pass
