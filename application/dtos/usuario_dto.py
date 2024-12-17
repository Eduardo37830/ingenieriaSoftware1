class UsuarioDTO:
    def __init__(self, id_usuario, nombre, correo, rol):
        """
        Representa los datos básicos de un usuario que se transferirán a través de la capa de aplicación.
        :param id_usuario: ID del usuario.
        :param nombre: Nombre del usuario.
        :param correo: Correo del usuario.
        :param rol: Rol del usuario (e.g., "paciente", "médico").
        """
        self.id = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def __str__(self):
        """
        Representación en texto del DTO de usuario.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Rol: {self.rol}"
