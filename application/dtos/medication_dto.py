class MedicationDTO:
    def __init__(self, id: int, name: str, type: str, stock: int):
        self.id = id
        self.name = name
        self.type = type
        self.stock = stock
