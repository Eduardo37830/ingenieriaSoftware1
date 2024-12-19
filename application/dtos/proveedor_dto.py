from domain.entities.proveedor import Proveedor


class ProveedorDTO:
    def __init__(self, id_proveedor, nombre, fecha_entrega, costo, telefono_vendedor, direccion):
        """
        Clase DTO para representar un proveedor.
        :param id_proveedor: ID único del proveedor.
        :param nombre: Nombre del proveedor.
        :param fecha_entrega: Fecha de entrega (datetime).
        :param costo: Costo de la entrega.
        :param telefono_vendedor: Teléfono del vendedor.
        :param direccion: Dirección del proveedor.
        """
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.fecha_entrega = fecha_entrega
        self.costo = costo
        self.telefono_vendedor = telefono_vendedor
        self.direccion = direccion  # Se añadió la dirección

    def to_dict(self):
        """
        Convierte el DTO a un diccionario para facilitar el transporte o la conversión.
        """
        return {
            "id_proveedor": self.id_proveedor,
            "nombre": self.nombre,
            "fecha_entrega": self.fecha_entrega,
            "costo": self.costo,
            "telefono_vendedor": self.telefono_vendedor,
            "direccion": self.direccion,  # Se añadió la dirección
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un DTO desde un diccionario.
        """
        return ProveedorDTO(
            id_proveedor=data["id_proveedor"],
            nombre=data["nombre"],
            fecha_entrega=data["fecha_entrega"],
            costo=data["costo"],
            telefono_vendedor=data["telefono_vendedor"],
            direccion=data["direccion"],  # Se añadió la dirección
        )

    def to_entity(self) -> Proveedor:
        """
        Convierte el DTO en una entidad Proveedor.
        """
        return Proveedor(
            id_proveedor=self.id_proveedor,
            nombre=self.nombre,
            fecha_entrega=self.fecha_entrega,
            costo=self.costo,
            telefono_vendedor=self.telefono_vendedor,
            direccion=self.direccion,  # Se añadió la dirección
        )

    @staticmethod
    def from_entity(proveedor: Proveedor) -> 'ProveedorDTO':
        """
        Crea un DTO desde una entidad Proveedor.
        """
        return ProveedorDTO(
            id_proveedor= proveedor.id,
            nombre= proveedor.nombre,
            fecha_entrega= proveedor.fecha_entrega,
            costo= proveedor.costo,
            telefono_vendedor= proveedor.telefono_vendedor,
            direccion= proveedor.direccion,  # Se añadió la dirección
        )