CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    categoria_id INT REFERENCES categorias(id) ON DELETE CASCADE
);

CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    producto_id INT REFERENCES productos(id) ON DELETE CASCADE,
    cliente_id INT NOT NULL,
    fecha_venta DATE NOT NULL,
    cantidad INT NOT NULL
);
