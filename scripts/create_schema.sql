-- Tabla de PACIENTES
CREATE TABLE PACIENTES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT,
    telefono INT,
    historialMedico TEXT
);

-- Tabla de CITAS
CREATE TABLE CITAS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    motivoConsulta TEXT NOT NULL,
    fechaConsulta TEXT NOT NULL,
    horaConsulta TEXT NOT NULL,
    nombrePaciente TEXT,
    paciente_id INTEGER NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES PACIENTES (id)
);

-- Tabla de PERSONAL_MEDICO
CREATE TABLE PERSONAL_MEDICO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipoDocumento TEXT,
    disponibilidad BOOLEAN,
    horarioEntrada DATETIME,
    horarioSalida DATETIME,
    especialidad TEXT,
    departamento TEXT
);

-- Tabla de HABITACION
CREATE TABLE HABITACIONES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disponibilidad BOOLEAN,
    tipoHabitacion TEXT
);

-- Tabla de CIRUGIA
CREATE TABLE CIRUGIAS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fechaCirugia DATETIME,
    tipoCirugia TEXT,
    id_paciente INTEGER NOT NULL,
    id_habitacion INTEGER,
    horaCirugia TEXT,
    FOREIGN KEY (id_paciente) REFERENCES PACIENTES (id),
    FOREIGN KEY (id_habitacion) REFERENCES HABITACIONES (id)
);

-- Tabla de FORMULA
CREATE TABLE FORMULAS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medicamento TEXT NOT NULL,
    tiempoUso TEXT,
    cantidad INT,
    nombrePaciente TEXT
);

-- Tabla de MEDICAMENTOS
CREATE TABLE MEDICAMENTOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipoMedicamento TEXT,
    fechaFabricacion DATETIME,
    fechaVencimiento DATETIME,
    cantidad INT,
    id_proveedor INTEGER,
    FOREIGN KEY (id_proveedor) REFERENCES PROVEEDORES (id)
);

-- Tabla de PROVEEDORES
CREATE TABLE PROVEEDORES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT,
    direccion TEXT
);

-- Tabla de EQUIPOS_MEDICOS
CREATE TABLE EQUIPOS_MEDICOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipoEquipo TEXT NOT NULL,
    funcionalidad TEXT,
    disponibilidad BOOLEAN
);
