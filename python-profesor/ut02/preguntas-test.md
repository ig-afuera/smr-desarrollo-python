# UT02 · Banco de preguntas tipo test

Uso de estructuras de control · 48 preguntas de 4 opciones (una correcta).

| Apartado | Preguntas |
|---|---|
| a) Estructuras de selección | 1 – 12 |
| b) Estructuras de repetición | 13 – 26 |
| c) Estructuras de salto | 27 – 33 |
| d) Control de excepciones | 34 – 48 |

---

## a) Estructuras de selección

### 1. [a · básica]
¿Qué carácter es obligatorio al final de la línea que contiene un `if`?

- A) `;`
- B) `end`
- C) `then`
- D) `:`

**Respuesta: D** — Los dos puntos indican que a continuación empieza un bloque indentado.

### 2. [a · básica]
¿Qué muestra este código?
```python
x = 7
if x > 5:
    print("A")
elif x > 3:
    print("B")
else:
    print("C")
```

- A) Solo `A`.
- B) `A` y `B`.
- C) Solo `B`.
- D) Solo `C`.

**Respuesta: A** — Con `if / elif / else` solo se ejecuta el primer bloque cuya condición es verdadera; el resto se ignora.

### 3. [a · media]
¿Qué muestra este código?
```python
x = 7
if x > 5:
    print("A")
if x > 3:
    print("B")
else:
    print("C")
```

- A) Solo `A`.
- B) Solo `B`.
- C) `A` y `B` (en líneas distintas).
- D) `A`, `B` y `C`.

**Respuesta: C** — Son **dos** condicionales independientes. El primero muestra `A`; el segundo (con su propio `else`) muestra `B`.

### 4. [a · media]
¿Qué muestra este código?
```python
nota = 9.5
if nota >= 5:
    print("Aprobado")
elif nota >= 9:
    print("Sobresaliente")
```

- A) `Sobresaliente`
- B) `Aprobado`
- C) `Aprobado` y `Sobresaliente`
- D) Nada.

**Respuesta: B** — El orden importa: `nota >= 5` ya es verdadera, así que el `elif` nunca se evalúa. Las condiciones deben ir de la más restrictiva a la más general.

### 5. [a · básica]
¿Qué ocurre al ejecutar `if x = 3:`?

- A) `SyntaxError`: se ha usado `=` (asignación) en lugar de `==` (comparación).
- B) Se asigna 3 a `x` y la condición es verdadera.
- C) Se compara `x` con 3.
- D) `TypeError`.

**Respuesta: A** — Una asignación no puede usarse como condición de un `if`.

### 6. [a · media]
¿Qué valor tiene `resultado`?
```python
resultado = "par" if 8 % 2 == 0 else "impar"
```

- A) `'impar'`
- B) `True`
- C) `0`
- D) `'par'`

**Respuesta: D** — Es una expresión condicional (operador ternario): `8 % 2 == 0` es verdadero, así que se elige `"par"`.

### 7. [a · básica]
La instrucción `match` / `case` requiere como mínimo la versión de Python…

- A) 3.6
- B) 3.10
- C) 3.8
- D) 2.7

**Respuesta: B** — `match` se introdujo en Python 3.10. En versiones anteriores da `SyntaxError`.

### 8. [a · media]
En una instrucción `match`, `case _:` equivale a…

- A) un `elif`.
- B) un `break`.
- C) el `else` de un `if`: se ejecuta si ningún otro caso coincide.
- D) un `pass`.

**Respuesta: C** — El guion bajo es el comodín que captura todo lo que no encajó en los casos anteriores.

### 9. [a · media]
¿Qué muestra este código?
```python
dia = "sábado"
match dia:
    case "sábado" | "domingo":
        print("Fin de semana")
    case _:
        print("Laborable")
```

- A) `Laborable`
- B) Da error.
- C) `Fin de semana`
- D) No muestra nada.

**Respuesta: C** — El símbolo `|` permite agrupar varios valores en un mismo `case`.

### 10. [a · avanzada]
¿Por qué la condición `if x == 1 or 2:` es un error de lógica?

