class Habitacion:
    def __init__(self, id, disponibilidad, tipo_habitacion, capacidad):
        """
        Clase para representar una habitación.
        :param id: Identificador único de la habitación.
        :param disponibilidad: Indica si la habitación está disponible (bool).
        :param tipo_habitacion: Tipo de habitación (por ejemplo, "Individual", "Doble").
        :param capacidad: Capacidad de la habitación.
        """
        self.id = id
        self.disponibilidad = disponibilidad
        self.tipo_habitacion = tipo_habitacion
        self.capacidad = capacidad
        self.cita_asignada = None  # ID de la cita asignada, si aplica

    def asignar_acomodacion(self, id_cita):
        """
        Asigna la habitación a una cita específica si está disponible.
        :param id_cita: ID de la cita a asignar.
        :return: Mensaje indicando el resultado de la asignación.
        """
        if self.disponibilidad:
            self.disponibilidad = False
            self.cita_asignada = id_cita
            return f"Habitación {self.id} asignada a la cita {id_cita}."
        else:
            return f"Habitación {self.id} no disponible para asignación."

    def liberar_acomodacion(self):
        """
        Libera la habitación, haciéndola nuevamente disponible.
        """
        if not self.disponibilidad:
            self.disponibilidad = True
            self.cita_asignada = None
            return f"Habitación {self.id} ha sido liberada."
        else:
            return f"Habitación {self.id} ya estaba disponible."

    def __str__(self):
        """
        Representación en texto de la habitación.
        """
        estado = "Disponible" if self.disponibilidad else f"Ocupada por la cita {self.cita_asignada}"
        return (
            f"Habitación ID: {self.id}\n"
            f"Tipo: {self.tipo_habitacion}\n"
            f"Capacidad: {self.capacidad}\n"
            f"Estado: {estado}\n"
        )
