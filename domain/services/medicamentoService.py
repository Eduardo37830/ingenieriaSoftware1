from ingenieriaSoftware1.domain.repositories.i_medicamento_repository import IMedicamentoRepository
from ingenieriaSoftware1.domain.entities.medicamento import Medicamento


class MedicationService:
    def __init__(self, medicamento_repository: IMedicamentoRepository):
        # Inicializa el servicio con un repositorio de medicamentos.
        self.medicamento_repository = medicamento_repository

    def manage_inventory(self, medication_id: int, quantity: int) -> None:
        """Actualiza el inventario de un medicamento."""
        # Busca el medicamento por su ID.
        medication = self.medicamento_repository.find_by_id(medication_id)
        if not medication:
            raise ValueError("El medicamento con el ID proporcionado no existe.")

        # Actualiza la cantidad en inventario.
        medication.update_quantity(quantity)
        self.medicamento_repository.save(medication)

    def verify_stock(self, medication_id: int, required_quantity: int) -> bool:
        """Verifica si hay suficiente stock de un medicamento."""
        # Busca el medicamento por su ID.
        medication = self.medicamento_repository.find_by_id(medication_id)
        if not medication:
            raise ValueError("El medicamento con el ID proporcionado no existe.")

        # Verifica si la cantidad requerida está disponible.
        return medication.is_available(required_quantity)

    def get_low_stock_medications(self, threshold: int) -> list[Medicamento]:
        """Obtiene una lista de medicamentos con stock bajo."""
        # Busca medicamentos con stock por debajo del umbral.
        return self.medicamento_repository.find_low_stock(threshold)

    def get_all_medications(self) -> list[Medicamento]:
        """Obtiene todos los medicamentos registrados en el sistema."""
        # Devuelve todos los medicamentos del repositorio.
        return self.medicamento_repository.find_all()
