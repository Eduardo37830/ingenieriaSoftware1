from flask import Blueprint, request, jsonify

from application.dtos.medicamento_dto import MedicamentoDTO
from application.services.medicamento_service import MedicamentoApplicationService
from domain.entities.medicamento import Medicamento
from infrastructure.repositories import SQLiteMedicamentoRepository

medicamento_bp = Blueprint('medicamento_bp', __name__)
medicamento_reposirory = SQLiteMedicamentoRepository("hospital.db")
service = MedicamentoApplicationService(medicamento_reposirory)

@medicamento_bp.route('/medicamentos', methods=['POST'])
def registrar_medicamento():
    data = request.get_json()
    medicamento = MedicamentoDTO(
        medicamento_id=None,
        nombre=data.get("nombre"),
        tipoMedicamento=data.get("tipo_medicamento"),
        fechaFabricacion=data.get("fecha_fabricacion"),
        fechaVencimiento=data.get("fecha_vencimiento"),
        cantidad=data.get("cantidad"),
        id_proveedor=data.get("proveedor_id"),
    )
    service.registrar_medicamento(medicamento)
    return jsonify({"mensaje": "Medicamento registrado exitosamente"}), 201

@medicamento_bp.route('/medicamentos', methods=['GET'])
def listar_medicamentos():
    medicamentos = service.listar_medicamentos()
    return jsonify([m.to_entity() for m in medicamentos]), 200
