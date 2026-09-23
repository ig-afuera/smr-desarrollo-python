# f) Operadores y expresiones

Un **operador** es un símbolo que realiza una operación. Un **operando** es cada valor sobre el que actúa: en `3 + 4`, el operador es `+` y los operandos son `3` y `4`.

## 1. Operadores aritméticos

| Operador | Operación | Ejemplo | Resultado |
|:---:|---|---|:---:|
| `+` | Suma | `7 + 2` | `9` |
| `-` | Resta | `7 - 2` | `5` |
| `*` | Multiplicación | `7 * 2` | `14` |
| `/` | División (siempre `float`) | `7 / 2` | `3.5` |
| `//` | División entera | `7 // 2` | `3` |
| `%` | Módulo (resto) | `7 % 2` | `1` |
| `**` | Potencia | `7 ** 2` | `49` |

```pycon
>>> 7 / 2
3.5
>>> 7 // 2
3
>>> 7 % 2
1
>>> 2 ** 10
1024
>>> -7 // 2          # la división entera redondea hacia abajo
-4
>>> -7 % 2
1
```

!!! tip "Usos típicos de `//` y `%`"
    - **¿Es par?** `n % 2 == 0`.
    - **Convertir segundos en minutos y segundos**: `minutos = total // 60` y `segundos = total % 60`.
    - **Última cifra** de un número: `n % 10`.
    - **Quitar la última cifra**: `n // 10`.

## 2. Operadores de asignación

Además de `=`, existe la **asignación aumentada**, que abrevia operaciones sobre la misma variable:

| Forma corta | Equivale a |
|:---:|:---:|
| `x += 3` | `x = x + 3` |
| `x -= 3` | `x = x - 3` |
| `x *= 3` | `x = x * 3` |
| `x /= 3` | `x = x / 3` |
| `x //= 3` | `x = x // 3` |
| `x %= 3` | `x = x % 3` |
| `x **= 3` | `x = x ** 3` |

```pycon
>>> saldo = 100
>>> saldo += 50
>>> saldo -= 20
>>> saldo
130
```

## 3. Operadores de comparación

Comparan dos valores y devuelven un `bool`.

| Operador | Significado |
|:---:|---|
| `==` | Igual a |
| `!=` | Distinto de |
| `<` | Menor que |
| `>` | Mayor que |
| `<=` | Menor o igual |
| `>=` | Mayor o igual |

```pycon
>>> 5 == 5
True
>>> 5 != 5
False
>>> 3 <= 2
False
>>> 1 < 5 < 10           # comparación encadenada: 1 < 5 y 5 < 10
True
>>> "a" < "b"            # las cadenas se comparan alfabéticamente
True
>>> "Z" < "a"            # las mayúsculas van antes que las minúsculas
True
```

!!! warning "`=` no es `==`"
    `=` **asigna**; `==` **compara**. Confundirlos es uno de los errores más comunes al empezar.

!!! warning "No compares decimales con `==`"
    ```pycon
    >>> 0.1 + 0.2 == 0.3
    False
    >>> import math
    >>> math.isclose(0.1 + 0.2, 0.3)
    True
    ```

## 4. Operadores lógicos

Combinan valores booleanos.

| Operador | Significado | Resultado |
|:---:|---|---|
| `and` | Y | `True` solo si **ambos** son `True` |
| `or` | O | `True` si **al menos uno** es `True` |
| `not` | No | Invierte el valor |

**Tablas de verdad**

| `a` | `b` | `a and b` | `a or b` |
|:---:|:---:|:---:|:---:|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

```pycon
>>> edad = 20
>>> edad >= 18 and edad < 65
True
>>> not edad >= 18
False
```

### Evaluación en cortocircuito

Python **deja de evaluar** en cuanto conoce el resultado:

- `and`: si el primer operando es `False`, el resultado ya es `False` y no mira el segundo.
- `or`: si el primer operando es `True`, el resultado ya es `True` y no mira el segundo.

```pycon
>>> False and (1 / 0 > 1)        # nunca se calcula 1/0, así que no hay error
False
>>> True or (1 / 0 > 1)
True
```

Además, `and` y `or` devuelven **uno de sus operandos**, no siempre un `bool`. Se usa mucho para dar un valor por defecto:

```pycon
>>> "" or "sin nombre"
'sin nombre'
>>> "Ana" or "sin nombre"
'Ana'
```

## 5. Operadores de identidad y de pertenencia

### Identidad: `is` / `is not`

Comprueba si dos nombres apuntan **al mismo objeto** (no si valen lo mismo).

