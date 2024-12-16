from ingenieriaSoftware1.domain.entities.patient import Patient
from ingenieriaSoftware1.domain.entities.medicalHistory import HistorialMedico
from ingenieriaSoftware1.domain.repositories.i_cita_repository import ICitaRepository

class PatientService:
    def __init__(self, appointment_repository: ICitaRepository):
        self.appointment_repository = appointment_repository

    def register_patient(self, patient: Patient) -> None:
        """Registrar la información del paciente."""
        patient.save()

    def add_medical_history_entry(self, patient: Patient, history_entry: HistorialMedico) -> None:
        """Agregar una entrada al historial médico."""
        patient.add_history_entry(history_entry)

    def list_appointments(self, patient_id: int):
        """Consultar las citas programadas."""
        return self.appointment_repository.find_all_by_paciente(patient_id)

    def cancel_appointment(self, appointment_id: int) -> None:
        """Cancelar una cita."""
        self.appointment_repository.delete(appointment_id)
