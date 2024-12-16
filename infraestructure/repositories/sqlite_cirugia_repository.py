import sqlite3
from typing import List
from domain.repositories.i_cirugia_repository import ICirugiaRepository
from domain.entities.cirugia import Cirugia

class SQLiteCirugiaRepository(ICirugiaRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, cirugia: Cirugia) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO CIRUGIAS (id, fechaCirugia, tipoCirugia, id_paciente, id_habitacion, horaCirugia)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (cirugia.id, cirugia.fechaCirugia, cirugia.tipoCirugia, cirugia.id_paciente, cirugia.id_habitacion, cirugia.horaCirugia)
            )
            conn.commit()

    def find_by_id(self, cirugia_id: int) -> Cirugia:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, fechaCirugia, tipoCirugia, id_paciente, id_habitacion, horaCirugia FROM CIRUGIAS WHERE id = ?", (cirugia_id,))
            row = cursor.fetchone()
            if row:
                return Cirugia(*row)
            raise ValueError("Cirugía no encontrada")

    def find_all(self) -> List[Cirugia]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, fechaCirugia, tipoCirugia, id_paciente, id_habitacion, horaCirugia FROM CIRUGIAS")
            rows = cursor.fetchall()
            return [Cirugia(*row) for row in rows]
