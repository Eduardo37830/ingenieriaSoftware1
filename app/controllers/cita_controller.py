from flask import Blueprint, request, jsonify
from application.services.cita_service import CitaApplicationService
from domain.entities.cita import Cita
from infrastructure.repositories import SQLiteCitaRepository

cita_bp = Blueprint('cita_bp', __name__)
cita_repository = SQLiteCitaRepository("hospital.db")
service = CitaApplicationService(cita_repository)

@cita_bp.route('/citas', methods=['POST'])
def agendar_cita():
    data = request.get_json()
    cita = Cita(
        id=None,
        motivoConsulta=data.get("motivoConsulta"),
        fechaConsulta=data.get("fechaConsulta"),
        horaConsulta=data.get("horaConsulta"),
        paciente_id=data.get("paciente_id"),
        personalMedico_id=data.get("personalMedico_id"),
        habitacion_id=data.get("habitacion_id"),
        costoTotal=data.get("costoTotal"),
    )
    service.crear_cita(cita)
    return jsonify({"mensaje": "Cita agendada exitosamente"}), 201

@cita_bp.route('/citas', methods=['GET'])
def listar_citas():
    citas = service.listar_citas()
    return jsonify([c.to_entity() for c in citas]), 200
