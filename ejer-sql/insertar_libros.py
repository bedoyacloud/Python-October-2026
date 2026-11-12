import sqlite3

# Abrimos la conexión a la base de datos ya creada por crear_biblioteca.py
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

titulo_nuevo = "1984"
autor_nuevo = "George Orwell"
anio_nuevo = 1949

# Sentencia SQL fija con "huecos" parametrizados (?)
sentencia = "INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)"
datos_empaquetados = (titulo_nuevo, autor_nuevo, anio_nuevo) # Obligatoriamente en Tupla

cursor.execute(sentencia, datos_empaquetados)

# ¡VITAL! Si no hacemos commit, este nuevo libro no persistirá físicamente en la unidad de almacenamiento general.
conexion.commit()
print("Libro procesado de forma segura y guardado permanentemente.")

# Procedemos a poblar datos auxiliares controlados para ejemplificar los conjuntos de operadores subsiguientes
cursor.execute(sentencia, ("Dune", "Frank Herbert", 1965))
cursor.execute(sentencia, ("Fundación", "Isaac Asimov", 1951))
cursor.execute(sentencia, ("El Quijote", "Miguel de Cervantes", 1605))
conexion.commit()

# Cerramos la conexión para liberar el archivo
conexion.close()
