import sqlite3
from domain.entities.medicamento import Medicamento
from domain.repositories.i_medicamento_repository import IMedicamentoRepository
from typing import List

class SQLiteMedicamentoRepository(IMedicamentoRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, medicamento: Medicamento) -> None:
        """Inserta o actualiza un medicamento"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if medicamento.medicamento_id is None:
                cursor.execute(
                    """
                    INSERT INTO MEDICAMENTOS (nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad, proveedor_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        medicamento.nombre,
                        medicamento.tipoMedicamento,
                        medicamento.fechaFabricacion,
                        medicamento.fechaVencimiento,
                        medicamento.cantidad,
                        medicamento.id_proveedor,
                    ),
                )
            else:
                cursor.execute(
                    """
                    UPDATE MEDICAMENTOS SET nombre = ?, tipoMedicamento = ?, fechaFabricacion = ?, fechaVencimiento = ?, cantidad = ?, proveedor_id = ?
                    WHERE id = ?
                    """,
                    (
                        medicamento.nombre,
                        medicamento.tipoMedicamento,
                        medicamento.fechaFabricacion,
                        medicamento.fechaVencimiento,
                        medicamento.cantidad,
                        medicamento.id_proveedor,
                        medicamento.medicamento_id,
                    ),
                )
            conn.commit()

    def find_by_id(self, medicamento_id: int) -> Medicamento:
        """Busca un medicamento por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad, proveedor_id
                FROM MEDICAMENTOS
                WHERE id = ?
                """,
                (medicamento_id,),
            )
            row = cursor.fetchone()
            if row:
                return Medicamento(*row)
            return None

    def find_all(self) -> List[Medicamento]:
        """Devuelve todos los medicamentos"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad, proveedor_id
                FROM MEDICAMENTOS
                """
            )
            rows = cursor.fetchall()
            return [Medicamento(*row) for row in rows]

    def delete(self, medicamento_id: int) -> None:
        """Elimina un medicamento por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM MEDICAMENTOS WHERE id = ?", (medicamento_id,))
            conn.commit()
