from ingenieriaSoftware1.domain.entities.medicamento import Medicamento
from datetime import datetime

class MedicamentoDTO:
    def __init__(self, medicamento_id, nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad):
        self.medicamento_id = medicamento_id
        self.nombre = nombre
        self.tipoMedicamento = tipoMedicamento
        self.fechaFabricacion = fechaFabricacion
        self.fechaVencimiento = fechaVencimiento
        self.cantidad = cantidad

    def __repr__(self):
        return (f"MedicamentoDTO(medicamento_id={self.medicamento_id}, nombre='{self.nombre}', "
                f"tipoMedicamento='{self.tipoMedicamento}', fechaFabricacion={self.fechaFabricacion}, "
                f"fechaVencimiento={self.fechaVencimiento}, cantidad={self.cantidad})")

    @staticmethod
    def from_entity(medicamento: Medicamento) -> 'MedicamentoDTO':
        """Convierte una entidad Medicamento a MedicamentoDTO."""
        return MedicamentoDTO(
            medicamento_id=medicamento.medicamento_id,
            nombre=medicamento.nombre,
            tipoMedicamento=medicamento.tipoMedicamento,
            fechaFabricacion=medicamento.fechaFabricacion,
            fechaVencimiento=medicamento.fechaVencimiento,
            cantidad=medicamento.cantidad
        )

    def to_entity(self) -> Medicamento:
        """Convierte un MedicamentoDTO a entidad Medicamento."""
        return Medicamento(
            medicamento_id=self.medicamento_id,
            nombre=self.nombre,
            tipoMedicamento=self.tipoMedicamento,
            fechaFabricacion=self.fechaFabricacion,
            fechaVencimiento=self.fechaVencimiento,
            cantidad=self.cantidad
        )
