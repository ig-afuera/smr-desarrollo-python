# UT01 · Preguntas tipo test con código (con trampa)

Identificación de los elementos de un programa informático · 14 ejercicios de código de 4 opciones (una correcta).

Cada pregunta muestra un fragmento de código y pide predecir qué ocurre **sin ejecutarlo**. Todas esconden una trampa: el detalle que hace fallar a quien responde «a ojo». Tras la respuesta se indica cuál es.

| Apartado | Preguntas |
|---|---|
| a) Estructura y bloques fundamentales | 1 |
| b) Variables | 2 |
| c) Tipos de datos | 3 – 6 |
| d) Literales | — |
| e) Constantes | 7 – 8 |
| f) Operadores y expresiones | 9 – 10 |
| g) Conversiones de tipo | 11 – 13 |
| h) Comentarios | 14 |

---

## a) Estructura y bloques fundamentales

### 1. [a · media]
¿Cuál de estas líneas, ejecutada por separado, produce un **error**?

```python
true = 1        # línea A
print = 1       # línea B
True = 1        # línea C
```

- A) Línea A
- B) Línea B
- C) Línea C
- D) Ninguna produce error

**Respuesta: C** — `True` es una palabra reservada: `SyntaxError: cannot assign to True`. `true` (en minúscula) es un nombre válido y `print = 1` funciona aunque «pisa» la función.

> **Trampa:** la línea B parece la peligrosa, pero Python la acepta sin quejarse; el problema aparecería después, al intentar usar `print()`.

## b) Variables

### 2. [b · básica]
Se quiere intercambiar el valor de dos variables. ¿Qué muestra el programa?

```python
a = 3
b = 7
a = b
b = a
print(a, b)
```

- A) `7 3`
- B) `3 7`
- C) `7 7`
- D) `3 3`

**Respuesta: C** — En la tercera línea `a` pasa a valer 7 y el 3 se pierde. Cuando se ejecuta `b = a`, `a` ya vale 7.

> **Trampa:** parece un intercambio, pero para eso hace falta `a, b = b, a` (o una variable auxiliar).

---

## c) Tipos de datos

### 3. [c · media]
¿Qué muestra el programa?

```python
print(bool("0.0"), bool(0.0), bool(" "), bool(""))
```

- A) `False False False False`
- B) `False False True False`
- C) `True False True False`
- D) `True True True False`

**Respuesta: C** — `"0.0"` y `" "` son textos **no vacíos** → `True`. `0.0` es el número cero → `False`. `""` es el texto vacío → `False`.

> **Trampa:** el texto `"0.0"` «parece» cero, y el espacio `" "` «parece» vacío.

### 4. [c · básica]
¿Qué muestra el programa?

```python
x = "3"
y = x * 3
print(y + "1")
```

- A) `10`
- B) `91`
- C) `3331`
- D) `TypeError`

**Respuesta: C** — `x` es texto: `"3" * 3` repite el texto (`"333"`) y `+ "1"` lo concatena.

> **Trampa:** las comillas de la primera línea pasan desapercibidas y se calcula `3 * 3 + 1`.

### 5. [c · media]
¿Qué muestra el programa?

```python
edad: int = "veinte"
edad = edad + " años"
print(type(edad))
```

- A) `<class 'int'>`
- B) `<class 'str'>`
- C) `TypeError`, porque `edad` debe ser `int`.
- D) `SyntaxError` en la primera línea.

**Respuesta: B** — Las anotaciones de tipo son solo documentación: Python no las comprueba. `edad` guarda un texto y se concatena sin problemas.

> **Trampa:** creer que `: int` obliga a que la variable sea un entero.

### 6. [c · avanzada]
¿Qué muestra el programa?

```python
print(len(str(10 / 2)))
```

- A) `1`
- B) `2`
- C) `3`
- D) `TypeError`: `len()` no funciona con números.

**Respuesta: C** — `10 / 2` vale `5.0` (la división `/` siempre da `float`). Convertido a texto es `"5.0"`, que tiene 3 caracteres.

> **Trampa:** pensar que `10 / 2` es `5` y que su texto tiene un solo carácter.

---

## d) Literales


---

## e) Constantes

### 7. [e · avanzada]
¿Qué muestra el programa?

```python
import math

math.pi = 3
print(round(math.pi * 2))
```

- A) `6`
- B) `6.283185307179586`
- C) `AttributeError`: no se puede modificar `math.pi`.
- D) `SyntaxError`: `math.pi` es una constante.

