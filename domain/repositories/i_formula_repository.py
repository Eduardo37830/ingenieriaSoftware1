# domain/repositories/i_formula_repository.py
from abc import ABC, abstractmethod
from typing import List
from ingenieriaSoftware1.domain.entities.formula import Formula

class IformulaRepository(ABC):
    @abstractmethod
    def save(self, formula: Formula) -> None:
        """Guarda o actualiza un formula."""
        pass

    @abstractmethod
    def find_by_id(self, formula_id: int) -> Formula:
        """Busca un formula por su ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[Formula]:
        """Obtiene todos los formulas."""
        pass
