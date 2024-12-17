from historialMedico import HistorialMedico
from usuario import Usuario


class Paciente(Usuario):
    """
    Representa a un paciente que hereda de la clase Usuario.

    Atributos:
        historial_medico (list): Lista de entradas del historial médico (instancias de HistorialMedico).
        citas (list): Lista de citas del paciente.
        formulas (list): Lista de fórmulas médicas asociadas.
    """

    def __init__(self, id, nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento):
        super().__init__(id, nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento)
        self.historial_medico = []
        self.citas = []
        self.formulas = []

    def agregar_historial(self, historial_medico):
        """
        Agrega una nueva entrada al historial médico del paciente.

        Args:
            historial_medico (HistorialMedico): Instancia de HistorialMedico que representa una entrada del historial.
        """
        if isinstance(historial_medico, HistorialMedico):
            self.historial_medico.append(historial_medico)
        else:
            raise ValueError("La entrada debe ser una instancia de HistorialMedico.")

    def mostrar_historial(self):
        """
        Muestra el historial médico completo del paciente.

        Returns:
            str: Representación textual del historial médico.
        """
        return "\n".join(str(entry) for entry in self.historial_medico)
