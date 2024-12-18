import sqlite3
from domain.entities.proveedor import Proveedor
from domain.repositories.i_proveedor_repository import IProveedorRepository
from typing import List

class SQLiteProveedorRepository(IProveedorRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, proveedor: Proveedor) -> None:
        """Inserta o actualiza un proveedor"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if proveedor.id is None:
                cursor.execute(
                    """
                    INSERT INTO PROVEEDORES (nombre, fecha_entrega, costo, telefono_vendedor)
                    VALUES (?, ?, ?, ?)
                    """,
                    (proveedor.nombre, proveedor.fecha_entrega, proveedor.costo, proveedor.telefono_vendedor),
                )
            else:
                cursor.execute(
                    """
                    UPDATE PROVEEDORES SET nombre = ?, fecha_entrega = ?, costo = ?, telefono_vendedor = ?
                    WHERE id = ?
                    """,
                    (proveedor.nombre, proveedor.fecha_entrega, proveedor.costo, proveedor.telefono_vendedor, proveedor.id),
                )
            conn.commit()

    def find_by_id(self, proveedor_id: int) -> Proveedor:
        """Busca un proveedor por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, nombre, fecha_entrega, costo, telefono_vendedor
                FROM PROVEEDORES
                WHERE id = ?
                """,
                (proveedor_id,),
            )
            row = cursor.fetchone()
            if row:
                return Proveedor(*row)
            return None

    def find_all(self) -> List[Proveedor]:
        """Devuelve todos los proveedores"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, nombre, fecha_entrega, costo, telefono_vendedor
                FROM PROVEEDORES
                """
            )
            rows = cursor.fetchall()
            return [Proveedor(*row) for row in rows]

    def delete(self, proveedor_id: int) -> None:
        """Elimina un proveedor por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM PROVEEDORES WHERE id = ?", (proveedor_id,))
            conn.commit()
