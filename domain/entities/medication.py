from datetime import datetime

class Medication:
    def __init__(self, medicamento_id, name, medicationType, manufactureDate, expirationDate, quantity):
        """
        Clase para representar un medicamento.
        :param medicamento_id: ID único del medicamento.
        :param name: Nombre del medicamento.
        :param medicationType: Tipo de medicamento (por ejemplo, "Analgésico").
        :param manufactureDate: Fecha de fabricación (datetime).
        :param expirationDate: Fecha de vencimiento (datetime).
        :param quantity: Cantidad disponible en inventario.
        """
        self.medicamento_id = medicamento_id
        self.name = name
        self.medicationType = medicationType
        self.manufactureDate = manufactureDate
        self.expirationDate = expirationDate
        self.quantity = quantity

    def verificarDisponibilidad(self, cantidadRequerida):
        """
        Verifica si hay suficiente cantidad disponible.
        :param cantidadRequerida: Cantidad requerida.
        :return: True si hay suficiente cantidad, False en caso contrario.
        """
        return self.quantity >= cantidadRequerida

    def actualizarCantidad(self, cantidad):
        """
        Actualiza la cantidad del medicamento en inventario.
        :param cantidad: Valor a añadir (positivo) o reducir (negativo).
        :return: Mensaje indicando el resultado.
        """
        self.quantity += cantidad
        return f"Cantidad actualizada. Nueva cantidad: {self.quantity}."

    def verificarSiExpirado(self):
        """
        Verifica si el medicamento está expirado.
        :return: True si está expirado, False en caso contrario.
        """
        return datetime.now() > self.expirationDate

    def __str__(self):
        """
        Representación en texto del medicamento.
        """
        estado = "Expirado" if self.verificarSiExpirado() else "Vigente"
        return (
            f"Medicamento ID: {self.medicamento_id}\n"
            f"Nombre: {self.name}\n"
            f"Tipo: {self.medicationType}\n"
            f"Fabricación: {self.manufactureDate}\n"
            f"Vencimiento: {self.expirationDate} ({estado})\n"
            f"Cantidad: {self.quantity}\n"
        )
