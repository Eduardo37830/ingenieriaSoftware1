from domain.entities.personalMedico import PersonalMedico
from datetime import datetime

class PersonalMedicoDTO:
    def __init__(self, id: int, nombre: str, especializacion: str, disponibilidad: bool,
                 hora_inicio_turno, hora_fin_turno):
        """
        DTO para transferir la información del personal médico.
        :param id: Identificador único del personal médico.
        :param nombre: Nombre del personal médico.
        :param especializacion: Especialización del médico.
        :param disponibilidad: Indica si el personal está disponible.
        :param horaInicioTurno: Hora de inicio del turno.
        :param horaFinTurno: Hora de fin del turno.
        :param departamento_id: ID del departamento al que pertenece el personal.
        """
        self.id = id
        self.nombre = nombre
        self.especializacion = especializacion
        self.disponibilidad = disponibilidad
        self.hora_inicio_turno = hora_inicio_turno
        self.hora_fin_turno = hora_fin_turno

    def __repr__(self):
        """
        Representación en formato cadena del DTO.
        :return: String con los detalles del personal médico.
        """
        return (f"PersonalMedicoDTO(id={self.id}, nombre='{self.nombre}', especializacion='{self.especializacion}', "
                f"disponibilidad={self.disponibilidad}, horaInicioTurno='{self.horaInicioTurno.strftime('%H:%M')}', "
                f"horaFinTurno='{self.horaFinTurno.strftime('%H:%M')}')")

    def to_dict(self):
        """Convierte el objeto en un diccionario para facilitar la transferencia de datos."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especializacion": self.especializacion,
            "disponibilidad": self.disponibilidad,
            "hora_inicio_turno": self.hora_inicio_turno,
            "hora_fin_turno": self.hora_fin_turno,
        }

    @staticmethod
    def from_entity(personal_medico: PersonalMedico) -> 'PersonalMedicoDTO':
        """
        Convierte una entidad PersonalMedico a PersonalMedicoDTO.
        :param personal_medico: Entidad PersonalMedico.
        :return: Un objeto PersonalMedicoDTO con los datos del personal médico.
        """
        return PersonalMedicoDTO(
            id=personal_medico.id,
            nombre=personal_medico.nombre,
            especializacion=personal_medico.especializacion,
            disponibilidad=personal_medico.disponibilidad,
            horaInicioTurno=personal_medico.horaInicioTurno,
            horaFinTurno=personal_medico.horaFinTurno,
        )

    @staticmethod
    def to_entity(self) -> PersonalMedico:
        """
        Convierte un PersonalMedicoDTO a entidad PersonalMedico.
        :return: Instancia de la entidad PersonalMedico con los datos del DTO.
        """
        return PersonalMedico(
            id=self.id,
            nombre=self.nombre,
            especializacion=self.especializacion,
            disponibilidad=self.disponibilidad,
            horaInicioTurno=self.horaInicioTurno,
            horaFinTurno=self.horaFinTurno,
        )

