CREATE SCHEMA ventas;

CREATE SCHEMA clientes;

CREATE TABLE ventas.productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE ventas.pedidos (
    id SERIAL PRIMARY KEY,
    producto_id INT REFERENCES ventas.productos(id) ON DELETE CASCADE,
    cliente_id INT NOT NULL,
    cantidad INT NOT NULL
);

CREATE TABLE clientes.direcciones (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    direccion VARCHAR(255) NOT NULL
);
