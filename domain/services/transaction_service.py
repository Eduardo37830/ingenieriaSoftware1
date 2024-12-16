# domain/services/transaction_service.py

from application.dtos.transaction_dto import TransactionDTO
from application.dtos.informe_dto import InformeDTO

class TransactionService:
    def create_transaction(self, amount: float, description: str):
        # Lógica para crear una transacción
        return TransactionDTO(amount, description)

    def generate_financial_report(self):
        # Lógica para generar un informe financiero
        # Aquí podríamos agregar las operaciones necesarias para obtener los totales
        total_depositos = 1000.0  # Esto sería calculado dinámicamente
        total_retiros = 500.0
        saldo_promedio = 700.0
        return InformeDTO(total_depositos, total_retiros, saldo_promedio)
