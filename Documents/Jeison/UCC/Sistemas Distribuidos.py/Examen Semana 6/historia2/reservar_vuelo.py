def reservar_vuelo(conexion, pasajero_id, vuelo_id):
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        INSERT INTO reservas (pasajero_id, vuelo_id, estado)
        VALUES (%s, %s, 'reservado');
        """, (pasajero_id, vuelo_id))
        
        conexion.commit()
        print("Reserva creada exitosamente")
    except Exception as e:
        print("Error al reservar vuelo:", e)
        conexion.rollback()
    finally:
        cursor.close()
