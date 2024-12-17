from ingenieriaSoftware1.domain.repositories.i_formula_repository import IformulaRepository
from ingenieriaSoftware1.application.dtos.formula_dto import FormulaDTO
from ingenieriaSoftware1.application.exceptions.application_error import NotFoundError

class FormulaApplicationService:
    def __init__(self, formula_repository: IformulaRepository):
        self.formula_repository = formula_repository

    def registrar_formula(self, formula_dto: FormulaDTO) -> None:
        """Registra una nueva fórmula médica."""
        formula = formula_dto.to_entity()  # Convertir el DTO a la entidad
        self.formula_repository.save(formula)

    def obtener_formula_por_id(self, formula_id: int) -> FormulaDTO:
        """Obtiene una fórmula médica por su ID."""
        formula = self.formula_repository.find_by_id(formula_id)
        if not formula:
            raise NotFoundError(f"No se encontró una fórmula con el ID {formula_id}")
        return FormulaDTO.from_entity(formula)  # Convertir la entidad a DTO

    def listar_formulas_por_paciente(self, paciente_id: int) -> list[FormulaDTO]:
        """Lista todas las fórmulas médicas de un paciente."""
        formulas = self.formula_repository.find_all_by_paciente(paciente_id)
        return [FormulaDTO.from_entity(f) for f in formulas]  # Convertir las entidades en DTOs
