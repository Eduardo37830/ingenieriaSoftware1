class Supplier:
    def __init__(self, supplier_id, name, deliveryDate, cost, sellerPhone):
        self.supplier_id = supplier_id
        self.name = name
        self.deliveryDate = deliveryDate
        self.cost = cost
        self.sellerPhone = sellerPhone
        self.medications = []
