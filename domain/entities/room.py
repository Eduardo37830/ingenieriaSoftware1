class Room:
    def __init__(self, id, availability, roomType, capacity):
        """
        Clase para representar una habitación.
        :param id: Identificador único de la habitación.
        :param availability: Indica si la habitación está disponible (bool).
        :param roomType: Tipo de habitación (por ejemplo, "Individual", "Doble").
        :param capacity: Capacidad de la habitación.
        """
        self.id = id
        self.availability = availability
        self.roomType = roomType
        self.capacity = capacity
        self.assignedAppointment = None  # ID de la cita asignada, si aplica

    def asignarAcomodacion(self, idCita):
        """
        Asigna la habitación a una cita específica si está disponible.
        :param idCita: ID de la cita a asignar.
        :return: Mensaje indicando el resultado de la asignación.
        """
        if self.availability:
            self.availability = False
            self.assignedAppointment = idCita
            return f"Habitación {self.id} asignada a la cita {idCita}."
        else:
            return f"Habitación {self.id} no disponible para asignación."

    def liberarAcomodacion(self):
        """
        Libera la habitación, haciéndola nuevamente disponible.
        """
        if not self.availability:
            self.availability = True
            self.assignedAppointment = None
            return f"Habitación {self.id} ha sido liberada."
        else:
            return f"Habitación {self.id} ya estaba disponible."

    def __str__(self):
        """
        Representación en texto de la habitación.
        """
        estado = "Disponible" if self.availability else f"Ocupada por la cita {self.assignedAppointment}"
        return (
            f"Habitación ID: {self.id}\n"
            f"Tipo: {self.roomType}\n"
            f"Capacidad: {self.capacity}\n"
            f"Estado: {estado}\n"
        )
