# ---------------------------------------------------------------------------
# Importaciones
# ---------------------------------------------------------------------------
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, session, url_for
from controllers.transaction_controller import (transaction_blueprint,admission_blueprint, personalAdmistraccion,
proveedoresAdmistraccion,almacenAdmistraccion,medicamentoAdmistraccion, equipoMedicoAdmistraccion,
pacientesAdmistraccion, habitacionesAdmistraccion, cirugiaAdmistraccion, citasAdmindistraccion)


app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesario para usar sesiones
app.register_blueprint(transaction_blueprint)
app.register_blueprint(admission_blueprint)
app.register_blueprint(personalAdmistraccion)
app.register_blueprint(proveedoresAdmistraccion)
app.register_blueprint(almacenAdmistraccion)
app.register_blueprint(medicamentoAdmistraccion)
app.register_blueprint(equipoMedicoAdmistraccion)
app.register_blueprint(pacientesAdmistraccion)
app.register_blueprint(habitacionesAdmistraccion)
app.register_blueprint(cirugiaAdmistraccion)
app.register_blueprint(citasAdmindistraccion)
# ---------------------------------------------------------------------------Home
@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------------------------------------------------------General

# ---------------------------------------------------------------------Iniciar Sesion

# Simulación de una base de datos
usuarios = {
    "123": {"password": "1234", "rol": 3},  # Ejemplo de usuario (Medico)
    "987": {"password": "abcd", "rol": 2},  # Ejemplo de usuario (Paciente)
    "111": {"password": "admin", "rol": 1}  # Ejemplo de usuario (Administrador)
}
# ---------------------------------------------------------------------Iniciar Sesión
@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')

@app.route('/procesar_inicio_sesion', methods=['POST'])
def procesar_inicio_sesion():
    cedula = request.form['cedula']
    contraseña = request.form['password']

    # Verificar si el usuario existe en la "base de datos"
    if cedula in usuarios and usuarios[cedula]["password"] == contraseña:
        # Almacenar la cédula en la sesión
        session['cedula'] = cedula
        rol = usuarios[cedula]["rol"]

        # Redirigir según el rol
        if rol == 3:
            return redirect(url_for('inicio_medico'))
        elif rol == 2:
            return redirect(url_for('inicio_cliente'))
        elif rol == 1:
            return redirect(url_for('admissions.show_admissions'))
    else:
        # Si las credenciales son incorrectas
        return "Credenciales incorrectas", 401
# ---------------------------------------------------------------------------
# Registrarse
# ---------------------------------------------------------------------------
@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellidos = request.form.get('apellidos')
        cedula = request.form.get('cedula')
        correo = request.form.get('correo')
        contraseña = request.form.get('password')
        rol = request.form.get('rol')

        # Aquí puedes agregar la lógica para almacenar los datos en la base de datos
        print(f"Nombres: {nombres}, Apellidos: {apellidos}, Cédula: {cedula}, Correo: {correo}, Contraseña: {contraseña}, Rol: {rol}")

        # Redirige a una página de éxito o muestra un mensaje
        return "Registro exitoso"

    return render_template('registrarse.html')
# ---------------------------------------------------------------------Cerrar sesion
@app.route('/cerrar_sesion')
def cerrar_sesion():
    # Elimina todos los datos de la sesión
    session.clear()
    # Redirige al usuario a la página de inicio de sesión o inicio
    return redirect(url_for('home'))

# ---------------------------------------------------------------------------Cliente

# ---------------------------------------------------------------------Inicio Cliente
@app.route('/inicio_cliente')
def inicio_cliente():
    return render_template('inicio_cliente.html')

# ---------------------------------------------------------------------AGENDAR CITA
@app.route('/agendar_cita', methods=["GET", "POST"])
def agendar_cita():
    
    cedula_usuario = session.get('cedula')
    if request.method == "POST":
        # Capturar los datos del formulario
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")
        tipo = request.form.get("tipo")
        medico = request.form.get("medico")
        
        
        print(f"Fecha: {fecha}, Hora: {hora}, Tipo: {tipo}, Médico: {medico},Cédula: {cedula_usuario}")
        
        # Mensaje de confirmación (puedes redirigir a otra página o mostrar un mensaje)
        mensaje = f"Cita agendada con éxito: Fecha: {fecha}, Hora: {hora}, Tipo: {tipo}, Médico: {medico}"
        return render_template("agendar_cita.html", mensaje=mensaje)
    
    # Si es un GET, simplemente renderiza el formulario
    return render_template('agendar_cita.html')

