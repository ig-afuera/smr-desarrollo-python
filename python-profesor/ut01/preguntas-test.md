# UT01 · Banco de preguntas tipo test

Identificación de los elementos de un programa informático · 54 preguntas de 4 opciones (una correcta).

| Apartado | Preguntas |
|---|---|
| a) Estructura y bloques fundamentales | 1 – 6 |
| b) Variables | 7 – 11 |
| c) Tipos de datos | 12 – 19 |
| d) Literales | 20 – 26 |
| e) Constantes | 27 – 30 |
| f) Operadores y expresiones | 31 – 42 |
| g) Conversiones de tipo | 43 – 49 |
| h) Comentarios | 50 – 54 |

---

## a) Estructura y bloques fundamentales

### 1. [a · básica]
¿Qué caracteriza a un lenguaje **interpretado** como Python?

- A) El programa se traduce completo a código máquina antes de ejecutarse.
- B) Un intérprete traduce y ejecuta las instrucciones una a una.
- C) Solo puede ejecutarse en un sistema operativo concreto.
- D) No necesita ningún programa para poder ejecutarse.

**Respuesta: B** — El intérprete lee, traduce y ejecuta el código sobre la marcha. La opción A describe un lenguaje compilado.

### 2. [a · básica]
En Python, ¿cómo se delimita un bloque de código (por ejemplo, el cuerpo de un `if`)?

- A) Con llaves `{ }`.
- B) Con las palabras `begin` y `end`.
- C) Con la indentación, tras una línea que termina en dos puntos.
- D) Con paréntesis.

**Respuesta: C** — Python usa la indentación (por convención, 4 espacios) tras los dos puntos `:`.

### 3. [a · básica]
Quieres comprobar rápidamente qué devuelve `round(2.5)` sin crear ningún archivo. ¿Qué herramienta es la más adecuada?

- A) La consola de Python (REPL).
- B) Crear un programa `.py` y guardarlo en una carpeta.
- C) El depurador de VS Code.
- D) Un documento de texto.

**Respuesta: A** — El REPL evalúa cada instrucción al momento y muestra el resultado, ideal para pruebas rápidas.

### 4. [a · media]
¿Cuál de los siguientes es un identificador **válido** en Python?

- A) `3_notas`
- B) `nota-final`
- C) `for`
- D) `nota_final`

**Respuesta: D** — `3_notas` empieza por un dígito, `nota-final` contiene un guion (operador resta) y `for` es una palabra reservada.

### 5. [a · media]
¿Cuál es el orden habitual de las fases de desarrollo de un programa?

- A) Codificación, análisis, diseño, prueba, documentación.
- B) Análisis, diseño, codificación, prueba, documentación.
- C) Diseño, prueba, análisis, codificación, documentación.
- D) Prueba, codificación, diseño, análisis, documentación.

**Respuesta: B** — Primero se entiende el problema (análisis), luego se planifica la solución (diseño), después se programa, se prueba y se documenta.

### 6. [a · media]
En un cuaderno de Jupyter ejecutas primero la celda 3 (que usa la variable `total`) y después la celda 1 (que define `total`). ¿Qué ocurre?

- A) La celda 3 falla con `NameError`, porque `total` aún no existe cuando se ejecuta.
- B) Jupyter reordena las celdas automáticamente y todo funciona.
- C) La celda 3 muestra `0`, el valor por defecto de las variables.
- D) La celda 3 se ejecuta sin errores y espera a que definas `total`.

**Respuesta: A** — Un cuaderno recuerda las variables según el **orden de ejecución** de las celdas, no el orden en que aparecen en la página.

---

## b) Variables

### 7. [b · básica]
¿Qué ocurre con este código?
```python
x = 5
x = "cinco"
```

- A) `TypeError`, porque cambia el tipo de la variable.
- B) Es válido: Python tiene tipado dinámico y `x` pasa a apuntar a un texto.
- C) `SyntaxError`, porque no se puede reutilizar el nombre.
- D) `x` sigue valiendo 5 y la segunda línea se ignora.

**Respuesta: B** — Una variable es un nombre que apunta a un valor; puede reasignarse a un valor de otro tipo.

### 8. [b · básica]
Tras ejecutar:
```python
a, b = 3, 8
a, b = b, a
```
¿cuánto valen `a` y `b`?

