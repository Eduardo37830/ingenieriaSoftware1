import sqlite3
from domain.entities.historialMedico import HistorialMedico
from domain.repositories.i_historial_medico_repository import IHistorialMedicoRepository
from typing import List

class SQLiteHistorialMedicoRepository(IHistorialMedicoRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, historial: HistorialMedico) -> None:
        """Inserta o actualiza un historial médico"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if historial.id is None:
                cursor.execute(
                    """
                    INSERT INTO HISTORIALES_MEDICOS (fecha, diagnostico, tratamiento, observaciones, medico_id, paciente_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (historial.fecha, historial.diagnostico, historial.tratamiento, historial.observaciones, historial.medico_id, historial.paciente_id),
                )
            else:
                cursor.execute(
                    """
                    UPDATE HISTORIALES_MEDICOS SET fecha = ?, diagnostico = ?, tratamiento = ?, observaciones = ?, medico_id = ?, paciente_id = ?
                    WHERE id = ?
                    """,
                    (historial.fecha, historial.diagnostico, historial.tratamiento, historial.observaciones, historial.medico_id, historial.paciente_id, historial.id),
                )
            conn.commit()

    def find_by_id(self, historial_id: int) -> HistorialMedico:
        """Busca un historial médico por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, fecha, diagnostico, tratamiento, observaciones, medico_id, paciente_id
                FROM HISTORIALES_MEDICOS
                WHERE id = ?
                """,
                (historial_id,),
            )
            row = cursor.fetchone()
            if row:
                return HistorialMedico(*row)
            return None

    def find_all(self) -> List[HistorialMedico]:
        """Devuelve todos los historiales médicos"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, fecha, diagnostico, tratamiento, observaciones, medico_id, paciente_id
                FROM HISTORIALES_MEDICOS
                """
            )
            rows = cursor.fetchall()
            return [HistorialMedico(*row) for row in rows]

    def delete(self, historial_id: int) -> None:
        """Elimina un historial médico por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM HISTORIALES_MEDICOS WHERE id = ?", (historial_id,))
            conn.commit()
