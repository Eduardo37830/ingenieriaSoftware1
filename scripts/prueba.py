import sys
import os

# Agregar el directorio raíz al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from infrastructure.repositories.sqlite_paciente_repository import SQLitePacienteRepository
from domain.entities.paciente import Paciente

# Configuración de la base de datos
DB_PATH = "test_hospital.db"
repo = SQLitePacienteRepository(DB_PATH)
"""  
# Crear un paciente
nuevo_paciente = Paciente( 
    id=None, # Será generado automáticamente
    nombre="Juan Pérez",
    correo="juan.perez@example.com",
    contrasena="1234",
    rol="Paciente",
    direccion="Calle 123",
    telefono=123456789,
    tipo_documento="DNI",
    numero_documento="12345678"
)

# Guardar el paciente en la base de datos
repo.save(nuevo_paciente)
print("Paciente insertado correctamente.")

"""
# Prueba: Buscar un paciente por ID
def test_find_by_id():
    paciente = repo.find_by_id(1)
    if paciente:
        print("Paciente encontrado:", paciente.nombre)
    else:
        print("Paciente no encontrado.")

if __name__ == "__main__":
    test_find_by_id()

test_find_by_id()