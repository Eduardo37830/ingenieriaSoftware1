import unittest
from unittest.mock import MagicMock
from application.services.proveedor_service import ProveedorApplicationService
from application.dtos.proveedor_dto import ProveedorDTO
from domain.entities.medicamento import Medicamento

class TestProveedorApplicationService(unittest.TestCase):

    def setUp(self):
        """
        Configura los mocks y objetos de prueba antes de cada test.
        """
        self.proveedor_repository = MagicMock()
        self.proveedor_service = ProveedorApplicationService(self.proveedor_repository)

        # Configuración de datos ficticios
        self.nombre = "Proveedor S.A."
        self.fecha_entrega = "2024-12-01"
        self.costo = 500.00
        self.telefono_vendedor = "3123456789"
        self.direccion = "Calle 123, Ciudad"

        # Datos de prueba
        self.proveedor_dto = ProveedorDTO(
            id_proveedor=1,
            nombre=self.nombre,
            fecha_entrega=self.fecha_entrega,
            costo=self.costo,
            telefono_vendedor=self.telefono_vendedor,
            direccion=self.direccion
        )

        # Datos ficticios de medicamento
        self.nombre_medicamento = "Ibuprofeno"
        self.tipo_medicamento = "Analgésico"
        self.fecha_fabricacion = "2024-11-01"
        self.fecha_vencimiento = "2025-11-01"
        self.cantidad = 100
        self.id_proveedor = 1

        self.medicamento = Medicamento(
            medicamento_id=1,
            nombre=self.nombre_medicamento,
            tipoMedicamento=self.tipo_medicamento,
            fechaFabricacion=self.fecha_fabricacion,
            fechaVencimiento=self.fecha_vencimiento,
            cantidad=self.cantidad,
            id_proveedor=self.id_proveedor
        )

    def test_registrar_proveedor(self):
        """
        Test de registro de un proveedor.
        """
        print("Ejecutando test: test_registrar_proveedor")
        proveedor_guardado = self.proveedor_dto.to_entity()
        proveedor_guardado.id_proveedor = 1

        self.proveedor_repository.save.return_value = 1
        self.proveedor_repository.buscar_por_id.return_value = proveedor_guardado

        # Registrar el proveedor
        proveedor_creado = self.proveedor_service.registrar_proveedor(self.proveedor_dto)

        # Verificar que el proveedor fue registrado correctamente
        self.proveedor_repository.save.assert_called_once()
        self.assertEqual(proveedor_creado.id_proveedor, 1)
        print("Resultado: Proveedor registrado correctamente.")

    def test_consultar_proveedor_por_id(self):
        """
        Verifica la consulta de un proveedor por su ID.
        """
        print("Ejecutando test: test_consultar_proveedor")

        # Crear el DTO de proveedor simulado con los atributos correctos
        proveedor = self.proveedor_dto.to_entity()

        # Asegurarse de que el mock tiene el valor correcto para id_proveedor
        proveedor.id_proveedor = 1  # Asignar el valor de id_proveedor de manera explícita

        # Configurar el mock para que el retorno de buscar_por_id sea el proveedor
        self.proveedor_repository.buscar_por_id.return_value = proveedor

        # Obtener el proveedor
        proveedor_obtenido = self.proveedor_service.consultar_proveedor_por_id(1)

        # Verificar que el proveedor fue encontrado
        self.assertEqual(proveedor_obtenido.id_proveedor, 1)

        print("Resultado: Proveedor consultado correctamente.")

    def test_actualizar_proveedor(self):
        """
        Verifica la actualización de un proveedor.
        """
        print("Ejecutando test: test_actualizar_proveedor")
        self.proveedor_repository.buscar_por_id.return_value = self.proveedor_dto.to_entity()

        # DTO con nuevos datos
        proveedor_dto_actualizado = ProveedorDTO(
            id_proveedor=1,
            nombre="Proveedor XYZ",
            fecha_entrega="2024-12-10",
            costo=450.00,
            telefono_vendedor="3129876543",
            direccion="Calle 456, Ciudad"
        )

        # Crear la entidad actualizada desde el DTO
        proveedor_actualizado = proveedor_dto_actualizado.to_entity()

        # Ejecutar el método
        resultado = self.proveedor_service.actualizar_proveedor(proveedor_dto_actualizado)

        # Verificar el resultado
        self.assertEqual(resultado, "Proveedor actualizado correctamente.")

        # Verificar que el save fue llamado una sola vez
        self.proveedor_repository.save.assert_called_once()

        # Verificar los atributos del objeto guardado
        # Obtener el objeto pasado al save
        args, _ = self.proveedor_repository.save.call_args
        proveedor_guardado = args[0]

        # Comprobar que los atributos del objeto guardado son los mismos
        self.assertEqual(proveedor_guardado.id, proveedor_actualizado.id)  # Cambio aquí
        self.assertEqual(proveedor_guardado.nombre, proveedor_actualizado.nombre)
        self.assertEqual(proveedor_guardado.fecha_entrega, proveedor_actualizado.fecha_entrega)
        self.assertEqual(proveedor_guardado.costo, proveedor_actualizado.costo)
        self.assertEqual(proveedor_guardado.telefono_vendedor, proveedor_actualizado.telefono_vendedor)
        self.assertEqual(proveedor_guardado.direccion, proveedor_actualizado.direccion)

        print("Resultado: Proveedor actualizado correctamente.")

    def test_eliminar_proveedor(self):
        """
        Verifica la eliminación de un proveedor.
        """
        print("Ejecutando test: test_eliminar_proveedor")
        self.proveedor_repository.buscar_por_id.return_value = self.proveedor_dto.to_entity()

        # Ejecutar el método
        resultado = self.proveedor_service.eliminar_proveedor(1)

        # Verificar que el repositorio eliminar fue llamado
        self.proveedor_repository.eliminar.assert_called_once_with(1)
        self.assertTrue(resultado)
        print("Resultado: Proveedor eliminado correctamente.")

    def test_registrar_pedido(self):
        """
        Verifica el registro de un pedido de medicamento.
        """
        print("Ejecutando test: test_registrar_pedido")
        # Simulamos que el medicamento ya existe
        self.proveedor_dto.to_entity().registrar_pedido(self.medicamento, 50)

        # Ejecutar el método
        resultado = self.proveedor_service.registrar_pedido(self.proveedor_dto.id_proveedor, self.medicamento.medicamento_id, 50)

        # Verificar el resultado
        self.assertEqual(resultado, f"Pedido registrado: 50 unidades de {self.medicamento.nombre}.")
        print("Resultado: Pedido registrado correctamente.")

if __name__ == '__main__':
    unittest.main()
