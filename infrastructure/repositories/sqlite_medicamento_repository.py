import sqlite3
from typing import List
from domain.repositories.i_medicamento_repository import IMedicamentoRepository
from domain.entities.medicamento import Medicamento

class SQLiteMedicamentoRepository(IMedicamentoRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, medicamento: Medicamento) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO MEDICAMENTOS (id, nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad, id_proveedor)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (medicamento.id, medicamento.nombre, medicamento.tipoMedicamento,
                 medicamento.fechaFabricacion, medicamento.fechaVencimiento, medicamento.cantidad, medicamento.id_proveedor)
            )
            conn.commit()

    def find_by_id(self, medicamento_id: int) -> Medicamento:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad, id_proveedor FROM MEDICAMENTOS WHERE id = ?", (medicamento_id,))
            row = cursor.fetchone()
            if row:
                return Medicamento(*row)
            raise ValueError("Medicamento no encontrado")

    def find_all(self) -> List[Medicamento]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad, id_proveedor FROM MEDICAMENTOS")
            rows = cursor.fetchall()
            return [Medicamento(*row) for row in rows]
