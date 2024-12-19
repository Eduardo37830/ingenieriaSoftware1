from domain.entities.usuario import Usuario
from datetime import datetime, time


class PersonalMedico(Usuario):
    """
    Representa al personal médico que hereda de la clase Usuario.

    Atributos:
        disponibilidad (bool): Indica si el personal está disponible en general.
        horaInicioTurno (time): Hora de inicio de turno.
        horaFinTurno (time): Hora de fin de turno.
        especializacion (str): Especialización médica.
        departamento_id (int): ID del departamento al que pertenece.
    """

    def __init__(self, id, nombre, correo, contrasena, rol, direccion, telefono, tipoDocumento, numeroDocumento, disponibilidad,
                 horaInicioTurno, horaFinTurno, especializacion):
        super().__init__(id, nombre, correo, contrasena, rol, direccion, telefono, tipoDocumento, numeroDocumento)
        self.disponibilidad = disponibilidad  # Indica si está disponible en general (bool)
        self.horaInicioTurno = horaInicioTurno  # Hora de inicio del turno (time)
        self.horaFinTurno = horaFinTurno  # Hora de fin del turno (time)
        self.especializacion = especializacion

    def esta_disponible(self, fecha_hora):
        """
        Verifica si el personal médico está disponible en una fecha y hora específicas.

        Args:
            fecha_hora (datetime): Fecha y hora para verificar la disponibilidad.

        Returns:
            bool: True si está disponible, False en caso contrario.
        """
        if not self.disponibilidad:
            return False  # Si no está disponible en general, retorna False.

        # Extraer solo la hora de la fecha proporcionada
        hora = fecha_hora.time()

        # Verificar si la hora está dentro del rango de trabajo
        return self.horaInicioTurno <= hora <= self.horaFinTurno

    def mostrar_disponibilidad(self, fecha):
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


    def to_dict(self):
        """Convierte la instancia en un diccionario."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "tipo_documento": self.tipo_documento,
            "numero_documento": self.numero_documento,
            "disponibilidad": self.disponibilidad,
            "hora_inicio_turno": self.horaInicioTurno,
            "hora_fin_turno": self.horaFinTurno,
            "especializacion": self.especializacion,
        }