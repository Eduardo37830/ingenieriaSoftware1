from datetime import datetime

class PersonalMedico:
    def __init__(self, id: int, tipoDocumento: str, disponibilidad: bool, horarioEntrada: datetime, horarioSalida: datetime, especialidad: str):
        self.id = id
        self.tipoDocumento = tipoDocumento
        self.disponibilidad = disponibilidad
        self.horarioEntrada = horarioEntrada
        self.horarioSalida = horarioSalida
        self.especialidad = especialidad

    def consultarDisponibilidad(self, fecha: datetime, hora: str) -> bool:
        return self.disponibilidad and self.horarioEntrada <= fecha and self.horarioSalida >= fecha