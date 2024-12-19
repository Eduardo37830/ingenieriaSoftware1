from flask import Blueprint, request, jsonify, render_template
from application.services.cita_service import CitaApplicationService
from infrastructure.repositories import SQLiteCitaRepository
from datetime import datetime

cita_bp = Blueprint('cita_bp', __name__)

# Inicialización del repositorio y servicio
cita_repository = SQLiteCitaRepository("hospital.db")
service = CitaApplicationService(cita_repository)


@cita_bp.route('/citas', methods=['POST'])
def agendar_cita():
    data = request.get_json()

    try:
        # Obtener los datos y crear la cita
        paciente_id = data.get("paciente_id")
        motivo = data.get("motivoConsulta")
        fecha = datetime.strptime(data.get("fechaConsulta"), "%Y-%m-%d")
        hora = datetime.strptime(data.get("horaConsulta"), "%H:%M:%S")
        personalMedico_id = data.get("personalMedico_id")
        habitacion_id = data.get("habitacion_id")

        # Llamar al servicio de la aplicación para crear la cita
        cita_dto = service.crear_cita(
            paciente_id=paciente_id,
            fecha=fecha,
            hora=hora,
            motivo=motivo,
            personalMedico_id=personalMedico_id,
            habitacion_id=habitacion_id
        )

        # Devolver respuesta
        return jsonify({"mensaje": "Cita agendada exitosamente", "cita": cita_dto.to_dict()}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error al agendar la cita", "detalle": str(e)}), 500


@cita_bp.route('/', methods=['GET'])
def listar_citas():
    try:
        # Obtener todas las citas a través del servicio
        citas_dto = service.listar_citas()

        # Convertir los DTOs a un formato adecuado para JSON
        citas = [cita.to_dict() for cita in citas_dto]

        return jsonify(citas), 200
    except Exception as e:
        return jsonify({"error": "Error al listar las citas", "detalle": str(e)}), 500

@cita_bp.route('/agendar_cita', methods=["GET", "POST"])
def agendar_cita_get():
    if request.method == "POST":
        paciente_id = request.form.get("paciente_id")
        motivo = request.form.get("motivoConsulta")
        fecha = request.form.get("fechaConsulta")
        hora = request.form.get("horaConsulta")
        personalMedico_id = request.form.get("personalMedico_id")
        habitacion_id = request.form.get("habitacion_id")

        try:
            # Llamar al servicio de la aplicación para crear la cita
            cita_dto = service.crear_cita(
                paciente_id=paciente_id,
                fecha=fecha,
                hora=hora,
                motivo=motivo,
                personalMedico_id=personalMedico_id,
                habitacion_id=habitacion_id
            )

            return jsonify({"mensaje": "Cita agendada exitosamente", "cita": cita_dto.to_dict()}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Error al agendar la cita", "detalle": str(e)}), 500

    return render_template("agendar_cita.html")

@cita_bp.route('/citas_agendadas', methods=["GET", "POST"])
def citas_agendadas():
    if request.method == "POST":
        paciente_id = request.form.get("paciente_id")
        citas = service.obtener_cita_por_id(paciente_id)
        return jsonify([cita.to_dict() for cita in citas]), 200

    return render_template("citas_agendadas.html")

@cita_bp.route('/citas_medicas')
def citas_medicas():
    return render_template('citas_medicas.html')