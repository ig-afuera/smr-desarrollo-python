# Ejercicio evaluable: Estimación de una copia de seguridad en red

**Formato:** 45 minutos, sin internet ni apuntes. VS Code (`.py`) o Jupyter.

Un técnico de sistemas quiere estimar, antes de lanzarla, cuánto ocupará y cuánto tardará una copia de seguridad por red.

## Requisitos

1. Al inicio del archivo, un **docstring** que explique qué hace el programa. Añade **comentarios** donde aporten valor (el porqué, no el qué).
2. Define dos constantes para los **bits por megabyte** (son 8) y el **margen de seguridadd** (usaremos 0.1)
3. Pide por teclado: nombre del servidor, tamaño de los datos a copiar en GB (decimal), velocidad de la red en Mbps (decimal). Convierte cada dato al **tipo adecuado**.
4. Calcula:
   - el tamaño en megabits: `GB → MB (×1024) → bits (× 8)`,
   - el tiempo teórico en segundos = tamaño en megabits / velocidad en Mbps,
   - el tiempo con margen = tiempo teórico × `(1 + margen de seguridad)`,
   - ese tiempo con margen convertido a formato `h:mm:ss` (usa `//` y `%`).
5. Muestra un resumen con formato cuidado: nombre del servidor en **mayúsculas**, tamaño con 2 decimales, y el tiempo final en `h:mm:ss`.
6. Calcula y muestra, **sin usar `if`**, dos valores lógicos:
   - `copia_grande`: el tamaño supera los 100 GB.
   - `fuera_horario_recomendado`: el tiempo con margen supera las 2 horas (conviene lanzarla de noche).

## Ejemplo de ejecución

```text
Nombre del servidor: srv-backup01
Tamaño de los datos (GB): 50.5
Velocidad de red (Mbps): 100
Código de prioridad (hex): 1A

RESUMEN DE COPIA — SRV-BACKUP01
----------------------------------
Tamaño a copiar:        50.50 GB
Tiempo estimado:        1:15:50
----------------------------------
¿Copia grande (>100 GB)?        False
¿Fuera de horario recomendado?  False
```

## Criterios de autocorrección

- [ ] El programa se ejecuta de principio a fin sin errores.
- [ ] Hay docstring, comentarios y constantes en MAYÚSCULAS (sin números mágicos).
- [ ] Los datos se convierten con `float()`, y la prioridad con `int(texto, 16)`.
- [ ] El cálculo de tiempo en `h:mm:ss` es correcto (comprobar con `//` y `%`).
- [ ] El código de prioridad se muestra también en binario con `bin()`.
- [ ] Los dos valores lógicos son expresiones de comparación, sin `if`.

## Solución

```python
"""Estimación de una copia de seguridad en red.

Pide los datos del trabajo y calcula tamaño, tiempo estimado
y si conviene lanzar la copia fuera de horario laboral.
"""

BITS_POR_BYTE = 8
MARGEN_SEGURIDAD = 0.10      # 10 % extra por overhead de red

# --- Entrada de datos ---
servidor = input("Nombre del servidor: ")
tamano_gb = float(input("Tamaño de los datos (GB): "))
velocidad_mbps = float(input("Velocidad de red (Mbps): "))
prioridad = int(input("Código de prioridad (hex): "), 16)

# --- Cálculos ---
tamano_mb = tamano_gb * 1024
tamano_megabits = tamano_mb * BITS_POR_BYTE
tiempo_teorico = tamano_megabits / velocidad_mbps
tiempo_con_margen = tiempo_teorico * (1 + MARGEN_SEGURIDAD)

total_segundos = int(tiempo_con_margen)
horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

# --- Valores lógicos ---
copia_grande = tamano_gb > 100
fuera_horario_recomendado = tiempo_con_margen / 3600 > 2

# --- Salida ---
print()
print(f"RESUMEN DE COPIA — {servidor.upper()}")
print("-" * 34)
print(f"Tamaño a copiar:   {tamano_gb:>8.2f} GB")
print(f"Prioridad:         {prioridad:>5} (0b{prioridad:b})")
print(f"Tiempo estimado:   {horas}:{minutos:02d}:{segundos:02d}")
print("-" * 34)
print(f"¿Copia grande (>100 GB)?        {copia_grande}")
print(f"¿Fuera de horario recomendado?  {fuera_horario_recomendado}")
```
