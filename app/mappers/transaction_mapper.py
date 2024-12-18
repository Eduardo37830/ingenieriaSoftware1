
class TransactionMapper:
    def get_all_transactions(self):
        return [
            {'id': 1, 'description': 'Compra en Amazon', 'amount': 100.5},  # Primera transacción simulada
            {'id': 2, 'description': 'Pago de servicios', 'amount': 50.0}   # Segunda transacción simulada
        ]
    def get_citas(self):
        return [
            {'Nombre': 'Carlos Hurtado', 'Hora consulta': '09:00 AM', 'Fecha consulta': '2024-06-20', 'Motivo de la consulta': 'Chequeo general', 'tipo': 'Presencial', 'Nombre del medico': 'Dra. Ana López'},
            {'Nombre': 'María González', 'Hora consulta': '02:30 PM', 'Fecha consulta': '2024-06-21', 'Motivo de la consulta': 'Consulta de seguimiento', 'tipo': 'Virtual', 'Nombre del medico': 'Dr. Juan Martínez'},
            {'Nombre': 'Luis Ramírez', 'Hora consulta': '11:00 AM', 'Fecha consulta': '2024-06-22', 'Motivo de la consulta': 'Dolor de espalda', 'tipo': 'Presencial', 'Nombre del medico': 'Dr. José Pérez'},
            {'Nombre': 'Ana Torres', 'Hora consulta': '01:00 PM', 'Fecha consulta': '2024-06-23', 'Motivo de la consulta': 'Revisión de análisis', 'tipo': 'Virtual', 'Nombre del medico': 'Dra. Laura Gómez'},
            {'Nombre': 'Pedro López', 'Hora consulta': '03:30 PM', 'Fecha consulta': '2024-06-24', 'Motivo de la consulta': 'Consulta cardiológica', 'tipo': 'Presencial', 'Nombre del medico': 'Dr. Francisco Morales'}
        ]
    def get_cirugias(self):
        return [
            {'Nombre': 'Carlos Hurtado', 'Hora': '08:00 AM', 'Fecha': '2024-06-01', 'Habitacion': '101', 'tipo': 'Consulta', 'lista personal medico': 'Dra. Pérez', 'lista equipo medico': 'Electrocardiograma'},
            {'Nombre': 'María González', 'Hora': '09:30 AM', 'Fecha': '2024-06-01', 'Habitacion': '202', 'tipo': 'Cirugía', 'lista personal medico': 'Dr. López', 'lista equipo medico': 'Bisturí, Monitor cardíaco'},
            {'Nombre': 'Pedro Martínez', 'Hora': '11:00 AM', 'Fecha': '2024-06-02', 'Habitacion': '303', 'tipo': 'Revisión', 'lista personal medico': 'Dra. Ruiz', 'lista equipo medico': 'Tensiómetro'},
            {'Nombre': 'Ana Torres', 'Hora': '01:00 PM', 'Fecha': '2024-06-02', 'Habitacion': '404', 'tipo': 'Consulta', 'lista personal medico': 'Dr. Ramírez', 'lista equipo medico': 'Estetoscopio'},
            {'Nombre': 'Luis Ramírez', 'Hora': '03:00 PM', 'Fecha': '2024-06-03', 'Habitacion': '505', 'tipo': 'Emergencia', 'lista personal medico': 'Dra. Hernández', 'lista equipo medico': 'Desfibrilador'}
        ]
    def get_proveedores(self):
        return [
            {'Nombre': 'Proveedor A', 'Direccion': 'Calle Principal 123', 'Telefono': '555-1234', 'PedidoPendiente': 'Medicamentos', 'FechaEntrega': '2024-12-20', 'CantidadPedidos': 5},
            {'Nombre': 'Proveedor B', 'Direccion': 'Av. Secundaria 456', 'Telefono': '555-5678', 'PedidoPendiente': 'Equipos Médicos', 'FechaEntrega': '2024-12-22', 'CantidadPedidos': 3},
            {'Nombre': 'Proveedor C', 'Direccion': 'Carrera Tercera 789', 'Telefono': '555-9012', 'PedidoPendiente': 'Insumos Quirúrgicos', 'FechaEntrega': '2024-12-25', 'CantidadPedidos': 8},
            {'Nombre': 'Proveedor D', 'Direccion': 'Boulevard Central 321', 'Telefono': '555-3456', 'PedidoPendiente': 'Instrumentos', 'FechaEntrega': '2024-12-27', 'CantidadPedidos': 2},
            {'Nombre': 'Proveedor E', 'Direccion': 'Av. Tecnológica 654', 'Telefono': '555-7890', 'PedidoPendiente': 'Ropa Quirúrgica', 'FechaEntrega': '2024-12-30', 'CantidadPedidos': 6}
        ]
    def get_personal_medico(self):
        return [
            {'Nombre': 'Dr. Juan Pérez', 'Departamento': 'Cardiología', 'Profesion': 'Cardiólogo', 'HorarioEntrada': '08:00 AM', 'HorarioSalida': '04:00 PM', 'Disponibilidad': 'Disponible'},
            {'Nombre': 'Dra. Ana Gómez', 'Departamento': 'Pediatría', 'Profesion': 'Pediatra', 'HorarioEntrada': '09:00 AM', 'HorarioSalida': '05:00 PM', 'Disponibilidad': 'Disponible'},
            {'Nombre': 'Dr. Luis Martínez', 'Departamento': 'Traumatología', 'Profesion': 'Traumatólogo', 'HorarioEntrada': '07:00 AM', 'HorarioSalida': '03:00 PM', 'Disponibilidad': 'No disponible'},
            {'Nombre': 'Dra. Carla Torres', 'Departamento': 'Ginecología', 'Profesion': 'Ginecóloga', 'HorarioEntrada': '10:00 AM', 'HorarioSalida': '06:00 PM', 'Disponibilidad': 'Disponible'},
            {'Nombre': 'Dr. Pedro Sánchez', 'Departamento': 'Urgencias', 'Profesion': 'Médico General', 'HorarioEntrada': '06:00 PM', 'HorarioSalida': '02:00 AM', 'Disponibilidad': 'Disponible'}
        ]
    def get_pacientes(self):
        return [
            {'Nombre': 'María López', 'Telefono': '555-1234', 'Direccion': 'Av. Siempre Viva 123', 'HistorialMedico': 'Diabetes, Hipertensión'},
            {'Nombre': 'Juan Pérez', 'Telefono': '555-5678', 'Direccion': 'Calle Falsa 456', 'HistorialMedico': 'Alergia a penicilina'},
            {'Nombre': 'Ana Gómez', 'Telefono': '555-9012', 'Direccion': 'Boulevard Central 789', 'HistorialMedico': 'Asma'},
            {'Nombre': 'Luis Torres', 'Telefono': '555-3456', 'Direccion': 'Carrera Segunda 321', 'HistorialMedico': 'Cirugía de corazón en 2020'},
            {'Nombre': 'Pedro Sánchez', 'Telefono': '555-7890', 'Direccion': 'Plaza Mayor 654', 'HistorialMedico': 'Colesterol alto'}
        ]
    def get_medicamentos(self):
        return [
            {'Nombre': 'Paracetamol', 'Tipo': 'Analgésico', 'CantidadDisponible': 100, 'FechaVencimiento': '2025-06-01', 'FechaFabricacion': '2023-06-01', 'Cantidad': 20, 'NombreProveedor': 'Proveedor A'},
            {'Nombre': 'Ibuprofeno', 'Tipo': 'Antiinflamatorio', 'CantidadDisponible': 150, 'FechaVencimiento': '2026-04-01', 'FechaFabricacion': '2024-01-15', 'Cantidad': 30, 'NombreProveedor': 'Proveedor B'},
            {'Nombre': 'Amoxicilina', 'Tipo': 'Antibiótico', 'CantidadDisponible': 200, 'FechaVencimiento': '2025-08-01', 'FechaFabricacion': '2023-05-20', 'Cantidad': 50, 'NombreProveedor': 'Proveedor C'},
            {'Nombre': 'Lorazepam', 'Tipo': 'Ansiolítico', 'CantidadDisponible': 80, 'FechaVencimiento': '2024-12-15', 'FechaFabricacion': '2022-12-15', 'Cantidad': 15, 'NombreProveedor': 'Proveedor D'},
            {'Nombre': 'Omeprazol', 'Tipo': 'Antiinflamatorio', 'CantidadDisponible': 120, 'FechaVencimiento': '2027-02-01', 'FechaFabricacion': '2024-02-01', 'Cantidad': 25, 'NombreProveedor': 'Proveedor E'}
        ]
    def get_habitaciones(self):
        return [
            {'Nombre': 'Habitación 101', 'Capacidad': 2, 'Tipo': 'Individual', 'Disponibilidad': 'Disponible'},
            {'Nombre': 'Habitación 102', 'Capacidad': 4, 'Tipo': 'Doble', 'Disponibilidad': 'No disponible'},
            {'Nombre': 'Habitación 103', 'Capacidad': 3, 'Tipo': 'Triple', 'Disponibilidad': 'Disponible'},
            {'Nombre': 'Habitación 104', 'Capacidad': 1, 'Tipo': 'Individual', 'Disponibilidad': 'Disponible'},
            {'Nombre': 'Habitación 105', 'Capacidad': 5, 'Tipo': 'Familiar', 'Disponibilidad': 'No disponible'}
        ]
    def get_equipos_medicos(self):
        return [
            {'Nombre': 'Electrocardiograma', 'Tipo': 'Monitoreo', 'Funcionalidad': 'Monitoreo de la actividad eléctrica del corazón', 'CantidadDisponible': 5, 'NombreProveedor': 'Proveedor A'},
            {'Nombre': 'Bisturí', 'Tipo': 'Corte', 'Funcionalidad': 'Realización de cortes quirúrgicos', 'CantidadDisponible': 3, 'NombreProveedor': 'Proveedor B'},
            {'Nombre': 'Desfibrilador', 'Tipo': 'Resucitación', 'Funcionalidad': 'Reanimación mediante descarga eléctrica', 'CantidadDisponible': 2, 'NombreProveedor': 'Proveedor C'},
            {'Nombre': 'Monitor cardíaco', 'Tipo': 'Monitoreo', 'Funcionalidad': 'Monitoreo de ritmo cardíaco', 'CantidadDisponible': 4, 'NombreProveedor': 'Proveedor D'},
            {'Nombre': 'Estetoscopio', 'Tipo': 'Diagnóstico', 'Funcionalidad': 'Escucha de sonidos corporales', 'CantidadDisponible': 6, 'NombreProveedor': 'Proveedor E'}
        ]

    





