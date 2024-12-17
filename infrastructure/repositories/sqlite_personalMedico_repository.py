import sqlite3
from typing import List
from domain.repositories.i_personalMedico_repository import IPersonalMedicoRepository
from domain.entities.personalMedico import PersonalMedico


class SQLitePersonalMedicoRepository(IPersonalMedicoRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def save(self, personal: PersonalMedico) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO PERSONAL_MEDICO (
                    id, nombre, tipoDocumento, disponibilidad, horarioEntrada, 
                    horarioSalida, especialidad, departamento
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    nombre = excluded.nombre,
                    tipoDocumento = excluded.tipoDocumento,
                    disponibilidad = excluded.disponibilidad,
                    horarioEntrada = excluded.horarioEntrada,
                    horarioSalida = excluded.horarioSalida,
                    especialidad = excluded.especialidad,
                    departamento = excluded.departamento
                """,
                (
                    personal.id,
                    personal.nombre,
                    personal.tipoDocumento,
                    personal.disponibilidad,
                    personal.horaInicioTurno,
                    personal.horaFinTurno,
                    personal.especializacion,
                    personal.departamento,
                )
            )
            conn.commit()

    def find_by_id(self, personal_id: int) -> PersonalMedico:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, nombre, tipoDocumento, disponibilidad, horarioEntrada, 
                       horarioSalida, especialidad, departamento 
                FROM PERSONAL_MEDICO 
                WHERE id = ?
                """,
                (personal_id,)
            )
            row = cursor.fetchone()
            if row:
                return PersonalMedico(*row)
            raise ValueError("Personal Médico no encontrado")

    def find_all(self) -> List[PersonalMedico]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, nombre, tipoDocumento, disponibilidad, horarioEntrada, 
                       horarioSalida, especialidad, departamento 
                FROM PERSONAL_MEDICO
                """
            )
            rows = cursor.fetchall()
            return [PersonalMedico(*row) for row in rows]
