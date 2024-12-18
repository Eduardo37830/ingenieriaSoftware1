from flask import Blueprint, request, jsonify

from application.dtos.formula_dto import FormulaDTO
from application.services.formula_service import FormulaApplicationService
from domain.entities.formula import Formula
from infrastructure.repositories import SQLiteFormulaRepository

formula_bp = Blueprint('formula_bp', __name__)
formula_reposirory = SQLiteFormulaRepository("hospital.db")
service = FormulaApplicationService(formula_reposirory)

@formula_bp.route('/formulas', methods=['POST'])
def registrar_formula():
    data = request.get_json()
    formula = FormulaDTO(
        id=None,
        paciente_id=data.get("paciente_id"),
        medicamento_id=data.get("medicamento_id"),
        descripcion=data.get("descripcion"),
        cantidad=data.get("cantidad"),
    )
    service.registrar_formula(formula)
    return jsonify({"mensaje": "Fórmula registrada exitosamente"}), 201

@formula_bp.route('/formulas', methods=['GET'])
def listar_formulas():
    formulas = service.listar_formulas()
    return jsonify([f.to_dict() for f in formulas]), 200

@formula_bp.route('/formulas/<int:id>', methods=['GET'])
def obtener_formula(id):
    formula = service.obtener_formula_por_id(id)
    if formula:
        return jsonify(formula.to_entity()), 200
    return jsonify({"error": "Fórmula no encontrada"}), 404
