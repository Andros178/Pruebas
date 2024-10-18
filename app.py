import psycopg2

# Conexión a la base de datos PostgreSQL
def connect_db():
    return psycopg2.connect(
        host="dpg-cs8n3gdds78s738ievrg-a.oregon-postgres.render.com",
        database="db_mzlr",
        user="db_mzlr_user",
        password="Ck3u4ecUVP6awJmhC08NHegTwbyoQPJn",
        port="5432"
    )

# Función para obtener un usuario por ID, vulnerable a inyección SQL
def get_user_vulnerable():
    user_id = input("Introduce el ID del usuario: ")  # Solicitamos el ID del usuario
    connection = None
    try:
        connection = connect_db()
        cursor = connection.cursor()

        # Consulta vulnerable a inyección SQL
        query = f"SELECT * FROM users WHERE id = {user_id};"
        print(f"Ejecutando consulta: {query}")
        cursor.execute(query)

        user = cursor.fetchall()
        print("Resultado de la consulta:")
        print(user)

        cursor.close()
    except Exception as e:
        print(f"Error al realizar la consulta: {e}")
    finally:
        if connection is not None:
            connection.close()
            print("hola")

if __name__ == "__main__":
    get_user_vulnerable()
