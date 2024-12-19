from application.services.cirugia_service import CirugiaApplicationService
from application.services.equipo_medico_service import EquipoMedicoApplicationService
from application.services.formula_service import FormulaApplicationService
from application.services.habitacion import HabitacionApplicationService
from application.services.historial_medico_service import HistorialMedicoApplicationService
from application.services.medicamento_service import MedicamentoApplicationService
from application.services.paciente_service import PacienteApplicationService
from application.services.personalMedico_service import PersonalMedicoService
from application.services.proveedor_service import ProveedorApplicationService
from application.services.usuario_service import UsuarioService
from application.services.cita_service import CitaApplicationService

class ServiceFactory:
    """
    Factory to create service instances based on the configured repository.
    """

    _services = {
        "personal_medico": PersonalMedicoService,
        "proveedor": ProveedorApplicationService,
        "usuario": UsuarioService,
        "cita": CitaApplicationService,
        "habitacion": HabitacionApplicationService,
        "paciente": PacienteApplicationService,
        "historial_medico": HistorialMedicoApplicationService,
        "medicamento": MedicamentoApplicationService,
        "formula": FormulaApplicationService,
        "cirugia": CirugiaApplicationService,
        "equipo_medico": EquipoMedicoApplicationService,

    }

    @staticmethod
    def get_service(service_type: str, repository):
        service_class = ServiceFactory._services.get(service_type)
        if service_class:
            return service_class(repository)
        raise ValueError(f"Service type not supported: {service_type}")