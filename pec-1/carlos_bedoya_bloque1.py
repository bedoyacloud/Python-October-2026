"""
PSEUDOCÓDIGO - Gestor de gastos personales

PREPARACIÓN
1. Configurar el logging para escribir en el archivo finanzas.log
2. Crear una lista vacía llamada gastos
3. Registrar en el log (INFO): "Aplicación iniciada"

PROGRAMA PRINCIPAL (se repite hasta que el usuario elija salir)
4. Mostrar el menú con las 3 opciones
5. Pedir al usuario que escriba una opción
6. Intentar convertir la opción a número entero
   - Si falla (el usuario escribió letras):
       * Registrar en el log (ERROR)
       * Avisar al usuario
       * Volver al paso 4

7. Según la opción elegida:

   OPCIÓN 1 - Añadir gasto
   a. Pedir el concepto (texto)
   b. Repetir hasta tener una cantidad válida:
        - Pedir la cantidad e intentar convertirla a número decimal
        - Si falla: registrar en el log (ERROR) y avisar al usuario
   c. Guardar en la lista un diccionario {"concepto": ..., "cantidad": ...}
   d. Registrar en el log (INFO) que se añadió el gasto
   e. Avisar al usuario que se guardó

   OPCIÓN 2 - Ver resumen
   a. Si la lista tiene gastos:
        - Recorrer la lista y mostrar cada concepto y cantidad
        - Sumar todas las cantidades
        - Mostrar el total al final
   b. Si la lista está vacía: mostrar "No hay gastos registrados"

   OPCIÓN 3 - Salir
   a. Terminar el bucle

   CUALQUIER OTRA OPCIÓN (por ejemplo 7)
   a. Registrar en el log (ERROR)
   b. Avisar al usuario y volver al menú

FINALIZACIÓN
8. Registrar en el log (INFO): "Aplicación detenida"
"""

import logging
import os
import subprocess

