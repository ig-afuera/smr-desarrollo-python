# e) Constantes

## 1. Constante frente a variable

- Una **variable** es un valor que **puede cambiar** durante el programa (el saldo de una cuenta, un contador...).
- Una **constante** es un valor que **no debe cambiar** (el IVA, el número π, el número de días de la semana...).

## 2. Constantes en Python

Python **no tiene constantes reales**: cualquier variable se puede reasignar. Se sigue una **convención**:

> Las constantes se escriben en **MAYÚSCULAS**, con guion bajo para separar palabras, y se definen al **principio** del programa.

```python
IVA = 0.21
DIAS_SEMANA = 7
NOMBRE_TIENDA = "Informática Sur"
```

```pycon
>>> IVA = 0.21
>>> IVA = 0.10      # Python lo permite, pero rompe la convención: NO lo hagas
```

Las mayúsculas son un **aviso para las personas** que leen el código: «este valor no se toca».

## 3. Constantes predefinidas

El módulo `math` incluye constantes matemáticas. Para usarlas hay que importarlo:

```pycon
>>> import math
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.tau               # 2π
6.283185307179586
>>> math.inf               # infinito
inf
```

| Constante | Significado |
|---|---|
| `math.pi` | π (3,14159...) |
| `math.e` | Número de Euler (2,71828...) |
| `math.tau` | 2π |
| `math.inf` | Infinito positivo |

Otras constantes útiles de la biblioteca estándar:

```pycon
>>> import sys
>>> sys.maxsize > 10**18        # tamaño máximo de un índice en este sistema
True
>>> import string
>>> string.digits
'0123456789'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
```

## 4. Por qué usar constantes

Compara estos dos programas:

=== "Con «números mágicos» ❌"

    ```python
    precio = float(input("Precio sin IVA: "))
    total = precio + precio * 0.21
    print(total)
    ```

    ¿Qué es `0.21`? Y si el IVA cambia, habría que buscarlo por todo el programa.

=== "Con constante ✅"

    ```python
    IVA = 0.21

    precio = float(input("Precio sin IVA: "))
    total = precio + precio * IVA
    print(total)
    ```

    Se entiende de un vistazo y, si cambia el IVA, se modifica **en un solo sitio**.

**Ventajas:**

- **Legibilidad**: el nombre explica qué significa el valor.
- **Mantenimiento**: cambias el valor una vez y afecta a todo el programa.
- **Menos errores**: no escribes `0.21` en un sitio y `0.12` en otro por despiste.

!!! tip "Regla práctica"
    Si en tu programa aparece un número que no sea `0`, `1` o algo evidente, y se repite o tiene un significado propio, conviértelo en una **constante** con nombre.

!!! warning "En Jupyter, cuidado"
    En un cuaderno es fácil redefinir una constante en otra celda sin darte cuenta. Si un resultado no te cuadra, reinicia el kernel y ejecuta todo de nuevo.

## Resumen

- Constante = valor que no debe cambiar. Se escribe en **MAYÚSCULAS** al inicio del programa.
- Python no impide reasignarla: es una convención.
- El módulo `math` ofrece `pi`, `e`, `tau` e `inf`.
- Evita los «números mágicos»: usar constantes hace el código más claro y fácil de mantener.
