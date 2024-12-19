import unittest
from unittest.mock import Mock
from datetime import datetime
from application.dtos.cita_dto import CitaDTO
from application.exceptions.application_error import NotFoundError
from application.services.cita_service import CitaApplicationService

class TestCitaApplicationService(unittest.TestCase):
    def setUp(self):
        """Configurar el entorno de prueba."""
        print("\nConfigurando entorno de prueba...")
        # Crear un mock para el repositorio de citas
        self.cita_repository = Mock()
        self.cita_service = CitaApplicationService(self.cita_repository)

        # Configuración de datos ficticios
        self.fecha = datetime(2024, 6, 20)
        self.hora = datetime(2024, 6, 20, 10, 0, 0)
        self.motivo = "Consulta general"
        self.paciente_id = 1
        self.personalMedico_id = 2
        self.habitacion_id = 5

        # Datos ficticios de cita
        self.cita_dto = CitaDTO(
            id=1,
            motivoConsulta=self.motivo,
            fechaConsulta=self.fecha,
            horaConsulta=self.hora,
            paciente_id=self.paciente_id,
            personalMedico_id=self.personalMedico_id,
            habitacion_id=self.habitacion_id
        )

    def test_registrar_cita(self):
        """Prueba para registrar una nueva cita."""
        print("Iniciando test_registrar_cita...")
        # Configurar el repositorio mock para devolver una cita con ID asignado
        cita_guardada = self.cita_dto.to_entity()
        cita_guardada.id = 1  # Asignar un ID después de guardar la cita

        #Guardar la cita
        self.cita_repository.save.return_value = 2
        self.cita_repository.find_by_id.return_value = cita_guardada  # Simular que la cita fue guardada

        # Registrar la cita
        cita_creada = self.cita_service.registrar_cita(self.cita_dto)

        # Verificar que la cita fue registrada correctamente
        self.cita_repository.save.assert_called_once()
        self.assertEqual(cita_creada.id, 1)  # El ID debe ser 1 después de ser asignado automáticamente
        print("Finalizando test_registrar_cita...")

    def test_obtener_cita_por_id(self):
        """Prueba para obtener una cita por su ID."""
        print("Iniciando test_obtener_cita_por_id...")
        # Configurar el repositorio mock para devolver una cita
        self.cita_repository.find_by_id.return_value = self.cita_dto.to_entity()

        # Obtener la cita
        cita_obtenida = self.cita_service.obtener_cita_por_id(1)

        # Verificar que la cita se obtuvo correctamente
        self.assertEqual(cita_obtenida.id, 1)
        self.assertEqual(cita_obtenida.motivoConsulta, self.motivo)
        print("Finalizando test_obtener_cita_por_id...")

    def test_obtener_cita_por_id_no_encontrada(self):
        """Prueba cuando la cita no se encuentra por su ID."""
        print("Iniciando test_obtener_cita_por_id_no_encontrada...")
        # Configurar el repositorio mock para devolver None
        self.cita_repository.find_by_id.return_value = None

        # Verificar que se lanza la excepción NotFoundError
        with self.assertRaises(NotFoundError):
            self.cita_service.obtener_cita_por_id(999)
        print("Finalizando test_obtener_cita_por_id_no_encontrada...")

    def test_verificar_conflicto(self):
        """Prueba para verificar si una cita entra en conflicto con otras."""
        print("Iniciando test_verificar_conflicto...")
        # Crear una cita ficticia para comparar
        cita_conflictiva = CitaDTO(
            id=2,
            motivoConsulta="Consulta de seguimiento",
            fechaConsulta=self.fecha,
            horaConsulta=self.hora,
            paciente_id=2,
            personalMedico_id=self.personalMedico_id,
            habitacion_id=self.habitacion_id
        )

        # Configurar el repositorio mock para devolver citas existentes
        self.cita_repository.find_all.return_value = [self.cita_dto.to_entity()]

        # Verificar que el conflicto se detecta
        conflicto_detectado = self.cita_service.verificar_conflicto(cita_conflictiva)
        self.assertTrue(conflicto_detectado)
        print("Finalizando test_verificar_conflicto...")

    def test_crear_cita(self):
        """Prueba para crear una nueva cita médica."""
        print("Iniciando test_crear_cita...")
        # Configurar el repositorio mock para devolver la cita creada
        self.cita_repository.save.return_value = None
        self.cita_repository.find_by_id.return_value = self.cita_dto.to_entity()

        # Llamar al servicio para crear la cita
        cita_creada = self.cita_service.crear_cita(
            paciente_id=self.paciente_id,
            fecha=self.fecha,
            hora=self.hora,
            motivo=self.motivo,
            personalMedico_id=self.personalMedico_id,
            habitacion_id=self.habitacion_id
        )

        # Verificar que la cita fue creada correctamente
        self.cita_repository.save.assert_called_once()
        self.assertEqual(cita_creada.motivoConsulta, self.motivo)
        self.assertEqual(cita_creada.horaConsulta, self.hora)
        print("Finalizando test_crear_cita...")

    def test_eliminar_cita(self):
        """Prueba para eliminar una cita existente."""
        print("Iniciando test_eliminar_cita...")
        # Configurar el repositorio mock para devolver la cita
        self.cita_repository.find_by_id.return_value = self.cita_dto.to_entity()

        # Llamar al servicio para eliminar la cita
        resultado = self.cita_service.eliminar_cita(1)

        # Verificar que la cita fue eliminada correctamente
        self.cita_repository.eliminar.assert_called_once_with(1)
        self.assertTrue(resultado)
        print("Finalizando test_eliminar_cita...")

    def test_eliminar_cita_no_encontrada(self):
        """Prueba para eliminar una cita que no existe."""
        print("Iniciando test_eliminar_cita_no_encontrada...")
        # Configurar el repositorio mock para devolver None (no encontrado)
        self.cita_repository.find_by_id.return_value = None

        # Llamar al servicio para intentar eliminar una cita que no existe
        resultado = self.cita_service.eliminar_cita(999)

        # Verificar que la cita no fue eliminada
        self.cita_repository.eliminar.assert_not_called()
        self.assertFalse(resultado)
        print("Finalizando test_eliminar_cita_no_encontrada...")

if __name__ == "__main__":
    unittest.main()
