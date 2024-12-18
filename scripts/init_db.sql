-- Insertar datos en la tabla USUARIOS
INSERT INTO USUARIOS (nombre, correo, contrasena, rol, direccion, telefono, tipo_documento, numero_documento) VALUES
('Carlos Pérez', 'carlos.perez@example.com', 'password123', 'Paciente', 'Calle 123', 1234567890, 'DNI', '12345678'),
('Ana Gómez', 'ana.gomez@example.com', 'password456', 'Médico', 'Calle 456', 987654321, 'DNI', '87654321'),
('Luis Fernández', 'luis.fernandez@example.com', 'password789', 'Médico', 'Avenida 789', 555555555, 'Pasaporte', 'A1234567'),
('Clara Torres', 'clara.torres@example.com', 'password321', 'Administrador', 'Boulevard 321', 444444444, 'DNI', '23456789');

-- Insertar datos en la tabla PACIENTES
INSERT INTO PACIENTES (usuario_id) VALUES
(1);

-- Insertar datos en la tabla PERSONAL_MEDICO
INSERT INTO PERSONAL_MEDICO (usuario_id, disponibilidad, horaInicioTurno, horaFinTurno, especializacion) VALUES
(2, 1, '08:00', '16:00', 'Cardiología'),
(3, 0, '14:00', '22:00', 'Neurología');

-- Insertar datos en la tabla HABITACIONES
INSERT INTO HABITACIONES (disponibilidad, tipo_habitacion, capacidad) VALUES
(1, 'Individual', 1),
(0, 'Doble', 2);

-- Insertar datos en la tabla HISTORIALES_MEDICOS
INSERT INTO HISTORIALES_MEDICOS (fecha, diagnostico, tratamiento, observaciones, medico_id, paciente_id) VALUES
('2023-01-15', 'Hipertensión', 'Tomar medicación diariamente', 'Control regular necesario', 1, 1),
('2023-03-10', 'Migraña crónica', 'Medicamentos específicos', 'Reducir estrés', 2, 1);

-- Insertar datos en la tabla CITAS
INSERT INTO CITAS (motivoConsulta, fechaConsulta, horaConsulta, costoTotal, paciente_id, personalMedico_id, habitacion_id) VALUES
('Dolor de cabeza', '2023-05-20', '09:00', 500.00, 1, 2, 1),
('Chequeo general', '2023-06-15', '14:00', 300.00, 1, 2, 2);

-- Insertar datos en la tabla MEDICAMENTOS
INSERT INTO MEDICAMENTOS (nombre, tipoMedicamento, fechaFabricacion, fechaVencimiento, cantidad, proveedor_id) VALUES
('Paracetamol', 'Analgesico', '2023-01-01', '2025-01-01', 100, 1),
('Ibuprofeno', 'Antiinflamatorio', '2023-02-01', '2025-02-01', 50, 2);

-- Insertar datos en la tabla FORMULAS
INSERT INTO FORMULAS (paciente_id, medicamento_id, descripcion, cantidad) VALUES
(1, 1, 'Tomar dos veces al día', 20),
(1, 2, 'Tomar una vez al día', 15);

-- Insertar datos en la tabla PROVEEDORES
INSERT INTO PROVEEDORES (nombre, fecha_entrega, costo, telefono_vendedor) VALUES
('Proveedor 1', '2023-01-01', 1000.00, '111111111'),
('Proveedor 2', '2023-02-01', 500.00, '222222222');

-- Insertar datos en la tabla CIRUGIAS
INSERT INTO CIRUGIAS (fechaCirugia, tipoCirugia, id_paciente, id_habitacion, horaCirugia) VALUES
('2023-05-01 08:00:00', 'Cirugía de corazón', 1, 1, '08:00');

-- Insertar datos en la tabla EQUIPOS_MEDICOS
INSERT INTO EQUIPOS_MEDICOS (tipoEquipo, funcionalidad, disponibilidad) VALUES
('Monitor cardíaco', 'Supervisión constante de ritmo cardíaco', 1),
('Tomógrafo', 'Imagen de alta precisión del cerebro', 0);
