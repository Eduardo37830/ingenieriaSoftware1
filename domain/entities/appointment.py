class Appointment:
    def __init__(self, id, reasonForConsultation, appointmentDateTime, patient_id, medicalStaff_id, totalFee,room_id):
        self.id = id
        self.reasonForConsultation = reasonForConsultation
        self.appointmentDateTime = appointmentDateTime
        self.totalFee = totalFee
        self.patient_id = patient_id
        self.medicalStaff_id = medicalStaff_id
        self.room_id = room_id



