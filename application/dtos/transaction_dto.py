class TransactionDTO:
    def __init__(self, description: str, amount: float, transaction_type: str):
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type
