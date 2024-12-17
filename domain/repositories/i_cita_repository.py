# domain/repositories/i_cita_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.cita import Cita

class ICitaRepository(ABC):
    @abstractmethod
    def save(self, cita: Cita) -> None:
        """Guarda o actualiza una cita."""
        pass

    @abstractmethod
    def find_by_id(self, cita_id: int) -> Cita:
        """Busca una cita por su ID."""
        pass

    @abstractmethod
    def find_all_by_paciente(self, paciente_id: int) -> List[Cita]:
        """Obtiene todas las citas de un paciente."""
        pass

    @abstractmethod
    def delete(self, cita_id: int) -> None:
        """Elimina una cita."""
        pass

    def find_all(self):
        """Obtiene todas las citas."""
        pass

    def find_all_by_personal_medico(self, personalMedico_id):

        pass
