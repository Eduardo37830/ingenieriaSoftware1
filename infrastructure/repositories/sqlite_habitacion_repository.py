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
    def find_by_id(self, habitacion_id: int) -> Habitacion:
        """Busca una habitación por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, disponibilidad, tipo_habitacion, capacidad
                FROM HABITACIONES
                WHERE id = ?
                """,
                (habitacion_id,),
            )
            row = cursor.fetchone()
            if row is None:
                return None
            return Habitacion(*row)
    def find_all_by_paciente(self, paciente_id: int) -> List[Habitacion]:
        """Obtiene todas las habitaciones de un paciente"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, disponibilidad, tipo_habitacion, capacidad
                FROM HABITACIONES
                WHERE paciente_id = ?
                """,
                (paciente_id,),
            )
            return [Habitacion(*row) for row in cursor.fetchall()]
    def delete(self, habitacion_id: int) -> None:
        """Elimina una habitación"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM HABITACIONES
                WHERE id = ?
                """,
                (habitacion_id,),
            )
            conn.commit()