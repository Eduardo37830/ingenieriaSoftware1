from datetime import datetime
from typing import List

class HistorialMedico:
    def __init__(self, fecha: datetime, descripcion: str):
        self.fecha = fecha
        self.descripcion = descripcion

class Paciente:
    def __init__(self, id: int, direccion: str, telefono: str, historialMedico: List[HistorialMedico]):
        self.id = id
        self.direccion = direccion
        self.telefono = telefono
        self.historialMedico = historialMedico

    def agregarEntradaHistorial(self, entrada: HistorialMedico):
        self.historialMedico.append(entrada)

    def consultarHistorialMedico(self):
        return self.historialMedico
