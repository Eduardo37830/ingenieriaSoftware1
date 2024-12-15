
class TransactionApplicationService:

    def __init__(self, transaction_repository: ITransactionRepository, account_repository: IAccountRepository,
                 transaction_service: TransactionService):
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository
        self.transaction_service = transaction_service

    def create_transaction(self, transaction_dto: TransactionDTO):
        #Crea una nueva transacción, delegando la lógica de negocio a los servicios de dominio.

        # Delegar la lógica de negocio al servicio de dominio
        transaction = self.transaction_service.create_transaction(
            description=transaction_dto.description,
            amount=transaction_dto.amount,
            transaction_type=transaction_dto.transaction_type
        )
        self.transaction_repository.save(transaction)
        return transaction

    def get_all_transactions(self):
        #Obtiene todas las transacciones almacenadas.

        transactions = self.transaction_repository.get_all()
        return transactions

    def generate_financial_report(self):
        #Genera un informe financiero de las transacciones.

        # Delegar la generación del informe a la capa de dominio
        total_depositos, total_retiros, saldo_promedio = self.transaction_service.generate_report()
        informe_dto = InformeDTO(
            total_depositos=total_depositos,
            total_retiros=total_retiros,
            saldo_promedio=saldo_promedio
        )
        return informe_dto
