import sqlite3

# 1. Definimos una Clase que representa exactamente una fila de nuestra tabla 'libros'
class Libro:
    def __init__(self, id_libro, titulo, autor, anio):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"📖 {self.titulo} (escrito por {self.autor} en {self.anio})"

# 2. Nos conectamos, leemos los datos crudos y los transformamos en Objetos
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM libros")
datos_crudos = cursor.fetchall()
conexion.close()

# 3. El Mapeo (Mapping)
inventario_objetos = []
for fila in datos_crudos:
    # Desempaquetamos la tupla y creamos una instancia dinámica de Libro
    nuevo_objeto = Libro(fila[0], fila[1], fila[2], fila[3])
    inventario_objetos.append(nuevo_objeto)

# 4. Ahora trabajamos con Objetos puros de Python, mucho más limpios y seguros
print("--- INVENTARIO CARGADO EN OBJETOS ---")
for obj_libro in inventario_objetos:
    # Fíjate qué elegante es acceder a sus propiedades con el 'punto'
    if obj_libro.anio > 1950:
        print(f"Obra moderna: {obj_libro.titulo}")

    # Usamos su método mágico __str__
    print(obj_libro)
    print("-" * 20)
