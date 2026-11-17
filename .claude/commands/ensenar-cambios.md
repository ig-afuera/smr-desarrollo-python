---
description: Levanta el servidor de mkdocs de python-alumno para ver los cambios
---
Muestra los apuntes del alumno en local con mkdocs.

1. Comprueba si existe `python-alumno/.venv/Scripts/python.exe`.
   - Si no existe, sigue primero las instrucciones de `.claude/commands/preparar-entorno-alumno.md`. Si falla, detente e informa.
2. Desde la carpeta `python-alumno`, lanza el servidor con el Python del entorno virtual (equivale a activarlo):
   `.venv/Scripts/python.exe -m mkdocs serve --open`
   Ejecútalo **en segundo plano**, porque es un proceso que no termina.
   La opción `--open` abre el navegador en la URL servida en cuanto el servidor arranca.
3. Si el navegador no se ha abierto, ábrelo tú con la URL que muestre mkdocs en su salida
   (por defecto http://127.0.0.1:8000), por ejemplo en PowerShell:
   `Start-Process "http://127.0.0.1:8000"`
4. Indica al usuario la URL y cómo parar el servidor.
   Si da error al arrancar, muéstraselo al usuario.