- A) `a = 3`, `b = 8`
- B) `a = 3`, `b = 3`
- C) `a = 8`, `b = 8`
- D) `a = 8`, `b = 3`

**Respuesta: D** — Se evalúa primero la parte derecha `(8, 3)` y luego se asigna, con lo que se intercambian los valores.

### 9. [b · media]
```python
a = b = 4
a = 7
```
¿Cuánto vale `b` al final?

- A) `7`
- B) `None`
- C) `4`
- D) Da error.

**Respuesta: C** — `a = 7` hace que el nombre `a` apunte a otro valor; `b` sigue apuntando a `4`. Los enteros son inmutables.

### 10. [b · media]
Tras ejecutar `del saldo`, se escribe `print(saldo)`. ¿Qué ocurre?

- A) Se produce un `NameError`, porque la variable ya no existe.
- B) Muestra `None`.
- C) Muestra `0`.
- D) Muestra el último valor que tuvo la variable.

**Respuesta: A** — `del` elimina el nombre; usarlo después provoca `NameError: name 'saldo' is not defined`.

### 11. [b · media]
¿Cuál es el ámbito de una variable creada **dentro** de una función?

- A) Global: se puede usar en todo el programa.
- B) Es una constante.
- C) Local: solo existe mientras se ejecuta la función.
- D) Existe hasta que se cierra el editor.

**Respuesta: C** — Las variables creadas dentro de una función son locales y desaparecen al terminar esta.

---

## c) Tipos de datos

### 12. [c · básica]
¿De qué tipo es el resultado de `10 / 2`?

- A) `int`
- B) `str`
- C) `bool`
- D) `float`

**Respuesta: D** — La división `/` devuelve siempre `float`: el resultado es `5.0`.

### 13. [c · básica]
¿Qué resultado da `"5" + 3`?

- A) `8`
- B) `TypeError`
- C) `"53"`
- D) `53`

**Respuesta: B** — Python es de tipado fuerte: no mezcla texto y número sin una conversión explícita.

### 14. [c · media]
¿Cómo se describe el sistema de tipos de Python?

- A) Dinámico y fuerte.
- B) Estático y fuerte.
- C) Estático y débil.
- D) Dinámico y débil.

**Respuesta: A** — Dinámico (el tipo lo determina el valor, no se declara) y fuerte (no convierte tipos de forma implícita cuando no tiene sentido).

### 15. [c · media]
¿Cuánto vale `bool("False")`?

- A) `False`
- B) `None`
- C) `True`
- D) Da error.

**Respuesta: C** — Es una cadena no vacía, y toda cadena no vacía es *truthy*. `bool` no interpreta el contenido del texto.

### 16. [c · media]
¿Cuál de estos valores se evalúa como *falsy* (falso)?

- A) `"0"`
- B) `"False"`
- C) `-1`
- D) `0.0`

**Respuesta: D** — `0.0` es falso. `"0"` y `"False"` son cadenas no vacías y `-1` es un número distinto de cero: los tres son verdaderos.

### 17. [c · media]
¿Qué valor devuelve `True + True`?

- A) `True`
- B) `2`
- C) `"TrueTrue"`
- D) Da error.

**Respuesta: B** — Los booleanos son enteros: `True` vale 1 y `False` vale 0.

### 18. [c · avanzada]
Dada `s = "hola"`, ¿qué ocurre al ejecutar `s[0] = "H"`?

- A) `s` pasa a valer `"Hola"`.
- B) Se crea una variable nueva llamada `H`.
- C) La consola pide confirmación.
- D) `TypeError`, porque las cadenas son inmutables.

**Respuesta: D** — Las cadenas no se pueden modificar carácter a carácter. Para «cambiar» un texto hay que crear otro nuevo.

### 19. [c · media]
¿Qué hace Python con este código?
```python
edad: int = "veinte"
```

- A) `SyntaxError`.
- B) `TypeError`.
- C) Se ejecuta sin error: las anotaciones de tipo no se comprueban al ejecutar.
- D) Convierte `"veinte"` a entero.

**Respuesta: C** — Las anotaciones de tipo son documentación y ayuda para el editor; el intérprete no las impone.

---

## d) Literales

### 20. [d · básica]
¿Cuál es el valor decimal del literal `0b101`?

- A) `5`
- B) `101`
- C) `10`
- D) `3`

**Respuesta: A** — `0b` indica binario: 1·4 + 0·2 + 1·1 = 5.

