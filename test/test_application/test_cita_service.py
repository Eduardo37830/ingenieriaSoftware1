import unittest
from unittest.mock import MagicMock
from ingenieriaSoftware1.application.dtos.usuario_dto import UsuarioDTO
from ingenieriaSoftware1.application.services.usuario_service import UsuarioService
from ingenieriaSoftware1.domain.entities.usuario import Usuario
from ingenieriaSoftware1.domain.repositories.i_user_repository import IUserRepository as UsuarioRepository
from ingenieriaSoftware1.domain.entities.historialMedico import HistorialMedico


class TestUsuarioService(unittest.TestCase):

    def setUp(self):
        """
        Configura el entorno antes de cada test.
        """
        self.usuario_repository = MagicMock(UsuarioRepository)
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

    def test_autenticar_usuario_incorrecto(self):
        """
        Test de autenticación con credenciales incorrectas.
        """
        # Simulamos que el repositorio devuelve el usuario la contraseña es incorrecta
        self.usuario_repository.buscar_por_correo.return_value = self.usuario

        # Ejecutamos el método de autenticación con una contraseña incorrecta
        usuario_dto = self.usuario_service.autenticar_usuario("juan.perez@example.com", "password")

        # Verificamos que el usuario no fue autenticado
        self.assertIsNone(usuario_dto)

    def test_obtener_usuario_por_id(self):
        """
        Test para obtener los detalles de un usuario por su ID.
        """
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

    def test_obtener_usuario_por_id_no_existente(self):
        """
        Test cuando el usuario no existe en la base de datos.
        """
        # Simulamos que el repositorio no encuentra el usuario
        self.usuario_repository.buscar_por_id.return_value = None

        # Ejecutamos el método de obtención de usuario por ID
        usuario_dto = self.usuario_service.obtener_usuario_por_id(99)

        # Verificamos que no se encontró el usuario
        self.assertIsNone(usuario_dto)

if __name__ == '__main__':
    unittest.main()
