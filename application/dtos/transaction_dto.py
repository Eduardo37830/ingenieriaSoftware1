# application/dtos/transaction_dto.py

class TransactionDTO:
    def __init__(self, amount: float, description: str):
        self.amount = amount
        self.description = description
