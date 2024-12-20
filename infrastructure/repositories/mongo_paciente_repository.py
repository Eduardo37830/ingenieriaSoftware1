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
                INSERT INTO PACIENTES (id, nombre, direccion, telefono, historialMedico)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                nombre = excluded.nombre,
                direccion = excluded.direccion,
                telefono = excluded.telefono,
                historialMedico = excluded.historialMedico
                """,
                (paciente.id, paciente.nombre, paciente.direccion, paciente.telefono, paciente.historial_medico)
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
