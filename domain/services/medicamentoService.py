from typing import Dict, Any

from domain.repositories.i_medicamento_repository import IMedicamentoRepository
from domain.entities.medicamento import Medicamento


class MedicationService:
    def __init__(self, medicamento_repository: IMedicamentoRepository):
        """
        Inicializa el servicio con un repositorio de medicamentos.
        :param medicamento_repository: Repositorio que maneja los medicamentos.
        """
        self.medicamento_repository = medicamento_repository

    def manage_inventory(self, medicamento_id: int, cantidad: int) -> dict:
        """
        Actualiza el inventario de un medicamento.
        :param medicamento_id: ID del medicamento.
        :param cantidad: Cantidad a agregar (positiva) o reducir (negativa).
        :return: Mensaje indicando el resultado de la operación.
        """
        medicamento = self.medicamento_repository.find_by_id(medicamento_id)
        if not medicamento:
            raise ValueError(f"El medicamento con ID {medicamento_id} no existe.")

        medicamento.actualizarCantidad(cantidad)
        self.medicamento_repository.save(medicamento)
        return {"mensaje": "Inventario actualizado", "stock_actual": medicamento.cantidad}

    def verify_stock(self, medicamento_id: int, cantidad_requerida: int) -> bool:
        """
        Verifica si hay suficiente stock de un medicamento.
        :param medicamento_id: ID del medicamento.
        :param cantidad_requerida: Cantidad que se requiere.
        :return: True si hay suficiente stock, False de lo contrario.
        """
        medicamento = self.medicamento_repository.find_by_id(medicamento_id)
        if not medicamento:
            raise ValueError(f"El medicamento con ID {medicamento_id} no existe.")

        # Verificar disponibilidad
        return medicamento.verificarDisponibilidad(cantidad_requerida)

    def get_low_stock_medications(self, umbral: int) -> list[Medicamento]:
        """
        Obtiene una lista de medicamentos con stock por debajo del umbral.
        :param umbral: Valor mínimo de stock para considerar como bajo.
        :return: Lista de medicamentos con stock bajo.
        """
        return self.medicamento_repository.find_low_stock(umbral)

    def get_expired_medications(self) -> list[Medicamento]:
        """
        Obtiene una lista de medicamentos expirados.
        :return: Lista de medicamentos cuya fecha de vencimiento ha pasado.
        """
        all_medications = self.medicamento_repository.find_all()
        return [med for med in all_medications if med.verificarSiExpirado()]

    def get_all_medications(self) -> list[Medicamento]:
        """
        Obtiene todos los medicamentos registrados en el sistema.
        :return: Lista de medicamentos.
        """
        return self.medicamento_repository.find_all()
