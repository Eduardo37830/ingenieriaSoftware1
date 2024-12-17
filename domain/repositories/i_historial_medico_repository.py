from domain.entities.historialMedico import HistorialMedico

class IHistorialMedicoRepository():
    def __init__(self, session):
        self.session = session  # Aquí deberías incluir tu mecanismo de conexión a la base de datos

    def save(self, historial_medico: HistorialMedico):
        self.session.add(historial_medico)
        self.session.commit()

    def find_by_id(self, historial_id: int) -> HistorialMedico:
        return self.session.query(HistorialMedico).filter_by(id=historial_id).first()

    def find_all_by_paciente(self, paciente_id: int) -> list:
        return self.session.query(HistorialMedico).filter_by(paciente_id=paciente_id).all()
