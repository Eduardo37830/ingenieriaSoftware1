import unittest
from unittest.mock import Mock
from ingenieriaSoftware1.application.services.medicamento_service import MedicationService
from ingenieriaSoftware1.domain.entities.medicamento import Medicamento


class TestMedicationService(unittest.TestCase):
    def setUp(self):
        # Mock del repositorio
        self.medication_repository = Mock()

        # Crear instancia del servicio
        self.service = MedicationService(
            medication_repository=self.medication_repository
        )

    def test_register_medication(self):
        # Crear datos de prueba
        medicamento = Medicamento(id=1, nombre="Paracetamol", stock=100)

        # Ejecutar método
        self.service.register_medication(medicamento)

        # Verificar interacción
        self.medication_repository.save.assert_called_once_with(medicamento)

    def test_find_low_stock_medications(self):
        # Configurar mock
        low_stock = [Medicamento(id=1, nombre="Ibuprofeno", stock=5)]
        self.medication_repository.find_low_stock.return_value = low_stock

        # Ejecutar método
        result = self.service.find_low_stock_medications(10)

        # Verificar resultados
        self.medication_repository.find_low_stock.assert_called_once_with(10)
        self.assertEqual(result, low_stock)


if __name__ == "__main__":
    unittest.main()
