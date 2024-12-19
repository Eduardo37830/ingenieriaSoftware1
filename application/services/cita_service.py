from domain.repositories.i_cita_repository import ICitaRepository
from application.dtos.cita_dto import CitaDTO
from application.exceptions.application_error import NotFoundError
from domain.entities.cita import Cita
from datetime import datetime, time

class CitaApplicationService:
    def __init__(self, cita_repository: ICitaRepository):
        """
        Inicializa el servicio de aplicación de citas.
        :param cita_repository: Repositorio de citas que interactúa con la capa de persistencia.
        """
        self.cita_repository = cita_repository

    def registrar_cita(self, cita_dto: CitaDTO) -> CitaDTO:
        """
        Registra una nueva cita médica.
        :param cita_dto: Objeto de transferencia de datos (DTO) con la información de la cita.
        :return: CitaDTO con los datos de la cita creada.
        """
        cita = cita_dto.to_entity()  # Convertir el DTO a una entidad de dominio
        self.cita_repository.save(cita)  # Guardar en el repositorio
        return CitaDTO.from_entity(cita)

    def obtener_cita_por_id(self, cita_id: int) -> CitaDTO:
        """
        Obtiene los detalles de una cita por su ID.
        :param cita_id: ID de la cita a buscar.
        :return: CitaDTO con los detalles de la cita.
        :raises NotFoundError: Si la cita no se encuentra.
        """
        cita = self.cita_repository.find_by_id(cita_id)
        if not cita:
            raise NotFoundError(f"No se encontró una cita con el ID {cita_id}")
        return CitaDTO.from_entity(cita)

    def verificar_conflicto(self, cita_dto: CitaDTO) -> bool:
        """
        Verifica si la nueva cita entra en conflicto con alguna existente.
        :param cita_dto: DTO de la cita a verificar.
        :return: True si hay conflicto, False de lo contrario.
        """
        cita = cita_dto.to_entity()  # Convertir el DTO a entidad
        todas_las_citas = self.cita_repository.find_all()
        for otra_cita in todas_las_citas:
            if cita.verificarConflicto(otra_cita):  # Método en la entidad Cita
                return True
        return False

    def crear_cita(self, paciente_id: int, fecha: datetime, hora: time, motivo: str,
                   costoTotal: float,
                   personalMedico_id: int, habitacion_id: int = None) -> CitaDTO:
        """
        Crea una nueva cita médica.
        :param costoTotal:
        :param paciente_id: ID del paciente.
        :param fecha: Fecha de la cita (datetime).
        :param hora: Hora de la cita (datetime).
        :param motivo: Motivo de la consulta.
        :param personalMedico_id: ID del personal médico.
        :param habitacion_id: ID de la habitación (opcional).
        :return: CitaDTO con los datos de la cita creada.
        :raises ValueError: Si algún dato de entrada no es válido.
        """
        # Validación de entradas
        if not personalMedico_id or personalMedico_id <= 0:
            raise ValueError("El ID del personal médico no es válido.")
        if not paciente_id or paciente_id <= 0:
            raise ValueError("El ID del paciente no es válido.")

        # Crear la entidad de cita
        cita = Cita(
            id=1, # Se asigna automáticamente
            motivoConsulta=motivo,
            fechaConsulta=fecha,
            horaConsulta=hora,
            paciente_id=paciente_id,
            personalMedico_id=personalMedico_id,
            habitacion_id=habitacion_id,
            costoTotal=costoTotal
        )

        # Guardar la cita en el repositorio
        self.cita_repository.save(cita)

        # Retornar el DTO basado en la entidad creada
        return CitaDTO.from_entity(cita)

    def eliminar_cita(self, cita_id: int) -> bool:
        """
        Elimina una cita por su ID si existe.
        :param cita_id: ID de la cita a eliminar.
        :return: True si la cita fue eliminada, False si no se encontró.
        """
        cita = self.cita_repository.find_by_id(cita_id)
        if not cita:
            return False  # La cita no existe
        self.cita_repository.eliminar(cita_id)
        return True

    def listar_citas(self) -> list[CitaDTO]:
        """
        Lista todas las citas existentes.
        :return: Lista de CitaDTO con los detalles de cada cita.
        """
        citas = self.cita_repository.find_all()
        return [CitaDTO.from_entity(cita) for cita in citas]
