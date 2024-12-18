import sqlite3
from domain.entities.equipoMedico import EquipoMedico
from domain.repositories.i_equipoMedico_repository import IEquipoMedicoRepository
from typing import List

class SQLiteEquipoMedicoRepository(IEquipoMedicoRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, equipo: EquipoMedico) -> None:
        """Inserta o actualiza un equipo médico"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if equipo.id is None:
                cursor.execute(
                    """
                    INSERT INTO EQUIPOS_MEDICOS (tipoEquipo, funcionalidad, disponibilidad)
                    VALUES (?, ?, ?)
                    """,
                    (equipo.tipo_equipo, equipo.funcionalidad, equipo.disponibilidad),
                )
            else:
                cursor.execute(
                    """
                    UPDATE EQUIPOS_MEDICOS SET tipoEquipo = ?, funcionalidad = ?, disponibilidad = ?
                    WHERE id = ?
                    """,
                    (equipo.tipo_equipo, equipo.funcionalidad, equipo.disponibilidad, equipo.id),
                )
            conn.commit()

    def find_by_id(self, equipo_id: int) -> EquipoMedico:
        """Busca un equipo médico por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, tipoEquipo, funcionalidad, disponibilidad
                FROM EQUIPOS_MEDICOS
                WHERE id = ?
                """,
                (equipo_id,),
            )
            row = cursor.fetchone()
            if row:
                return EquipoMedico(*row)
            return None

    def find_all(self) -> List[EquipoMedico]:
        """Devuelve todos los equipos médicos"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, tipoEquipo, funcionalidad, disponibilidad
                FROM EQUIPOS_MEDICOS
                """
            )
            rows = cursor.fetchall()
            return [EquipoMedico(*row) for row in rows]

    def delete(self, equipo_id: int) -> None:
        """Elimina un equipo médico por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM EQUIPOS_MEDICOS WHERE id = ?", (equipo_id,))
            conn.commit()
