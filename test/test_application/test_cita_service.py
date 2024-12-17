import unittest
from unittest.mock import MagicMock
from ingenieriaSoftware1.application.services.cita_service import CitaService
from ingenieriaSoftware1.application.dtos.cita_dto import CitaDTO
from ingenieriaSoftware1.domain.entities.cita import Cita
from ingenieriaSoftware1.domain.repositories.i_cita_repository import ICitaRepository as CitaRepository


class TestCitaService(unittest.TestCase):

    def setUp(self):
        """
        Configura el entorno antes de cada test.
        """
        # Crear un mock con spec para el repositorio
        self.cita_repository = MagicMock(spec=CitaRepository)
        self.cita_service = CitaService(self.cita_repository)

        # Creamos una cita de ejemplo
        self.cita = Cita(
            id=1,
            usuario_id=1,
            fecha="2024-12-20",
            hora="10:00",
            detalles="Consulta médica general"
        )

    def test_crear_cita_correcta(self):
        """
        Test para crear una cita con datos correctos.
        """
        print("Ejecutando test: test_crear_cita_correcta")
        # Simulamos que el repositorio devuelve la cita creada
        self.cita_repository.crear.return_value = self.cita

        # Ejecutamos el método de creación de cita
        cita_dto = self.cita_service.crear_cita(1, "2024-12-20", "10:00", "Consulta médica general")

        # Verificamos que se haya devuelto el DTO de la cita
        self.assertIsInstance(cita_dto, CitaDTO)
        self.assertEqual(cita_dto.id, 1)
        self.assertEqual(cita_dto.usuario_id, 1)
        self.assertEqual(cita_dto.fecha, "2024-12-20")
        self.assertEqual(cita_dto.hora, "10:00")
        self.assertEqual(cita_dto.detalles, "Consulta médica general")

        # Verificar que se llamó correctamente al método del repositorio
        self.cita_repository.crear.assert_called_once_with(1, "2024-12-20", "10:00", "Consulta médica general")
        print("Resultado del test: Cita creada correctamente.")

    def test_obtener_cita_por_id(self):
        """
        Test para obtener una cita por su ID.
        """
        print("Ejecutando test: test_obtener_cita_por_id")
        # Simulamos que el repositorio devuelve la cita correcta
        self.cita_repository.buscar_por_id.return_value = self.cita

        # Ejecutamos el método de obtención de cita por ID
        cita_dto = self.cita_service.obtener_cita_por_id(1)

        # Verificamos que se haya devuelto el DTO de la cita
        self.assertIsInstance(cita_dto, CitaDTO)
        self.assertEqual(cita_dto.id, 1)
        self.assertEqual(cita_dto.usuario_id, 1)
        self.assertEqual(cita_dto.fecha, "2024-12-20")
        self.assertEqual(cita_dto.hora, "10:00")
        self.assertEqual(cita_dto.detalles, "Consulta médica general")

        # Verificar que se llamó correctamente al método del repositorio
        self.cita_repository.buscar_por_id.assert_called_once_with(1)
        print("Resultado del test: Cita obtenida correctamente.")

    def test_obtener_cita_por_id_no_existente(self):
        """
        Test cuando la cita no existe en la base de datos.
        """
        print("Ejecutando test: test_obtener_cita_por_id_no_existente")
        # Simulamos que el repositorio no encuentra la cita
        self.cita_repository.buscar_por_id.return_value = None

        # Ejecutamos el método de obtención de cita por ID
        cita_dto = self.cita_service.obtener_cita_por_id(99)

        # Verificamos que no se encontró la cita
        self.assertIsNone(cita_dto)

        # Verificar que se llamó correctamente al método del repositorio
        self.cita_repository.buscar_por_id.assert_called_once_with(99)
        print("Resultado del test: Cita no encontrada verificada.")

    def test_eliminar_cita_existente(self):
        """
        Test para eliminar una cita existente.
        """
        print("Ejecutando test: test_eliminar_cita_existente")
        # Simulamos que la cita existe
        self.cita_repository.buscar_por_id.return_value = self.cita
        self.cita_repository.eliminar = MagicMock()

        # Ejecutamos el método para eliminar la cita
        resultado = self.cita_service.eliminar_cita(1)

        # Verificamos que la eliminación fue exitosa
        self.assertTrue(resultado)

        # Verificar que se llamaron los métodos correctos del repositorio
        self.cita_repository.buscar_por_id.assert_called_once_with(1)
        self.cita_repository.eliminar.assert_called_once_with(1)
        print("Resultado del test: Cita eliminada correctamente.")

    def test_eliminar_cita_no_existente(self):
        """
        Test para intentar eliminar una cita que no existe.
        """
        print("Ejecutando test: test_eliminar_cita_no_existente")
        # Simulamos que la cita no existe
        self.cita_repository.buscar_por_id.return_value = None
        self.cita_repository.eliminar = MagicMock()

        # Ejecutamos el método para eliminar la cita
        resultado = self.cita_service.eliminar_cita(1)

        # Verificamos que la eliminación no fue exitosa
        self.assertFalse(resultado)

        # Verificar que se llamaron los métodos correctos del repositorio
        self.cita_repository.buscar_por_id.assert_called_once_with(1)
        self.cita_repository.eliminar.assert_not_called()
        print("Resultado del test: Cita no encontrada para eliminar verificada.")


if __name__ == '__main__':
    unittest.main()
