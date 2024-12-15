class Prescription:
    """
    Representa una prescripción médica para un paciente.

    Atributos:
        id (int): ID único de la prescripción.
        patient_id (int): ID del paciente asociado.
        medication_id (int): ID del medicamento asociado.
        description (str): Descripción de la prescripción.
        quantity (int): Cantidad de medicamento recetada.
    """

    def __init__(self, id, patient_id, medication_id, description, quantity):
        self.id = id
        self.patient_id = patient_id
        self.medication_id = medication_id
        self.description = description
        self.quantity = quantity
