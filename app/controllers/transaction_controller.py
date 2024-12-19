
from flask import Blueprint, render_template, jsonify
from app.mappers.transaction_mapper import TransactionMapper


# Crea un Blueprint llamado 'transactions'.
# Un Blueprint es una forma de organizar las rutas y lógica relacionada para una sección específica de la aplicación.

transaction_blueprint = Blueprint('transactions', __name__)
admission_blueprint = Blueprint('admissions', __name__)
personalAdmistraccion = Blueprint('personalAdmistraccion', __name__)
proveedoresAdmistraccion = Blueprint('proveedoresAdmistraccion', __name__)
almacenAdmistraccion = Blueprint('almacenAdmistraccion', __name__)
medicamentoAdmistraccion = Blueprint('medicamentoAdmistraccion', __name__)
equipoMedicoAdmistraccion = Blueprint('equipoMedicoAdmistraccion', __name__)
pacientesAdmistraccion = Blueprint('pacientesAdmistraccion', __name__)
habitacionesAdmistraccion = Blueprint('habitacionesAdmistraccion', __name__)
cirugiaAdmistraccion = Blueprint('cirugiaAdmistraccion', __name__)
citasAdmindistraccion = Blueprint('citasAdmindistraccion', __name__)
mapper = TransactionMapper()


@transaction_blueprint.route('/transactions')
def show_transactions():
    transactions = mapper.get_all_transactions()
    return render_template('transactions.html', transactions=transactions)
@admission_blueprint.route('/Administrador')
def show_admissions():
    return render_template('inicioAdministrador.html')
@personalAdmistraccion.route('/Administrador/personalmedico')
def show_personal():
    personal_medico= mapper.get_personal_medico()
    return render_template('personalMedicoAdmistrador.html',personal_medico=personal_medico)
@proveedoresAdmistraccion.route('/Administrador/proveedores')
def show_proveedores():
    proveedores= mapper.get_proveedores()
    return render_template('proveedoresAdmistrador.html',proveedores=proveedores)
@almacenAdmistraccion.route('/Administrador/almacen')
def show_almacen():
    return render_template('almacenAdmistrador.html')
@medicamentoAdmistraccion.route('/Administrador/almacen/medicamentos')
def show_medicamento():
    medicamentos= mapper.get_medicamentos()
    return render_template('medicamentosAdmistrador.html', medicamentos=medicamentos)
@equipoMedicoAdmistraccion.route('/Administrador/almacen/Equipo_medico')
def show_equipomedico():
    equiposmedicos = mapper.get_equipos_medicos()
    return render_template('equipoMedicoAdmistrador.html', equiposmedicos=equiposmedicos)
@pacientesAdmistraccion.route('/Administrador/pacientes')
def show_pacientes():
    pacientes= mapper.get_pacientes()
    return render_template('pacientesAdmistrador.html', pacientes=pacientes)
@habitacionesAdmistraccion.route('/Administrador/habitaciones')
def show_habitaciones():
    habitaciones= mapper.get_habitaciones()
    return render_template('habitacionesAdmistrador.html', habitaciones=habitaciones)
@cirugiaAdmistraccion.route('/Administrador/cirugias')
def show_cirugias():
    cirugias = mapper.get_cirugias()
    return render_template('cirugiasAdmistrador.html', cirugias=cirugias)
@citasAdmindistraccion.route('/Administrador/citas')
def show_citas():
    citas = mapper.get_citas()
    return render_template('citasAdmistrador.html', citas=citas)