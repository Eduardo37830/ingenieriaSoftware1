from datetime import datetime
from application.dtos.personal_medico_dto import PersonalMedicoDTO
from domain.repositories.i_personalMedico_repository import IPersonalMedicoRepository
class PersonalMedicoService:
    def __init__(self, personal_repository: IPersonalMedicoRepository):
        """
        Inicializa el servicio con el repositorio que gestionará el acceso a los datos.
        :param repository: Repositorio para interactuar con la base de datos.
        """
        self.personal_repository = personal_repository

    def verificar_disponibilidad(self, medico_id, fecha_hora):
        """
        Verifica si un médico está disponible para una cita en la fecha y hora especificada.
        :param medico_id: ID del médico.
        :param fecha_hora: Fecha y hora para verificar la disponibilidad.
        :return: Verdadero si el médico está disponible, falso en caso contrario.
        """
        medico = self.personal_repository.obtener_por_id(medico_id)
        if medico:
            return medico.esta_disponible(fecha_hora)
        return False

    def obtener_disponibilidad(self, medico_id, fecha):
        """
        Obtiene la disponibilidad de un médico para una fecha específica.
        :param medico_id: ID del médico.
        :param fecha: Fecha para verificar la disponibilidad.
        :return: Un mensaje sobre la disponibilidad del médico.
        """
        medico = self.repository.obtener_por_id(medico_id)
        if medico:
            return medico.mostrar_disponibilidad(fecha)
        return f"El médico con ID {medico_id} no fue encontrado."

    def asignar_turno(self, medico_id, fecha_hora):
        """
        Asigna un turno a un médico si está disponible.
        :param medico_id: ID del médico.
        :param fecha_hora: Fecha y hora para asignar el turno.
        :return: Mensaje indicando el resultado de la asignación.
        """
        medico = self.repository.obtener_por_id(medico_id)
        if medico:
            if medico.esta_disponible(fecha_hora):
                # Aquí puedes agregar lógica para asignar el turno
                return f"Turno asignado con éxito al médico {medico.nombre} en {fecha_hora.strftime('%Y-%m-%d %H:%M')}."
            else:
                return f"El médico {medico.nombre} no está disponible en esa fecha y hora."
        return f"Médico con ID {medico_id} no encontrado."

    def obtener_medico_dto(self, medico_id):
        """
        Obtiene un DTO del médico por ID.
        :param medico_id: ID del médico.
        :return: Un objeto PersonalMedicoDTO con los detalles del médico.
        """
        medico = self.repository.obtener_por_id(medico_id)
        if medico:
            return PersonalMedicoDTO(
                id=medico.id,
                nombre=medico.nombre,
                especializacion=medico.especializacion,
                disponibilidad=medico.disponibilidad,
                horaInicioTurno=medico.horaInicioTurno,
                horaFinTurno=medico.horaFinTurno,
                departamento_id=medico.departamento_id
            )

    def listar_personal_medico(self):
        return [PersonalMedicoDTO.from_entity(personal_medico) for personal_medico in self.personal_repository.find_all()]
