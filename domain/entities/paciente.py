from domain.entities.historialMedico import HistorialMedico
from domain.entities.usuario import Usuario


class Paciente(Usuario):
    """
    Representa a un paciente que hereda de la clase Usuario.

    Atributos:
        historial_medico (list): Lista de entradas del historial médico (instancias de HistorialMedico).
    """

    def __init__(self, id_usuario, nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento):
        super().__init__(id_usuario, nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento)
        self.historial_medico = []
        self.citas = []
        self.formulas = []

    def agregarHistorial(self, historialMedico):
        """
        Agrega una nueva entrada al historial médico del paciente.

        Args:
            historialMedico (HistorialMedico): Instancia de HistorialMedico que representa una entrada del historial.

        Raises:
            ValueError: Si el objeto proporcionado no es una instancia de HistorialMedico.
        """
        if isinstance(historialMedico, HistorialMedico):
            self.historial_medico.append(historialMedico)
        else:
            raise ValueError("La entrada debe ser una instancia de HistorialMedico.")

    def mostrarHistorial(self):
        """
        Muestra el historial médico completo del paciente.

        Returns:
            str: Representación textual del historial médico.
        """
        return "\n".join(str(entry) for entry in self.historial_medico)