# -----------------------------------------------------------------------Citas Agendadas
@app.route('/citas_agendadas', methods=["GET", "POST"])
def citas_agendadas():
    # Simulamos que estos datos vienen de una fuente externa
    todas_las_citas = [
        {"id": 1, "fecha": "2024-12-15", "hora": "10:00", "tipo": "Consulta General", "medico": "Juan Pérez", "cedula": 123},
        {"id": 2, "fecha": "2024-12-16", "hora": "14:00", "tipo": "Revisión Médica", "medico": "María Gómez", "cedula": 987},
        {"id": 3, "fecha": "2024-12-17", "hora": "09:30", "tipo": "Examen Especial", "medico": "Carlos López", "cedula": 987},
    ]
    # Obtener la cédula del usuario desde la sesión
    cedula_usuario = session.get('cedula')

    if not cedula_usuario:
        return "No se ha iniciado sesión o no se ha proporcionado una cédula.", 403

    # Filtrar las citas asociadas a la cédula
    try:
        cedula_usuario = int(cedula_usuario)  # Convertir la cédula a entero
    except ValueError:
        return "Cédula inválida.", 400

    citas_usuario = [cita for cita in todas_las_citas if cita['cedula'] == cedula_usuario]

    if request.method == "POST":
        # Manejar la cancelación de citas
        cita_id = request.form.get("cita_id")
        if cita_id:
            try:
                cita_id = int(cita_id)
                citas_usuario = [cita for cita in citas_usuario if cita['id'] != cita_id]
                # Aquí se podría implementar la lógica para eliminar la cita de la base de datos o lista
            except ValueError:
                return "ID de cita inválido.", 400

    return render_template('citas_agendadas.html', citas=citas_usuario)


@app.route('/cancelar_cita', methods=["POST"])
def cancelar_cita():
    selected_id = request.form.get("seleccionar_cita")
    if selected_id:
        try:
            selected_id = int(selected_id)
            # Aquí podrías eliminar la cita de la base de datos o lista
            print(f"Cita cancelada con ID: {selected_id}")
            # Simulación: Redirigimos a citas_agendadas para que se actualice la lista
        except ValueError:
            return "ID de cita inválido.", 400
    else:
        return "No se seleccionó ninguna cita para cancelar.", 400
    return redirect(url_for('citas_agendadas'))

# ----------------------------------------------------------------------Historial Medico
@app.route('/historial_medico')
def historial_medico():
    # Simulamos que estos datos vienen de una fuente externa
    todos_los_historiales = [
        {"cedula": "987", "fecha": "2024-06-01", "diagnostico": "Gripe", "tratamiento": "Reposo y líquidos", "medico": "Dr. Ramírez"},
        {"cedula": "987", "fecha": "2024-06-10", "diagnostico": "Faringitis", "tratamiento": "Antibióticos", "medico": "Dra. González"},
        {"cedula": "123", "fecha": "2024-06-15", "diagnostico": "Migraña", "tratamiento": "Descanso y analgésicos", "medico": "Dr. López"},
        {"cedula": "987", "fecha": "2024-06-20", "diagnostico": "Dolor de cabeza", "tratamiento": "Analgésicos", "medico": "Dr. Pérez"},
    ]

    # Obtener la cédula del parámetro de la URL (si existe) o de la sesión
    cedula = request.args.get('cedula') or session.get('cedula')

    if not cedula:
        return "No se ha iniciado sesión o no se ha proporcionado una cédula.", 403

    # Filtrar el historial asociado a la cédula
    historial = [registro for registro in todos_los_historiales if registro['cedula'] == cedula]

    return render_template('historial_medico.html', historial=historial)


# ---------------------------------------------------------------------------
# Medicamentos
# ---------------------------------------------------------------------------
@app.route('/medicamentos')
def medicamentos_view():
    # Simulamos que estos datos vienen de una fuente externa
    todos_los_medicamentos = [
        {"cedula": "987", "fecha": "2024-06-01", "cantidad": 2, "nombre": "Paracetamol", "dosis": "500mg cada 8 horas"},
        {"cedula": "987", "fecha": "2024-06-05", "cantidad": 1, "nombre": "Ibuprofeno", "dosis": "400mg cada 6 horas"},
        {"cedula": "123", "fecha": "2024-06-08", "cantidad": 2, "nombre": "Loratadina", "dosis": "10mg cada 24 horas"},
        {"cedula": "987", "fecha": "2024-06-10", "cantidad": 8, "nombre": "Amoxicilina", "dosis": "500mg cada 12 horas"},
    ]

    # Obtener la cédula de la sesión
    cedula = session.get('cedula')

    if not cedula:
        return "No se ha iniciado sesión o no se ha proporcionado una cédula.", 403

    # Filtrar los medicamentos asociados a la cédula
    medicamentos = [medicamento for medicamento in todos_los_medicamentos if medicamento['cedula'] == cedula]

    return render_template('medicamentos.html', medicamentos=medicamentos)

