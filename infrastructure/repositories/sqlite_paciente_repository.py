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
            cursor.execute(
                """
                INSERT INTO PACIENTES (
                    id, nombre, correo, contrasena, rol, direccion, telefono, tipoDocumento, numeroDocumento
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    nombre = excluded.nombre,
                    correo = excluded.correo,
                    contrasena = excluded.contrasena,
                    rol = excluded.rol,
                    direccion = excluded.direccion,
                    telefono = excluded.telefono,
                    tipoDocumento = excluded.tipoDocumento,
                    numeroDocumento = excluded.numeroDocumento
                """,
                (
                    paciente.id_usuario,
                    paciente.nombre,
                    paciente.correo,
                    paciente.contrasena,
                    paciente.rol,
                    paciente.direccion,
                    paciente.telefono,
                    paciente.tipoDocumento,
                    paciente.numeroDocumento,
                )
            )
            conn.commit()


    def find_by_id(self, paciente_id: int) -> Paciente:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, direccion, telefono, historialMedico FROM PACIENTES WHERE id = ?", (paciente_id,))
            row = cursor.fetchone()
            if row:
                return Paciente(*row)
            raise ValueError("Paciente no encontrado")

    def find_all(self) -> List[Paciente]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, direccion, telefono, historialMedico FROM PACIENTES")
            rows = cursor.fetchall()
            return [Paciente(*row) for row in rows]
