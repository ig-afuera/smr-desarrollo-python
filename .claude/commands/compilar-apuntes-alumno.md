---
description: Compila los apuntes de python-alumno con mkdocs build y deja un zip de la carpeta site
---
Compila los apuntes del alumno y empaquétalos.

1. Comprueba si existe `python-alumno/.venv/Scripts/python.exe`.
   - Si no existe, sigue primero las instrucciones de `.claude/commands/preparar-entorno-alumno.md`. Si falla, detente e informa.
2. Desde la carpeta `python-alumno`, compila con el Python del entorno virtual (equivale a activarlo):
   `.venv/Scripts/python.exe -m mkdocs build`
3. Si el build **falla**: muestra al usuario el error de mkdocs y detente. No generes ningún zip.
4. Si el build **termina bien**: comprime la carpeta `python-alumno/site` en `site.zip` dentro del directorio de trabajo actual (pwd). Si ya existe un `site.zip`, sobrescríbelo. En Windows usa PowerShell:
   `Compress-Archive -Path "python-alumno/site/*" -DestinationPath "site.zip" -Force`
5. Informa al usuario de la ruta completa del zip y de los avisos (WARNING) que haya mostrado mkdocs, si los hay.
