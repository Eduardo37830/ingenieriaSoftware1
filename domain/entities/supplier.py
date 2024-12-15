class Supplier:
    def __init__(self, supplier_id, name, deliveryDate, cost, sellerPhone):
        """
        Clase para representar un proveedor.
        :param supplier_id: ID único del proveedor.
        :param name: Nombre del proveedor.
        :param deliveryDate: Fecha de entrega (datetime).
        :param cost: Costo de la entrega.
        :param sellerPhone: Teléfono del vendedor.
        """
        self.supplier_id = supplier_id
        self.name = name
        self.deliveryDate = deliveryDate
        self.cost = cost
        self.sellerPhone = sellerPhone
        self.medications = []  # Lista de medicamentos gestionados por este proveedor

    def registrarPedido(self, medicamento, cantidad):
        """
        Registra un pedido de un medicamento con este proveedor.
        :param medicamento: Instancia de la clase Medication.
        :param cantidad: Cantidad pedida.
        :return: Mensaje indicando el resultado del registro.
        """
        self.medications.append({"medicamento": medicamento, "cantidad": cantidad})
        return f"Pedido registrado: {cantidad} unidades de {medicamento.name}."

    def consultarPedidos(self):
        """
        Consulta los medicamentos registrados con este proveedor.
        :return: Lista de medicamentos gestionados.
        """
        return [
            f"{item['cantidad']} unidades de {item['medicamento'].name}"
            for item in self.medications
        ]

    def actualizarDetalles(self, name=None, deliveryDate=None, cost=None, sellerPhone=None):
        """
        Actualiza los detalles del proveedor.
        :param name: Nuevo nombre del proveedor (opcional).
        :param deliveryDate: Nueva fecha de entrega (opcional).
        :param cost: Nuevo costo de la entrega (opcional).
        :param sellerPhone: Nuevo número de teléfono (opcional).
        :return: Mensaje indicando los cambios realizados.
        """
        if name:
            self.name = name
        if deliveryDate:
            self.deliveryDate = deliveryDate
        if cost:
            self.cost = cost
        if sellerPhone:
            self.sellerPhone = sellerPhone
        return "Detalles del proveedor actualizados."

    def __str__(self):
        """
        Representación en texto del proveedor.
        """
        return (
            f"Proveedor ID: {self.supplier_id}\n"
            f"Nombre: {self.name}\n"
            f"Fecha de Entrega: {self.deliveryDate}\n"
            f"Costo: {self.cost}\n"
            f"Teléfono: {self.sellerPhone}\n"
        )
