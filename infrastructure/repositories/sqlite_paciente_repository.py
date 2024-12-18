import sqlite3
from domain.entities.paciente import Paciente
from domain.repositories.i_paciente_repository import IPacienteRepository
from typing import List

class SQLitePacienteRepository(IPacienteRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, paciente: Paciente) -> None:
        """Inserta o actualiza un paciente"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if paciente.id is None:
                # Insertar en USUARIOS y PACIENTES
                cursor.execute(
                    """
                    INSERT INTO USUARIOS (nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        paciente.nombre,
                        paciente.correo,
                        paciente.contrasena,
                        "Paciente",
                        paciente.direccion,
                        paciente.telefono,
                        paciente.tipo_documento,
                        paciente.numero_documento,
                    ),
                )
                usuario_id = cursor.lastrowid
                cursor.execute("INSERT INTO PACIENTES (usuario_id) VALUES (?)", (usuario_id,))
            else:
                # Actualizar en USUARIOS
                cursor.execute(
                    """
                    UPDATE USUARIOS SET nombre = ?, correo = ?, direccion = ?, telefono = ?, tipo_documento = ?, numero_documento = ?
                    WHERE id = ?
                    """,
                    (
                        paciente.nombre,
                        paciente.correo,
                        paciente.direccion,
                        paciente.telefono,
                        paciente.tipo_documento,
                        paciente.numero_documento,
                        paciente.id,
                    ),
                )
            conn.commit()

    def find_by_id(self, paciente_id: int) -> Paciente:
        """Busca un paciente por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.correo, u.direccion, u.telefono, u.tipo_documento, u.numero_documento
                FROM PACIENTES p
                JOIN USUARIOS u ON p.usuario_id = u.id
                WHERE p.id = ?
                """,
                (paciente_id,),
            )
            row = cursor.fetchone()
            if row:
                return Paciente(*row)
            return None

    def find_all(self) -> List[Paciente]:
        """Devuelve todos los pacientes"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.correo, u.direccion, u.telefono, u.tipo_documento, u.numero_documento
                FROM PACIENTES p
                JOIN USUARIOS u ON p.usuario_id = u.id
                """
            )
            rows = cursor.fetchall()
            return [Paciente(*row) for row in rows]

    def delete(self, paciente_id: int) -> None:
        """Elimina un paciente por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM PACIENTES WHERE id = ?
                """,
                (paciente_id,),
            )
            conn.commit()