- A) Es siempre verdadera, porque `2` se evalúa como *truthy*.
- B) Solo es verdadera si `x` vale 1 o 2.
- C) Da `SyntaxError`.
- D) Solo es verdadera si `x` vale 2.

**Respuesta: A** — Se interpreta como `(x == 1) or 2`, y el número `2` siempre es verdadero. Lo correcto es `x == 1 or x == 2`.

### 11. [a · media]
¿Qué ocurre con este código si el usuario escribe `20`?
```python
edad = input("Edad: ")
if edad >= 18:
    print("Mayor de edad")
```

- A) `SyntaxError`.
- B) `TypeError`, porque se compara un texto con un número.
- C) `ValueError`.
- D) Muestra «Mayor de edad».

**Respuesta: B** — `input()` devuelve un `str`; hay que convertirlo con `int()` antes de comparar.

### 12. [a · media]
¿Cuál de estas condiciones equivale a `1 <= mes <= 12`?

- A) `1 <= mes or mes <= 12`
- B) `1 <= mes and 12`
- C) `mes in 1..12`
- D) `mes >= 1 and mes <= 12`

**Respuesta: D** — La comparación encadenada equivale a unir las dos comparaciones con `and`.

---

## b) Estructuras de repetición

### 13. [b · básica]
¿Qué muestra este código?
```python
i = 1
while i <= 3:
    print(i)
    i += 1
```

- A) `1 2 3 4`
- B) `1 2 3`
- C) `0 1 2`
- D) `1 2`

**Respuesta: B** — Muestra 1, 2 y 3 (uno por línea). Cuando `i` vale 4, la condición es falsa y el bucle termina.

### 14. [b · básica]
¿Qué valores recorre `range(2, 10, 3)`?

- A) `2, 5, 8, 10`
- B) `3, 6, 9`
- C) `2, 4, 6, 8`
- D) `2, 5, 8`

**Respuesta: D** — Empieza en 2 y suma 3 cada vez, sin llegar a 10: 2, 5, 8.

### 15. [b · básica]
¿Cuántas veces se ejecuta el cuerpo de `for i in range(1, 6):`?

- A) 5
- B) 6
- C) 4
- D) 0

**Respuesta: A** — Recorre 1, 2, 3, 4 y 5: el valor final (6) no se incluye.

### 16. [b · media]
¿Cuál de estos bucles es infinito?

- A) `i = 0` / `while i < 3: i += 1`
- B) `for i in range(10): print(i)`
- C) `i = 0` / `while i < 3: print(i)`
- D) `i = 5` / `while i > 10: i -= 1`

**Respuesta: C** — La variable `i` nunca cambia dentro del bucle, así que la condición siempre es verdadera. En D, la condición es falsa desde el principio y el bucle no llega a ejecutarse.

### 17. [b · media]
¿Cuántas líneas muestra este código?
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

- A) 3
- B) 5
- C) 2
- D) 6

**Respuesta: D** — El bucle interno se ejecuta completo (2 veces) por cada vuelta del externo (3 veces): 3 × 2 = 6.

### 18. [b · media]
¿Qué valores recorre `range(10, 0, -3)`?

- A) `10, 7, 4, 1, 0`
- B) `10, 7, 4, 1`
- C) `7, 4, 1`
- D) `10, 3`

**Respuesta: B** — Con paso negativo cuenta hacia atrás mientras el valor sea mayor que el final (0, no incluido): 10, 7, 4, 1.

### 19. [b · básica]
Quieres pedir números al usuario hasta que teclee `0`. ¿Qué bucle es el más adecuado?

- A) `while`, porque no se sabe cuántas veces se repetirá.
- B) `for` con `range(10)`.
- C) `for` con `range(0)`.
- D) Ninguno.

**Respuesta: A** — Cuando la repetición depende de una condición y no de un número fijo de vueltas, se usa `while`.

### 20. [b · media]
¿Qué muestra este código?
```python
for i in range(3):
    print(i)
else:
    print("fin")
```

- A) `0 1 2`
- B) `fin`
- C) `0 1 2 fin`
- D) `fin 0 1 2`

