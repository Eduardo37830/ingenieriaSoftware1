from datetime import datetime


class Medicamento:
    def __init__(self, medicamento_id, nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad):
        """
        Clase para representar un medicamento.
        :param medicamento_id: ID único del medicamento.
        :param nombre: Nombre del medicamento.
        :param tipoMedicamento: Tipo de medicamento (por ejemplo, "Analgésico").
        :param fechaFabricacion: Fecha de fabricación (datetime).
        :param fechaVencimiento: Fecha de vencimiento (datetime).
        :param cantidad: Cantidad disponible en inventario.
        """
        self.medicamento_id = medicamento_id
        self.nombre = nombre
        self.tipoMedicamento = tipoMedicamento
        self.fechaFabricacion = fechaFabricacion
        self.fechaVencimiento = fechaVencimiento
        self.cantidad = cantidad

    def verificarDisponibilidad(self, cantidadRequerida):
        """
        Verifica si hay suficiente cantidad disponible.
        :param cantidadRequerida: Cantidad requerida.
        :return: True si hay suficiente cantidad, False en caso contrario.
        """
        return self.cantidad >= cantidadRequerida

    def actualizarCantidad(self, cantidad):
        """
        Actualiza la cantidad del medicamento en inventario.
        :param cantidad: Valor a añadir (positivo) o reducir (negativo).
        :return: Mensaje indicando el resultado.
        """
        self.cantidad += cantidad
        return f"Cantidad actualizada. Nueva cantidad: {self.cantidad}."

    def verificarSiExpirado(self):
        """
        Verifica si el medicamento está expirado.
        :return: True si está expirado, False en caso contrario.
        """
        return datetime.now() > self.fechaVencimiento

    def __str__(self):
        """
        Representación en texto del medicamento.
        """
        estado = "Expirado" if self.verificarSiExpirado() else "Vigente"
        return (
            f"Medicamento ID: {self.medicamento_id}\n"
            f"Nombre: {self.nombre}\n"
            f"Tipo: {self.tipoMedicamento}\n"
            f"Fabricación: {self.fechaFabricacion}\n"
            f"Vencimiento: {self.fechaVencimiento} ({estado})\n"
            f"Cantidad: {self.cantidad}\n"
        )
