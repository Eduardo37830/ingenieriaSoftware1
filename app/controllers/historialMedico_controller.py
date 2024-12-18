from flask import Blueprint, request, jsonify

from application.dtos.historial_medico_dto import HistorialMedicoDTO
from application.services.historial_medico_service import HistorialMedicoApplicationService
from domain.entities.historialMedico import HistorialMedico
from infrastructure.repositories.sqlite_historialMedico_repository import SQLiteHistorialMedicoRepository

historial_bp = Blueprint('historial_bp', __name__)
historial_repository = SQLiteHistorialMedicoRepository("hospital.db")
service = HistorialMedicoApplicationService(historial_repository)

@historial_bp.route('/historiales', methods=['POST'])
def registrar_historial():
    data = request.get_json()
    historial = HistorialMedicoDTO(
        id=None,
        fecha=data.get("fecha"),
        diagnostico=data.get("diagnostico"),
        tratamiento=data.get("tratamiento"),
        observaciones=data.get("observaciones"),
        medico_id=data.get("medico_id"),
        paciente_id=data.get("paciente_id"),
    )
    service.registrar_historial(historial)
    return jsonify({"mensaje": "Historial médico registrado exitosamente"}), 201

@historial_bp.route('/historiales', methods=['GET'])
def listar_historiales():
    historiales = service.listar_historiales()
    return jsonify([h.to_dict() for h in historiales]), 200

@historial_bp.route('/historiales/<int:id>', methods=['GET'])
def obtener_historial(id):
    historial = service.obtener_historial_por_id(id)
    if historial:
        return jsonify(historial.to_dict()), 200
    return jsonify({"error": "Historial médico no encontrado"}), 404
