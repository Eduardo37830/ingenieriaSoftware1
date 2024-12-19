from domain.entities.paciente import Paciente

class PacienteDTO:
    def __init__(self, id_usuario: int, nombre: str, correo: str, contrasena: str, rol: str, direccion: str,
                 telefono: str, tipoDocumento: str, numeroDocumento: str):
        """
        Constructor del DTO de Paciente.
        :param id_usuario: Identificador único del usuario.
        :param nombre: Nombre del paciente.
        :param correo: Correo electrónico del paciente.
        :param contrasena: Contraseña asociada al usuario.
        :param rol: Rol del usuario (por ejemplo, paciente).
        :param direccion: Dirección del paciente.
        :param telefono: Teléfono del paciente.
        :param tipoDocumento: Tipo de documento (e.g., "DNI", "PASAPORTE").
        :param numeroDocumento: Número del documento del paciente.
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        self.direccion = direccion
        self.telefono = telefono
        self.tipoDocumento = tipoDocumento
        self.numeroDocumento = numeroDocumento

    def __repr__(self):
        """
        Representación en formato cadena del DTO.
        :return: String con los detalles del paciente.
        """
        return (f"PacienteDTO(id_usuario={self.id_usuario}, nombre='{self.nombre}', correo='{self.correo}', "
                f"rol='{self.rol}', direccion='{self.direccion}', telefono='{self.telefono}', "
                f"tipoDocumento='{self.tipoDocumento}', numeroDocumento='{self.numeroDocumento}')")

    @staticmethod
    def from_entity(paciente: Paciente) -> 'PacienteDTO':
        """
        Convierte una entidad Paciente a un PacienteDTO.
        :param paciente: Entidad Paciente.
        :return: Un objeto PacienteDTO con los datos del paciente.
        """
        return PacienteDTO(
            id_usuario=paciente.id,
            nombre=paciente.nombre,
            correo=paciente.correo,
            contrasena=paciente.contrasena,
            rol=paciente.rol,
            direccion=paciente.direccion,
            telefono=paciente.telefono,
            tipoDocumento=paciente.tipo_documento,
            numeroDocumento=paciente.numero_documento
        )

    def to_entity(self) -> Paciente:
        """
        Convierte un PacienteDTO a una entidad Paciente.
        :return: Instancia de la entidad Paciente con los datos del DTO.
        """
        return Paciente(
            id_usuario=self.id_usuario,
            nombre=self.nombre,
            correo=self.correo,
            contrasena=self.contrasena,
            rol=self.rol,
            direccion=self.direccion,
            telefono=self.telefono,
            tipoDocumento=self.tipoDocumento,
            numeroDocumento=self.numeroDocumento
        )
    def to_dict (self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasena": self.contrasena,
            "rol": self.rol,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "tipoDocumento": self.tipoDocumento,
            "numeroDocumento": self.numeroDocumento
        }