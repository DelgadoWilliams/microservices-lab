import os
import sys

# Se usa la librería psycopg2 para PostgreSQL y redis para Redis
try:
    import psycopg2
    import redis
except ImportError:
    print("❌ Error: psycopg2-binary o redis no están instalados. Asegúrese de que el Dockerfile los instale.")
    sys.exit(1)

def test_postgres_connection():
    """Prueba la conexión a PostgreSQL."""
    try:
        # Se usa 'postgres' como host, que es el nombre del servicio en docker-compose
        conn = psycopg2.connect(
            host='postgres',
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            connect_timeout=5
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        print("✅ Conexión a PostgreSQL exitosa.")
        conn.close()
    except Exception as e:
        print(f"❌ Falló la conexión a PostgreSQL. Mensaje: {e}")

def test_redis_connection():
    """Prueba la conexión a Redis."""
    try:
        # Se usa 'redis' como host, que es el nombre del servicio en docker-compose
        r = redis.Redis(
            host='redis',
            port=int(os.getenv("REDIS_PORT")),
            socket_connect_timeout=5
        )
        r.ping()
        print("✅ Conexión a Redis exitosa (PING OK).")
        
        # Prueba de lectura/escritura (opcional, pero útil)
        r.set('auth_test', 'connected')
        if r.get('auth_test').decode() == 'connected':
            print("✅ Lectura/Escritura en Redis OK.")
        else:
             print("❌ Error en Lectura/Escritura en Redis.")

    except Exception as e:
        print(f"❌ Falló la conexión a Redis. Mensaje: {e}")

if __name__ == "__main__":
    print("--- Probando Conexiones de Microservicio Auth ---")
    test_postgres_connection()
    test_redis_connection()