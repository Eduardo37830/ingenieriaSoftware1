class ProveedorDTO:
    def __init__(self, id_proveedor, nombre, fecha_entrega, costo, telefono_vendedor):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.fecha_entrega = fecha_entrega
        self.costo = costo
        self.telefono_vendedor = telefono_vendedor

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
            telefono_vendedor=data["telefono_vendedor"]
        )
