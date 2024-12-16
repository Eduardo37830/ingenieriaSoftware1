import unittest
from unittest.mock import Mock
from datetime import datetime, time
from ingenieriaSoftware1.application.services.appointment_service import AppointmentService
from ingenieriaSoftware1.domain.entities.cita import Cita
from ingenieriaSoftware1.domain.entities.medicalStaff import MedicalStaff  # Asegúrate de importar correctamente
from ingenieriaSoftware1.domain.entities.patient import Patient  # Asegúrate de importar correctamente


class TestAppointmentService(unittest.TestCase):
    def setUp(self):
        # Mock repositorios
        self.appointment_repository = Mock()
        self.personal_repository = Mock()

        # Crear instancia del servicio
        self.service = AppointmentService(
            appointment_repository=self.appointment_repository,
            personal_repository=self.personal_repository
        )

    def test_schedule_appointment_success(self):
        # Configurar mocks
        self.personal_repository.check_availability.return_value = True

        # Crear datos de prueba
        work_start_time = time(8, 0)  # Hora de inicio del turno
        work_end_time = time(17, 0)  # Hora de fin del turno
        personal_medico = MedicalStaff(
            id=1,
            name="Dr. Juan",
            email="juan.medico@example.com",
            password="password123",
            role="Medico",
            address="Calle Medica 456",
            phone="9876543210",
            documentType="DNI",
            documentNumber="87654321",
            availability=True,
            workStartTime=work_start_time,
            workEndTime=work_end_time,
            specialization="Cardiología",
            department=101
        )

        # Crear paciente con todos los atributos requeridos
        paciente = Patient(
            userid=1,
            name="Carlos Pérez",
            email="carlos.perez@example.com",
            password="password123",
            role="Paciente",
            address="Calle Falsa 123",
            phone="1234567890",
            documentType="DNI",
            documentNumber="12345678"
        )

        # Crear cita con los datos del paciente y el médico
        cita = Cita(
            id=1,
            motivoConsulta="Consulta de rutina",
            fechaHoraConsulta=datetime(2024, 12, 16, 10, 0),  # Fecha y hora de la cita
            paciente=paciente,  # Asignar paciente a la cita
            personalMedico=personal_medico,  # Asignar médico a la cita
            totalAPagar=50.0
        )

        # Ejecutar método
        self.service.schedule_appointment(cita)

        # Verificar interacciones
        self.personal_repository.check_availability.assert_called_once_with(1, datetime(2024, 12, 16, 10, 0))
        self.appointment_repository.save.assert_called_once_with(cita)

    def test_schedule_appointment_failure_due_to_unavailability(self):
        # Configurar mocks
        self.personal_repository.check_availability.return_value = False

        # Crear datos de prueba
        work_start_time = time(8, 0)  # Hora de inicio del turno
        work_end_time = time(17, 0)  # Hora de fin del turno
        personal_medico = MedicalStaff(
            id=1,
            name="Dr. Juan",
            email="juan.medico@example.com",
            password="password123",
            role="Medico",
            address="Calle Medica 456",
            phone="9876543210",
            documentType="DNI",
            documentNumber="87654321",
            availability=True,
            workStartTime=work_start_time,
            workEndTime=work_end_time,
            specialization="Cardiología",
            department=101
        )

        # Crear paciente con todos los atributos requeridos
        paciente = Patient(
            userid=1,
            name="Carlos Pérez",
            email="carlos.perez@example.com",
            password="password123",
            role="Paciente",
            address="Calle Falsa 123",
            phone="1234567890",
            documentType="DNI",
            documentNumber="12345678"
        )

        # Crear cita con los datos del paciente y el médico
        cita = Cita(
            id=1,
            motivoConsulta="Consulta de rutina",
            fechaHoraConsulta=datetime(2024, 12, 16, 10, 0),  # Fecha y hora de la cita
            paciente=paciente,  # Asignar paciente a la cita
            personalMedico=personal_medico,  # Asignar médico a la cita
            totalAPagar=50.0
        )

        # Ejecutar y verificar excepción
        with self.assertRaises(Exception) as context:
            self.service.schedule_appointment(cita)
        self.assertEqual(str(context.exception), "El personal médico no está disponible.")

        # Verificar que no se guardó la cita
        self.appointment_repository.save.assert_not_called()


if __name__ == "__main__":
    unittest.main()
