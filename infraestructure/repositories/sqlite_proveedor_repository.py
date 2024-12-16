import sqlite3
from typing import List
from domain.repositories.i_proveedor_repository import IProveedorRepository
from domain.entities.proveedor import Proveedor

class SQLiteProveedorRepository(IProveedorRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, proveedor: Proveedor) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO PROVEEDORES (id, nombre, telefono, direccion)
                VALUES (?, ?, ?, ?)
                """,
                (proveedor.id, proveedor.nombre, proveedor.telefono, proveedor.direccion)
            )
            conn.commit()

    def find_by_id(self, proveedor_id: int) -> Proveedor:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, telefono, direccion FROM PROVEEDORES WHERE id = ?", (proveedor_id,))
            row = cursor.fetchone()
            if row:
                return Proveedor(*row)
            raise ValueError("Proveedor no encontrado")

    def find_all(self) -> List[Proveedor]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, telefono, direccion FROM PROVEEDORES")
            rows = cursor.fetchall()
            return [Proveedor(*row) for row in rows]