```pycon
>>> a = 1000
>>> b = a
>>> a is b
True
```

!!! tip "¿`is` o `==`?"
    Para comparar **valores**, usa `==`. `is` se reserva para casos concretos (por ejemplo, comparar con `None`).

### Pertenencia: `in` / `not in`

Comprueba si un elemento está dentro de otro. Con cadenas, si un texto está dentro de otro:

```pycon
>>> "ol" in "hola"
True
>>> "z" in "hola"
False
>>> "z" not in "hola"
True
```

## 6. Precedencia y asociatividad

Cuando una expresión tiene varios operadores, Python los evalúa según su **precedencia** (de mayor a menor):

| Prioridad | Operadores |
|:---:|---|
| 1 (más alta) | `( )` paréntesis |
| 2 | `**` |
| 3 | `-x` (cambio de signo) |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` |
| 7 | `not` |
| 8 | `and` |
| 9 (más baja) | `or` |

Con igual precedencia se evalúa de **izquierda a derecha** (asociatividad), salvo `**`, que va de **derecha a izquierda**.

```pycon
>>> 2 + 3 * 4
14
>>> (2 + 3) * 4
20
>>> -2 ** 2              # primero la potencia, luego el signo
-4
>>> 2 ** 3 ** 2          # 2 ** (3 ** 2)
512
>>> 10 - 4 - 3           # (10 - 4) - 3
3
>>> True or False and False     # and antes que or: True or (False and False)
True
```

!!! tip "Ante la duda, paréntesis"
    Los paréntesis no cuestan nada y hacen el código más claro: `(a + b) * c` deja clara tu intención.

## 7. Expresiones

Una **expresión** es una combinación de valores, variables y operadores que **produce un valor**. Se evalúa paso a paso:

```text
precio * 3 + 5 > 20      con precio = 4
   4 * 3 + 5 > 20
   12 + 5 > 20
   17 > 20
   False
```

Una **sentencia** hace algo (como asignar); una **expresión** calcula un valor. Las expresiones pueden ir en muchos sitios: en una asignación, dentro de `print()`, en una condición...

## 8. Operador *walrus* (`:=`): introducción

Permite **asignar y usar** un valor en la misma expresión. Los paréntesis son obligatorios en la mayoría de los casos:

```pycon
>>> (n := 10) * 2
20
>>> n
10
```

Su uso más habitual es en condiciones, para no calcular algo dos veces:

```python
texto = input("Escribe algo: ")
if (largo := len(texto)) > 10:
    print(f"Texto largo: {largo} caracteres")
```

!!! note "Nota"
    Es un recurso avanzado: no lo necesitas para nada de lo que veremos, pero te lo encontrarás al leer código de otras personas.

## 9. El módulo `math` en las expresiones

Para cálculos más allá de las operaciones básicas:

```pycon
>>> import math
>>> math.sqrt(16)             # raíz cuadrada
4.0
>>> math.pow(2, 3)            # potencia (devuelve float)
8.0
>>> math.floor(-2.5)          # redondea hacia abajo
-3
>>> math.ceil(2.1)            # redondea hacia arriba
3
>>> math.hypot(3, 4)          # hipotenusa
5.0
```

Y algunas funciones predefinidas que no necesitan `import`:

```pycon
>>> abs(-7)
7
>>> round(3.14159, 2)
3.14
>>> max(3, 9, 4)
9
>>> min(3, 9, 4)
3
>>> pow(2, 10)
1024
```

!!! warning "`round()` redondea 2,5 a 2"
    Python redondea los «medios» al **par más cercano**: `round(2.5)` es `2` y `round(3.5)` es `4`.
    Para mostrar dinero, es más seguro formatear con `:.2f`.

Dos formas de importar:

```python
import math                 # usas math.sqrt(...)
from math import sqrt, pi   # usas sqrt(...) y pi directamente
```

**Ejemplo: área de un círculo**

```python
import math

radio = float(input("Radio: "))
area = math.pi * radio ** 2
print(f"El área es {area:.2f}")
```

## Resumen

- Aritméticos (`+ - * / // % **`), de asignación (`+=`, `-=`...), de comparación, lógicos (`and or not`), de identidad (`is`) y de pertenencia (`in`).
- `/` da siempre `float`; `//` es la división entera y `%` el resto.
- `and` y `or` usan **cortocircuito**.
- Precedencia: `**` > `* / // %` > `+ -` > comparaciones > `not` > `and` > `or`. Los paréntesis mandan.
- Una **expresión** es lo que produce un valor. El módulo `math` amplía las posibilidades de cálculo.
