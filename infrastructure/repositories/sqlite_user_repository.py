import sqlite3
from typing import List, Optional
from domain.repositories.i_user_repository import IUserRepository
from domain.entities.usuario import Usuario


class SqliteUserRepository(IUserRepository):

    def __init__(self, db_path: str):
        self.db_path = db_path

    def save(self, user: Usuario) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT OR REPLACE INTO USUARIOS 
               (id, nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento) 
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (user.id, user.nombre, user.correo, user.contrasena, user.rol, user.direccion,
             user.telefono, user.tipo_documento, user.numero_documento)
        )
        conn.commit()
        conn.close()

    def buscar_por_id(self, user_id: int) -> Usuario:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM USUARIOS WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        return Usuario(*user) if user else None

    def get_all(self) -> List[Usuario]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM USUARIOS')
        users = cursor.fetchall()
        conn.close()
        return [Usuario(*user) for user in users]

    def delete(self, user_id: int) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM user WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()

    def buscar_por_cedula(self, numero_documento: str) -> Optional[Usuario]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM USUARIOS WHERE numero_documento = ?', (numero_documento,))
        user = cursor.fetchone()
        conn.close()
        return Usuario(*user) if user else None

    def delete (self, user_id: int) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM USUARIOS WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
