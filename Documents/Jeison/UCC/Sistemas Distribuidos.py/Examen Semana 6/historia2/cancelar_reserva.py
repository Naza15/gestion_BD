def cancelar_reserva(conexion, reserva_id):
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        DELETE FROM reservas WHERE reserva_id = %s;
        """, (reserva_id,))
        
        conexion.commit()
        print("Reserva cancelada exitosamente")
    except Exception as e:
        print("Error al cancelar reserva:", e)
        conexion.rollback()
    finally:
        cursor.close()