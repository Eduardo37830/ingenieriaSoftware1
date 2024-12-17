import sqlite3
from typing import List
from domain.repositories.i_paciente_repository import IPacienteRepository
from domain.entities.paciente import Paciente


class SQLitePacienteRepository(IPacienteRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, paciente: Paciente) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()

            # 1. Insertar en USUARIOS
            cursor.execute(
                """
                INSERT INTO USUARIOS (nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    paciente.nombre,
                    paciente.correo,
                    paciente.contrasena,
                    paciente.rol,
                    paciente.direccion,
                    paciente.telefono,
                    paciente.tipo_documento,
                    paciente.numero_documento
                )
            )
            # Obtener el ID generado para USUARIOS
            usuario_id = cursor.lastrowid

            # 2. Insertar en PACIENTES usando el ID de USUARIOS
            cursor.execute(
                """
                INSERT INTO PACIENTES (usuario_id)
                VALUES (?)
                """,
                (usuario_id,)
            )

            conn.commit()
            print("Paciente guardado correctamente.")

    def find_by_id(self, paciente_id: int) -> Paciente:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.correo, u.contrasena, u.rol, u.direccion, 
                    u.telefono, u.tipo_documento, u.numero_documento
                FROM PACIENTES p
                JOIN USUARIOS u ON p.usuario_id = u.id
                WHERE p.id = ?
                """,
                (paciente_id,)
            )
            row = cursor.fetchone()
            if row:
                return Paciente(
                    id=row[0],
                    nombre=row[1],
                    correo=row[2],
                    contrasena=row[3],
                    rol=row[4],
                    direccion=row[5],
                    telefono=row[6],
                    tipo_documento=row[7],
                    numero_documento=row[8]
                )
            else:
                raise ValueError("Paciente no encontrado.")


    def find_all(self) -> List[Paciente]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.correo, u.contrasena, u.rol, u.direccion, 
                    u.telefono, u.tipo_documento, u.numero_documento
                FROM PACIENTES p
                JOIN USUARIOS u ON p.usuario_id = u.id
                """
            )
            rows = cursor.fetchall()
            return [
                Paciente(
                    id=row[0],
                    nombre=row[1],
                    correo=row[2],
                    contrasena=row[3],
                    rol=row[4],
                    direccion=row[5],
                    telefono=row[6],
                    tipo_documento=row[7],
                    numero_documento=row[8]
                )
                for row in rows
            ]
