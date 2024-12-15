
from flask import Blueprint, render_template, jsonify

from mappers.transaction_mapper import TransactionMapper

from ingenieriaSoftware1.application.services import transaction_application_service

# Crea un Blueprint llamado 'transactions'.
# Un Blueprint es una forma de organizar las rutas y lógica relacionada para una sección específica de la aplicación.
transaction_blueprint = Blueprint('transactions', __name__)
admission_blueprint = Blueprint('admissions', __name__)
personalAdmistraccion = Blueprint('personalAdmistraccion', __name__)
proveedoresAdmistraccion = Blueprint('proveedoresAdmistraccion', __name__)

# Crea una instancia de TransactionMapper, que se utilizará para obtener las transacciones.
mapper = TransactionMapper()

# Define una ruta asociada al Blueprint 'transactions'.
# Esta ruta se activa cuando el usuario visita la URL '/transactions'.
@transaction_blueprint.route('/transactions')
def show_transactions():
    # Llama al método `get_all_transactions` del `TransactionMapper` para obtener todas las transacciones.
    transactions = mapper.get_all_transactions()
    
    # Renderiza la plantilla 'transactions.html' y pasa la lista de transacciones al contexto de la plantilla.
    # Esto permite mostrar las transacciones en la interfaz de usuario.
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


@transaction_blueprint.route('/transactions/report')
def generate_report():
    #Genera un informe financiero de las transacciones.

    informe_dto = transaction_application_service.generate_financial_report()

    # Puedes mostrar el informe como JSON o renderizarlo en una plantilla HTML
    return jsonify({
        'total_depositos': informe_dto.total_depositos,
        'total_retiros': informe_dto.total_retiros,
        'saldo_promedio': informe_dto.saldo_promedio
    })
