### 21. [d · básica]
¿Cuánto vale el literal `0xFF`?

- A) `15`
- B) `16`
- C) `255`
- D) `256`

**Respuesta: C** — `0x` indica hexadecimal: 15·16 + 15 = 255.

### 22. [d · media]
¿Qué valor representa el literal `1.5e3`?

- A) `15.3`
- B) `1.53`
- C) `150`
- D) `1500.0`

**Respuesta: D** — Notación científica: 1,5 × 10³ = 1500.0.

### 23. [d · media]
¿Qué muestra `print("Ruta: C:\\datos")`?

- A) `Ruta: C:\\datos`
- B) `Ruta: C:\datos`
- C) `Ruta: C:datos`
- D) Da error.

**Respuesta: B** — `\\` es la secuencia de escape de una barra invertida, y se muestra una sola.

### 24. [d · media]
¿Qué valor devuelve `f"{3.14159:.2f}"`?

- A) `'3.14'`
- B) `'3.14159'`
- C) `'3.1'`
- D) `'3'`

**Respuesta: A** — `:.2f` formatea el número con 2 decimales.

### 25. [d · media]
¿Qué muestra `print(r"C:\nuevo")`?

- A) `C:` y, en la línea siguiente, `uevo`.
- B) Da error.
- C) `C:\nuevo`
- D) `C:nuevo`

**Respuesta: C** — Con el prefijo `r` (*raw*) las barras invertidas no se interpretan como secuencias de escape.

### 26. [d · básica]
¿Cuál de estos es un literal lógico válido en Python?

- A) `true`
- B) `TRUE`
- C) `"True"`
- D) `True`

**Respuesta: D** — Los literales lógicos se escriben con la primera letra en mayúscula. `"True"` (con comillas) es un texto.

---

## e) Constantes

### 27. [e · básica]
¿Qué convención se sigue en Python para nombrar las constantes?

- A) Minúsculas: `iva`.
- B) MAYÚSCULAS con guion bajo: `IVA`, `MAX_INTENTOS`.
- C) camelCase: `maxIntentos`.
- D) Con el prefijo `const_`.

**Respuesta: B** — Es la convención de PEP 8.

### 28. [e · media]
Si defines `IVA = 0.21` y más adelante escribes `IVA = 0.10`, ¿qué ocurre?

- A) Error de sintaxis.
- B) `TypeError`.
- C) Solo falla en Jupyter.
- D) Python lo permite: la mayúscula es solo una convención.

**Respuesta: D** — Python no tiene constantes reales; no se debe reasignar por convención, pero el lenguaje no lo impide.

### 29. [e · media]
¿Cuál es la principal ventaja de definir `IVA = 0.21` y usarlo en los cálculos, en lugar de escribir `0.21` cada vez?

- A) El código se ejecuta más rápido.
- B) Si el valor cambia, se modifica en un solo sitio, y el nombre explica qué significa.
- C) Ocupa menos memoria.
- D) Python lo exige.

**Respuesta: B** — Mejora la legibilidad y el mantenimiento, y evita inconsistencias.

### 30. [e · básica]
¿Qué necesitas hacer para poder usar `math.pi` en tu programa?

- A) Nada, está siempre disponible.
- B) Definir `pi = 3.14`.
- C) Escribir `import math` antes.
- D) Escribir `from pi import math`.

**Respuesta: C** — El módulo `math` no está disponible hasta que se importa.

---

## f) Operadores y expresiones

### 31. [f · básica]
¿Cuánto vale `17 // 5`?

- A) `3.4`
- B) `3`
- C) `2`
- D) `4`

**Respuesta: B** — `//` es la división entera: cociente sin decimales.

### 32. [f · básica]
¿Cuánto vale `17 % 5`?

- A) `3`
- B) `12`
- C) `3.4`
- D) `2`

**Respuesta: D** — `%` devuelve el resto de la división: 17 = 5·3 + 2.

### 33. [f · media]
¿Cuánto vale `-7 // 2`?

- A) `-4`
- B) `-3`
- C) `-3.5`
- D) `3`

**Respuesta: A** — La división entera redondea hacia abajo (hacia −∞), por lo que −3,5 pasa a −4.

### 34. [f · media]
¿Cuánto vale `2 ** 3 ** 2`?

- A) `64`
- B) `36`
- C) `512`
- D) `128`