**Respuesta: C** — El `else` de un bucle se ejecuta cuando este termina de forma natural, sin `break`.

### 21. [b · avanzada]
¿Qué muestra este código?
```python
for i in range(5):
    if i == 2:
        break
else:
    print("fin")
print(i)
```

- A) `fin` y `2`
- B) Solo `2`
- C) Solo `fin`
- D) `4`

**Respuesta: B** — El `break` interrumpe el bucle, así que **no** se ejecuta el `else`. Después se muestra el valor de `i`, que es 2.

### 22. [b · media]
¿Qué muestra este código?
```python
suma = 0
for n in range(1, 5):
    suma += n
print(suma)
```

- A) `15`
- B) `5`
- C) `6`
- D) `10`

**Respuesta: D** — Suma 1 + 2 + 3 + 4 = 10 (el 5 no entra en `range(1, 5)`).

### 23. [b · media]
¿Qué muestra este código?
```python
c = 0
for n in range(1, 11):
    if n % 2 == 0:
        c += 1
print(c)
```

- A) `5`
- B) `10`
- C) `4`
- D) `6`

**Respuesta: A** — Cuenta los números pares entre 1 y 10: 2, 4, 6, 8 y 10.

### 24. [b · media]
¿Qué dibuja este código?
```python
for i in range(1, 4):
    print("*" * i)
```

- A) Una línea con `***`.
- B) Tres líneas con `*`.
- C) Tres líneas: `*`, `**` y `***`.
- D) Tres líneas: `***`, `**` y `*`.

**Respuesta: C** — En cada vuelta se repite el asterisco `i` veces: 1, 2 y 3.

### 25. [b · media]
En un bucle controlado por **centinela**, el centinela es…

- A) el contador de vueltas.
- B) el primer dato leído.
- C) un valor especial que indica que no hay más datos.
- D) una variable lógica.

**Respuesta: C** — Por ejemplo, el `0` en «introduce números y termina con 0».

### 26. [b · básica]
¿Cómo se interrumpe un bucle infinito que se está ejecutando en la terminal de VS Code?

- A) `Ctrl+C`
- B) `Ctrl+S`
- C) `Ctrl+Z`
- D) `Alt+F4`

**Respuesta: A** — `Ctrl+C` envía una interrupción (`KeyboardInterrupt`) al programa. En Jupyter se usa el botón *Interrumpir*.

---

## c) Estructuras de salto

### 27. [c · básica]
¿Qué hace la sentencia `break` dentro de un bucle?

- A) Sale del programa.
- B) Salta a la siguiente iteración.
- C) No hace nada.
- D) Termina el bucle inmediatamente.

**Respuesta: D** — El programa continúa con la primera instrucción posterior al bucle.

### 28. [c · básica]
¿Qué hace la sentencia `continue`?

- A) Termina el bucle.
- B) Se salta el resto de la iteración actual y pasa a la siguiente.
- C) Repite la iteración actual.
- D) Vuelve al principio del programa.

**Respuesta: B** — El bucle sigue funcionando: solo se omite lo que queda del bloque en esa vuelta.

### 29. [c · media]
¿Qué muestra este código?
```python
for n in range(1, 6):
    if n == 3:
        continue
    print(n, end=" ")
```

- A) `1 2 4 5`
- B) `1 2`
- C) `1 2 3 4 5`
- D) `4 5`

**Respuesta: A** — Cuando `n` vale 3, `continue` salta el `print` pero el bucle sigue con 4 y 5.

### 30. [c · media]
¿Qué muestra este código?
```python
for n in range(1, 6):
    if n == 3:
        break
    print(n, end=" ")
```

- A) `1 2 4 5`
- B) `1 2 3`
- C) `1 2`
- D) `4 5`

**Respuesta: C** — Al llegar a 3, `break` termina el bucle.

### 31. [c · básica]
¿Para qué sirve `pass`?

- A) Para salir de un bucle.
- B) Como marcador de un bloque vacío: no hace nada, pero cumple la sintaxis.
- C) Para saltar una iteración.
- D) Para detener el programa.

