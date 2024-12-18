-- Tabla de USUARIOS
CREATE TABLE USUARIOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    rol TEXT NOT NULL,
    direccion TEXT,
    telefono INT,
    tipo_documento TEXT,
    numero_documento TEXT NOT NULL UNIQUE
);

-- Tabla de PACIENTES
CREATE TABLE PACIENTES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS (id)
);

-- Tabla de PERSONAL_MEDICO
CREATE TABLE PERSONAL_MEDICO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    disponibilidad BOOLEAN,
    horaInicioTurno TIME,
    horaFinTurno TIME,
    especializacion TEXT,
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS (id)
);

-- Tabla de HISTORIALES_MEDICOS
CREATE TABLE HISTORIALES_MEDICOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha DATE NOT NULL,
    diagnostico TEXT NOT NULL,
    tratamiento TEXT,
    observaciones TEXT,
    medico_id INTEGER NOT NULL,
    paciente_id INTEGER NOT NULL,
    FOREIGN KEY (medico_id) REFERENCES PERSONAL_MEDICO (id),
    FOREIGN KEY (paciente_id) REFERENCES PACIENTES (id)
);

-- Tabla de CITAS
CREATE TABLE CITAS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    motivoConsulta TEXT NOT NULL,
    fechaConsulta DATE NOT NULL,
    horaConsulta TIME NOT NULL,
    costoTotal REAL,
    paciente_id INTEGER NOT NULL,
    personalMedico_id INTEGER NOT NULL,
    habitacion_id INTEGER,
    FOREIGN KEY (paciente_id) REFERENCES PACIENTES (id),
    FOREIGN KEY (personalMedico_id) REFERENCES PERSONAL_MEDICO (id),
    FOREIGN KEY (habitacion_id) REFERENCES HABITACIONES (id)
);

-- Tabla de HABITACIONES
CREATE TABLE HABITACIONES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disponibilidad BOOLEAN NOT NULL,
    tipo_habitacion TEXT NOT NULL,
    capacidad INT NOT NULL
);

-- Tabla de FORMULAS
CREATE TABLE FORMULAS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    medicamento_id INTEGER NOT NULL,
    descripcion TEXT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES PACIENTES (id),
    FOREIGN KEY (medicamento_id) REFERENCES MEDICAMENTOS (id)
);

-- Tabla de MEDICAMENTOS
CREATE TABLE MEDICAMENTOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipoMedicamento TEXT NOT NULL,
    fechaFabricacion DATE NOT NULL,
    fechaVencimiento DATE NOT NULL,
    cantidad INT NOT NULL,
    proveedor_id INTEGER,
    FOREIGN KEY (proveedor_id) REFERENCES PROVEEDORES (id)
);

-- Tabla de PROVEEDORES
CREATE TABLE PROVEEDORES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    fecha_entrega DATE,
    costo REAL,
    telefono_vendedor TEXT
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
-- Tabla de EQUIPOS_MEDICOS
CREATE TABLE EQUIPOS_MEDICOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipoEquipo TEXT NOT NULL,
    funcionalidad TEXT,
    disponibilidad BOOLEAN
);
