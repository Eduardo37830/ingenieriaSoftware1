from ingenieriaSoftware1.domain.entities.cita import Cita
from ingenieriaSoftware1.domain.repositories.i_cita_repository import ICitaRepository
from ingenieriaSoftware1.domain.repositories.i_personalMedico_repository import IPersonalMedicoRepository

class AppointmentService:
    def __init__(self, appointment_repository: ICitaRepository, personal_repository: IPersonalMedicoRepository):
        self.appointment_repository = appointment_repository
        self.personal_repository = personal_repository

    def schedule_appointment(self, appointment: Cita) -> None:
        """Agendar una cita si el personal médico está disponible."""
        available = self.personal_repository.check_availability(
            appointment.personal_medico.id,
            appointment.fechaHoraConsulta
        )
        if not available:
            raise Exception("El personal médico no está disponible.")
        self.appointment_repository.save(appointment)

    def cancel_appointment(self, appointment_id: int) -> None:
        """Cancelar una cita."""
        self.appointment_repository.delete(appointment_id)

    def list_appointments_by_patient(self, patient_id: int):
        """Consultar las citas de un paciente."""
        return self.appointment_repository.find_all_by_paciente(patient_id)
