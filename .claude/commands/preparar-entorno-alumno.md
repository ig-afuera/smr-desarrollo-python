---
description: Crea el entorno virtual (.venv) de python-alumno e instala sus dependencias si no existe
---
Prepara el entorno virtual del repositorio del alumno (`python-alumno`, ruta relativa a la raíz del proyecto).

1. Comprueba si existe `python-alumno/.venv/Scripts/python.exe`.
   - Si existe, informa al usuario de que el entorno ya está montado y termina.
2. Si no existe, créalo desde la carpeta `python-alumno`:
   `python -m venv .venv`
3. Instala las dependencias usando el Python del entorno (no hace falta activarlo, cada llamada a la shell es independiente):
   `.venv/Scripts/python.exe -m pip install -r requirements.txt`
4. Informa al usuario del resultado. Si algún paso falla, muestra el error y detente.

No instales ninguna librería que no esté en `requirements.txt`.
