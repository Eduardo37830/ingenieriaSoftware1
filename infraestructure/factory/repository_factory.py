from infraestructure.repositories.sqlite_paciente_repository import SQLitePacienteRepository
from infraestructure.repositories.sqlite_cita_repository import SQLiteCitaRepository
from infraestructure.repositories.sqlite_personalMedico_repository import SQLitePersonalMedicoRepository
from infraestructure.repositories.sqlite_habitacion_repository import SQLiteHabitacionRepository
from infraestructure.repositories.sqlite_cirugia_repository import SQLiteCirugiaRepository
from infraestructure.repositories.sqlite_formula_repository import SQLiteFormulaRepository
from infraestructure.repositories.sqlite_medicamento_repository import SQLiteMedicamentoRepository
from infraestructure.repositories.sqlite_proveedor_repository import SQLiteProveedorRepository
from infraestructure.repositories.sqlite_equipoMedico_repository import SQLiteEquipoMedicoRepository

class RepositoryFactory:
    """
    Fábrica para crear instancias de repositorios según la base de datos configurada.
    Actualmente soporta SQLite.
    """
    
    @staticmethod
    def get_paciente_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLitePacienteRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")

    @staticmethod
    def get_cita_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLiteCitaRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")

    @staticmethod
    def get_personal_medico_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLitePersonalMedicoRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")

    @staticmethod
    def get_habitacion_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLiteHabitacionRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")

    @staticmethod
    def get_cirugia_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLiteCirugiaRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")

    @staticmethod
    def get_formula_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLiteFormulaRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")

    @staticmethod
    def get_medicamento_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLiteMedicamentoRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")

    @staticmethod
    def get_proveedor_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLiteProveedorRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")

    @staticmethod
    def get_equipo_medico_repository(db_type: str, config: dict):
        if db_type == "sqlite":
            return SQLiteEquipoMedicoRepository(config["db_path"])
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")
