import sqlite3

# Abrimos la conexión a la base de datos (debe existir y tener libros)
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

print("--- TODOS LOS LIBROS (SIN RESTRICCIONES PONDERADAS) ---")
cursor.execute("SELECT * FROM libros")
todos = cursor.fetchall()
for libro in todos:
    print(f"[{libro[0]}] {libro[1]}")

print("\n--- WHERE MATEMÁTICO: Libros del Registros Acotados desde la Década de 1900 ---")
# Busca libros que se hayan publicado a partir del año 1900 adelante.
cursor.execute("SELECT titulo, anio FROM libros WHERE anio >= 1900")
libros_modernos = cursor.fetchall()
for libro in libros_modernos:
    print(f"-> {libro[0]} ({libro[1]})")

print("\n--- WHERE POR EVALUACIÓN DE PATRÓN LÓGICO: Textos que empiecen por F ---")
# LIKE seguido de F y un %. Esto significa "Empieza por F estricto y luego admite cadenas de extensión indefinida ulteriores".
cursor.execute("SELECT titulo, autor FROM libros WHERE titulo LIKE 'F%'")
libros_f = cursor.fetchall()
for libro in libros_f:
    print(f"-> {libro[0]} de {libro[1]}")

print("\n--- MULTIPLES WHERE: AND y OR ---")
cursor.execute("SELECT titulo FROM libros WHERE anio < 1960 AND autor = 'Isaac Asimov'")
libros_clasicos_asimov = cursor.fetchall()
for libro in libros_clasicos_asimov:
    print(f"-> Conjunto cruzado: {libro[0]}")

# Solo leemos datos, así que no hace falta commit. Cerramos la conexión.
conexion.close()
