CREATE TABLE conductores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL
);

CREATE TABLE vehiculos (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    conductor_id INT REFERENCES conductores(id) ON DELETE CASCADE
);

CREATE TABLE peajes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);

-- Crear tabla pagos
CREATE TABLE pagos (
    id SERIAL PRIMARY KEY,
    vehiculo_id INT REFERENCES vehiculos(id) ON DELETE CASCADE,
    peaje_id INT REFERENCES peajes(id) ON DELETE CASCADE,
    fecha_pago DATE NOT NULL,
    total_pago DECIMAL(10, 2) NOT NULL
);