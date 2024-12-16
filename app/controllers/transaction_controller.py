
from flask import Blueprint, render_template


from mappers.transaction_mapper import TransactionMapper, SimulacionCitasAdmistrador, SimulacionCirujias

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
simuladorcitas = SimulacionCitasAdmistrador()
simuladorcirugias = SimulacionCirujias()


@transaction_blueprint.route('/transactions')
def show_transactions():
    transactions = mapper.get_all_transactions()
    return render_template('transactions.html', transactions=transactions)
@admission_blueprint.route('/Administrador')
def show_admissions():
    return render_template('inicioAdministrador.html')
@personalAdmistraccion.route('/Administrador/personalmedico')
def show_personal():
    return render_template('personalMedicoAdmistrador.html')
@proveedoresAdmistraccion.route('/Administrador/proveedores')
def show_proveedores():
    return render_template('proveedoresAdmistrador.html')
@almacenAdmistraccion.route('/Administrador/almacen')
def show_almacen():
    return render_template('almacenAdmistrador.html')
@medicamentoAdmistraccion.route('/Administrador/almacen/medicamentos')
def show_medicamento():
    return render_template('medicamentosAdmistrador.html')
@equipoMedicoAdmistraccion.route('/Administrador/almacen/Equipo_medico')
def show_equipomedico():
    return render_template('equipoMedicoAdmistrador.html')
@pacientesAdmistraccion.route('/Administrador/pacientes')
def show_pacientes():
    return render_template('pacientesAdmistrador.html')
@habitacionesAdmistraccion.route('/Administrador/habitaciones')
def show_habitaciones():
    return render_template('habitacionesAdmistrador.html')
@cirugiaAdmistraccion.route('/Administrador/cirugias')
def show_cirugias():
    cirugias = simuladorcirugias.get_cirugias()
    return render_template('cirugiasAdmistrador.html', cirugias=cirugias)
@citasAdmindistraccion.route('/Administrador/citas')
def show_citas():
    citas = simuladorcitas.get_citas()
    return render_template('citasAdmistrador.html', citas=citas)