def crear_vuelo(conexion, numero_vuelo, origen, destino, fecha_salida, capacidad):
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        INSERT INTO vuelos (numero_vuelo, origen, destino, fecha_salida, capacidad)
        VALUES (%s, %s, %s, %s, %s);
        """, (numero_vuelo, origen, destino, fecha_salida, capacidad))
        
        conexion.commit()
        print("Vuelo creado exitosamente")
    except Exception as e:
        print("Error al crear vuelo:", e)
        conexion.rollback()
    finally:
        cursor.close()
