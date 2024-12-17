import sqlite3
from typing import List
from domain.repositories.i_formula_repository import IFormulaRepository
from domain.entities.formula import Formula

class SQLiteFormulaRepository(IFormulaRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, formula: Formula) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO FORMULAS (id, medicamento_id, cantidad, paciente_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                (formula.id, formula.medicamento_id, formula.cantidad, formula.paciente_id)
            )
            conn.commit()

    def find_by_id(self, formula_id: int) -> Formula:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, medicamento_id, cantidad, paciente_id FROM FORMULAS WHERE id = ?", (formula_id,))
            row = cursor.fetchone()
            if row:
                return Formula(*row)
            raise ValueError("Fórmula no encontrada")

    def find_all(self) -> List[Formula]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, medicamento_id, cantidad, paciente_id FROM FORMULAS")
            rows = cursor.fetchall()
            return [Formula(*row) for row in rows]
