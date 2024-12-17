import sqlite3
from typing import List
from domain.repositories.i_user_repository import IUserRepository
from domain.entities.usuario import Usuario

class SqliteUserRepository(IUserRepository):

    def __init__(self, db_path: str):
        self.db_path = db_path

    def save(self, user: Usuario) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT OR REPLACE INTO USUARIOS (id, nombre, apellido, email, password) VALUES (?, ?, ?, ?, ?)',
            (user.id, user.nombre, user.apellido, user.email, user.password)
        )
        conn.commit()
        conn.close()

    def find_by_id(self, user_id: int) -> Usuario:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        return Usuario(*user) if user else None

    def find_all(self) -> List[Usuario]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user')
        users = cursor.fetchall()
        conn.close()
        return [Usuario(*user) for user in users]

    def delete(self, user_id: int) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM user WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()