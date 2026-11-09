# import os

# print(os.getcwd())
# print(os.listdir())

from pathlib import Path
print(Path.cwd())

lista_directorios = list(Path.cwd().iterdir())

for elemento in lista_directorios:
    print(f"Suffix: {elemento.suffix}")
    print(f"Name: {elemento.name}")
    print(f"Stem: {elemento.stem}")
    print(f"Parent: {elemento.parent}")