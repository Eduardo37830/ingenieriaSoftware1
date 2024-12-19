from domain.entities.cirugia import Cirugia
from domain.repositories.i_cirugia_repository import ICirugiaRepository
from application.dtos.cirugia_dto import CirugiaDTO
from application.exceptions.application_error import NotFoundError
from datetime import datetime


class CirugiaApplicationService:
    def __init__(self, cirugia_repository: ICirugiaRepository):
        """
        Inicializa el servicio de aplicación de cirugías.
        :param cirugia_repository: Repositorio de cirugías que interactúa con la capa de persistencia.
        """
        self.cirugia_repository = cirugia_repository

    def registrar_cirugia(self, cirugia_dto: CirugiaDTO) -> CirugiaDTO:
        """
        Registra una nueva cirugía.
        :param cirugia_dto: Objeto de transferencia de datos (DTO) con la información de la cirugía.
        :return: CirugiaDTO con los datos de la cirugía creada.
        """
        # Convertimos el DTO a entidad de dominio
        cirugia = cirugia_dto.to_entity()
        self.cirugia_repository.save(cirugia)  # Guardamos la cirugía en el repositorio
        return CirugiaDTO.from_entity(cirugia)  # Retornamos el DTO basado en la entidad guardada

    def obtener_cirugia_por_id(self, cirugia_id: int) -> CirugiaDTO:
        """
        Obtiene los detalles de una cirugía por su ID.
        :param cirugia_id: ID de la cirugía a buscar.
        :return: CirugiaDTO con los detalles de la cirugía.
        :raises NotFoundError: Si la cirugía no se encuentra.
        """
        cirugia = self.cirugia_repository.find_by_id(cirugia_id)
        if not cirugia:
            raise NotFoundError(f"No se encontró una cirugía con el ID {cirugia_id}")
        return CirugiaDTO.from_entity(cirugia)  # Convertimos la entidad en un DTO y lo retornamos

    def verificar_conflicto(self, cirugia_dto: CirugiaDTO) -> bool:
        """
        Verifica si la nueva cirugía entra en conflicto con alguna existente en el repositorio.
        :param cirugia_dto: DTO de la cirugía a verificar.
        :return: True si hay conflicto, False si no lo hay.
        """
        cirugia = cirugia_dto.to_entity()  # Convertimos el DTO en una entidad
        todas_las_cirugias = self.cirugia_repository.find_all()  # Obtenemos todas las cirugías
        for otra_cirugia in todas_las_cirugias:
            if cirugia.verificarConflicto(
                    otra_cirugia):  # Llamamos al método de la entidad Cirugia para verificar conflicto
                return True
        return False

    def crear_cirugia(self, paciente_id: int, fecha: datetime, hora: datetime, tipo: str,
                      personalMedico_id: int, habitacion_id: int = None) -> CirugiaDTO:
        """
        Crea una nueva cirugía.
        :param paciente_id: ID del paciente.
        :param fecha: Fecha de la cirugía (datetime).
        :param hora: Hora de la cirugía (datetime).
        :param tipo: Tipo de cirugía.
        :param personalMedico_id: ID del personal médico.
        :param habitacion_id: ID de la habitación (opcional).
        :return: CirugiaDTO con los datos de la cirugía creada.
        :raises ValueError: Si algún dato de entrada no es válido.
        """
        # Validación de entradas
        if not personalMedico_id or personalMedico_id <= 0:
            raise ValueError("El ID del personal médico no es válido.")
        if not paciente_id or paciente_id <= 0:
            raise ValueError("El ID del paciente no es válido.")
        if not tipo or len(tipo) == 0:
            raise ValueError("El tipo de cirugía no es válido.")

        # Crear la entidad de cirugía
        cirugia = Cirugia(
            id=None,  # El ID se asignará automáticamente
            tipo_cirugia=tipo,
            fecha_cirugia=fecha,
            hora_cirugia=hora,
            id_paciente=paciente_id,
            id_habitacion=habitacion_id,
        )

        # Guardar la cirugía en el repositorio
        self.cirugia_repository.save(cirugia)

        # Retornar el DTO basado en la entidad creada
        return CirugiaDTO.from_entity(cirugia)

    def eliminar_cirugia(self, cirugia_id: int) -> bool:
        """
        Elimina una cirugía por su ID si existe.
        :param cirugia_id: ID de la cirugía a eliminar.
        :return: True si la cirugía fue eliminada, False si no se encontró.
        """
        cirugia = self.cirugia_repository.find_by_id(cirugia_id)
        if not cirugia:
            return False  # La cirugía no existe
        self.cirugia_repository.delete(cirugia_id)
        return True

    def listar_cirugias(self) -> list[CirugiaDTO]:
        """
        Lista todas las cirugías existentes.
        :return: Lista de CirugiaDTO con los detalles de cada cirugía.
        """
        cirugias = self.cirugia_repository.find_all()
        return [CirugiaDTO.from_entity(cirugia) for cirugia in cirugias]  # Retorna una lista de DTOs