# ---------------------------------------------------------------------------Medico

# ---------------------------------------------------------------------Inicio Medico

# Datos simulados de citas asociadas a cada médico
citas_por_medico = {
    "123": [  # Médico con cédula "123"
        {"id": 1, "nombre": "Pedro Pérez", "hora": "10:00", "fecha": "2024-12-15", "motivo": "Consulta General"},
        {"id": 2, "nombre": "María Gómez", "hora": "14:00", "fecha": "2024-12-16", "motivo": "Revisión Médica"},
    ],
    "987": [  # Paciente con cédula "987"
        {"id": 3, "nombre": "Carlos López", "hora": "09:30", "fecha": "2024-12-17", "motivo": "Examen Especial"},
    ],
}

@app.route('/inicio_medico')
def inicio_medico():
    return render_template('inicio_medico.html')
# ---------------------------------------------------------------------------
# Citas Medicas
# ---------------------------------------------------------------------------
@app.route('/citas_medicas')
def citas_medicas():
    # Ejemplo de datos de citas (se podría conectar a una base de datos)
    todas_las_citas = [
        {"id": 1, "nombre": "Juan Pérez", "hora": "10:00", "fecha": "2024-12-15", "motivo": "Consulta General", "cedula_paciente": 987, "cedula": 123},
        {"id": 2, "nombre": "María Gómez", "hora": "14:00", "fecha": "2024-12-16", "motivo": "Revisión Médica", "cedula_paciente": 987},
        {"id": 3, "nombre": "Carlos López", "hora": "09:30", "fecha": "2024-12-17", "motivo": "Examen Especial", "cedula_paciente": 987},
    ]

    # Verificar si hay una sesión activa
    cedula_medico = session.get('cedula')
    if not cedula_medico:
        return redirect(url_for('iniciar_sesion'))  # Redirigir al inicio de sesión si no hay sesión

    # Obtener las citas asociadas a la cédula del médico
    citas_medico = [cita for cita in todas_las_citas if cita.get("cedula") == int(cedula_medico)]

    return render_template('citas_medicas.html', citas=citas_medico)

# ---------------------------------------------------------------------------
# Cirugias
# ---------------------------------------------------------------------------
# Datos de ejemplo para cirugías
cirugias = [
    {"nombre_paciente": "Juan Pérez", "hora": "08:00", "fecha": "2024-06-15", "habitacion": "101", "tipo": "Cardíaca", "personal_medico": "Dr. Gómez, Dra. López", "equipo_medico": "Anestesiólogo, Enfermero", "cedula_paciente": "987"},
    {"nombre_paciente": "María López", "hora": "10:00", "fecha": "2024-06-16", "habitacion": "102", "tipo": "Ortopédica", "personal_medico": "Dr. Martínez, Dra. Ruiz", "equipo_medico": "Asistente, Enfermero", "cedula_paciente": "987"},
    {"nombre_paciente": "Carlos Ramírez", "hora": "12:00", "fecha": "2024-06-17", "habitacion": "103", "tipo": "Neurológica", "personal_medico": "Dr. Pérez, Dra. Torres", "equipo_medico": "Instrumentista, Anestesiólogo", "cedula_paciente": "123"},
]


@app.route('/cirugias')
def cirugias_view():
    # Obtener la cédula del usuario desde la sesión
    cedula_usuario = session.get('cedula')

    # Filtrar las cirugías asociadas a la cédula del usuario
    cirugias_usuario = [cirugia for cirugia in cirugias if cirugia['cedula_paciente'] == cedula_usuario]

    # Renderizar la plantilla con las cirugías filtradas
    return render_template('cirugias.html', cirugias=cirugias_usuario)

# ---------------------------------------------------------------------------
# Formula
# ---------------------------------------------------------------------------
@app.route('/formula')
def formula():
    return render_template('formula.html')
# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)