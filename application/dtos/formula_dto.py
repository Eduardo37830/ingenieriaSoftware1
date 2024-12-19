from domain.entities.formula import Formula

class FormulaDTO:
    def __init__(self, id: int, paciente_id: int, medicamento_id: int, descripcion: str, cantidad: int):
        """
        Constructor del DTO de Formula.
        :param id: Identificador único de la fórmula.
        :param paciente_id: ID del paciente asociado con la fórmula.
        :param medicamento_id: ID del medicamento recetado.
        :param descripcion: Descripción de la fórmula.
        :param cantidad: Cantidad de medicamento recetada.
        """
        self.id = id
        self.paciente_id = paciente_id
        self.medicamento_id = medicamento_id
        self.descripcion = descripcion
        self.cantidad = cantidad

    def __repr__(self):
        """Representación del DTO en formato string para facilitar la depuración."""
        return (f"FormulaDTO(id={self.id}, paciente_id={self.paciente_id}, medicamento_id={self.medicamento_id}, "
                f"descripcion='{self.descripcion}', cantidad={self.cantidad})")

    @staticmethod
    def from_entity(formula: Formula) -> 'FormulaDTO':
        """Convierte una entidad Formula en un DTO FormulaDTO."""
        return FormulaDTO(
            id=formula.id,
            paciente_id=formula.paciente_id,
            medicamento_id=formula.medicamento_id,
            descripcion=formula.descripcion,
            cantidad=formula.cantidad
        )

    def to_entity(self) -> Formula:
        """Convierte un FormulaDTO en una entidad Formula."""
        return Formula(
            id=self.id,
            paciente_id=self.paciente_id,
            medicamento_id=self.medicamento_id,
            descripcion=self.descripcion,
            cantidad=self.cantidad
        )

    def to_dict(self) -> dict:
        """Convierte el DTO a un diccionario, útil para su serialización en una API."""
        return {
            "id": self.id,
            "paciente_id": self.paciente_id,
            "medicamento_id": self.medicamento_id,
            "descripcion": self.descripcion,
            "cantidad": self.cantidad
        }
