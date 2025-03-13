def checkin_pasajero(conexion, reserva_id):
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        UPDATE reservas
        SET estado = 'check-in'
        WHERE reserva_id = %s;
        """, (reserva_id,))
        
        conexion.commit()
        print("Check-in realizado exitosamente")
    except Exception as e:
        print("Error al realizar check-in:", e)
        conexion.rollback()
    finally:
        cursor.close()
