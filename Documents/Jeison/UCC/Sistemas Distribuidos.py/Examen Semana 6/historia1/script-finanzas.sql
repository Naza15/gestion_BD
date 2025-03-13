CREATE DATABASE bank_db;
\c bank_db;

CREATE TABLE clientes (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    saldo DECIMAL(10, 2)
);

CREATE TABLE transacciones (
    transaccion_id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(cliente_id),
    tipo VARCHAR(50),
    monto DECIMAL(10, 2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
