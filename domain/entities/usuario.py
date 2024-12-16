
class Usuario:
    """
    Representa a un usuario general del sistema.

    Atributos:
        id (int): ID único del usuario.
        nombre (str): Nombre del usuario.
        correo (str): Correo electrónico.
        contrasena (str): Contraseña.
        rol (str): Rol del usuario (e.g., "paciente", "médico").
        direccion (str): Dirección del usuario.
        telefono (str): Número de teléfono del usuario.
        tipo_documento (str): Tipo de documento de identidad.
        numero_documento (str): Número de documento de identidad.
    """

    def __init__(self, id, nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        self.direccion = direccion
        self.telefono = telefono
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento

    def autenticar(self, correo, contrasena):
        """
        Verifica las credenciales de autenticación del usuario.

        Args:
            correo (str): Correo electrónico proporcionado.
            contrasena (str): Contraseña proporcionada.

        Returns:
            bool: True si las credenciales son correctas, False en caso contrario.
        """
        return self.correo == correo and self.contrasena == contrasena
