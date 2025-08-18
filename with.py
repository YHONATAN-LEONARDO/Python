import socket
import sqlite3

print("=== Archivos ===")
# Guardar logs de una prueba de penetración
with open('log_hacking.txt', 'w') as log:
    log.write("Inicio de prueba de pentesting\n")
    log.write("Escaneo de puertos iniciado...\n")

# Leer los logs
with open('log_hacking.txt', 'r') as log:
    for linea in log:
        print("Log:", linea.strip())

print("\n=== Socket TCP ===")
# Crear un socket TCP de forma segura
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)  # timeout de 5 segundos
    target = ('127.0.0.1', 80)
    try:
        s.connect(target)
        print(f"Conectado a {target}")
        # Enviar un mensaje
        s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        # Recibir respuesta
        respuesta = s.recv(1024)
        print("Respuesta del servidor:", respuesta.decode())
    except Exception as e:
        print("Error en socket:", e)
# El socket se cierra automáticamente al salir del bloque

print("\n=== Base de datos SQLite ===")
# Registrar información de pruebas en una DB
with sqlite3.connect('pentesting.db') as conexion:
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS resultados (puerto INT, estado TEXT)")
    cursor.execute("INSERT INTO resultados VALUES (?, ?)", (80, "abierto"))
    conexion.commit()
    cursor.execute("SELECT * FROM resultados")
    for fila in cursor.fetchall():
        print(f"Puerto {fila[0]}: {fila[1]}")
# La conexión se cierra automáticamente
