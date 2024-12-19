class InformeDTO:
    def __init__(self, total_depositos: float, total_retiros: float, saldo_promedio: float):
        """
        Constructor del DTO de Informe, que contiene información sobre los depósitos, retiros y saldo promedio.
        :param total_depositos: Total de los depósitos realizados.
        :param total_retiros: Total de los retiros realizados.
        :param saldo_promedio: Promedio del saldo durante un período.
        """
        self.total_depositos = total_depositos
        self.total_retiros = total_retiros
        self.saldo_promedio = saldo_promedio

    def __repr__(self):
        """
        Representación en formato de cadena del DTO para facilitar la depuración.
        :return: String con los detalles del informe.
        """
        return (f"InformeDTO(total_depositos={self.total_depositos}, total_retiros={self.total_retiros}, "
                f"saldo_promedio={self.saldo_promedio})")

    @staticmethod
    def from_entity(entity) -> 'InformeDTO':
        """
        Convierte una entidad (si existiera una) en un InformeDTO.
        :param entity: Entidad que contiene los datos (por ejemplo, una entidad que tiene los mismos atributos).
        :return: InformeDTO con los datos de la entidad.
        """
        # Aquí puedes mapear desde la entidad a DTO si tienes una clase de entidad correspondiente.
        # Suponiendo que `entity` tiene los mismos atributos.
        return InformeDTO(
            total_depositos=entity.total_depositos,
            total_retiros=entity.total_retiros,
            saldo_promedio=entity.saldo_promedio
        )

    def to_dict(self):
        """
        Convierte el DTO a un diccionario para su serialización.
        :return: Diccionario con los datos del informe.
        """
        return {
            "total_depositos": self.total_depositos,
            "total_retiros": self.total_retiros,
            "saldo_promedio": self.saldo_promedio
        }
