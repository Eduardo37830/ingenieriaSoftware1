from ingenieriaSoftware1.domain.entities.medicamento import Medicamento
from typing import List

class MedicamentoService:
    def __init__(self, medicamento_repository):
        self.medicamento_repository = medicamento_repository

    def gestionarInventario(self, idMedicamento: int, cantidad: int):
        # Gestionar inventario (aumentar o disminuir cantidad)
        medicamento = self.medicamento_repository.obtenerPorId(idMedicamento)
        medicamento.actualizarCantidad(cantidad)

    def verificarStock(self, idMedicamento: int, cantidadRequerida: int) -> bool:
        # Verificar si hay suficiente stock
        medicamento = self.medicamento_repository.obtenerPorId(idMedicamento)
        return medicamento.verificarDisponibilidad(cantidadRequerida)
