from domain.entities.paciente import Paciente

class PacienteDTO:
    def __init__(self, id_usuario, nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        self.direccion = direccion
        self.telefono = telefono
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento

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
            tipo_documento=paciente.tipo_documento,
            numero_documento=paciente.numero_documento
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
            tipo_documento=self.tipo_documento,
            numero_documento=self.numero_documento
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
            "tipo_documento": self.tipo_documento,
            "numero_documento": self.numero_documento
        }