logging.basicConfig(
    filename="finanzas.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear')

gastos = []

logging.info("Aplicación iniciada")

while True:
    clear_screen()
    print("\n")
    print("\033[0;37m▄\033[0;97m█\033[0;37m▀ ▄\033[0;97;47m▄\033[0;37m ▄\033[0;97;47m█\033[0;97m▀\033[0;97;47m█▄\033[0;37m \033[0;97m██\033[0;37m▀\033[0;97;47m▄\033[0;37m▄ ▄\033[0;97;47m█\033[0;97m▀\033[0;97;47m█▄\033[0;37m \033[0;97m█\033[0;97;47m▄\033[0;37m▀\033[0;97;47m▄\033[0;37m▄ \033[0;97m██\033[0;37m▀\033[0;97;47m▄\033[0;37m▄ ▄\033[0;97;47m▄\033[0;37m▀\033[0;97;47m▄\033[0;37m▄      \033[0;97m██\033[0;37m▀\033[0;97;47m▄\033[0;37m▄ \033[0;97m██\033[0;37m▀\033[0;97;47m▄\033[0;37m▄ \033[0;97m██\033[0;37m▀\033[0;97;47m▄\033[0;37m▄ \033[0;97m██\033[0;37m▀\033[0;97;47m▄\033[0;37m▄      \033[0;97;47m██\033[0;37m▀\033[0;97;47m█\033[0;37m▄ \033[0;97;47m▄\033[0;97m█\033[0;37m \033[0;97;47m▄\033[0;37m▄ ▄\033[0;97;47m█\033[0;97m▀\033[0;97;47m█▄\033[0;97m▀\033[0;97;47m█▄\033[0;37m ▄\033[0;97;47m█\033[0;97m▀\033[0;97;47m█▄\033[0;97m▀\033[0;97;47m█▄\033[0;37m ▄\033[0;97;47m▄\033[0;37m ▄\033[0;97m█\033[0;37m▀ ▄\033[0;97;47m▄\033[0;37m▀\033[0;97;47m▄\033[0;37m▄\033[0m")
    print("\033[0;97m██\033[0;37m  \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m    \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m         \033[0;97m██\033[0;37m \033[0;97;47m█▀\033[0;37m \033[0;97m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m█▀\033[0;37m \033[0;97m██\033[0;37m \033[0;97m██\033[0;37m      \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97m██\033[0;37m  \033[0;97;47m██\033[0;37m   \033[0m")
    print("\033[0;97m██\033[0;37m▀ \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m▀\033[0;97;47m█\033[0;97m█\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m ▄\033[0;97;47m▄\033[0;37m▀▀  \033[0;97m██\033[0;37m▀\033[0;97;47m█\033[0;97m█\033[0;37m  ▀▀\033[0;97;47m▄\033[0;37m▄      \033[0;97m██\033[0;37m▀▀  \033[0;97m██\033[0;37m▀\033[0;97;47m█\033[0;97m█\033[0;37m \033[0;97m██\033[0;37m▀\033[0;97;47m█\033[0;37m▄ \033[0;97m██\033[0;37m▀\033[0;97;47m█\033[0;97m█\033[0;37m      \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97m██\033[0;37m▀  ▀▀\033[0;97;47m▄\033[0;37m▄\033[0m")
    print("\033[0;97m██\033[0;37m  \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m▄▄\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m▄▄\033[0;37m \033[0;97;47m██\033[0;37m      \033[0;97m██\033[0;37m    \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m      \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97m██\033[0;37m  \033[0;97m▄▄\033[0;37m \033[0;97;47m██\033[0m")
    print("\033[0;97m██\033[0;37m  \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m ▀\033[0;97;47m▀\033[0;37m▄\033[0;97;47m▀\033[0;97m█\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m ▀\033[0;97;47m▀\033[0;37m▄\033[0;97;47m▀\033[0;37m▀      \033[0;97m██\033[0;37m    \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m \033[0;97;47m██\033[0;37m      \033[0;97;47m██\033[0;97m▄\033[0;97;47m█\033[0;37m▀ ▀\033[0;97;47m▀\033[0;37m▄\033[0;97;47m▀\033[0;37m▀ \033[0;97;47m██\033[0;37m \033[0;97;47m▀\033[0;37m▀ \033[0;97;47m██\033[0;37m \033[0;97;47m██\033[0;37m \033[0;97;47m▀\033[0;37m▀ \033[0;97;47m██\033[0;37m \033[0;97m██\033[0;37m ▀\033[0;97m█\033[0;37m▄ ▀\033[0;97;47m▀\033[0;37m▄\033[0;97;47m▀\033[0;37m▀\033[0m")

    print("\n")
    print("Bienvenido al programa de Carlos Bedoya")
    print()

    print("Seleccione una opción:")
    print("1. Añadir Gasto")
    print("2. Ver Resumen de Gastos")
    print("3. Salir del Programa")
    print()

    opcion = input("Ingrese el número de la opción deseada: ")

    try:
        opcion = int(opcion)
    except ValueError:
        logging.error("Opción inválida ingresada")
        print("Por favor, ingrese un número válido para la opción.")
        input("Presione Enter para continuar...")
        continue

    if opcion == 1:
        clear_screen()
        print("Añadir Gasto")
        print()
        concepto = input("Ingrese el nombre del concepto: ")
        while True:
            try:
                cantidad = float(input("Introduce la cantidad: "))
                if cantidad <= 0 or cantidad != cantidad or cantidad == float("inf"):
                    raise ValueError("Cantidad inválida")
                break
            except ValueError:
                logging.error("Cantidad inválida al añadir gasto")
                print("Por favor, ingrese un número válido para el monto.")
        gastos.append({"concepto": concepto, "cantidad": cantidad})
        logging.info(f"Gasto añadido: {concepto} - {cantidad:.2f}")
        print(f"Gasto '{concepto}' de {cantidad:.2f} añadido correctamente.")
        input("Presione Enter para continuar...")

    elif opcion == 2:
        clear_screen()
        print("Ver Resumen de Gastos")
        print()
        if gastos:
            total_gastos = sum(gasto["cantidad"] for gasto in gastos)
            print("Detalles de los gastos:")
            for gasto in gastos:
                print(f"  - {gasto['concepto']}: {gasto['cantidad']:.2f}")
            print(f"\nTotal de gastos: {total_gastos:.2f}")
            logging.info(f"Resumen de gastos mostrado. Total: {total_gastos:.2f}")
        else:
            print("No hay gastos registrados.")
        input("Presione Enter para continuar...")

    elif opcion == 3:
        clear_screen()
        print("Saliendo del programa...")
        break

    else:
        logging.error("Opción inválida seleccionada")
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione Enter para continuar...")

logging.info("Aplicación detenida")