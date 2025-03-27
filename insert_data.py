from db_connection import connect_db

def insert_data():
    conn = connect_db()
    cursor = conn.cursor()

    # Insertar Pasajeros
    cursor.execute("INSERT INTO Pasajeros (Nombre, Direccion) VALUES (%s, %s) RETURNING Pasajero_ID", ('Juan Pérez', 'Calle 123'))
    pasajero_id_juan = cursor.fetchone()[0]
    
    cursor.execute("INSERT INTO Pasajeros (Nombre, Direccion) VALUES (%s, %s) RETURNING Pasajero_ID", ('Ana García', 'Calle 456'))
    pasajero_id_ana = cursor.fetchone()[0]

    # Insertar Vuelos
    cursor.execute("INSERT INTO Vuelos (Vuelo_Numero, Vuelo_Fecha) VALUES (%s, %s)", ('AA101', '2025-07-01'))
    cursor.execute("INSERT INTO Vuelos (Vuelo_Numero, Vuelo_Fecha) VALUES (%s, %s)", ('BA202', '2025-07-02'))

    # Insertar Checkins
    cursor.execute("INSERT INTO Checkins (Pasajero_ID, Vuelo_Numero, Asiento, Estado_Checkin, Total_Fee) VALUES (%s, %s, %s, %s, %s)", (pasajero_id_juan, 'AA101', '12A', 'Confirmado', 50.00))
    cursor.execute("INSERT INTO Checkins (Pasajero_ID, Vuelo_Numero, Asiento, Estado_Checkin, Total_Fee) VALUES (%s, %s, %s, %s, %s)", (pasajero_id_ana, 'BA202', '1A', 'Confirmado', 45.00))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_data()
