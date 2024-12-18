import sqlite3
from abc import ABC

from domain.entities.habitacion import Habitacion
from domain.repositories.i_habitacion_repository import IHabitacionRepository
from typing import List

class SQLiteHabitacionRepository(IHabitacionRepository, ABC):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, habitacion: Habitacion) -> None:
        """Inserta o actualiza una habitación"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if habitacion.id is None:
                cursor.execute(
                    """
                    INSERT INTO HABITACIONES (disponibilidad, tipo_habitacion, capacidad)
                    VALUES (?, ?, ?)
                    """,
                    (habitacion.disponibilidad, habitacion.tipo_habitacion, habitacion.capacidad),
                )
            else:
                cursor.execute(
                    """
                    UPDATE HABITACIONES SET disponibilidad = ?, tipo_habitacion = ?, capacidad = ?
                    WHERE id = ?
                    """,
                    (habitacion.disponibilidad, habitacion.tipo_habitacion, habitacion.capacidad, habitacion.id),
                )
            conn.commit()
