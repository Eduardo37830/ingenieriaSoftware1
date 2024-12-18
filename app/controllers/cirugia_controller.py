from flask import Blueprint, request, jsonify

from application.dtos.cirugia_dto import CirugiaDTO
from application.services.cirugia_service import CirugiaApplicationService
from domain.entities.cirugia import Cirugia
from infrastructure.repositories import SQLiteCirugiaRepository

cirugia_bp = Blueprint('cirugia_bp', __name__)
cirugia_repository = SQLiteCirugiaRepository("hospital.db")
service = CirugiaApplicationService(cirugia_repository)

@cirugia_bp.route('/cirugias', methods=['POST'])
def registrar_cirugia():
    data = request.get_json()
    cirugia = CirugiaDTO(
        id=None,
        fecha_cirugia=data.get("fechaCirugia"),
        tipo_cirugia=data.get("tipoCirugia"),
        id_paciente=data.get("id_paciente"),
        id_habitacion=data.get("id_habitacion"),
        hora_cirugia=data.get("horaCirugia"),
    )
    service.registrar_cirugia(cirugia)
    return jsonify({"mensaje": "Cirugía registrada exitosamente"}), 201
