import sqlite3

# 1. Establecemos la conexión (Establece el enlace lógico (crea el archivo si la ruta carece de él))
conexion = sqlite3.connect("biblioteca.db")

# 2. Instanciamos el Cursor para procesar sentencias SQL hacia el motor
cursor = conexion.cursor()

# 3. Le damos al cursor una sentencia SQL para ejecutar
# Usamos IF NOT EXISTS para que, si ejecutas esta celda dos veces, no dé un error.
# AUTOINCREMENT hace que la base de datos asigne el ID 1, 2, 3... automáticamente a cada registro.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        anio INTEGER
    )
""")

# 4. Las transacciones de alteración de esquema (DDL) como CREATE normalmente incurren en comprobación automática, pero garantizamos el flujo confirmando,
# pero es buena práctica sellar la transacción al final.
conexion.commit()
print("Esquema matricial 'libros' validado y operante exitosamente.")

# 5. Cerramos la conexión para liberar el archivo
conexion.close()
