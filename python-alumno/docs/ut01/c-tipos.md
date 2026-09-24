# c) Tipos de datos

Cada valor en Python pertenece a un **tipo** que determina qué puede guardar y qué operaciones admite.
Con `type()` puedes preguntar el tipo de cualquier valor.

| Tipo | Qué guarda | Ejemplos |
|---|---|---|
| `int` | Números enteros | `7`, `-3`, `0` |
| `float` | Números con decimales | `3.14`, `-0.5`, `2.0` |
| `bool` | Verdadero o falso | `True`, `False` |
| `str` | Texto (cadena de caracteres) | `"hola"`, `'Ana'` |

```pycon
>>> type(7)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type("hola")
<class 'str'>
```

!!! note "Hay más tipos"
    Existen tipos para guardar colecciones de datos (listas, tuplas, diccionarios...). Los verás en la UT04.

## 1. Tipado dinámico y fuerte

- **Dinámico**: no declaras el tipo de una variable; Python lo deduce del valor, y la misma variable puede cambiar de tipo.
- **Fuerte**: en lenguajes como **Java**, cuando declaras una variable indicas su tipo, y ese tipo queda **fijado para siempre**. A partir de ahí la variable solo puede guardar valores de ese tipo. Si intentas guardar otro, el programa ni siquiera llega a ejecutarse.

```java
int edad = 16;           // edad es un int, y lo será siempre
edad = 17;               // correcto: sigue siendo un int
edad = "dieciséis";      // ERROR: incompatible types: String cannot be converted to int
```

En Python, en cambio, la misma variable puede pasar de un tipo a otro sin problema:

```pycon
>>> x = 5
>>> type(x)
<class 'int'>
>>> x = "cinco"          # dinámico: cambia de int a str sin problema
>>> type(x)
<class 'str'>
```

## 2. Tipos numéricos: `int` y `float`

### `int` (enteros)

```pycon
>>> 2 ** 100
1267650600228229401496703205376
```

### `float` (decimales)

- Se escriben con **punto** decimal (no coma): `3.5`, no `3,5`.
- Se guardan con precisión limitada, así que a veces aparecen pequeños errores de redondeo:

```pycon
>>> 0.1 + 0.2
0.30000000000000004
```

!!! warning "No es un fallo de Python"
    Los ordenadores guardan los decimales en binario y algunos (como 0.1) no se pueden representar exactamente. Para mostrar resultados usa `round()` o formatea con `:.2f` (lo verás en el [apartado d](d-literales.md)).

### `5` y `5.0` no son lo mismo

```pycon
>>> type(5)
<class 'int'>
>>> type(5.0)
<class 'float'>
>>> type(10 / 2)         # la división "/" siempre da float
<class 'float'>
```

## 3. Tipo lógico: `bool`

Solo tiene dos valores, `True` y `False` (con la primera letra en **mayúscula**). Son el resultado de las comparaciones:

```pycon
>>> 5 > 3
True
>>> 5 == 3
False
```

Internamente `True` vale 1 y `False` vale 0:

```pycon
>>> True + True
2
```

### Valores *truthy* y *falsy*

Cualquier valor puede usarse como condición. Se considera **falso** (*falsy*): el `0`, el `0.0` y el texto vacío `""`. **Todo lo demás es verdadero** (*truthy*).

```pycon
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool("")
False
>>> bool(7)
True
>>> bool("hola")
True
>>> bool("False")        # ¡texto no vacío! es True
True
```


## 4. Tipo cadena: `str`

Una **cadena** es una secuencia de caracteres entre comillas. Se estudia a fondo en la UT04; de momento:

```pycon
>>> nombre = "Ana"
>>> len(nombre)             # longitud
3
>>> "Hola, " + nombre       # concatenar
'Hola, Ana'
>>> "ab" * 3                # repetir
'ababab'
```

- `+` entre dos textos los **une**. `*` con un número **repite** el texto.
- Una cadena que parece un número (`"25"`) **sigue siendo texto**. Con ella no se puede calcular hasta que la conviertas ([apartado g](g-conversiones.md)).

## 5. Mutabilidad e inmutabilidad

Un objeto es **inmutable** si, una vez creado, no se puede modificar. Todos los tipos de esta unidad (`int`, `float`, `bool`, `str`) son **inmutables**.

Cuando «cambias» una variable, en realidad Python crea un **objeto nuevo** y hace que el nombre apunte a él:

```pycon
>>> x = 5
>>> antes = id(x)
>>> x = x + 1
>>> id(x) == antes          # ahora apunta a otro objeto
False
```

Y una cadena no se puede modificar carácter a carácter:

```pycon
>>> palabra = "hola"
>>> palabra[0] = "H"
Traceback (most recent call last):
  ...
TypeError: 'str' object does not support item assignment
```

!!! note "Adelanto"
    Existen tipos **mutables** (por ejemplo, las listas) que sí se pueden modificar «en el sitio». Los estudiarás en la UT04, y entender esta diferencia será importante.

## 6. Anotaciones de tipo (*type hints*): introducción

Puedes indicar en el código qué tipo esperas que tenga una variable:

```python
nombre: str = "Ana"
edad: int = 16
precio: float = 9.99
es_alumno: bool = True
```

- Son **documentación**: ayudan a quien lee el código y a VS Code, que te avisa si algo no encaja.
- Python **no las obliga**. Este código se ejecuta sin errores aunque no las cumpla:

```python
edad: int = "dieciséis"      # el editor te avisará, pero Python lo ejecuta
```

## Resumen

- Los cuatro tipos básicos: `int`, `float`, `bool`, `str`. Con `type()` los identificas.
- Python es de tipado **dinámico** (el tipo lo decide el valor) y **fuerte** (no mezcla tipos sin sentido).
- `/` siempre devuelve `float`. Los `float` pueden tener pequeños errores de redondeo.
- Son *falsy*: `0`, `0.0` y `""`. Todo lo demás es *truthy*.
- Los tipos básicos son **inmutables**.
- Las anotaciones de tipo son una ayuda, no una obligación.
