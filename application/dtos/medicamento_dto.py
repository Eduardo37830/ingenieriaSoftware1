from domain.entities.medicamento import Medicamento
from datetime import datetime

class MedicamentoDTO:
    def __init__(self, medicamento_id, nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad, id_proveedor):
        self.medicamento_id = medicamento_id
        self.nombre = nombre
        self.tipoMedicamento = tipoMedicamento
        self.fechaFabricacion = fechaFabricacion
        self.fechaVencimiento = fechaVencimiento
        self.cantidad = cantidad
        self.id_proveedor = id_proveedor

    def __repr__(self):
        return (f"MedicamentoDTO(medicamento_id={self.medicamento_id}, nombre='{self.nombre}', "
                f"tipoMedicamento='{self.tipoMedicamento}', fechaFabricacion={self.fechaFabricacion}, "
                f"fechaVencimiento={self.fechaVencimiento}, cantidad={self.cantidad}, proveedor_id={self.id_proveedor})")

    @staticmethod
    def from_entity(medicamento: Medicamento) -> 'MedicamentoDTO':
        """Convierte una entidad Medicamento a MedicamentoDTO."""
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
        """Convierte un MedicamentoDTO a entidad Medicamento."""
        return Medicamento(
            medicamento_id=self.medicamento_id,
            nombre=self.nombre,
            tipoMedicamento=self.tipoMedicamento,
            fechaFabricacion=self.fechaFabricacion,
            fechaVencimiento=self.fechaVencimiento,
            cantidad=self.cantidad,
            id_proveedor=self.id_proveedor
        )
