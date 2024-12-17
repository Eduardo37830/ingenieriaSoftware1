# domain/repositories/i_equipoMedico_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.equipoMedico import EquipoMedico

class IEquipoMedicoRepository(ABC):
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

    def delete(self, equipo_medico_id):
        """Elimina un equipoMedico por su ID."""
        pass
