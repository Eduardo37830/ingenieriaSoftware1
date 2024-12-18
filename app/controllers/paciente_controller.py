from flask import Blueprint, request, jsonify

from application.dtos.paciente_dto import PacienteDTO
from application.services.paciente_service import PacienteApplicationService
from domain.entities.paciente import Paciente
from infrastructure.repositories import SQLitePacienteRepository

paciente_bp = Blueprint('paciente_bp', __name__)
paciente_repository = SQLitePacienteRepository("hospital.db")
service = PacienteApplicationService(paciente_repository)

@paciente_bp.route('/pacientes', methods=['POST'])
def registrar_paciente():
    data = request.get_json()
    paciente = PacienteDTO(
        id_usuario=None,
        nombre=data.get("nombre"),
        correo=data.get("correo"),
        direccion=data.get("direccion"),
        telefono=data.get("telefono"),
        tipoDocumento=data.get("tipo_documento"),
        numeroDocumento=data.get("numero_documento"),
    )
    service.registrar_paciente(paciente)
    return jsonify({"mensaje": "Paciente registrado exitosamente"}), 201

@paciente_bp.route('/pacientes', methods=['GET'])

@paciente_bp.route('/pacientes/<int:id>', methods=['GET'])
def obtener_paciente(id):
    paciente = service.obtener_paciente_por_id(id)
    if paciente:
        return jsonify(paciente.to_entity()), 200
    return jsonify({"error": "Paciente no encontrado"}), 404
