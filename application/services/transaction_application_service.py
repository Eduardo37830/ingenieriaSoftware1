# application/services/transaction_application_service.py
from ingenieriaSoftware1.domain.repositories.i_transaction_repository import ITransactionRepository
from ingenieriaSoftware1.application.dtos.transaction_dto import TransactionDTO
from ingenieriaSoftware1.application.exceptions.application_error import NotFoundError

class TransactionApplicationService:
    def __init__(self, transaction_repository: ITransactionRepository):
        self.transaction_repository = transaction_repository

    def registrar_transaccion(self, transaction_dto: TransactionDTO) -> None:
        """Registra una nueva transacción."""
        transaction = transaction_dto.to_entity()
        self.transaction_repository.save(transaction)

    def obtener_transaccion_por_id(self, transaction_id: int) -> TransactionDTO:
        """Obtiene una transacción por su ID."""
        transaction = self.transaction_repository.get_by_id(transaction_id)
        if not transaction:
            raise NotFoundError(f"No se encontró una transacción con el ID {transaction_id}")
        return TransactionDTO.from_entity(transaction)

    def listar_transacciones(self) -> list[TransactionDTO]:
        """Lista todas las transacciones."""
        transactions = self.transaction_repository.get_all()
        return [TransactionDTO.from_entity(t) for t in transactions]
