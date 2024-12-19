import sqlite3
from datetime import time, datetime

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
            # Convertimos horaConsulta a string si es un objeto datetime.time
            horaConsulta_str = (
                cita.horaConsulta.strftime("%H:%M") if isinstance(cita.horaConsulta, time) else cita.horaConsulta
            )

            if cita.id is None:
                # Inserción
                cursor.execute(
                    """
                    INSERT INTO CITAS (motivoConsulta, fechaConsulta, horaConsulta, costoTotal, paciente_id, personalMedico_id, habitacion_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        cita.motivoConsulta,
                        cita.fechaConsulta,
                        horaConsulta_str,  # Usamos la conversión
                        cita.costoTotal,
                        cita.paciente_id,
                        cita.personalMedico_id,
                        cita.habitacion_id,
                    ),
                )
            else:
                # Actualización
                cursor.execute(
                    """
                    UPDATE CITAS SET motivoConsulta = ?, fechaConsulta = ?, horaConsulta = ?, costoTotal = ?, paciente_id = ?, personalMedico_id = ?, habitacion_id = ?
                    WHERE id = ?
                    """,
                    (
                        cita.motivoConsulta,
                        cita.fechaConsulta,
                        horaConsulta_str,  # Usamos la conversión
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
            return [
                Cita(
                    id=row[0],
                    motivoConsulta=row[1],
                    fechaConsulta=row[2],
                    horaConsulta=row[3],
                    costoTotal=row[4],
                    paciente_id=row[5],
                    personalMedico_id=row[6],
                    habitacion_id=row[7],
                )
                for row in rows
            ]

    def delete(self, cita_id: int) -> None:
        """Elimina una cita por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM CITAS WHERE id = ?", (cita_id,))
            conn.commit()

    def find_all_by_paciente(self, paciente_id: int) -> List[Cita]:
        """Devuelve todas las citas de un paciente"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, motivoConsulta, fechaConsulta, horaConsulta, costoTotal, paciente_id, personalMedico_id, habitacion_id
                FROM CITAS
                WHERE paciente_id = ?
                """,
                (paciente_id,),
            )
            rows = cursor.fetchall()
            return [Cita(*row) for row in rows]
