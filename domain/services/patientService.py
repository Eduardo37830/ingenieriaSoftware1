from domain.entities.paciente import Patient
from domain.entities.cita import Cita
from domain.repositories.i_cita_repository import ICitaRepository

class PatientService:
    def __init__(self, cita_repository: ICitaRepository):
        # Inicializa el servicio con un repositorio de citas.
        self.cita_repository = cita_repository

    def schedule_appointment(self, patient: Patient, appointment: Cita) -> None:
        """Agenda una cita para un paciente."""
        if appointment.medical_staff.is_available(appointment.date_time):
            self.cita_repository.save(appointment)
        else:
            raise ValueError("El personal médico no está disponible en la fecha y hora seleccionadas.")

    def cancel_appointment(self, appointment_id: int) -> None:
        """Cancela una cita programada."""
        appointment = self.cita_repository.find_by_id(appointment_id)
        if not appointment:
            raise ValueError("Cita no encontrada.")
        self.cita_repository.delete(appointment_id)

    def get_patient_appointments(self, patient_id: int):
        """Obtiene todas las citas de un paciente."""
        return self.cita_repository.find_all_by_paciente(patient_id)
