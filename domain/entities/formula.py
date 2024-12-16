class Formula:
    """
    Representa una prescripción médica para un paciente.

    Atributos:
        id (int): ID único de la prescripción.
        paciente_id (int): ID del paciente asociado.
        medicamento_id (int): ID del medicamento asociado.
        descripcion (str): Descripción de la prescripción.
        cantidad (int): Cantidad de medicamento recetada.
    """

    def __init__(self, id, paciente_id, medicamento_id, descripcion, cantidad):
        self.id = id
        self.paciente_id = paciente_id
        self.medicamento_id = medicamento_id
        self.descripcion = descripcion
        self.cantidad = cantidad
