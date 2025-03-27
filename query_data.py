from db_connection import connect_db

def query_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Checkins")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    query_data()
