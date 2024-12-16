# domain/repositories/i_transaction_repository.py

from abc import ABC, abstractmethod
from ingenieriaSoftware1.application.dtos.transaction_dto import TransactionDTO


class ITransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: TransactionDTO):
        pass

    @abstractmethod
    def get_all(self) -> list[TransactionDTO]:
        pass

    @abstractmethod
    def get_by_id(self, transaction_id: int) -> TransactionDTO:
        pass
