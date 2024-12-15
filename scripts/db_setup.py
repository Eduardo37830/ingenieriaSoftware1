import sqlite3

def setup_database(db_name: str, schema_file: str):
    """Configura la base de datos SQLite ejecutando un script SQL."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Leer el script SQL desde el archivo
    with open(schema_file, "r") as file:
        script_sql = file.read()

    # Ejecutar el script SQL
    try:
        cursor.executescript(script_sql)
        print("Base de datos configurada correctamente.")
    except Exception as e:
        print(f"Error al configurar la base de datos: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    setup_database("hospital.db", "scripts/create_schema.sql")
