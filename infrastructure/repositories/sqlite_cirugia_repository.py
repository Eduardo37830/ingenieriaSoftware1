import sqlite3
from domain.entities.cirugia import Cirugia
from domain.repositories.i_cirugia_repository import ICirugiaRepository
from typing import List

class SQLiteCirugiaRepository(ICirugiaRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, cirugia: Cirugia) -> None:
        """Inserta o actualiza una cirugía"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if cirugia.id is None:
                cursor.execute(
                    """
                    INSERT INTO CIRUGIAS (fechaCirugia, tipoCirugia, id_paciente, id_habitacion, horaCirugia)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        cirugia.fecha_cirugia,
                        cirugia.tipo_cirugia,
                        cirugia.id_paciente,
                        cirugia.id_habitacion,
                        cirugia.hora_cirugia,
                    ),
                )
            else:
                cursor.execute(
                    """
                    UPDATE CIRUGIAS SET fechaCirugia = ?, tipoCirugia = ?, id_paciente = ?, id_habitacion = ?, horaCirugia = ?
                    WHERE id = ?
                    """,
                    (
                        cirugia.fecha_cirugia,
                        cirugia.tipo_cirugia,
                        cirugia.id_paciente,
                        cirugia.id_habitacion,
                        cirugia.hora_cirugia,
                        cirugia.id,
                    ),
                )
            conn.commit()

    def find_by_id(self, cirugia_id: int) -> Cirugia:
        """Busca una cirugía por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, fechaCirugia, tipoCirugia, id_paciente, id_habitacion, horaCirugia
                FROM CIRUGIAS
                WHERE id = ?
                """,
                (cirugia_id,),
            )
            row = cursor.fetchone()
            if row:
                return Cirugia(*row)
            return None

    def find_all(self) -> List[Cirugia]:
        """Devuelve todas las cirugías"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, fechaCirugia, tipoCirugia, id_paciente, id_habitacion, horaCirugia
                FROM CIRUGIAS
                """
            )
            rows = cursor.fetchall()
            return [Cirugia(*row) for row in rows]

    def delete(self, cirugia_id: int) -> None:
        """Elimina una cirugía por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM CIRUGIAS WHERE id = ?", (cirugia_id,))
            conn.commit()
