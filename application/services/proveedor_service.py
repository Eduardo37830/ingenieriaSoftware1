from application.dtos.proveedor_dto import ProveedorDTO
from domain.entities.proveedor import Proveedor
from domain.repositories.i_proveedor_repository import IProveedorRepository
from application.exceptions.application_error import NotFoundError
from datetime import datetime
from domain.entities.medicamento import Medicamento

class ProveedorApplicationService:
    def __init__(self, proveedor_repository: IProveedorRepository):
        """
        Inicializa el servicio de aplicación de proveedores.
        :param proveedor_repository: Repositorio de proveedores que interactúa con la capa de persistencia.
        """
        self.proveedor_repository = proveedor_repository

    def registrar_proveedor(self, proveedor_dto: ProveedorDTO) -> ProveedorDTO:
        """
        Registra un nuevo proveedor.
        :param proveedor_dto: Objeto de transferencia de datos (DTO) con la información del proveedor.
        :return: ProveedorDTO con los datos del proveedor creado.
        """
        proveedor = proveedor_dto.to_entity()  # Convertir el DTO a una entidad de dominio
        self.proveedor_repository.save(proveedor)  # Guardar en el repositorio
        return ProveedorDTO.from_entity(proveedor)  # Retornar el DTO basado en la entidad guardada

    def actualizar_proveedor(self, proveedor_dto: ProveedorDTO) -> str:
        """
        Actualiza los datos de un proveedor existente.
        :param proveedor_dto: DTO con los nuevos datos del proveedor.
        :return: Mensaje de confirmación de la actualización.
        """
        proveedor_existente = self.proveedor_repository.find_by_id(proveedor_dto.id_proveedor)
        if not proveedor_existente:
            raise NotFoundError(f"Proveedor con ID {proveedor_dto.id_proveedor} no encontrado.")

        # Actualizar la entidad del proveedor
        proveedor_actualizado = proveedor_dto.to_entity()
        self.proveedor_repository.save(proveedor_actualizado)  # Guardar los cambios en el repositorio
        return "Proveedor actualizado correctamente."

    def obtener_proveedor_por_id(self, proveedor_id: int) -> ProveedorDTO:
        """
        Verifica la consulta de un proveedor por su ID.
        :param proveedor_id: ID del proveedor a buscar.
        :return: ProveedorDTO con los detalles del proveedor.
        :raises NotFoundError: Si el proveedor no se encuentra.
        """
        proveedor = self.proveedor_repository.find_by_id(proveedor_id)
        if not proveedor:
            raise NotFoundError(f"No se encontró un proveedor con el ID {proveedor_id}")
        return ProveedorDTO.from_entity(proveedor)

    def crear_proveedor(self, nombre: str, fecha_entrega: datetime, costo: float, telefono_vendedor: str,
                        direccion: str, medicamentos: list[dict] = None) -> ProveedorDTO:
        """
        Crea un nuevo proveedor con una lista de medicamentos.
        :param nombre: Nombre del proveedor.
        :param fecha_entrega: Fecha de entrega (datetime).
        :param costo: Costo de la entrega.
        :param telefono_vendedor: Teléfono del vendedor.
        :param direccion: Dirección del proveedor.
        :param medicamentos: Lista de diccionarios que representan los medicamentos.
        :return: ProveedorDTO con los datos del proveedor creado.
        """

        # Validación de entradas
        if not nombre:
            raise ValueError("El nombre del proveedor es requerido.")
        if not fecha_entrega:
            raise ValueError("La fecha de entrega es requerida.")

        # Crear la lista de medicamentos a partir de los diccionarios proporcionados
        lista_medicamentos = []
        if medicamentos:
            for medicamento_data in medicamentos:
                medicamento = Medicamento(
                    medicamento_id=medicamento_data.get('medicamento_id'),
                    nombre=medicamento_data.get('nombre'),
                    tipoMedicamento=medicamento_data.get('tipo_medicamento'),
                    fechaFabricacion=medicamento_data.get('fecha_fabricacion'),
                    fechaVencimiento=medicamento_data.get('fecha_vencimiento'),
                    cantidad=medicamento_data.get('cantidad'),
                    id_proveedor=medicamento_data.get('id_proveedor')
                )
                lista_medicamentos.append(medicamento)

        # Crear el proveedor
        proveedor = Proveedor(
            id_proveedor=None,
            nombre=nombre,
            fecha_entrega=fecha_entrega,
            costo=costo,
            telefono_vendedor=telefono_vendedor,
            direccion=direccion
        )

        # Guardar el proveedor en el repositorio
        self.proveedor_repository.save(proveedor)

        # Retornar el DTO del proveedor
        return ProveedorDTO.from_entity(proveedor)

    def eliminar_proveedor(self, proveedor_id: int) -> bool:
        """
        Elimina un proveedor por su ID si existe.
        :param proveedor_id: ID del proveedor a eliminar.
        :return: True si el proveedor fue eliminado, False si no se encontró.
        """
        proveedor = self.proveedor_repository.find_by_id(proveedor_id)
        if not proveedor:
            return False  # El proveedor no existe
        self.proveedor_repository.delete(proveedor)
        return True

    def listar_proveedores(self) -> list[ProveedorDTO]:
        """
        Lista todos los proveedores existentes.
        :return: Lista de ProveedorDTO con los detalles de cada proveedor.
        """
        proveedores = self.proveedor_repository.find_all()
        return [ProveedorDTO.from_entity(proveedor) for proveedor in proveedores]

    def registrar_pedido(self, id_proveedor, medicamento_id, param):
        proveedor = self.proveedor_repository.find_by_id(id_proveedor)
        if not proveedor:
            raise NotFoundError(f"No se encontró un proveedor con el ID {id_proveedor}")
        proveedor.registrar_pedido(medicamento_id, param)
        self.proveedor_repository.save(proveedor)
        return "Pedido registrado correctamente."
