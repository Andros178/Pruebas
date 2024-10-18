import psycopg2

# Función para conectar a la base de datos
def connect_db():
    return psycopg2.connect(
        host="dpg-cs8n3gdds78s738ievrg-a.oregon-postgres.render.com",  # Reemplaza con tu host
        database="db_mzlr",  # Reemplaza con tu nombre de base de datos
        user="db_mzlr_user",  # Reemplaza con tu nombre de usuario
        password="Ck3u4ecUVP6awJmhC08NHegTwbyoQPJn",  # Reemplaza con tu contraseña
        port="5432"  # Puerto por defecto para PostgreSQL
    )

# Función para listar las tablas de la base de datos
def list_tables():
    connection = None
    try:
        # Conectar a la base de datos
        connection = connect_db()
        cursor = connection.cursor()

        # Obtener los nombres de las tablas de la base de datos
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)

        # Recuperar todas las filas (nombres de las tablas)
        tables = cursor.fetchall()

        # Mostrar el listado de tablas
        if tables:
            print("Tablas en la base de datos:")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print("No se encontraron tablas en la base de datos.")

        # Cerrar cursor y conexión
        cursor.close()
    except Exception as error:
        print(f"Error al obtener las tablas: {error}")
    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    list_tables()
