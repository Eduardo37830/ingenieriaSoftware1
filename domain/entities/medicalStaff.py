from user import User
from datetime import datetime, time


class MedicalStaff(User):
    """
    Representa al personal médico que hereda de la clase User.

    Atributos:
        availability (bool): Indica si el personal está disponible en general.
        workStartTime (time): Hora de inicio de turno.
        workEndTime (time): Hora de fin de turno.
        specialization (str): Especialización médica.
        department_id (int): ID del departamento al que pertenece.
    """

    def __init__(self, id, name, email, password, role, address, phone, documentType, documentNumber, availability,
                 workStartTime, workEndTime, specialization, department):
        super().__init__(id, name, email, password, role, address, phone, documentType, documentNumber)
        self.availability = availability  # Indica si está disponible en general (bool)
        self.workStartTime = workStartTime  # Hora de inicio del turno (time)
        self.workEndTime = workEndTime  # Hora de fin del turno (time)
        self.specialization = specialization
        self.department_id = department

    def is_available(self, fecha_hora):
        """
        Verifica si el personal médico está disponible en una fecha y hora específicas.

        Args:
            fecha_hora (datetime): Fecha y hora para verificar la disponibilidad.

        Returns:
            bool: True si está disponible, False en caso contrario.
        """
        if not self.availability:
            return False  # Si no está disponible en general, retorna False.

        # Extraer solo la hora de la fecha proporcionada
        hora = fecha_hora.time()

        # Verificar si la hora está dentro del rango de trabajo
        return self.workStartTime <= hora <= self.workEndTime

    def show_availability(self, fecha):
        """
        Devuelve un mensaje sobre la disponibilidad del personal médico en una fecha específica.

        Args:
            fecha (datetime): Fecha para consultar la disponibilidad.

        Returns:
            str: Mensaje indicando si está disponible o no.
        """
        disponible = self.is_available(fecha)
        if disponible:
            return f"El personal médico está disponible el {fecha.strftime('%Y-%m-%d %H:%M')}."
        else:
            return f"El personal médico no está disponible el {fecha.strftime('%Y-%m-%d %H:%M')}."