**Respuesta: B** — Sirve cuando la sintaxis exige un bloque pero todavía no se ha escrito su contenido.

### 32. [c · avanzada]
¿Cuántas líneas muestra este código?
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

- A) 1
- B) 9
- C) 6
- D) 3

**Respuesta: D** — `break` solo interrumpe el bucle interno. Para cada `i` se muestra únicamente la pareja con `j == 0`: `0 0`, `1 0` y `2 0`.

### 33. [c · media]
Un bucle `while True:` necesita, para poder terminar…

- A) un `break` (o una excepción) dentro del bucle.
- B) un `else`.
- C) un `pass`.
- D) un `continue`.

**Respuesta: A** — La condición `True` nunca se vuelve falsa: la salida debe provocarse desde dentro.

---

## d) Control de excepciones

### 34. [d · media]
¿Cuál de estos errores es una **excepción** (error de ejecución)?

- A) `print("hola"` (falta el paréntesis de cierre)
- B) Calcular una media dividiendo entre 2 cuando hay 3 notas.
- C) `int("abc")`
- D) Olvidar los dos puntos al final de un `if`.

**Respuesta: C** — A y D son errores de sintaxis, y B es un error lógico. Solo `int("abc")` es correcto sintácticamente y falla al ejecutarse (`ValueError`).

### 35. [d · básica]
¿Qué excepción lanza `int("abc")`?

- A) `ValueError`
- B) `TypeError`
- C) `NameError`
- D) `SyntaxError`

**Respuesta: A** — El tipo del argumento es correcto (una cadena), pero su contenido no se puede convertir.

### 36. [d · básica]
¿Qué excepción lanza `"5" + 5`?

- A) `ValueError`
- B) `NameError`
- C) `ZeroDivisionError`
- D) `TypeError`

**Respuesta: D** — No se puede sumar un `str` con un `int`.

### 37. [d · básica]
¿Qué excepción lanza `10 / 0`?

- A) `OverflowError`
- B) `ZeroDivisionError`
- C) `TypeError`
- D) `IndexError`

**Respuesta: B** — División entre cero.

### 38. [d · básica]
En una traza (*traceback*) de Python, ¿dónde se indica el **tipo de error** y su motivo?

- A) En la primera línea.
- B) En la segunda línea.
- C) En la última línea.
- D) No se indica.

**Respuesta: C** — Se lee de abajo hacia arriba: la última línea dice qué ha fallado, y las anteriores, dónde.

### 39. [d · media]
¿Qué muestra este código?
```python
try:
    n = int("x")
    print("A")
except ValueError:
    print("B")
print("C")
```

- A) `A` y `C`
- B) `A`, `B` y `C`
- C) Solo `B`
- D) `B` y `C`

**Respuesta: D** — `int("x")` falla: se abandona el `try` sin mostrar `A`, se ejecuta el `except` (`B`) y el programa continúa (`C`).

### 40. [d · media]
¿Qué muestra este código?
```python
try:
    n = int("7")
except ValueError:
    print("error")
else:
    print("ok")
finally:
    print("fin")
```

- A) `ok` y `fin`
- B) `error` y `fin`
- C) Solo `ok`
- D) Solo `fin`

**Respuesta: A** — No hubo excepción, así que se ejecuta el `else`; el `finally` se ejecuta siempre.

### 41. [d · básica]
¿Cuándo se ejecuta el bloque `finally`?

- A) Solo si hay una excepción.
- B) Siempre, haya o no excepción.
- C) Solo si no hay excepción.
- D) Nunca, es opcional.

**Respuesta: B** — Se usa para tareas de limpieza que deben hacerse siempre (por ejemplo, cerrar un fichero).

### 42. [d · media]
¿Qué hace `raise ValueError("dato no válido")`?

- A) Captura una excepción de tipo `ValueError`.
- B) Ignora los errores del bloque anterior.
- C) Define un nuevo tipo de excepción.
- D) Lanza (provoca) una excepción de tipo `ValueError`.

**Respuesta: D** — `raise` genera la excepción; otra parte del programa podrá capturarla con `try` / `except`.

