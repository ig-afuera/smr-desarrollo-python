# g) Conversiones de tipo

A veces necesitas pasar un valor de un tipo a otro: el texto que teclea el usuario (`str`) hay que convertirlo a número para poder calcular.

## 1. Conversión implícita (coerción)

Python convierte **automáticamente** cuando no hay pérdida de información y la operación tiene sentido:

```pycon
>>> 3 + 4.0              # int + float → float
7.0
>>> True + 1             # bool + int → int
2
>>> 5 / 1                # la división siempre da float
5.0
```

El orden de «amplitud» es `bool` → `int` → `float`: el resultado toma el tipo más amplio.

Pero **nunca** convierte texto en número (ni al revés) por su cuenta:

```pycon
>>> "5" + 3
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "int") to str
```

## 2. Conversión explícita (*casting*)

Tú indicas el tipo al que quieres convertir, usando el nombre del tipo como si fuera una función.

| Función | Convierte a | Ejemplo | Resultado |
|---|---|---|---|
| `int(x)` | Entero | `int("42")` | `42` |
| `float(x)` | Decimal | `float("3.5")` | `3.5` |
| `str(x)` | Texto | `str(25)` | `'25'` |
| `bool(x)` | Lógico | `bool(0)` | `False` |

```pycon
>>> int("42") + 1
43
>>> float("3.5") * 2
7.0
>>> str(25) + " años"
'25 años'
>>> int(3.9)                 # ¡trunca! no redondea
3
>>> int(-3.9)
-3
>>> round(3.9)               # para redondear, usa round()
4
>>> float(7)
7.0
>>> int(True)
1
>>> bool("0")                # texto no vacío → True
True
```

!!! warning "`int()` no redondea, corta"
    `int(3.9)` es `3`. Si quieres redondear, usa `round()`.

### El caso más importante: `input()`

`input()` **siempre devuelve texto** (`str`), aunque el usuario teclee un número. Hay que convertirlo:

```python
edad = input("Edad: ")
print(edad + 1)             # ❌ TypeError: "17" + 1
```

```python
edad = int(input("Edad: "))     # ✅ convertimos a entero
print(edad + 1)

precio = float(input("Precio: "))   # ✅ y si admite decimales, a float
```

!!! tip "Decimales con coma"
    `float("3,5")` da error, porque Python solo entiende el **punto** decimal. Si tus usuarios escriben con coma,
    reemplázala antes: `float(texto.replace(",", "."))`. (`replace` es un método de cadenas que verás en la UT04.)

## 3. Conversión entre sistemas de numeración

| Función | Devuelve el número en... | Ejemplo | Resultado |
|---|---|---|---|
| `bin(n)` | Binario | `bin(10)` | `'0b1010'` |
| `oct(n)` | Octal | `oct(8)` | `'0o10'` |
| `hex(n)` | Hexadecimal | `hex(255)` | `'0xff'` |

Para ir **en sentido contrario** (de texto en otra base a entero), `int()` admite la base como segundo argumento:

```pycon
>>> bin(10)
'0b1010'
>>> hex(255)
'0xff'
>>> int("1010", 2)
10
>>> int("ff", 16)
255
>>> int("17", 8)
15
```

Con f-strings también se puede, y sin el prefijo:

```pycon
>>> f"{10:b}"
'1010'
>>> f"{255:X}"
'FF'
>>> f"{8:o}"
'10'
```

## 4. Errores habituales

| Error | Cuándo ocurre | Ejemplo |
|---|---|---|
| `ValueError` | El tipo es correcto pero el **contenido** no se puede convertir. | `int("hola")`, `int("3.5")`, `float("3,5")` |
| `TypeError` | La operación **no admite ese tipo**. | `"5" + 3`, `int([1, 2])` |

```pycon
>>> int("hola")
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'hola'
>>> int("3.5")               # un texto con decimales no se convierte directamente a int
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: '3.5'
>>> int(float("3.5"))        # solución: pasar primero por float
3
```

!!! note "Adelanto"
    En la [UT02 · apartado d](../ut02/d-excepciones.md) aprenderás a **capturar** estos errores para que el programa no se detenga cuando el usuario teclee algo incorrecto.

## 5. Comprobación de tipos: `type()` e `isinstance()`

```pycon
>>> type(5)
<class 'int'>
>>> type(5) == int
True
>>> isinstance(5, int)
True
>>> isinstance(5, float)
False
>>> isinstance(5, (int, float))      # ¿es int o float?
True
>>> isinstance(True, int)            # cuidado: un bool también cuenta como int
True
```

- `type(x)` devuelve el tipo exacto.
- `isinstance(x, tipo)` responde `True` o `False` y es la forma recomendada de comprobar tipos.

## Resumen

- **Implícita**: Python la hace solo entre tipos numéricos (`int` + `float` → `float`).
- **Explícita**: `int()`, `float()`, `str()`, `bool()`.
- `input()` devuelve **siempre** `str`: conviértelo antes de calcular.
- `int()` trunca; `round()` redondea. `float` solo entiende el punto decimal.
- `bin()`, `oct()`, `hex()` y `int(texto, base)` para cambiar de base.
- `ValueError` = contenido inválido; `TypeError` = operación no permitida con ese tipo.
- `type()` da el tipo; `isinstance()` comprueba si un valor es de un tipo.
