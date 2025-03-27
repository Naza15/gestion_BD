import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname='nombre_db',
        user='postgres',
        password='tu_contraseña',
        host='localhost',
        port='5432'
    )
    return conn
