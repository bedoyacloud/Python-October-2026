"""Punto de entrada del Gestor de Tareas CLI."""

from colorama import Fore, Style, init
from app.operaciones import añadir_tarea, listar_tareas, buscar_tarea

init(autoreset=True)


def mostrar_menu() -> None:
    """Muestra las opciones disponibles del menú principal."""
    print(Fore.CYAN + "\n=== GESTOR DE TAREAS ===")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Buscar tarea")
    print("4. Salir")


def main() -> None:
    """Ejecuta el bucle principal del programa."""
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            prioridad = input("Prioridad (opcional, Enter para omitir): ")

            if prioridad:
                tareas = añadir_tarea(tareas, nombre, prioridad=prioridad)
            else:
                tareas = añadir_tarea(tareas, nombre)

            print(Fore.GREEN + "Tarea añadida correctamente.")

        elif opcion == "2":
            lista = listar_tareas(tareas)
            if not lista:
                print(Fore.YELLOW + "No hay tareas registradas.")
            else:
                print(Fore.CYAN + "\n--- Tus tareas ---")
                for tarea in lista:
                    print(tarea)

        elif opcion == "3":
            palabra_clave = input("¿Qué quieres buscar?: ")
            resultados = buscar_tarea(tareas, palabra_clave)
            if not resultados:
                print(Fore.YELLOW + "No se encontraron coincidencias.")
            else:
                print(Fore.CYAN + "\n--- Resultados ---")
                for tarea in resultados:
                    print(tarea)

        elif opcion == "4":
            print(Fore.MAGENTA + "¡Hasta luego!")
            break

        else:
            print(Fore.RED + "Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()