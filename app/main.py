# ---------------------------------------------------------------------------
# Importaciones
# ---------------------------------------------------------------------------
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, session, url_for

from controllers.paciente_controller import paciente_bp
from controllers.cita_controller import cita_bp
from controllers.cirugia_controller import cirugia_bp
from controllers.habitacion_controller import habitacion_bp
from controllers.medicamento_controller import medicamento_bp
from controllers.proveedor_controller import proveedor_bp
from controllers.formula_controller import formula_bp
from controllers.historialMedico_controller import historial_bp
from controllers.equipoMedico_controller import equipo_bp
from controllers.personalMedico_controller import personal_medico_bp
from controllers.user_controller import usuario_bp


app = Flask(__name__)
app.secret_key = 'secret_key'
app.register_blueprint(paciente_bp, url_prefix='/pacientes')
app.register_blueprint(cita_bp, url_prefix='/citas')
app.register_blueprint(cirugia_bp, url_prefix='/cirugias')
app.register_blueprint(habitacion_bp, url_prefix='/habitaciones')
app.register_blueprint(medicamento_bp, url_prefix='/medicamentos')
app.register_blueprint(proveedor_bp, url_prefix='/proveedores')
app.register_blueprint(formula_bp, url_prefix='/formulas')
app.register_blueprint(historial_bp, url_prefix='/historiales')
app.register_blueprint(equipo_bp, url_prefix='/equipos')
app.register_blueprint(personal_medico_bp, url_prefix='/personal')
app.register_blueprint(usuario_bp, url_prefix='/usuarios')
# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------------------------------------------------------
# Iniciar Sesion
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------Iniciar Sesión
@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')


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
# ---------------------------------------------------------------------------
# Cerrar Sesion
# ---------------------------------------------------------------------------
@app.route('/cerrar_sesion')
def cerrar_sesion():
    # Elimina todos los datos de la sesión
    session.clear()
    # Redirige al usuario a la página de inicio de sesión o inicio
    return redirect(url_for('home'))

# ---------------------------------------------------------------------------
# Inicio Cliente
# ---------------------------------------------------------------------------

def inicio_medico():
    return render_template('inicio_medico.html')

@app.route('/rutas')
def listar_rutas():
    rutas = [str(rule) for rule in app.url_map.iter_rules()]
    return {"rutas_disponibles": rutas}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)