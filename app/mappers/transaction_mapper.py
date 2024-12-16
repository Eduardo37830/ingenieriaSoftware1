
class TransactionMapper:
    def get_all_transactions(self):
        return [
            {'id': 1, 'description': 'Compra en Amazon', 'amount': 100.5},  # Primera transacción simulada
            {'id': 2, 'description': 'Pago de servicios', 'amount': 50.0}   # Segunda transacción simulada
        ]
class SimulacionCitasAdmistrador:
    def get_citas(self):
        return [
            {'Nombre': 'Carlos Hurtado', 'Hora consulta': '09:00 AM', 'Fecha consulta': '2024-06-20', 'Motivo de la consulta': 'Chequeo general', 'tipo': 'Presencial', 'Nombre del medico': 'Dra. Ana López', 'Seleccionar': True},
            {'Nombre': 'María González', 'Hora consulta': '02:30 PM', 'Fecha consulta': '2024-06-21', 'Motivo de la consulta': 'Consulta de seguimiento', 'tipo': 'Virtual', 'Nombre del medico': 'Dr. Juan Martínez', 'Seleccionar': False},
            {'Nombre': 'Luis Ramírez', 'Hora consulta': '11:00 AM', 'Fecha consulta': '2024-06-22', 'Motivo de la consulta': 'Dolor de espalda', 'tipo': 'Presencial', 'Nombre del medico': 'Dr. José Pérez', 'Seleccionar': True},
            {'Nombre': 'Ana Torres', 'Hora consulta': '01:00 PM', 'Fecha consulta': '2024-06-23', 'Motivo de la consulta': 'Revisión de análisis', 'tipo': 'Virtual', 'Nombre del medico': 'Dra. Laura Gómez', 'Seleccionar': True},
            {'Nombre': 'Pedro López', 'Hora consulta': '03:30 PM', 'Fecha consulta': '2024-06-24', 'Motivo de la consulta': 'Consulta cardiológica', 'tipo': 'Presencial', 'Nombre del medico': 'Dr. Francisco Morales', 'Seleccionar': False}
        ]
class SimulacionCirujias:
    def get_cirugias(self):
        return [
            {'Nombre': 'Carlos Hurtado', 'Hora': '08:00 AM', 'Fecha': '2024-06-01', 'Habitacion': '101', 'tipo': 'Consulta', 'lista personal medico': 'Dra. Pérez', 'lista equipo medico': 'Electrocardiograma', 'Seleccionar': 1},
            {'Nombre': 'María González', 'Hora': '09:30 AM', 'Fecha': '2024-06-01', 'Habitacion': '202', 'tipo': 'Cirugía', 'lista personal medico': 'Dr. López', 'lista equipo medico': 'Bisturí, Monitor cardíaco', 'Seleccionar': 2},
            {'Nombre': 'Pedro Martínez', 'Hora': '11:00 AM', 'Fecha': '2024-06-02', 'Habitacion': '303', 'tipo': 'Revisión', 'lista personal medico': 'Dra. Ruiz', 'lista equipo medico': 'Tensiómetro', 'Seleccionar': 3},
            {'Nombre': 'Ana Torres', 'Hora': '01:00 PM', 'Fecha': '2024-06-02', 'Habitacion': '404', 'tipo': 'Consulta', 'lista personal medico': 'Dr. Ramírez', 'lista equipo medico': 'Estetoscopio', 'Seleccionar': 4},
            {'Nombre': 'Luis Ramírez', 'Hora': '03:00 PM', 'Fecha': '2024-06-03', 'Habitacion': '505', 'tipo': 'Emergencia', 'lista personal medico': 'Dra. Hernández', 'lista equipo medico': 'Desfibrilador', 'Seleccionar': 5}
        ]
class SimulacionPacientes:
    def get_paciente(self):
        return
