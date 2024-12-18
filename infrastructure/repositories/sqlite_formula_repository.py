import sqlite3
from domain.entities.formula import Formula
from domain.repositories.i_formula_repository import IFormulaRepository
from typing import List

class SQLiteFormulaRepository(IFormulaRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, formula: Formula) -> None:
        """Inserta o actualiza una fórmula médica"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if formula.id is None:
                cursor.execute(
                    """
                    INSERT INTO FORMULAS (paciente_id, medicamento_id, descripcion, cantidad)
                    VALUES (?, ?, ?, ?)
                    """,
                    (formula.paciente_id, formula.medicamento_id, formula.descripcion, formula.cantidad),
                )
            else:
                cursor.execute(
                    """
                    UPDATE FORMULAS SET paciente_id = ?, medicamento_id = ?, descripcion = ?, cantidad = ?
                    WHERE id = ?
                    """,
                    (formula.paciente_id, formula.medicamento_id, formula.descripcion, formula.cantidad, formula.id),
                )
            conn.commit()

    def find_by_id(self, formula_id: int) -> Formula:
        """Busca una fórmula por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, paciente_id, medicamento_id, descripcion, cantidad
                FROM FORMULAS
                WHERE id = ?
                """,
                (formula_id,),
            )
            row = cursor.fetchone()
            if row:
                return Formula(*row)
            return None

    def find_all(self) -> List[Formula]:
        """Devuelve todas las fórmulas médicas"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, paciente_id, medicamento_id, descripcion, cantidad
                FROM FORMULAS
                """
            )
            rows = cursor.fetchall()
            return [Formula(*row) for row in rows]

    def delete(self, formula_id: int) -> None:
        """Elimina una fórmula médica por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM FORMULAS WHERE id = ?", (formula_id,))
            conn.commit()
