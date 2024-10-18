import psycopg2

# Función para conectar a la base de datos
def connect_db():
    return psycopg2.connect(
        host="dpg-cs8n3gdds78s738ievrg-a.oregon-postgres.render.com",
        database="db_mzlr",
        user="db_mzlr_user",
        password="Ck3u4ecUVP6awJmhC08NHegTwbyoQPJn",
        port="5432"
    )

# Función para consultar todos los usuarios
def get_all_users():
    query = "SELECT * FROM users"
    connection = None
    try:
        # Conectar a la base de datos
        connection = connect_db()
        cursor = connection.cursor()

        # Ejecutar la consulta
        cursor.execute(query)
        users = cursor.fetchall()

        # Mostrar los resultados
        if users:
            print("Usuarios registrados en la base de datos:")
            for user in users:
                print(f"ID: {user[0]}, Nombre: {user[1]}, Email: {user[2]}")
        else:
            print("No se encontraron usuarios.")

        # Cerrar el cursor y la conexión
        cursor.close()
    except Exception as error:
        print(f"Error al obtener usuarios: {error}")
    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    # Llamar a la función para consultar y mostrar los usuarios
    get_all_users()
