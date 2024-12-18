from flask import Blueprint, request, jsonify

from application.dtos.equipo_medico_dto import EquipoMedicoDTO
from application.services.equipo_medico_service import EquipoMedicoApplicationService
from domain.entities.equipo_medico import EquipoMedico

equipo_bp = Blueprint('equipo_bp', __name__)
service = EquipoMedicoApplicationService("hospital.db")

@equipo_bp.route('/equipos', methods=['POST'])
def registrar_equipo():
    data = request.get_json()
    equipo = EquipoMedicoDTO(
        id=None,
        tipo_equipo=data.get("tipoEquipo"),
        funcionalidad=data.get("funcionalidad"),
        disponibilidad=data.get("disponibilidad"),
    )
    service.registrar_equipo(equipo)
    return jsonify({"mensaje": "Equipo médico registrado exitosamente"}), 201

@equipo_bp.route('/equipos', methods=['GET'])
def listar_equipos():
    equipos = service.listar_equipos()
    return jsonify([e.to_dict() for e in equipos]), 200

@equipo_bp.route('/equipos/<int:id>', methods=['GET'])
def obtener_equipo(id):
    equipo = service.obtener_equipo_por_id(id)
    if equipo:
        return jsonify(equipo.to_dict()), 200
    return jsonify({"error": "Equipo médico no encontrado"}), 404

@equipo_bp.route('/equipos/disponibles', methods=['GET'])
def listar_equipos_disponibles():
    equipos = service.listar_equipos_disponibles()
    return jsonify([e.to_dict() for e in equipos]), 200
