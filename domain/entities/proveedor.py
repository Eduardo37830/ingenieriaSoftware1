class Proveedor:
    def __init__(self, id_proveedor, nombre, fecha_entrega, costo, telefono_vendedor, direccion):
        """
        Clase para representar un proveedor.
        :param id_proveedor: ID único del proveedor.
        :param nombre: Nombre del proveedor.
        :param fecha_entrega: Fecha de entrega (datetime).
        :param costo: Costo de la entrega.
        :param telefono_vendedor: Teléfono del vendedor.
        """
        self.id = id_proveedor
        self.nombre = nombre
        self.fecha_entrega = fecha_entrega
        self.costo = costo
        self.telefono_vendedor = telefono_vendedor
        self.direccion = direccion
        self.medicamentos = []  # Lista de medicamentos gestionados por este proveedor

    def registrar_pedido(self, medicamento, cantidad):
        """
        Registra un pedido de un medicamento con este proveedor.
        :param medicamento: Instancia de la clase Medicamento.
        :param cantidad: Cantidad pedida.
        :return: Mensaje indicando el resultado del registro.
        """
        self.medicamentos.append({"medicamento": medicamento, "cantidad": cantidad})
        return f"Pedido registrado: {cantidad} unidades de {medicamento.nombre}."

    def consultar_pedidos(self):
        """
        Consulta los medicamentos registrados con este proveedor.
        :return: Lista de medicamentos gestionados.
        """
        return [
            f"{item['cantidad']} unidades de {item['medicamento'].nombre}"
            for item in self.medicamentos
        ]

    def actualizar_detalles(self, nombre=None, fecha_entrega=None, costo=None, telefono_vendedor=None):
        """
        Actualiza los detalles del proveedor.
        :param nombre: Nuevo nombre del proveedor (opcional).
        :param fecha_entrega: Nueva fecha de entrega (opcional).
        :param costo: Nuevo costo de la entrega (opcional).
        :param telefono_vendedor: Nuevo número de teléfono (opcional).
        :return: Mensaje indicando los cambios realizados.
        """
        if nombre:
            self.nombre = nombre
        if fecha_entrega:
            self.fecha_entrega = fecha_entrega
        if costo:
            self.costo = costo
        if telefono_vendedor:
            self.telefono_vendedor = telefono_vendedor
        return "Detalles del proveedor actualizados."

    def __str__(self):
        """
        Representación en texto del proveedor.
        """
        return (
            f"Proveedor ID: {self.id_proveedor}\n"
            f"Nombre: {self.nombre}\n"
            f"Fecha de Entrega: {self.fecha_entrega}\n"
            f"Costo: {self.costo}\n"
            f"Teléfono: {self.telefono_vendedor}\n"
        )