**Respuesta: A** — Python no tiene constantes reales: incluso `math.pi` se puede reasignar. A partir de esa línea vale 3, y `round(3 * 2)` es 6.

> **Trampa:** dar por hecho que las constantes predefinidas están protegidas.

### 8. [e · media]
¿Qué muestra el programa?

```python
DESCUENTO = 0.10
precio = 50
final = precio - precio * DESCUENTO
DESCUENTO = 0.50
print(final)
```

- A) `25.0`
- B) `45.0`
- C) `45`
- D) Un error, `DESCUENTO` es una constante y no se puede reasignar

**Respuesta: B** — `final` se calculó cuando `DESCUENTO` valía 0.10. Cambiar la constante después no recalcula nada.

> **Trampa:** pensar que `final` «se actualiza» como una fórmula de hoja de cálculo. La opción C olvida que multiplicar por un `float` da `float`.

---

## f) Operadores y expresiones

### 9. [f · media]
¿Qué muestra el programa?

```python
print(-3 ** 2 + 10 // 3 * 2)
```

- A) `15`
- B) `-3`
- C) `9.67`
- D) `-7`

**Respuesta: B** — `**` va antes que el signo: `-(3 ** 2)` = -9. Luego `10 // 3 * 2` (izquierda a derecha) = 3 * 2 = 6. Total: -9 + 6 = -3.

> **Trampa:** calcular `(-3) ** 2 = 9`, que da 15 (opción A), o hacer `3 * 2` antes que `10 // 3`.

### 10. [f · avanzada]
¿Qué muestra el programa?

```python
print((5 > 4) > 3)
```

- A) `True`
- B) `False`
- C) `TypeError` ya que no se pueden comparar un booleano y un entero
- D) `ValueError` no se pueden usar paréntesis con operaciones booleanas

**Respuesta: B** — `5 > 4 > 3` es una comparación encadenada: `5 > 4 and 4 > 3` → `True`. En cambio, `(5 > 4) > 3` compara `True > 3`, es decir, `1 > 3` → `False`.

> **Trampa:** los paréntesis parecen no cambiar nada, pero rompen el encadenamiento.

---

## g) Conversiones de tipo

### 11. [g · avanzada]
¿Qué muestra el programa?

```python
print(int(-2.7) + int("08"))
```

- A) `6`
- B) `5`
- C) `ValueError`, porque `"08"` empieza por cero.
- D) Otro error distinto a `ValueError`

**Respuesta: A** — `int(-2.7)` trunca (quita los decimales) → -2. `int("08")` → 8. Total: -2 + 8 = 6.

> **Trampa:** dos a la vez: `int` corta en vez de redondear (si diera -3 saldría 5, la opción B) y el cero a la izquierda en un texto no molesta.

### 12. [g · básica]
El usuario escribe `4` y después `5`. ¿Qué muestra el programa?

```python
a = input("Número: ")
b = input("Número: ")
print(a + b * 2)
```

- A) `14`
- B) `18`
- C) `455`
- D) `4545`

**Respuesta: C** — `input()` siempre devuelve texto. `b * 2` repite el texto (`"55"`) y `+` lo concatena con `"4"`.

> **Trampa:** olvidar que no hay conversión. La opción D sale si se hace la suma antes que la multiplicación.

### 13. [g · media]
¿Cuál de estas expresiones produce un **error**?

- A) `int(float("3.9"))`
- B) `float("3")`
- C) Ninguna, todas funcionan correctamente.
- D) `str(3.0) + "1"`

**Respuesta: C** — A da `3`: `float("3.9")` convierte el texto en `3.9` y `int()` lo trunca. B da `3.0` y D da `'3.01'`.

> **Trampa:** `int("3.9")` sí daría `ValueError`, porque `int()` no acepta textos con punto decimal; pero aquí el texto pasa antes por `float()`, que sí lo acepta.

---

## h) Comentarios

### 14. [h · media]
¿Qué muestra el programa?

```python
x = 5  # x = 10
"""
x = 20
"""
# x = 30
print(x)
```

- A) `10`
- B) `20`
- C) `30`
- D) `5`

**Respuesta: D** — Lo que va tras `#` se ignora, y lo que hay entre triples comillas es una cadena suelta que no se asigna a nada: `x = 20` es texto, no una instrucción.

> **Trampa:** creer que el código dentro de las triples comillas se ejecuta.
