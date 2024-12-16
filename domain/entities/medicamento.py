from datetime import datetime

class Medicamento:
    def __init__(self, id: int, nombre: str, tipoMedicamento: str, fechaFabricacion: datetime, fechaVencimiento: datetime, cantidad: int):
        self.id = id
        self.nombre = nombre
        self.tipoMedicamento = tipoMedicamento
        self.fechaFabricacion = fechaFabricacion
        self.fechaVencimiento = fechaVencimiento
        self.cantidad = cantidad

    def verificarDisponibilidad(self, cantidadRequerida: int) -> bool:
        return self.cantidad >= cantidadRequerida

    def actualizarCantidad(self, cantidad: int):
        self.cantidad += cantidad
