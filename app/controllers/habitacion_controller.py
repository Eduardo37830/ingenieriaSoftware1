from flask import Blueprint, request, jsonify

from application.dtos.habitacion_dto import HabitacionDTO
from application.services.habitacion import HabitacionApplicationService
from domain.entities.habitacion import Habitacion
from infrastructure.repositories import SQLiteHabitacionRepository

habitacion_bp = Blueprint('habitacion_bp', __name__)
habitacion_repository = SQLiteHabitacionRepository("hospital.db")
service = HabitacionApplicationService(habitacion_repository)

@habitacion_bp.route('/habitaciones', methods=['POST'])
def registrar_habitacion():
    data = request.get_json()
    habitacion = HabitacionDTO(
        id=None,
        disponibilidad=data.get("disponibilidad"),
        tipo_habitacion=data.get("tipo_habitacion"),
        capacidad=data.get("capacidad"),
    )
    service.registrar_habitacion(habitacion)
    return jsonify({"mensaje": "Habitación registrada exitosamente"}), 201
