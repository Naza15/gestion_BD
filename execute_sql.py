from db_connection import connect_db

def execute_sql():
    conn = connect_db()
    cursor = conn.cursor()

    with open('create_tables.sql', 'r') as f:
        cursor.execute(f.read())

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    execute_sql()
