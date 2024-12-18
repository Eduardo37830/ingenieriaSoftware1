from flask import Blueprint, request, jsonify

from application.dtos.personal_medico_dto import PersonalMedicoDTO
from application.services.personalMedico_service import PersonalMedicoService
from domain.entities.personalMedico import PersonalMedico

personal_medico_bp = Blueprint('personal_medico_bp', __name__)
service = PersonalMedicoService("hospital.db")

@personal_medico_bp.route('/personal', methods=['POST'])
def registrar_personal_medico():
    data = request.get_json()
    personal = PersonalMedicoDTO(
        id=None,
        nombre=data.get("nombre"),
        disponibilidad=data.get("disponibilidad"),
        horaInicioTurno=data.get("horaInicioTurno"),
        horaFinTurno=data.get("horaFinTurno"),
        especializacion=data.get("especializacion"),
        departamento_id=data.get("departamento"),
    )
    service.registrar_personal_medico(personal)
    return jsonify({"mensaje": "Personal médico registrado exitosamente"}), 201

@personal_medico_bp.route('/personal', methods=['GET'])
def listar_personal_medico():
    personal_medico = service.listar_personal_medico()
    return jsonify([p.to_dict() for p in personal_medico]), 200

@personal_medico_bp.route('/personal/<int:id>', methods=['GET'])
def obtener_personal_medico(id):
    personal = service.obtener_personal_medico_por_id(id)
    if personal:
        return jsonify(personal.to_dict()), 200
    return jsonify({"error": "Personal médico no encontrado"}), 404

@personal_medico_bp.route('/personal/<int:id>', methods=['DELETE'])
def eliminar_personal_medico(id):
    service.eliminar_personal_medico(id)
    return jsonify({"mensaje": "Personal médico eliminado exitosamente"}), 200
