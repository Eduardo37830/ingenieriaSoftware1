from application.dtos.usuario_dto import UsuarioDTO

class UsuarioService:
    def __init__(self, usuario_repository):
        """
        Inicializa el servicio de usuario.
        :param usuario_repository: Repositorio para interactuar con los datos del usuario.
        """
        self.usuario_repository = usuario_repository

    def autenticar_usuario(self, correo, contrasena):
        """
        Autentica a un usuario con sus credenciales.
        :param correo: Correo electrónico del usuario.
        :param contrasena: Contraseña del usuario.
        :return: UsuarioDTO si las credenciales son correctas, None si son incorrectas.
        """
        if not correo or not contrasena:
            raise ValueError("El correo y la contraseña son obligatorios")

        usuario = self.usuario_repository.buscar_por_cedula(correo)
        if usuario and usuario.autenticar(correo, contrasena):
            return UsuarioDTO(usuario.id, usuario.nombre, usuario.correo, usuario.rol)
        return None

    def obtener_usuario_por_id(self, id):
        """
        Obtiene los detalles de un usuario por su ID.
        :param id: ID del usuario.
        :return: UsuarioDTO con los detalles del usuario, o None si no existe.
        """
        if not id or id <= 0:
            raise ValueError("El ID debe ser un número positivo")

        usuario = self.usuario_repository.buscar_por_id(id)
        if usuario:
            return UsuarioDTO(usuario.id, usuario.nombre, usuario.correo, usuario.rol)
        return None

    def eliminar_usuario(self, user_id: int) -> bool:
        """
        Elimina un usuario por su ID.
        :param user_id: ID del usuario a eliminar.
        :return: True si se elimina, False si no se encuentra.
        """
        if not user_id or user_id <= 0:
            raise ValueError("El ID debe ser un número positivo")

        usuario = self.usuario_repository.buscar_por_id(user_id)
        if not usuario:
            return False  # Usuario no encontrado

        try:
            self.usuario_repository.eliminar(user_id)
            return True  # Usuario eliminado
        except Exception as e:
            # Manejo de errores más específico según el caso
            raise RuntimeError(f"Error al eliminar el usuario: {str(e)}")
