from ingenieriaSoftware1.application.dtos.usuario_dto import UsuarioDTO
from ingenieriaSoftware1.domain.entities.historialMedico import HistorialMedico


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
        usuario = self.usuario_repository.buscar_por_correo(correo)
        if usuario and usuario.autenticar(correo, contrasena):
            return UsuarioDTO(usuario.id, usuario.nombre, usuario.correo, usuario.rol)
        return None

    def obtener_usuario_por_id(self, id):
        """
        Obtiene los detalles de un usuario por su ID.
        :param id: ID del usuario.
        :return: UsuarioDTO con los detalles del usuario.
        """
        usuario = self.usuario_repository.buscar_por_id(id)
        if usuario:
            return UsuarioDTO(usuario.id, usuario.nombre, usuario.correo, usuario.rol)
        return None
