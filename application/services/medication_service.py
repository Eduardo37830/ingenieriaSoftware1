from ingenieriaSoftware1.domain.repositories.i_medicamento_repository import IMedicamentoRepository

class MedicationService:
    def __init__(self, medication_repository: IMedicamentoRepository):
        self.medication_repository = medication_repository

    def manage_inventory(self, medication_id: int, quantity: int) -> None:
        """Actualizar el inventario de medicamentos."""
        medication = self.medication_repository.find_by_id(medication_id)
        medication.update_quantity(quantity)
        self.medication_repository.save(medication)

    def check_stock(self, medication_id: int, required_quantity: int) -> bool:
        """Verificar si hay suficiente stock de un medicamento."""
        medication = self.medication_repository.find_by_id(medication_id)
        return medication.verify_availability(required_quantity)
