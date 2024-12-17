import sqlite3
from typing import List
from domain.repositories.i_cita_repository import ICitaRepository
from domain.entities.cita import Cita

class SQLiteCitaRepository(ICitaRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, cita: Cita) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            # Columnas opcionales manejadas condicionalmente
            query = """
                INSERT INTO CITAS (id, motivoConsulta, fechaConsulta, horaConsulta, paciente_id, personalMedico_id, costoTotal, habitacion_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                cita.id,
                cita.motivoConsulta,
                cita.fechaConsulta,
                cita.horaConsulta,
                cita.paciente_id,
                cita.personalMedico_id,
                cita.costoTotal,
                cita.habitacion_id
            ))
            conn.commit()

    def find_by_id(self, cita_id: int) -> Cita:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, motivoConsulta, fechaConsulta, horaConsulta, paciente_id, personalMedico_id, costoTotal, habitacion_id 
                FROM CITAS WHERE id = ?
            """, (cita_id,))
            row = cursor.fetchone()
            if row:
                return Cita(*row)
            raise ValueError("Cita no encontrada")

    def find_all_by_paciente(self, paciente_id: int) -> List[Cita]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, motivoConsulta, fechaConsulta, horaConsulta, paciente_id, personalMedico_id, costoTotal, habitacion_id 
                FROM CITAS WHERE paciente_id = ?
            """, (paciente_id,))
            rows = cursor.fetchall()
            return [Cita(*row) for row in rows]
