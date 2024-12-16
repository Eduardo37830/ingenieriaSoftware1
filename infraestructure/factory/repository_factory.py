# infrastructure/factory/repository_factory.py
from infraestructure.repositories.sqlite_paciente_repository import SQLitePacienteRepository
from infraestructure.repositories.mongo_paciente_repository import MongoPacienteRepository
from infraestructure.repositories.sqlite_cita_repository import SQLiteCitaRepository
from infraestructure.repositories.mongo_cita_repository import MongoCitaRepository


class RepositoryFactory:
    @staticmethod
    def get_paciente_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLitePacienteRepository(config["db_path"])
        elif db_type == "mongo":
            return MongoPacienteRepository(config["db_url"], config["db_name"])
        else:
            raise ValueError("Tipo de base de datos no soportado")

## cita_repository.py
class RepositoryFactory:
    @staticmethod
    def get_cita_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLiteCitaRepository(config["db_path"])
        elif db_type == "mongo":
            return MongoCitaRepository(config["db_url"], config["db_name"])
        else:
            raise ValueError("Tipo de base de datos no soportado")