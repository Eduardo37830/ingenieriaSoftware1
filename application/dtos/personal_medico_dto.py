from domain.entities.personalMedico import PersonalMedico

class PersonalMedicoDTO:
    def __init__(self, id, nombre, especializacion, disponibilidad, horaInicioTurno, horaFinTurno, departamento_id):
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
        self.horaInicioTurno = horaInicioTurno
        self.horaFinTurno = horaFinTurno
        self.departamento_id = departamento_id

    def to_dict(self):
        """Convierte el DTO a un diccionario para facilitar la transferencia de datos."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especializacion": self.especializacion,
            "disponibilidad": self.disponibilidad,
            "horaInicioTurno": self.horaInicioTurno.strftime('%H:%M'),
            "horaFinTurno": self.horaFinTurno.strftime('%H:%M'),
            "departamento_id": self.departamento_id
        }
