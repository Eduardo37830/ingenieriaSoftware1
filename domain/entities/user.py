class User:
    """
    Representa a un usuario general del sistema.

    Atributos:
        id (int): ID único del usuario.
        name (str): Nombre del usuario.
        email (str): Correo electrónico.
        password (str): Contraseña.
        role (str): Rol del usuario (e.g., "paciente", "médico").
        address (str): Dirección del usuario.
        phone (str): Número de teléfono del usuario.
        documentType (str): Tipo de documento de identidad.
        documentNumber (str): Número de documento de identidad.
    """

    def __init__(self, id, name, email, password, role, address, phone, documentType, documentNumber):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.address = address
        self.phone = phone
        self.documentType = documentType
        self.documentNumber = documentNumber

    def authenticate(self, email, password):
        """
        Verifica las credenciales de autenticación del usuario.

        Args:
            email (str): Correo electrónico proporcionado.
            password (str): Contraseña proporcionada.

        Returns:
            bool: True si las credenciales son correctas, False en caso contrario.
        """
        return self.email == email and self.password == password

