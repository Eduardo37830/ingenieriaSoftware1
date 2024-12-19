import unittest
from unittest.mock import MagicMock
from application.services.medicamento_service import MedicamentoApplicationService
from application.dtos.medicamento_dto import MedicamentoDTO
from domain.entities.medicamento import Medicamento
from domain.repositories.i_medicamento_repository import IMedicamentoRepository


class TestMedicamentoApplicationService(unittest.TestCase):

    def setUp(self):
        """
        Configura los mocks y objetos de prueba antes de cada test.
        """
        self.medicamento_repository = MagicMock(spec=IMedicamentoRepository)
        self.medicamento_service = MedicamentoApplicationService(self.medicamento_repository)

        # Datos de prueba
        self.medicamento = Medicamento(
            medicamento_id=1,
            nombre="Ibuprofeno",
            tipoMedicamento="Analgésico",
            fechaFabricacion="2024-11-01",
            fechaVencimiento="2025-11-01",
            cantidad=100,
            id_proveedor=1
        )

        self.medicamento_dto = MedicamentoDTO(
            medicamento_id=1,
            nombre="Ibuprofeno",
            tipoMedicamento="Analgésico",
            fechaFabricacion="2024-11-01",
            fechaVencimiento="2025-11-01",
            cantidad=100,
            id_proveedor=1
        )

    def test_registrar_medicamento(self):
        """
        Verifica el registro de un medicamento.
        """
        print("Ejecutando test: test_registrar_medicamento")
        # Simular que no hay duplicados en el repositorio
        self.medicamento_repository.buscar_por_id.return_value = None

        # Ejecutar el método
        resultado = self.medicamento_service.registrar_medicamento(self.medicamento_dto)

        # Verificar el resultado
        self.assertEqual(resultado, "Medicamento registrado correctamente.")
        self.medicamento_repository.guardar.assert_called_once()
        print("Resultado: Medicamento registrado correctamente.")

    def test_consultar_medicamento(self):
        """
        Verifica la consulta de un medicamento por su ID.
        """
        print("Ejecutando test: test_consultar_medicamento")
        self.medicamento_repository.buscar_por_id.return_value = self.medicamento

        # Ejecutar el método
        medicamento = self.medicamento_service.consultar_medicamento(1)

        # Verificar el resultado
        self.assertEqual(medicamento.nombre, "Ibuprofeno")
        self.medicamento_repository.buscar_por_id.assert_called_once_with(1)
        print(f"Resultado: Medicamento consultado correctamente: {medicamento}")

    def test_actualizar_medicamento(self):
        """
        Verifica la actualización de un medicamento.
        """
        print("Ejecutando test: test_actualizar_medicamento")
        self.medicamento_repository.buscar_por_id.return_value = self.medicamento

        # DTO con nuevos datos
        medicamento_dto_actualizado = MedicamentoDTO(
            medicamento_id=1,
            nombre="Paracetamol",
            tipoMedicamento="Antipirético",
            fechaFabricacion="2024-10-01",
            fechaVencimiento="2025-10-01",
            cantidad=150,
            id_proveedor=1
        )

        # Ejecutar el método
        resultado = self.medicamento_service.actualizar_medicamento(medicamento_dto_actualizado)

        # Verificar el resultado
        self.assertEqual(resultado, "Medicamento actualizado correctamente.")
        self.assertEqual(self.medicamento.nombre, "Paracetamol")
        self.assertEqual(self.medicamento.cantidad, 150)
        self.medicamento_repository.guardar.assert_called_once_with(self.medicamento)
        print("Resultado: Medicamento actualizado correctamente.")

    def test_eliminar_medicamento(self):
        """
        Verifica la eliminación de un medicamento existente.
        """
        print("Ejecutando test: test_eliminar_medicamento")
        self.medicamento_repository.buscar_por_id.return_value = self.medicamento

        # Ejecutar el método
        resultado = self.medicamento_service.eliminar_medicamento(1)

        # Verificar el resultado
        self.assertTrue(resultado)
        self.medicamento_repository.buscar_por_id.assert_called_once_with(1)
        self.medicamento_repository.eliminar.assert_called_once_with(1)
        print("Resultado: Medicamento eliminado correctamente.")

    def test_eliminar_medicamento_no_existente(self):
        """
        Verifica el intento de eliminar un medicamento que no existe.
        """
        print("Ejecutando test: test_eliminar_medicamento_no_existente")
        self.medicamento_repository.buscar_por_id.return_value = None

        # Ejecutar el método
        resultado = self.medicamento_service.eliminar_medicamento(99)

        # Verificar el resultado
        self.assertFalse(resultado)
        self.medicamento_repository.buscar_por_id.assert_called_once_with(99)
        self.medicamento_repository.eliminar.assert_not_called()
        print("Resultado: Medicamento no encontrado para eliminar.")

if __name__ == '__main__':
    unittest.main()
