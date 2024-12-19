from domain.entities.medicamento import Medicamento
from datetime import datetime

class MedicamentoDTO:
    def __init__(self, medicamento_id: int, nombre: str, tipoMedicamento: str, fechaFabricacion: datetime,
                 fechaVencimiento: datetime, cantidad: int, id_proveedor: int):
        """
        Constructor del DTO de Medicamento.
        :param medicamento_id: Identificador único del medicamento.
        :param nombre: Nombre del medicamento.
        :param tipoMedicamento: Tipo del medicamento (e.g. antibiótico, analgésico).
        :param fechaFabricacion: Fecha de fabricación del medicamento.
        :param fechaVencimiento: Fecha de vencimiento del medicamento.
        :param cantidad: Cantidad disponible del medicamento.
        :param id_proveedor: Identificador del proveedor del medicamento.
        """
        self.medicamento_id = medicamento_id
        self.nombre = nombre
        self.tipoMedicamento = tipoMedicamento
        self.fechaFabricacion = fechaFabricacion
        self.fechaVencimiento = fechaVencimiento
        self.cantidad = cantidad
        self.id_proveedor = id_proveedor

    def __repr__(self):
        """
        Representación en formato de cadena del DTO.
        :return: String con los detalles del medicamento.
        """
        return (f"MedicamentoDTO(medicamento_id={self.medicamento_id}, nombre='{self.nombre}', "
                f"tipoMedicamento='{self.tipoMedicamento}', "
                f"fechaFabricacion={self.fechaFabricacion.strftime('%Y-%m-%d')}, "
                f"fechaVencimiento={self.fechaVencimiento.strftime('%Y-%m-%d')}, "
                f"cantidad={self.cantidad}, proveedor_id={self.id_proveedor})")

    @staticmethod
    def from_entity(medicamento: Medicamento) -> 'MedicamentoDTO':
        """
        Convierte una entidad Medicamento a un MedicamentoDTO.
        :param medicamento: Entidad Medicamento.
        :return: MedicamentoDTO con los mismos atributos.
        """
        return MedicamentoDTO(
            medicamento_id=medicamento.medicamento_id,
            nombre=medicamento.nombre,
            tipoMedicamento=medicamento.tipoMedicamento,
            fechaFabricacion=medicamento.fechaFabricacion,
            fechaVencimiento=medicamento.fechaVencimiento,
            cantidad=medicamento.cantidad,
            id_proveedor=medicamento.id_proveedor
        )

    def to_entity(self) -> Medicamento:
        """
        Convierte un MedicamentoDTO a entidad Medicamento.
        :return: Instancia de la entidad Medicamento.
        """
        return Medicamento(
            medicamento_id=self.medicamento_id,
            nombre=self.nombre,
            tipoMedicamento=self.tipoMedicamento,
            fechaFabricacion=self.fechaFabricacion,
            fechaVencimiento=self.fechaVencimiento,
            cantidad=self.cantidad,
            id_proveedor=self.id_proveedor
        )
