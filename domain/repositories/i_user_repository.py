from abc import ABC, abstractmethod
from domain.entities.usuario import Usuario
from typing import List, Optional


class IUserRepository(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def get_all(self) -> List[Usuario]:
        pass

    @abstractmethod
    def save(self, user: Usuario) -> None:
        pass

    @abstractmethod
    def update(self, user: Usuario) -> None:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass

    @abstractmethod
    def buscar_por_correo(self, correo: str) -> Optional[Usuario]:
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def eliminar_usuario(self, user_id: int):
        pass

