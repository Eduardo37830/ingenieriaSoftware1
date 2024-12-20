from flask import Blueprint, request, jsonify, render_template

from application.dtos.personal_medico_dto import PersonalMedicoDTO
from application.services.personalMedico_service import PersonalMedicoService
from domain.entities.personalMedico import PersonalMedico
from infrastructure.repositories import SQLitePersonalMedicoRepository

personal_medico_bp = Blueprint('personal_medico_bp', __name__)
personal_repository = SQLitePersonalMedicoRepository("../hospital.db")
service = PersonalMedicoService(personal_repository)

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
    )
    service.registrar_personal_medico(personal)
    return jsonify({"mensaje": "Personal médico registrado exitosamente"}), 201

@personal_medico_bp.route('/', methods=['GET'])
def listar_personal_medico():
    """Devuelve una lista de personal médico renderizado en la plantilla."""
    try:
        # Llamada al servicio para obtener el personal médico
        personal_medico = service.listar_personal_medico()

        # Convertimos los datos a diccionarios para el HTML
        personal = [p.to_dict() for p in personal_medico]

        # Renderizamos la plantilla con la información
        return render_template('personal.html', personal_medico=personal)
    except Exception as e:
        return jsonify({"error": "Error al listar personal médico", "detalle": str(e)}), 500


@personal_medico_bp.route('/personal/<int:id>', methods=['GET'])
def obtener_personal_medico(id):
    personal = service.obtener_personal_medico(id)
    if personal:
        return jsonify(personal.to_dict()), 200
    return jsonify({"error": "Personal médico no encontrado"}), 404

@personal_medico_bp.route('/personal/<int:id>', methods=['DELETE'])
def eliminar_personal_medico(id):
    service.eliminar_personal_medico(id)
    return jsonify({"mensaje": "Personal médico eliminado exitosamente"}), 200

@personal_medico_bp.route('/inicio_cliente', methods=['GET'])
def inicio_medico():
    return render_template('inicio_medico.html')

