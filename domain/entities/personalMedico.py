from .usuario import Usuario
from datetime import datetime, time


class PersonalMedico(Usuario):
    """
    Representa al personal médico que hereda de la clase Usuario.

    Atributos:
        disponibilidad (bool): Indica si el personal está disponible en general.
        horaInicioTurno (time): Hora de inicio de turno.
        horaFinTurno (time): Hora de fin de turno.
        especializacion (str): Especialización médica.
        departamento (str): Departamento al que pertenece.
    """

    def __init__(
        self, id, nombre, correo, contrasena, rol, direccion, telefono, tipoDocumento, numeroDocumento,
        disponibilidad, horaInicioTurno, horaFinTurno, especializacion, departamento
    ):
        super().__init__(id, nombre, correo, contrasena, rol, direccion, telefono, tipoDocumento, numeroDocumento)
        self.disponibilidad = disponibilidad  # Indica si está disponible en general (bool)
        self.horaInicioTurno = horaInicioTurno  # Hora de inicio del turno (time)
        self.horaFinTurno = horaFinTurno  # Hora de fin del turno (time)
        self.especializacion = especializacion
        self.departamento = departamento

    def esta_disponible(self, fecha_hora: datetime) -> bool:
        """
        Verifica si el personal médico está disponible en una fecha y hora específicas.

        Args:
            fecha_hora (datetime): Fecha y hora para verificar la disponibilidad.

        Returns:
            bool: True si está disponible, False en caso contrario.
        """
        if not self.disponibilidad:
            return False  # No disponible en general.

        hora = fecha_hora.time()  # Extraer solo la hora
        return self.horaInicioTurno <= hora <= self.horaFinTurno

    def mostrar_disponibilidad(self, fecha: datetime) -> str:
        """
        Devuelve un mensaje sobre la disponibilidad del personal médico en una fecha específica.

        Args:
            fecha (datetime): Fecha para consultar la disponibilidad.

        Returns:
            str: Mensaje indicando si está disponible o no.
        """
        disponible = self.esta_disponible(fecha)
        if disponible:
            return f"El personal médico está disponible el {fecha.strftime('%Y-%m-%d %H:%M')}."
        else:
            return f"El personal médico no está disponible el {fecha.strftime('%Y-%m-%d %H:%M')}."
