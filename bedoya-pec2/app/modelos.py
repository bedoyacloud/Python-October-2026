"""Define la estructura de una tarea del gestor."""


def crear_tarea(nombre: str, **kwargs) -> dict:
    """Crea una tarea con un nombre y atributos adicionales.

    Args:
        nombre (str): El nombre de la tarea.
        **kwargs: Atributos adicionales de la tarea.

    Returns:
        dict: Un diccionario que representa la tarea.
    """
    tarea = {"nombre": nombre}
    tarea.update(kwargs)
    return tarea