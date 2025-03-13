def consultar_vuelos(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        SELECT * FROM vuelos;
        """)
        
        vuelos = cursor.fetchall()
        for vuelo in vuelos:
            print(vuelo)
    except Exception as e:
        print("Error al consultar vuelos:", e)
    finally:
        cursor.close()
