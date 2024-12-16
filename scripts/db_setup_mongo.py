from pymongo import MongoClient

# Configuración de conexión
MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "hospital_db"

def setup_mongo():
    """Configura la base de datos MongoDB inicializando colecciones."""
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    
    # 1. Crear colecciones (MongoDB las crea automáticamente al insertar datos)
    pacientes = db["pacientes"]
    citas = db["citas"]
    personal_medico = db["personal_medico"]
    habitaciones = db["habitaciones"]
    cirugias = db["cirugias"]
    formulas = db["formulas"]
    medicamentos = db["medicamentos"]
    proveedores = db["proveedores"]
    equipos_medicos = db["equipos_medicos"]

    # 2. Insertar datos de prueba (opcional)
    pacientes.insert_many([
        {"id": 1, "nombre": "Juan Pérez", "direccion": "Calle 123", "telefono": 123456789, "historialMedico": []},
        {"id": 2, "nombre": "Ana Gómez", "direccion": "Calle 456", "telefono": 987654321, "historialMedico": []}
    ])

    citas.insert_many([
        {"id": 1, "paciente_id": 1, "motivoConsulta": "Chequeo general", "fechaConsulta": "2024-06-20", "horaConsulta": "10:00"},
        {"id": 2, "paciente_id": 2, "motivoConsulta": "Dolor de cabeza", "fechaConsulta": "2024-06-21", "horaConsulta": "12:00"}
    ])

    print("Base de datos MongoDB configurada correctamente con datos de prueba.")
    client.close()

if __name__ == "__main__":
    setup_mongo()
