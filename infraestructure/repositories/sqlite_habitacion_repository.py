import sqlite3
from typing import List
from domain.repositories.i_habitacion_repository import IHabitacionRepository
from domain.entities.room import Habitacion

class SQLiteHabitacionRepository(IHabitacionRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, habitacion: Habitacion) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO HABITACIONES (id, disponibilidad, tipoHabitacion)
                VALUES (?, ?, ?)
                """,
                (habitacion.id, habitacion.disponibilidad, habitacion.tipoHabitacion)
            )
            conn.commit()

    def find_by_id(self, habitacion_id: int) -> Habitacion:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, disponibilidad, tipoHabitacion FROM HABITACIONES WHERE id = ?", (habitacion_id,))
            row = cursor.fetchone()
            if row:
                return Habitacion(*row)
            raise ValueError("Habitación no encontrada")

    def find_available(self) -> List[Habitacion]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, disponibilidad, tipoHabitacion FROM HABITACIONES WHERE disponibilidad = 1")
            rows = cursor.fetchall()
            return [Habitacion(*row) for row in rows]
