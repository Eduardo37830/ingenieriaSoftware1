from user import User


class Patient(User):
    def __init__(self, userid, name, email, password, role, address, phone,documentType, documentNumber):
        super().__init__(userid, name, email, password, role, address, phone,documentType, documentNumber)
        self.medical_history = []

