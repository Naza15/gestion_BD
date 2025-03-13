import psycopg2
from psycopg2 import sql

def conectar_db():
    # Configuración de la conexión
    try:
        conexion = psycopg2.connect(
            dbname="bank_db",  
            user="user",                      
            password="password",               
            host="localhost",
            port="5432"                             
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

def crear_tablas(conexion):
    cursor = conexion.cursor()
    try:
        # Crear tabla de Clientes
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Crear tabla de Cuentas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuentas (
            id SERIAL PRIMARY KEY,
            id_cliente INT REFERENCES clientes(id) ON DELETE CASCADE,
            tipo_cuenta VARCHAR(50) NOT NULL,
            saldo DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
            fecha_apertura TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Crear tabla de Transacciones
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacciones (
            id SERIAL PRIMARY KEY,
            id_cuenta INT REFERENCES cuentas(id) ON DELETE CASCADE,
            monto DECIMAL(10, 2) NOT NULL,
            tipo_transaccion VARCHAR(50) NOT NULL CHECK (tipo_transaccion IN ('Ingreso', 'Egreso')),
            fecha_transaccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Crear tabla de Categorías de Transacciones
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL UNIQUE
        );
        """)

        # Crear tabla de Transacciones-Categorías
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacciones_categorias (
            id_transaccion INT REFERENCES transacciones(id) ON DELETE CASCADE,
            id_categoria INT REFERENCES categorias(id) ON DELETE CASCADE,
            PRIMARY KEY (id_transaccion, id_categoria)
        );
        """)

        # Confirmar los cambios
        conexion.commit()
        print("Tablas creadas exitosamente")
    except Exception as e:
        print("Error al crear tablas:", e)
        conexion.rollback()
    finally:
        cursor.close()

def cerrar_conexion(conexion):
    if conexion:
        conexion.close()
        print("Conexión cerrada")

if __name__ == "__main__":
    conexion = conectar_db()
    if conexion:
        crear_tablas(conexion)
        cerrar_conexion(conexion)
