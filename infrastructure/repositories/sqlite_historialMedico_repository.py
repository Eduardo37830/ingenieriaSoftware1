import sqlite3
from typing import List
from domain.repositories.i_historial_medico_repository import IHistorialMedicoRepository
from domain.entities.historialMedico import HistorialMedico

class SqliteHistorialMedicoRepository(IHistorialMedicoRepository):
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, historial_medico: HistorialMedico):
        cursor = self.connection.cursor()
        cursor.execute(
            """
 INSERT INTO HISTORIALES_MEDICOS (paciente_id, fecha, diagnostico, tratamiento, observaciones, medico_id)
VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                historial_medico.paciente_id,
                historial_medico.fecha,
                historial_medico.diagnostico,
                historial_medico.tratamiento,
                historial_medico.observaciones,
                historial_medico.medico_id,
            ),
        )
        self.connection.commit()

    def find_by_id(self, historial_id: int) -> HistorialMedico:
        cursor = self.connection.cursor()
        cursor.execute(
            """
SELECT paciente_id, fecha, diagnostico, tratamiento, observaciones, medico_id
FROM HISTORIALES_MEDICOS
WHERE id = ?
            """,
            (historial_id,),
        )
        row = cursor.fetchone()
        if row:
            return HistorialMedico(*row)
        raise ValueError("Historial Médico no encontrado")
    
    def find_all_by_paciente(self, paciente_id: int) -> List[HistorialMedico]:
        cursor = self.connection.cursor()
        cursor.execute(
            """
SELECT id, fecha, diagnostico, tratamiento, observaciones, medico_id
FROM HISTORIALES_MEDICOS
WHERE paciente_id = ?
            """,
            (paciente_id,),
        )
        rows = cursor.fetchall()
        return [HistorialMedico(*row) for row in rows]
    
