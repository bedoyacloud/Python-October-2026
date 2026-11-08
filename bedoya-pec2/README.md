# Gestor de Tareas CLI

Proyecto de la Evaluación 2 (Arquitectura de Software) del curso de Python en CEI Sevilla.

**Autor:** Carlos Bedoya
**Repositorio (carpeta del proyecto):** https://github.com/bedoyacloud/Python-October-2026/tree/master/bedoya-pec2

## Descripción

Gestor de tareas por consola, con arquitectura modular: el código está dividido en un paquete `app/` (con `modelos.py` y `operaciones.py`) y un punto de entrada `main.py`.

## Requisitos

- Python 3
- Entorno virtual (`env/`)
- Librería `colorama` (ver `requirements.txt`)

## Cómo ejecutarlo

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Estructura del proyecto

```
bedoya-pec2/
├── .gitignore
├── requirements.txt
├── main.py
├── README.md
└── app/
    ├── __init__.py
    ├── modelos.py
    └── operaciones.py
```

## Funcionalidades

- Añadir tareas, con datos opcionales (prioridad, fecha límite, etc.) usando `**kwargs`.
- Ver la lista completa de tareas.
- Buscar tareas por palabra clave.