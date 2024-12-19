from flask import Blueprint, render_template, request, redirect, session, url_for
from infrastructure.repositories.sqlite_user_repository import SqliteUserRepository
from application.services.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario_bp', __name__)
user_repository = SqliteUserRepository("../hospital.db")
usuario_service = UsuarioService(user_repository)

@usuario_bp.route('/procesar_inicio_sesion', methods=['POST'])
def iniciar_sesion():
    """Ruta para manejar el inicio de sesión."""
    if request.method == 'POST':
        cedula = request.form['cedula']
        contrasena = request.form['password']
        user = usuario_service.autenticar_usuario(cedula, contrasena)
        if user:
            # Almacenar la información del usuario en la sesión
            session['user_id'] = user.id
            session['user_role'] = user.rol
            # Redirigir según el rol del usuariov
            if user.rol == 'Medico':
                return redirect(url_for('inicio_medico'))
            elif user.rol == 'Paciente':
                return redirect(url_for('paciente_bp.inicio_cliente'))
            elif user.rol == 'Administrador':
                return redirect(url_for('dashboard'))
        else:
            return "Credenciales incorrectas", 401
    return render_template('iniciar_sesion.html')

@usuario_bp.route('/cerrar_sesion')
def cerrar_sesion():
    """Cierra la sesión del usuario."""
    session.clear()
    return redirect(url_for('home'))
