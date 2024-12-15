class Prescription:
    def __init__(self, id, patient_id, medication_id, description, quantity):
        self.id = id
        self.patient_id = patient_id
        self.medication_id = medication_id
        self.description = description
        self.quantity = quantity
