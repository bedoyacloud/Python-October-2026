import sqlite3

# Abrimos la conexión a la base de datos
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

# 1. Creamos matriz física nueva de Usuarios con clave primaria estructurada con autoincremento garantizado
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT
    )
""")

# 2. Creamos tabla intercesora temporal de Alquileres diseñada para articular esquemas Muchos-A-Muchos (M:N)
# Declaramos textualmente que el entero id_usuario NO es valor escalar exento... ES en realidad una Llave Foránea atada a usuarios(id) original.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alquileres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        id_libro INTEGER,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
        FOREIGN KEY (id_libro) REFERENCES libros(id)
    )
""")

# 3. Insertamos y instanciamos e insertamos a un único usuario para alquilar el material atándolo por IDs.
cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Paco')")
cursor.execute("INSERT INTO alquileres (id_usuario, id_libro) VALUES (1, 1)") # El Usuario Paco (ID 1) solicita en préstamo vinculante y excluyente hacia 1984 (ID 1).
conexion.commit()

# 4. VISTA DE RESULTANTE EXTRAPOLADOR DE DATOS: IMPLEMENTACIÓN DE COMANDO JOIN
# Ejecutamos la consulta, concatenando las correlaciones PK/FK desde las tres vertientes uniendo de tal manera descripciones alfabéticas consolidadas.
consulta_join = """
    SELECT usuarios.nombre, libros.titulo
    FROM alquileres
    JOIN usuarios ON alquileres.id_usuario = usuarios.id
    JOIN libros ON alquileres.id_libro = libros.id
"""
cursor.execute(consulta_join)
prestamos = cursor.fetchall()

print("\n--- FORMATO DE SALIDA ESTANDARIZADA DE EXPEDIENTES Y REFERENCIAS (JOIN) ---")
for pr in prestamos:
    print(f"Alentamos al cobro del usuario '{pr[0]}' porque mantiene registro del ejemplar formal: '{pr[1]}'.")

# Cerramos formalmente nuestra conexión al final de la jornada completa de trabajo para liberar la memoria global.
conexion.close()
print("\nFlujo de la base de datos cerrado armónicamente.")
