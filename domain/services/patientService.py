from domain.entities.paciente import Paciente
from domain.entities.cita import Cita
from domain.repositories.i_cita_repository import ICitaRepository


class PatientService:
    def __init__(self, cita_repository: ICitaRepository):
        """
        Inicializa el servicio con un repositorio de citas.
        """
        self.cita_repository = cita_repository

    def schedule_appointment(self, patient: Paciente, appointment: Cita) -> None:
        """
        Agenda una cita para un paciente.

        Args:
            patient (Paciente): Instancia del paciente que agenda la cita.
            appointment (Cita): Instancia de la cita médica a agendar.

        Raises:
            ValueError: Si el personal médico no está disponible o hay un conflicto.
        """
        # Verificar disponibilidad del personal médico en la fecha y hora de la cita
        existing_appointments = self.cita_repository.find_all_by_personal_medico(appointment.personalMedico_id)
        for existing in existing_appointments:
            if appointment.verificarConflicto(existing):
                raise ValueError("El personal médico no está disponible en la fecha y hora seleccionadas.")

        # Guardar la cita si no hay conflictos
        self.cita_repository.save(appointment)

    def cancel_appointment(self, appointment_id: int) -> None:
        """
        Cancela una cita programada.

        Args:
            appointment_id (int): ID de la cita a cancelar.

        Raises:
            ValueError: Si la cita no existe.
        """
        appointment = self.cita_repository.find_by_id(appointment_id)
        if not appointment:
            raise ValueError("Cita no encontrada.")

        # Eliminar la cita si existe
        self.cita_repository.delete(appointment_id)

    def get_patient_appointments(self, patient_id: int):
        """
        Obtiene todas las citas de un paciente.

        Args:
            patient_id (int): ID del paciente.

        Returns:
            list: Lista de citas asociadas al paciente.
        """
        return self.cita_repository.find_all_by_paciente(patient_id)
