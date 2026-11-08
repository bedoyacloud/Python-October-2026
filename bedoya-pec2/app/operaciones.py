"""Operaciones para gestionar la lista de tareas: añadir, listar y buscar."""

from app.modelos import crear_tarea

def añadir_tarea(tareas: list, nombre:str, **kwargs) -> list:
    """Añade una nueva tarea a la lista de tareas.

    Args:
        tareas (list): La lista de tareas existente.
        nombre (str): El nombre de la nueva tarea.
        **kwargs: Atributos adicionales de la tarea.

    Returns:
        list: La lista actualizada de tareas.
    """
    nueva_tarea = crear_tarea(nombre, **kwargs)
    tareas.append(nueva_tarea)
    return tareas

def listar_tareas(tareas:list) -> list:
    """Lista todas las tareas en la lista de tareas.

    Args:
        tareas (list): La lista de tareas existente.

    Returns:
        list: La lista de tareas.
    """
    return tareas

def buscar_tarea(tareas: list, palabra_clave: str) -> list:
    """Busca tareas que contengan una palabra clave en su nombre.

    Args:
        tareas (list): La lista de tareas existente.
        palabra_clave (str): La palabra clave a buscar en los nombres de las tareas.

    Returns:
        list: Una lista de tareas que contienen la palabra clave.
    """
    palabra_clave = palabra_clave.lower()
    return [tarea for tarea in tareas if palabra_clave in tarea["nombre"].lower()]