# domain/repositories/i_Proveedor_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.proveedor import Proveedor

class IProveedorRepository(ABC):
    @abstractmethod
    def save(self, Proveedor: Proveedor) -> None:
        """Guarda o actualiza un Proveedor."""
        pass

    @abstractmethod
    def find_by_id(self, Proveedor_id: int) -> Proveedor:
        """Busca un Proveedor por su ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[Proveedor]:
        """Obtiene todos los Proveedores."""
        pass

    def delete(self, Proveedor: Proveedor) -> None:
        """Elimina un Proveedor."""
        pass