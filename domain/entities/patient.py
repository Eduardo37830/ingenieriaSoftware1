from medicalHistory import HistorialMedico
from user import User


class Patient(User):
    """
    Representa a un paciente que hereda de la clase User.

    Atributos:
        medical_history (list): Lista de entradas del historial médico (instancias de HistorialMedico).
    """

    def __init__(self, userid, name, email, password, role, address, phone, documentType, documentNumber):
        super().__init__(userid, name, email, password, role, address, phone, documentType, documentNumber)
        self.medical_history = []

    def addHistorialEntry(self, historialMedico):
        """
        Agrega una nueva entrada al historial médico del paciente.

        Args:
            historialMedico (HistorialMedico): Instancia de HistorialMedico que representa una entrada del historial.

        Raises:
            ValueError: Si el objeto proporcionado no es una instancia de HistorialMedico.
        """
        if isinstance(historialMedico, HistorialMedico):
            self.medical_history.append(historialMedico)
        else:
            raise ValueError("La entrada debe ser una instancia de HistorialMedico.")

    def showHistorial(self):
        """
        Muestra el historial médico completo del paciente.

        Returns:
            str: Representación textual del historial médico.
        """
        return "\n".join(str(entry) for entry in self.medical_history)

