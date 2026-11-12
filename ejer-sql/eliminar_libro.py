import sqlite3

# Abrimos la conexión a la base de datos
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

# Procedemos a eliminar un registro específico del sistema.
id_borrar = 4

# Instrucción de borrado que emplea la parametrización para garantizar una supresión unívoca.
# Ojo: (id_borrar,) lleva coma porque debe ser una tupla de un solo elemento.
cursor.execute("DELETE FROM libros WHERE id = ?", (id_borrar,))

# Consolidamos los cambios para hacer el borrado persistente.
conexion.commit()

print(f"Registro con ID {id_borrar} eliminado exitosamente de la base de datos.")

# Cerramos la conexión para liberar el archivo
conexion.close()
