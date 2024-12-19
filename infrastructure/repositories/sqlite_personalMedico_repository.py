import sqlite3
from domain.entities.personalMedico import PersonalMedico
from domain.repositories.i_personalMedico_repository import IPersonalMedicoRepository
from typing import List

class SQLitePersonalMedicoRepository(IPersonalMedicoRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, personal: PersonalMedico) -> None:
        """Inserta o actualiza un personal médico"""
        with self._connect() as conn:
            cursor = conn.cursor()
            if personal.id is None:
                cursor.execute(
                    """
                    INSERT INTO USUARIOS (nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        personal.nombre,
                        personal.correo,
                        personal.contrasena,
                        "Personal Médico",
                        personal.direccion,
                        personal.telefono,
                        personal.tipo_documento,
                        personal.numero_documento,
                    ),
                )
                usuario_id = cursor.lastrowid
                cursor.execute(
                    """
                    INSERT INTO PERSONAL_MEDICO (usuario_id, disponibilidad, horaInicioTurno, horaFinTurno, especializacion)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        usuario_id,
                        personal.disponibilidad,
                        personal.horaInicioTurno,
                        personal.horaInicioTurno,
                        personal.especializacion,
                    ),
                )
            else:
                cursor.execute(
                    """
                    UPDATE USUARIOS SET nombre = ?, correo = ?, direccion = ?, telefono = ?, tipo_documento = ?, numero_documento = ?
                    WHERE id = ?
                    """,
                    (
                        personal.nombre,
                        personal.correo,
                        personal.direccion,
                        personal.telefono,
                        personal.tipo_documento,
                        personal.numero_documento,
                        personal.usuario_id,
                    ),
                )
                cursor.execute(
                    """
                    UPDATE PERSONAL_MEDICO SET disponibilidad = ?, horaInicioTurno = ?, horaFinTurno = ?, especializacion = ?
                    WHERE usuario_id = ?
                    """,
                    (
                        personal.disponibilidad,
                        personal.hora_inicio_turno,
                        personal.hora_fin_turno,
                        personal.especializacion,
                        personal.usuario_id,
                    ),
                )
            conn.commit()

    def find_by_id(self, personal_id: int) -> PersonalMedico:
        """Busca un personal médico por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.correo, u.direccion, u.telefono, u.tipo_documento, u.numero_documento,
                       p.disponibilidad, p.horaInicioTurno, p.horaFinTurno, p.especializacion
                FROM PERSONAL_MEDICO p
                JOIN USUARIOS u ON p.usuario_id = u.id
                WHERE p.id = ?
                """,
                (personal_id,),
            )
            row = cursor.fetchone()
            if row:
                return PersonalMedico(*row)
            return None

    def find_all(self) -> List[PersonalMedico]:
        """Devuelve todo el personal médico."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.correo, u.contrasena, u.rol, u.direccion, u.telefono, u.tipo_documento, u.numero_documento,
                       p.disponibilidad, p.horaInicioTurno, p.horaFinTurno, p.especializacion
                FROM PERSONAL_MEDICO p
                JOIN USUARIOS u ON p.usuario_id = u.id
                """
            )
            rows = cursor.fetchall()
            return [
                PersonalMedico(
                    id=row[0],
                    nombre=row[1],
                    correo=row[2],
                    contrasena=row[3],
                    rol=row[4],
                    direccion=row[5],
                    telefono=row[6],
                    tipoDocumento=row[7],
                    numeroDocumento=row[8],
                    disponibilidad=row[9],
                    horaInicioTurno=row[10],
                    horaFinTurno=row[11],
                    especializacion=row[12],
                )
                for row in rows
            ]

    def delete(self, personal_id: int) -> None:
        """Elimina un personal médico por ID"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM PERSONAL_MEDICO WHERE id = ?", (personal_id,))
            conn.commit()

    def find_available (self, fecha_hora) -> List[PersonalMedico]:
        """Devuelve todo el personal médico disponible en una fecha y hora específicas"""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.correo, u.direccion, u.telefono, u.tipo_documento, u.numero_documento,
                       p.disponibilidad, p.horaInicioTurno, p.horaFinTurno, p.especializacion
                FROM PERSONAL_MEDICO p
                JOIN USUARIOS u ON p.usuario_id = u.id
                WHERE p.disponibilidad = 1 AND p.horaInicioTurno <= ? AND p.horaFinTurno >= ?
                """,
                (fecha_hora.time(), fecha_hora.time()),
            )
            rows = cursor.fetchall()
            return [PersonalMedico(*row) for row in rows]