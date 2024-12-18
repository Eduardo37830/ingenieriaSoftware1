import sqlite3
from domain.entities.cita import Cita
from domain.repositories.i_cita_repository import ICitaRepository
from typing import List

class SQLiteCitaRepository(ICitaRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, cita: Cita) -> None:
        """Inserta o actualiza una cita"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if cita.id is None:
                cursor.execute(
                    """
                    INSERT INTO CITAS (motivoConsulta, fechaConsulta, horaConsulta, costoTotal, paciente_id, personalMedico_id, habitacion_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        cita.motivoConsulta,
                        cita.fechaConsulta,
                        cita.horaConsulta,
                        cita.costoTotal,
                        cita.paciente_id,
                        cita.personalMedico_id,
                        cita.habitacion_id,
                    ),
                )
            else:
                cursor.execute(
                    """
                    UPDATE CITAS SET motivoConsulta = ?, fechaConsulta = ?, horaConsulta = ?, costoTotal = ?, paciente_id = ?, personalMedico_id = ?, habitacion_id = ?
                    WHERE id = ?
                    """,
                    (
                        cita.motivoConsulta,
                        cita.fechaConsulta,
                        cita.horaConsulta,
                        cita.costoTotal,
                        cita.paciente_id,
                        cita.personalMedico_id,
                        cita.habitacion_id,
                        cita.id,
                    ),
                )
            conn.commit()

    def find_by_id(self, cita_id: int) -> Cita:
        """Busca una cita por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, motivoConsulta, fechaConsulta, horaConsulta, costoTotal, paciente_id, personalMedico_id, habitacion_id
                FROM CITAS
                WHERE id = ?
                """,
                (cita_id,),
            )
            row = cursor.fetchone()
            if row:
                return Cita(*row)
            return None

    def find_all(self) -> List[Cita]:
        """Devuelve todas las citas"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, motivoConsulta, fechaConsulta, horaConsulta, costoTotal, paciente_id, personalMedico_id, habitacion_id
                FROM CITAS
                """
            )
            rows = cursor.fetchall()
            return [Cita(*row) for row in rows]

    def delete(self, cita_id: int) -> None:
        """Elimina una cita por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM CITAS WHERE id = ?", (cita_id,))
            conn.commit()
