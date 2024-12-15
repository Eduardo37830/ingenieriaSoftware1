from user import User


class MedicalStaff(User):
    def __init__(self, id, name, email, password, role, address, phone, documentType, documentNumber, availability,
                 workStartTime, workEndTime, specialization, department):
        super().__init__(id, name, email, password, role, address, phone, documentType, documentNumber)
        self.availability = availability
        self.workStartTime = workStartTime
        self.workEndTime = workEndTime
        self.specialization = specialization
        self.department_id = department
