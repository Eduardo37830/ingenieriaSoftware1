class ProveedorService:
    def __init__(self, proveedor_repository):
        """
        Inicializa el servicio con un repositorio de proveedores.
        :param proveedor_repository: Repositorio encargado de gestionar la persistencia de los proveedores.
        """
        self.proveedor_repository = proveedor_repository

    def registrar_pedido(self, id_proveedor, medicamento, cantidad):
        """
        Registra un pedido de medicamento a un proveedor específico.
        :param id_proveedor: ID del proveedor que realiza el pedido.
        :param medicamento: Instancia del medicamento que se está pidiendo.
        :param cantidad: Cantidad solicitada.
        :return: Mensaje con el resultado del pedido.
        """
        proveedor = self.proveedor_repository.get_by_id(id_proveedor)
        if not proveedor:
            raise ValueError("Proveedor no encontrado.")

        return proveedor.registrar_pedido(medicamento, cantidad)

    def consultar_pedidos(self, id_proveedor):
        """
        Consulta los pedidos realizados por un proveedor.
        :param id_proveedor: ID del proveedor.
        :return: Lista de pedidos.
        """
        proveedor = self.proveedor_repository.get_by_id(id_proveedor)
        if not proveedor:
            raise ValueError("Proveedor no encontrado.")

        return proveedor.consultar_pedidos()

    def actualizar_detalles(self, id_proveedor, nombre=None, fecha_entrega=None, costo=None, telefono_vendedor=None):
        """
        Actualiza los detalles del proveedor.
        :param id_proveedor: ID del proveedor a actualizar.
        :param nombre: Nuevo nombre (opcional).
        :param fecha_entrega: Nueva fecha de entrega (opcional).
        :param costo: Nuevo costo (opcional).
        :param telefono_vendedor: Nuevo teléfono de vendedor (opcional).
        :return: Mensaje de éxito.
        """
        proveedor = self.proveedor_repository.get_by_id(id_proveedor)
        if not proveedor:
            raise ValueError("Proveedor no encontrado.")

        return proveedor.actualizar_detalles(nombre, fecha_entrega, costo, telefono_vendedor)
