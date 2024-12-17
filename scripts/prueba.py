import sys
import os

# Agregar el directorio raíz al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from infrastructure.factory.repository_factory import RepositoryFactory
from domain.entities.paciente import Paciente



# Configuración para SQLite
config_sqlite = {"db_path": "hospital.db"}

# Crear instancia del repositorio de pacientes
paciente_repo = RepositoryFactory.get_paciente_repository("sqlite", config_sqlite)

# Ejemplo de uso: Guardar un paciente
nuevo_paciente = Paciente(
    id=1,
    nombre="Juan Pérez",
    correo="juan.perez@example.com",
    contrasena="1234",
    rol="Paciente",
    direccion="Calle 123",
    telefono=123456789,
    tipoDocumento="DNI",
    numeroDocumento="12345678"
)

paciente_repo.save(nuevo_paciente)

# Ejemplo de uso: Buscar paciente por ID
paciente = paciente_repo.find_by_id(1)
print(paciente)
