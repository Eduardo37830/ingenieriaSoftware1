import unittest
from unittest.mock import Mock
from ingenieriaSoftware1.application.services.paciente_service import PatientService
from ingenieriaSoftware1.domain.entities.patient import Patient
from ingenieriaSoftware1.domain.entities.medicalHistory import HistorialMedico


class TestPatientService(unittest.TestCase):
    def setUp(self):
        # Mock del repositorio
        self.patient_repository = Mock()
        self.medical_history_repository = Mock()

        # Crear instancia del servicio
        self.service = PatientService(
            patient_repository=self.patient_repository,
            medical_history_repository=self.medical_history_repository
        )

    def test_register_patient(self):
        # Crear datos de prueba
        patient = Patient(id=1, nombre="Carlos Pérez", direccion="Calle 123")

        # Ejecutar método
        self.service.register_patient(patient)

        # Verificar interacción
        self.patient_repository.save.assert_called_once_with(patient)

    def test_get_medical_history(self):
        # Configurar mock
        history = HistorialMedico(entries=["Consulta general", "Radiografía"])
        self.medical_history_repository.find_by_patient_id.return_value = history

        # Ejecutar método
        result = self.service.get_medical_history(1)

        # Verificar resultados
        self.medical_history_repository.find_by_patient_id.assert_called_once_with(1)
        self.assertEqual(result, history)


if __name__ == "__main__":
    unittest.main()
