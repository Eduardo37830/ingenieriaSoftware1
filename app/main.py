from flask import Flask, render_template, request, redirect, url_for
from controllers.transaction_controller import (transaction_blueprint,admission_blueprint, personalAdmistraccion,
proveedoresAdmistraccion,almacenAdmistraccion,medicamentoAdmistraccion, equipoMedicoAdmistraccion,
pacientesAdmistraccion, habitacionesAdmistraccion, cirugiaAdmistraccion, citasAdmindistraccion)

app = Flask(__name__)
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
  
@app.route("/")
def home():
    return render_template("index.html")
# ---------------------------------------------------------------------Inicio Cliente
@app.route('/inicio_cliente')
def inicio_cliente():
    return render_template('inicio_cliente.html')
# ---------------------------------------------------------------------AGENDAR CITA
@app.route('/agendar_cita', methods=["GET", "POST"])
def agendar_cita():
    if request.method == "POST":
        # Capturar los datos del formulario
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")
        tipo = request.form.get("tipo")
        medico = request.form.get("medico")
        
        print(f"Fecha: {fecha}, Hora: {hora}, Tipo: {tipo}, Médico: {medico}")
        
        # Mensaje de confirmación (puedes redirigir a otra página o mostrar un mensaje)
        mensaje = f"Cita agendada con éxito: Fecha: {fecha}, Hora: {hora}, Tipo: {tipo}, Médico: {medico}"
        return render_template("agendar_cita.html", mensaje=mensaje)
    
    # Si es un GET, simplemente renderiza el formulario
    return render_template('agendar_cita.html')

# ----------------------------------------------------------------------Citas Agendadas
# Datos de ejemplo (esto se puede conectar a una base de datos en producción)
citas = [
    {"id": 1, "fecha": "2024-12-15", "hora": "10:00", "tipo": "Consulta", "medico": "Dr. López"},
    {"id": 2, "fecha": "2024-12-16", "hora": "14:00", "tipo": "Revisión", "medico": "Dra. Gómez"},
    {"id": 3, "fecha": "2024-12-17", "hora": "09:30", "tipo": "Examen", "medico": "Dr. Pérez"}
]

# Ruta para mostrar las citas agendadas
@app.route('/citas_agendadas', methods=["GET", "POST"])
def citas_agendadas():
    if request.method == "POST":
        # Obtener el ID de la cita seleccionada para cancelar
        selected_id = request.form.get("seleccionar_cita")
        if selected_id:
            # Aquí manejarías la cancelación real (ej. eliminar de la base de datos)
            print(f"Cita cancelada con ID: {selected_id}")
        return redirect(url_for('citas_agendadas'))
    
    # Renderizar la plantilla con las citas
    return render_template('citas_agendadas.html', citas=citas)

@app.route('/cancelar_cita', methods=["POST"])
def cancelar_cita():
    selected_id = request.form.get("seleccionar_cita")
    if selected_id:
        print(f"Cita cancelada con ID: {selected_id}")
        # Aquí pondrías la lógica real para eliminar la cita de la base de datos
    return redirect(url_for('citas_agendadas'))

# ---------------------------------------------------------------------Historial Médico
@app.route('/historial_medico')
def historial_medico():
    # Datos de ejemplo para el historial médico
    historial = [
        {"fecha": "2024-06-01", "diagnostico": "Gripe", "tratamiento": "Reposo y líquidos", "medico": "Dr. Ramírez"},
        {"fecha": "2024-06-10", "diagnostico": "Faringitis", "tratamiento": "Antibióticos", "medico": "Dra. González"},
        {"fecha": "2024-06-20", "diagnostico": "Dolor de cabeza", "tratamiento": "Analgésicos", "medico": "Dr. Pérez"},
    ]
    return render_template('historial_medico.html', historial=historial)
# ---------------------------------------------------------------------Medicamentos
medicamentos = [
    {"fecha": "2024-06-01", "cantidad": 2, "nombre": "Paracetamol", "dosis": "500mg cada 8 horas"},
    {"fecha": "2024-06-05", "cantidad": 1, "nombre": "Ibuprofeno", "dosis": "400mg cada 6 horas"},
    {"fecha": "2024-06-10", "cantidad": 3, "nombre": "Amoxicilina", "dosis": "500mg cada 12 horas"},
]

@app.route('/medicamentos')
def medicamentos_view():
    return render_template('medicamentos.html', medicamentos=medicamentos)

# ---------------------------------------------------------------------Inicio Medico
@app.route('/inicio_medico')
def inicio_medico():
    return render_template('inicio_medico.html')
# ---------------------------------------------------------------------Citas Medicas
# Ejemplo de datos de citas (se podría conectar a una base de datos)
citas = [
    {"id": 1, "nombre": "Juan Pérez", "hora": "10:00", "fecha": "2024-12-15", "motivo": "Consulta General"},
    {"id": 2, "nombre": "María Gómez", "hora": "14:00", "fecha": "2024-12-16", "motivo": "Revisión Médica"},
    {"id": 3, "nombre": "Carlos López", "hora": "09:30", "fecha": "2024-12-17", "motivo": "Examen Especial"}
]
@app.route('/citas_medicas')
def citas_medicas():
    return render_template('citas_medicas.html', citas=citas)
# ---------------------------------------------------------------------Cirugias
# Datos de ejemplo para cirugías
cirugias = [
    {"nombre_paciente": "Juan Pérez", "hora": "08:00", "fecha": "2024-06-15", "habitacion": "101", "tipo": "Cardíaca", "personal_medico": "Dr. Gómez, Dra. López", "equipo_medico": "Anestesiólogo, Enfermero"},
    {"nombre_paciente": "María López", "hora": "10:00", "fecha": "2024-06-16", "habitacion": "102", "tipo": "Ortopédica", "personal_medico": "Dr. Martínez, Dra. Ruiz", "equipo_medico": "Asistente, Enfermero"},
    {"nombre_paciente": "Carlos Ramírez", "hora": "12:00", "fecha": "2024-06-17", "habitacion": "103", "tipo": "Neurológica", "personal_medico": "Dr. Pérez, Dra. Torres", "equipo_medico": "Instrumentista, Anestesiólogo"},
]

@app.route('/cirugias')
def cirugias_view():
    return render_template('cirugias.html', cirugias=cirugias)

# ---------------------------------------------------------------------Formula
@app.route('/formula')
def formula():
    return render_template('formula.html')
# ---------------------------------------------------------------------Main
if __name__ == "__main__":
    app.run(debug=True)
