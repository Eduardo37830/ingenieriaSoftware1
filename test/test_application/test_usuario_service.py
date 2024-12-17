import unittest
from unittest.mock import MagicMock
from application.dtos.usuario_dto import UsuarioDTO
from application.services.usuario_service import UsuarioService
from domain.entities.usuario import Usuario
from domain.repositories.i_user_repository import IUserRepository as UsuarioRepository


class TestUsuarioService(unittest.TestCase):

    def setUp(self):
        """
        Configura el entorno antes de cada test.
        """
        # Crear un mock con spec para el repositorio
        self.usuario_repository = MagicMock(spec=UsuarioRepository)
        self.usuario_service = UsuarioService(self.usuario_repository)

        # Creamos un usuario de ejemplo
        self.usuario = Usuario(
            id=1,
            nombre="Juan Pérez",
            correo="juan.perez@example.com",
            contrasena="password123",
            rol="paciente",
            direccion="Calle Falsa 123",
            telefono="123456789",
            tipo_documento="DNI",
            numero_documento="12345678"
        )

    def test_autenticar_usuario_correcto(self):
        """
        Test de autenticación con credenciales correctas.
        """
        print("Ejecutando test: test_autenticar_usuario_correcto")
        # Simulamos que el repositorio devuelve el usuario correcto
        self.usuario_repository.buscar_por_correo.return_value = self.usuario

        # Ejecutamos el método de autenticación
        usuario_dto = self.usuario_service.autenticar_usuario("juan.perez@example.com", "password123")

        # Verificamos que se haya devuelto el DTO del usuario
        self.assertIsInstance(usuario_dto, UsuarioDTO)
        self.assertEqual(usuario_dto.id, 1)
        self.assertEqual(usuario_dto.nombre, "Juan Pérez")
        self.assertEqual(usuario_dto.correo, "juan.perez@example.com")
        self.assertEqual(usuario_dto.rol, "paciente")

        # Verificar que se llamó correctamente al método del repositorio
        self.usuario_repository.buscar_por_correo.assert_called_once_with("juan.perez@example.com")
        print("Resultado del test: Autenticación correcta verificada.")

    def test_autenticar_usuario_incorrecto(self):
        """
        Test de autenticación con credenciales incorrectas.
        """
        print("Ejecutando test: test_autenticar_usuario_incorrecto")
        # Simulamos que el repositorio devuelve el usuario pero la contraseña es incorrecta
        self.usuario_repository.buscar_por_correo.return_value = self.usuario

        # Ejecutamos el método de autenticación con una contraseña incorrecta
        usuario_dto = self.usuario_service.autenticar_usuario("juan.perez@example.com", "wrong_password")

        # Verificamos que el usuario no fue autenticado
        self.assertIsNone(usuario_dto)

        # Verificar que se llamó correctamente al método del repositorio
        self.usuario_repository.buscar_por_correo.assert_called_once_with("juan.perez@example.com")
        print("Resultado del test: Autenticación incorrecta verificada.")

    def test_obtener_usuario_por_id(self):
        """
        Test para obtener los detalles de un usuario por su ID.
        """
        print("Ejecutando test: test_obtener_usuario_por_id")
        # Simulamos que el repositorio devuelve el usuario correcto
        self.usuario_repository.buscar_por_id.return_value = self.usuario

        # Ejecutamos el método de obtención de usuario por ID
        usuario_dto = self.usuario_service.obtener_usuario_por_id(1)

        # Verificamos que se haya devuelto el DTO del usuario
        self.assertIsInstance(usuario_dto, UsuarioDTO)
        self.assertEqual(usuario_dto.id, 1)
        self.assertEqual(usuario_dto.nombre, "Juan Pérez")
        self.assertEqual(usuario_dto.correo, "juan.perez@example.com")
        self.assertEqual(usuario_dto.rol, "paciente")

        # Verificar que se llamó correctamente al método del repositorio
        self.usuario_repository.buscar_por_id.assert_called_once_with(1)
        print("Resultado del test: Usuario obtenido por ID verificado.")

    def test_obtener_usuario_por_id_no_existente(self):
        """
        Test cuando el usuario no existe en la base de datos.
        """
        print("Ejecutando test: test_obtener_usuario_por_id_no_existente")
        # Simulamos que el repositorio no encuentra el usuario
        self.usuario_repository.buscar_por_id.return_value = None

        # Ejecutamos el método de obtención de usuario por ID
        usuario_dto = self.usuario_service.obtener_usuario_por_id(99)

        # Verificamos que no se encontró el usuario
        self.assertIsNone(usuario_dto)

        # Verificar que se llamó correctamente al método del repositorio
        self.usuario_repository.buscar_por_id.assert_called_once_with(99)
        print("Resultado del test: Usuario no encontrado verificado.")

    def test_eliminar_usuario_existente(self):
        """
        Test para eliminar un usuario existente.
        """
        print("Ejecutando test: test_eliminar_usuario_existente")
        self.usuario_repository.buscar_por_id.return_value = self.usuario
        self.usuario_repository.eliminar = MagicMock()

        resultado = self.usuario_service.eliminar_usuario(1)

        self.assertTrue(resultado)
        self.usuario_repository.buscar_por_id.assert_called_once_with(1)
        self.usuario_repository.eliminar.assert_called_once_with(1)
        print("Resultado del test: Usuario eliminado exitosamente.")

    def test_eliminar_usuario_no_existente(self):
        """
        Test para intentar eliminar un usuario que no existe.
        """
        print("Ejecutando test: test_eliminar_usuario_no_existente")
        self.usuario_repository.buscar_por_id.return_value = None
        self.usuario_repository.eliminar = MagicMock()

        resultado = self.usuario_service.eliminar_usuario(1)

        self.assertFalse(resultado)
        self.usuario_repository.buscar_por_id.assert_called_once_with(1)
        self.usuario_repository.eliminar.assert_not_called()
        print("Resultado del test: Usuario no encontrado para eliminar verificado.")


if __name__ == '__main__':
    unittest.main()