**Respuesta: C** — `**` se asocia de derecha a izquierda: `2 ** (3 ** 2)` = 2⁹ = 512.

### 35. [f · media]
¿Qué valor da `not True or True`?

- A) `False`
- B) `True`
- C) `None`
- D) Error.

**Respuesta: B** — `not` tiene más precedencia que `or`: `(not True) or True` → `False or True` → `True`.

### 36. [f · media]
```python
x = 5
x *= 2 + 1
```
¿Cuánto vale `x`?

- A) `11`
- B) `13`
- C) `10`
- D) `15`

**Respuesta: D** — Equivale a `x = x * (2 + 1)`: primero se calcula todo el lado derecho.

### 37. [f · media]
¿Qué devuelve `False and (10 / 0 > 1)`?

- A) `False`, sin llegar a evaluar la división entre cero.
- B) `ZeroDivisionError`.
- C) `True`.
- D) `None`.

**Respuesta: A** — Cortocircuito: con `and`, si el primer operando es falso el resultado ya es falso y no se evalúa el segundo.

### 38. [f · básica]
¿Qué devuelve `"ol" in "hola"`?

- A) `False`
- B) Error.
- C) `True`
- D) `'ol'`

**Respuesta: C** — `in` comprueba si un texto está contenido en otro.

### 39. [f · media]
¿Qué devuelve `1 < 5 < 3`?

- A) `True`
- B) `False`
- C) Error.
- D) `3`

**Respuesta: B** — La comparación encadenada equivale a `1 < 5 and 5 < 3`, que es falsa.

### 40. [f · media]
¿Cuál es la forma recomendada de comprobar si `0.1 + 0.2` y `0.3` son «iguales»?

- A) `0.1 + 0.2 == 0.3`
- B) `0.1 + 0.2 is 0.3`
- C) `int(0.1 + 0.2) == int(0.3)`
- D) `math.isclose(0.1 + 0.2, 0.3)`

**Respuesta: D** — Los decimales tienen errores de representación; `math.isclose` compara con una pequeña tolerancia.

### 41. [f · avanzada]
¿Qué devuelve `round(2.5)`?

- A) `3`
- B) `2`
- C) `2.5`
- D) `3.0`

**Respuesta: B** — Python redondea los «medios» al entero **par** más cercano (redondeo bancario): `round(2.5)` es `2` y `round(3.5)` es `4`.

### 42. [f · avanzada]
Tras ejecutar `(n := 4) * 2`, ¿qué valor devuelve la expresión y cuánto vale `n`?

- A) Devuelve `8` y `n` no existe.
- B) `SyntaxError`.
- C) Devuelve `8` y `n` vale `4`.
- D) Devuelve `4` y `n` vale `8`.

**Respuesta: C** — El operador *walrus* `:=` asigna `4` a `n` y, a la vez, usa ese valor en la expresión.

---

## g) Conversiones de tipo

### 43. [g · básica]
¿Cuánto vale `int(3.9)`?

- A) `4`
- B) `3`
- C) `3.9`
- D) Da error.

**Respuesta: B** — `int()` trunca los decimales, no redondea.

### 44. [g · básica]
¿Qué tipo de dato devuelve siempre la función `input()`?

- A) `int`
- B) `float`
- C) Depende de lo que escriba el usuario.
- D) `str`

**Respuesta: D** — Siempre devuelve texto; hay que convertirlo con `int()` o `float()` para operar con números.

### 45. [g · media]
¿Qué ocurre al ejecutar `int("3.5")`?

- A) `ValueError`.
- B) Devuelve `3`.
- C) Devuelve `4`.
- D) Devuelve `3.5`.

**Respuesta: A** — `int` no admite un texto con parte decimal. Habría que hacer `int(float("3.5"))`.

### 46. [g · media]
¿Qué devuelve `bin(10)`?

- A) `1010`
- B) `'1010'`
- C) `'0b1010'`
- D) `'0xa'`

**Respuesta: C** — Devuelve una cadena con el prefijo `0b`.

### 47. [g · media]
¿Qué devuelve `int("ff", 16)`?

- A) `15`
- B) `255`
- C) `ValueError`
- D) `'ff'`

**Respuesta: B** — El segundo argumento indica la base del texto: `ff` en hexadecimal es 255.

### 48. [g · media]
Un usuario escribe `3,5` y el programa ejecuta `float("3,5")`. ¿Qué ocurre?

