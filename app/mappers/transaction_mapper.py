# Define la clase TransactionMapper, que actúa como un "mapeador" para manejar transacciones.
# Se encarga de acceder a las transacciones, ya sea simuladas o provenientes de una base de datos.
class TransactionMapper:
    
    # Define un método llamado `get_all_transactions`.
    # Este método es responsable de devolver una lista de transacciones.
    def get_all_transactions(self):
        # Simula una lista de transacciones como datos estáticos.
        # Cada transacción es un diccionario que contiene:
        # - 'id': Identificador único de la transacción.
        # - 'description': Descripción de la transacción.
        # - 'amount': Monto de la transacción.
        return [
            {'id': 1, 'description': 'Compra en Amazon', 'amount': 100.5},  # Primera transacción simulada
            {'id': 2, 'description': 'Pago de servicios', 'amount': 50.0}   # Segunda transacción simulada
        ]
