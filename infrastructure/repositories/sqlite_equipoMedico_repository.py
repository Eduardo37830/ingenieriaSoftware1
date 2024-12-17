import sqlite3
from typing import List
from domain.repositories.i_equipoMedico_repository import IEquipoMedicoRepository
from domain.entities.equipoMedico import EquipoMedico

class SQLiteEquipoMedicoRepository(IEquipoMedicoRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, equipo: EquipoMedico) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO EQUIPOS_MEDICOS (id, tipo_equipo, funcionalidad, disponibilidad)
                VALUES (?, ?, ?, ?)
                """,
                (equipo.id, equipo.tipo_equipo, equipo.funcionalidad, equipo.disponibilidad)
            )
            conn.commit()

    def find_by_id(self, equipo_id: int) -> EquipoMedico:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, tipoEquipo, funcionalidad, disponibilidad FROM EQUIPOS_MEDICOS WHERE id = ?", (equipo_id,))
            row = cursor.fetchone()
            if row:
                return EquipoMedico(*row)
            raise ValueError("Equipo Médico no encontrado")

    def find_all(self) -> List[EquipoMedico]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, tipoEquipo, funcionalidad, disponibilidad FROM EQUIPOS_MEDICOS")
            rows = cursor.fetchall()
            return [EquipoMedico(*row) for row in rows]