### 43. [d · media]
¿Por qué se desaconseja usar `except:` sin indicar el tipo de error?

- A) Provoca un `SyntaxError`.
- B) Hace el programa más lento.
- C) Captura cualquier error, incluso los inesperados, y puede ocultar fallos reales.
- D) No funciona desde la versión 3.10.

**Respuesta: C** — Es mejor capturar solo las excepciones que sabemos tratar.

### 44. [d · media]
¿Qué estructura es la habitual para pedir un dato hasta que el usuario lo escriba correctamente?

- A) `while True` + `try` / `except` + `break`.
- B) `for i in range(1)`.
- C) Un `if` / `else`.
- D) Un `match`.

**Respuesta: A** — El bucle repite la pregunta y el `break` (tras una conversión correcta) lo termina.

### 45. [d · media]
¿Qué excepción lanza `assert edad >= 0, "Edad negativa"` si `edad` vale `-1`?

- A) `ValueError`
- B) `AssertionError`
- C) `TypeError`
- D) Ninguna.

**Respuesta: B** — `assert` lanza `AssertionError` con el mensaje indicado cuando la condición es falsa.

### 46. [d · avanzada]
El usuario escribe `4.5`. ¿Qué muestra este código?
```python
try:
    a = int(input())
except ZeroDivisionError:
    print("A")
except ValueError:
    print("B")
```

- A) `A`
- B) Nada: el programa termina con un error.
- C) `A` y `B`
- D) `B`

**Respuesta: D** — `int("4.5")` lanza `ValueError`, que es el que captura el segundo `except`.

### 47. [d · media]
¿Qué significa `except (ValueError, TypeError):`?

- A) Se capturan ambos errores a la vez.
- B) Solo se captura el primero.
- C) Se captura cualquiera de los dos tipos de error.
- D) Es un error de sintaxis.

**Respuesta: C** — Los paréntesis agrupan varios tipos; el bloque se ejecuta si ocurre cualquiera de ellos.

### 48. [d · media]
En el depurador de VS Code, ¿qué hace la tecla `F10`?

- A) Continúa la ejecución hasta el siguiente punto de interrupción.
- B) Ejecuta la línea actual sin entrar en las funciones que llame (*paso por encima*).
- C) Detiene la depuración.
- D) Reinicia el programa.

**Respuesta: B** — `F11` entra dentro de las funciones y `F5` continúa.

---

## Hoja de respuestas

| Nº | Apt. | Dificultad | Resp. | Nº | Apt. | Dificultad | Resp. |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | a | básica | **D** | 25 | b | media | **C** |
| 2 | a | básica | **A** | 26 | b | básica | **A** |
| 3 | a | media | **C** | 27 | c | básica | **D** |
| 4 | a | media | **B** | 28 | c | básica | **B** |
| 5 | a | básica | **A** | 29 | c | media | **A** |
| 6 | a | media | **D** | 30 | c | media | **C** |
| 7 | a | básica | **B** | 31 | c | básica | **B** |
| 8 | a | media | **C** | 32 | c | avanzada | **D** |
| 9 | a | media | **C** | 33 | c | media | **A** |
| 10 | a | avanzada | **A** | 34 | d | media | **C** |
| 11 | a | media | **B** | 35 | d | básica | **A** |
| 12 | a | media | **D** | 36 | d | básica | **D** |
| 13 | b | básica | **B** | 37 | d | básica | **B** |
| 14 | b | básica | **D** | 38 | d | básica | **C** |
| 15 | b | básica | **A** | 39 | d | media | **D** |
| 16 | b | media | **C** | 40 | d | media | **A** |
| 17 | b | media | **D** | 41 | d | básica | **B** |
| 18 | b | media | **B** | 42 | d | media | **D** |
| 19 | b | básica | **A** | 43 | d | media | **C** |
| 20 | b | media | **C** | 44 | d | media | **A** |
| 21 | b | avanzada | **B** | 45 | d | media | **B** |
| 22 | b | media | **D** | 46 | d | avanzada | **D** |
| 23 | b | media | **A** | 47 | d | media | **C** |
| 24 | b | media | **C** | 48 | d | media | **B** |
