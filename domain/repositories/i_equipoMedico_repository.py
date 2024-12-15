# domain/repositories/i_equipoMedico_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.equipo_medico import EquipoMedico

class IequipoMedicoRepository(ABC):
    @abstractmethod
    def save(self, equipoMedico: EquipoMedico) -> None:
        """Guarda o actualiza un equipoMedico."""
        pass

    @abstractmethod
    def find_by_id(self, equipoMedico_id: int) -> EquipoMedico:
        """Busca un equipoMedico por su ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[EquipoMedico]:
        """Obtiene todos los equipoMedicos."""
        pass
