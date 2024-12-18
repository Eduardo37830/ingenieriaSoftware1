from domain.entities.paciente import Paciente

class PacienteDTO:
    def __init__(self, id_usuario, nombre, correo, contrasena, rol, direccion, telefono, tipoDocumento, numeroDocumento):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        self.direccion = direccion
        self.telefono = telefono
        self.tipoDocumento = tipoDocumento
        self.numeroDocumento = numeroDocumento

    @staticmethod
    def from_entity(paciente: Paciente) -> 'PacienteDTO':
        """Convierte una entidad Paciente a PacienteDTO."""
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
        """Convierte un PacienteDTO a entidad Paciente."""
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
