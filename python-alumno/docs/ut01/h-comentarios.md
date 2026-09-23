# h) Comentarios

Un **comentario** es texto que Python **ignora** al ejecutar. Sirve para explicar el código a las personas que lo lean (incluido tú dentro de dos meses).

## 1. Comentarios de una línea y de varias líneas

Todo lo que va después de `#` hasta el final de la línea es un comentario:

```python
# Calcula el precio final con IVA
IVA = 0.21                        # 21 % en España

precio = 100
total = precio * (1 + IVA)        # precio con IVA incluido
```

Python no tiene comentarios de bloque propiamente dichos. Para varias líneas se pone `#` en cada una:

```python
# Este programa pide el radio de un círculo
# y muestra su longitud y su área.
# Autor: Ana García
```

!!! tip "Atajo en VS Code"
    Selecciona varias líneas y pulsa `Ctrl+K Ctrl+C` para comentarlas, o `Ctrl+/` para alternar el comentario.
    En una celda de Jupyter también funciona `Ctrl+/`.

!!! note "Y las triples comillas"
    A veces se usan `""" ... """` como comentario de varias líneas. En realidad es una cadena que no se asigna a nada, no un comentario.
    Funciona, pero por convención se reserva para los *docstrings*.

## 2. *Docstrings* (cadenas de documentación)

Un **docstring** es una cadena entre triples comillas situada **justo al principio** de un módulo (el archivo), una función o una clase. Describe **qué hace** y, a diferencia de un comentario, Python lo **conserva** y se puede consultar.

**Docstring del módulo** (primera cosa del archivo):

```python
"""Calculadora de presupuestos.

Pide las horas de trabajo y el precio de las piezas
y muestra el total con IVA.
"""

IVA = 0.21
# ...
```

**Docstring de una función** (las funciones se ven en la UT03):

```python
def area_circulo(radio):
    """Devuelve el área de un círculo a partir de su radio."""
    return 3.14159 * radio ** 2
```

Se pueden consultar con `__doc__` o con `help()`:

```pycon
>>> def area_circulo(radio):
...     """Devuelve el área de un círculo a partir de su radio."""
...     return 3.14159 * radio ** 2
...
>>> area_circulo.__doc__
'Devuelve el área de un círculo a partir de su radio.'
```

!!! success "`help()` funciona sin internet"
    Con `help(round)` o `help(math.sqrt)` la consola te muestra la documentación completa de cualquier función.
    En los proyectos de clase, sin conexión, es tu mejor aliado. Pulsa `q` para salir de la ayuda.

## 3. Buenas prácticas

**Comenta el porqué, no el qué.** El código ya dice *qué* hace; el comentario debe explicar *por qué* lo hace así.

```python
# ❌ Comentario inútil: repite lo que ya dice el código
edad = edad + 1       # suma 1 a edad

# ✅ Comentario útil: explica una decisión
edad = edad + 1       # la ficha se actualiza al cumplir años, no al inscribirse
```

| Haz | Evita |
|---|---|
| Explicar decisiones no evidentes. | Comentar lo obvio (`x = 5  # x vale 5`). |
| Poner al inicio del archivo qué hace el programa. | Dejar comentarios antiguos que ya no son ciertos. |
| Usar nombres de variable claros: casi elimina la necesidad de comentar. | Dejar bloques enteros de código comentado «por si acaso». |
| Marcar pendientes con `# TODO:` | Comentarios largos que mezclan varias ideas. |

!!! tip "Un buen nombre vale más que un comentario"
    `# tiempo en segundos` + `t = 30` se mejora con `tiempo_segundos = 30`, y así ya no hace falta el comentario.

## 4. Documentación y estilo de código: PEP 8 y PEP 257

Los **PEP** (*Python Enhancement Proposals*) son documentos de la comunidad. Dos importan ahora:

- **PEP 8**: guía de estilo del código.
- **PEP 257**: convenciones para los docstrings.

Resumen de las reglas de PEP 8 que ya puedes aplicar:

| Regla | Ejemplo correcto |
|---|---|
| Indentar con **4 espacios** | `····print("hola")` |
| Líneas de **79 caracteres** como mucho | Partir en varias líneas dentro de paréntesis |
| Nombres en *snake_case* | `precio_final` |
| Constantes en MAYÚSCULAS | `IVA = 0.21` |
| Espacio alrededor de operadores y tras las comas | `x = a + b`, `f(1, 2)` |
| Sin espacios dentro de paréntesis | `print(x)`, no `print( x )` |
| `import` al principio del archivo | `import math` |
| Comentarios con `#` y un espacio | `# Comentario` |

!!! info "Herramientas que te ayudan"
    - VS Code subraya en amarillo o rojo lo que incumple el estilo o puede ser un error (si tienes instalada la extensión de Python).
    - Puedes formatear el archivo automáticamente con `Shift+Alt+F`.
    - En **Jupyter**, las celdas de **Markdown** son tu forma de documentar: escribe ahí títulos y explicaciones entre las celdas de código.

## Resumen

- `#` comenta una línea; para varias líneas, un `#` en cada una.
- Un **docstring** (`"""..."""`) documenta un módulo, función o clase y se puede consultar con `help()` o `__doc__`.
- Comenta el **porqué**, no el qué; mantén los comentarios actualizados y usa nombres claros.
- **PEP 8** (estilo) y **PEP 257** (docstrings) son las guías que seguimos.