- A) Devuelve `3.5`.
- B) Devuelve `35.0`.
- C) Devuelve `3.0`.
- D) `ValueError`, porque Python solo reconoce el punto decimal.

**Respuesta: D** — Hay que sustituir la coma por un punto antes de convertir.

### 49. [g · avanzada]
¿Qué devuelve `isinstance(True, int)`?

- A) `True`, porque `bool` es un subtipo de `int`.
- B) `False`.
- C) `TypeError`.
- D) `None`.

**Respuesta: A** — En Python, `bool` hereda de `int`, por eso `True` se considera también un entero.

---

## h) Comentarios

### 50. [h · básica]
¿Qué es un comentario de una línea en Python?

- A) Un texto entre triples comillas.
- B) Una línea que empieza por `//`.
- C) Todo lo que sigue a `#` hasta el final de la línea, que Python ignora.
- D) Una línea que empieza por `--`.

**Respuesta: C** — `#` inicia un comentario que el intérprete ignora.

### 51. [h · media]
¿Qué es un *docstring*?

- A) Un comentario que Python ignora por completo.
- B) Una cadena entre triples comillas, situada al inicio de un módulo, función o clase, que documenta y se puede consultar con `help()` o `__doc__`.
- C) Una variable especial.
- D) Una constante definida en `math`.

**Respuesta: B** — A diferencia de los comentarios, los docstrings se conservan en tiempo de ejecución.

### 52. [h · media]
Ante la línea `total = base * 1.10`, ¿cuál es el **mejor** comentario?

- A) `# multiplica base por 1.10`
- B) `# total`
- C) `# TODO`
- D) `# se aplica el 10 % de IVA reducido de hostelería`

**Respuesta: D** — Un buen comentario explica el **porqué**, no repite lo que ya dice el código.

### 53. [h · básica]
Según PEP 8, ¿con qué se indenta el código en Python?

- A) 4 espacios.
- B) 1 tabulador.
- C) 2 espacios.
- D) 8 espacios.

**Respuesta: A** — La convención es de 4 espacios por nivel.

### 54. [h · básica]
Estás en un aula sin internet y necesitas recordar cómo funciona la función `round`. ¿Cómo lo consultas desde la consola de Python?

- A) `doc(round)`
- B) `round?`
- C) `help(round)`
- D) No se puede sin conexión.

**Respuesta: C** — `help()` muestra la documentación incorporada en Python, sin necesidad de conexión.

---

## Hoja de respuestas

| Nº | Apt. | Dificultad | Resp. | Nº | Apt. | Dificultad | Resp. |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | a | básica | **B** | 28 | e | media | **D** |
| 2 | a | básica | **C** | 29 | e | media | **B** |
| 3 | a | básica | **A** | 30 | e | básica | **C** |
| 4 | a | media | **D** | 31 | f | básica | **B** |
| 5 | a | media | **B** | 32 | f | básica | **D** |
| 6 | a | media | **A** | 33 | f | media | **A** |
| 7 | b | básica | **B** | 34 | f | media | **C** |
| 8 | b | básica | **D** | 35 | f | media | **B** |
| 9 | b | media | **C** | 36 | f | media | **D** |
| 10 | b | media | **A** | 37 | f | media | **A** |
| 11 | b | media | **C** | 38 | f | básica | **C** |
| 12 | c | básica | **D** | 39 | f | media | **B** |
| 13 | c | básica | **B** | 40 | f | media | **D** |
| 14 | c | media | **A** | 41 | f | avanzada | **B** |
| 15 | c | media | **C** | 42 | f | avanzada | **C** |
| 16 | c | media | **D** | 43 | g | básica | **B** |
| 17 | c | media | **B** | 44 | g | básica | **D** |
| 18 | c | avanzada | **D** | 45 | g | media | **A** |
| 19 | c | media | **C** | 46 | g | media | **C** |
| 20 | d | básica | **A** | 47 | g | media | **B** |
| 21 | d | básica | **C** | 48 | g | media | **D** |
| 22 | d | media | **D** | 49 | g | avanzada | **A** |
| 23 | d | media | **B** | 50 | h | básica | **C** |
| 24 | d | media | **A** | 51 | h | media | **B** |
| 25 | d | media | **C** | 52 | h | media | **D** |
| 26 | d | básica | **D** | 53 | h | básica | **A** |
| 27 | e | básica | **B** | 54 | h | básica | **C** |
