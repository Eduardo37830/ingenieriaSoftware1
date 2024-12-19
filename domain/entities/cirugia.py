from datetime import datetime

class Cirugia:
    def __init__(self, id, fecha_cirugia, tipo_cirugia, id_paciente, id_habitacion=None, hora_cirugia=""):
        """
        Clase para representar una cirugía.
        :param id: Identificador único de la cirugía.
        :param fecha_cirugia: Fecha y hora de la cirugía.
        :param tipo_cirugia: Tipo de cirugía realizada.
        :param id_paciente: ID del paciente asociado.
        :param id_habitacion: ID de la habitación asignada (opcional).
        :param hora_cirugia: Hora específica de la cirugía (formato string).
        """
        self.id = id
        self.fecha_cirugia = fecha_cirugia
        self.tipo_cirugia = tipo_cirugia
        self.id_paciente = id_paciente
        self.id_habitacion = id_habitacion
        self.hora_cirugia = hora_cirugia

    def verificarConflicto(self, otra_cirugia):
        pass