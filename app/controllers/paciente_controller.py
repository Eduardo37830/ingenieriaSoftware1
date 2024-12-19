from flask import Blueprint, request, jsonify, render_template

from application.dtos.paciente_dto import PacienteDTO
from application.services.paciente_service import PacienteApplicationService
from domain.entities.paciente import Paciente
from infrastructure.repositories import SQLitePacienteRepository

paciente_bp = Blueprint('paciente_bp', __name__)
paciente_repository = SQLitePacienteRepository("../hospital.db")
service = PacienteApplicationService(paciente_repository)


@paciente_bp.route('/pacientes', methods=['POST'])
def registrar_paciente():
    data = request.get_json()
    paciente = PacienteDTO(
        id_usuario=None,
        nombre=data.get("nombre"),
        correo=data.get("correo"),
        contrasena=data.get("contrasena"),
        direccion=data.get("direccion"),
        telefono=data.get("telefono"),
        tipo_documento=data.get("tipo_documento"),
        numero_documento=data.get("numero_documento"),
        rol=data.get("rol")
    )
    service.registrar_paciente(paciente)
    return jsonify({"mensaje": "Paciente registrado exitosamente"}), 201


# Ruta para manejar GET /pacientes
@paciente_bp.route('/', methods=['GET'])
def listar_pacientes():
    """Devuelve una lista de pacientes renderizados en la plantilla."""
    try:
        pacientes_dto = service.lista_pacientes()

        pacientes = [p.to_dict() for p in pacientes_dto]

        return render_template('pacientesAdmistrador.html', pacientes=pacientes)
    except Exception as e:
        return jsonify({"error": "Error al listar pacientes", "detalle": str(e)}), 500


@paciente_bp.route('/pacientes/<int:id>', methods=['GET'])
def obtener_paciente(id):
    paciente = service.obtener_paciente_por_id(id)
    if paciente:
        return jsonify(paciente.to_dict()), 200
    return jsonify({"error": "Paciente no encontrado"}), 404


@paciente_bp.route('/inicio_cliente', methods=['GET'])
def inicio_cliente():
    return render_template('inicio_cliente.html')


@paciente_bp.route('/historial_medico')
def historial_medico():
    return render_template('historial_medico.html')
