import sqlite3

# Abrimos la conexión a la base de datos
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

# Procedemos a actualizar el año de publicación del registro correspondiente a 'Dune'.
nuevo_anio = 2021
id_objetivo = 2

# Aplicamos la modificación de forma restrictiva y parametrizada utilizando la clave primaria.
cursor.execute("UPDATE libros SET anio = ? WHERE id = ?", (nuevo_anio, id_objetivo))

# Consolidamos la transacción en la base de datos.
conexion.commit()

print(f"Registro con ID {id_objetivo} actualizado correctamente.")

# Cerramos la conexión para liberar el archivo
conexion.close()
