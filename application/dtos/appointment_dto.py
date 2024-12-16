class AppointmentDTO:
    def __init__(self, id: int, reason: str, date: str, patient_id: int, doctor_id: int):
        self.id = id
        self.reason = reason
        self.date = date
        self.patient_id = patient_id
        self.doctor_id = doctor_id
