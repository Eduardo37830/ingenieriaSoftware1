# application/services/transaction_application_service.py

from ingenieriaSoftware1.application.dtos.transaction_dto import TransactionDTO
from ingenieriaSoftware1.domain.services.transaction_service import TransactionService
from ingenieriaSoftware1.domain.repositories.i_transaction_repository import ITransactionRepository


class TransactionApplicationService:
    def __init__(self, transaction_service: TransactionService, transaction_repository: ITransactionRepository):
        self.transaction_service = transaction_service
        self.transaction_repository = transaction_repository

    def create_transaction(self, transaction_dto: TransactionDTO):
        # Convierte el DTO a una entidad de dominio (Transaction)
        transaction = self.transaction_service.create_transaction(transaction_dto.amount, transaction_dto.description)

        # Guarda la transacción usando el repositorio
        self.transaction_repository.save(transaction)
        return transaction

    def get_all_transactions(self):
        # Recupera todas las transacciones del repositorio
        return self.transaction_repository.get_all()

    def generate_report(self):
        # Llama al servicio de dominio para generar un informe
        return self.transaction_service.generate_financial_report()
