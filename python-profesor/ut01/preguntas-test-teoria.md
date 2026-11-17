# UT01 · Preguntas tipo test de teoría (con trampa)

Identificación de los elementos de un programa informático · 31 preguntas de 4 opciones (una correcta).

Las preguntas están agrupadas por **criterio de evaluación** y completan lo que no cubren `preguntas-test.md` y `preguntas-test-ejercicios.md`. Se mezclan preguntas que piden la opción correcta con otras que piden la **INCORRECTA**, y algunas incluyen «todas son correctas» o «ninguna es correcta». Tras cada respuesta se indica la trampa.

| Criterio de evaluación | Preguntas |
|---|---|
| a) Bloques que componen la estructura de un programa | 1 – 5 |
| b) Creación de proyectos de desarrollo | 6 – 8 |
| c) Uso de entornos integrados de desarrollo | 9 – 10 |
| d) Tipos de variables y utilidad de cada uno | 11 – 16 |
| e) Modificación de código para crear y utilizar variables | 17 – 20 |
| f) Constantes, literales y operadores | 21 – 26 |
| g) Conversiones de tipo explícitas e implícitas | 27 – 29 |
| h) Comentarios en el código | 30 – 31 |

---

## a) Bloques que componen la estructura de un programa

### 1. [a · media]
Sobre los lenguajes compilados e interpretados, ¿cuál de estas afirmaciones es **INCORRECTA**?

- A) Un compilador traduce el programa entero antes de ejecutarlo y genera un archivo ejecutable.
- B) El intérprete de Python traduce y ejecuta el programa línea a línea.
- C) Los programas compilados suelen ejecutarse más rápido.
- D) Al ejecutar un programa de Python se genera un ejecutable que después funciona sin intérprete.

**Respuesta: D** — En un lenguaje interpretado no se genera ningún archivo: hace falta el intérprete cada vez que se ejecuta el programa.

> **Trampa:** la C parece una ventaja exagerada de los compilados, pero es cierta.

### 2. [a · media]
¿Cuál de estas afirmaciones sobre un **algoritmo** es correcta?

- A) Tiene que terminar en un número finito de pasos, por complejo que sea el problema.
- B) Sus pasos pueden ser ambiguos si quien programa los entiende.
- C) Se escribe siempre directamente en un lenguaje de programación.
- D) Ninguna es correcta.

**Respuesta: A** — Un algoritmo son pasos ordenados, precisos y **finitos**. Puede escribirse en lenguaje natural o en pseudocódigo; cuando se escribe en un lenguaje de programación, es un programa.

> **Trampa:** la C confunde algoritmo con programa.

### 3. [a · media]
¿Cuáles de estos identificadores son válidos?

```text
If      _total      nota2
```

- A) Solo `nota2`.
- B) `_total` y `nota2`.
- C) Solo `_total`.
- D) Los tres.

**Respuesta: D** — `If` no es la palabra reservada `if`, porque Python distingue mayúsculas de minúsculas. `_total` puede empezar por guion bajo y `nota2` lleva el dígito al final.

> **Trampa:** `If` «suena» a palabra reservada, y el guion bajo inicial parece prohibido.

### 4. [a · avanzada]
Sobre la estructura de un programa en Python, ¿cuál de estas afirmaciones es **INCORRECTA**?

- A) Las sentencias se ejecutan de arriba abajo, una tras otra.
- B) Las líneas de un mismo bloque pueden tener tabulados distintos, siempre que estén más a la derecha que la línea de los dos puntos.
- C) No hace falta poner punto y coma al final de cada sentencia.
- D) Dentro de unos paréntesis, una sentencia puede continuar en la línea siguiente.

**Respuesta: B** — Todas las líneas de un bloque deben tener **el mismo** sangrado; si no, se produce un `IndentationError`.

> **Trampa:** la B tiene una parte cierta (el bloque va más a la derecha) que esconde el error.

### 5. [a · media]
Un programa calcula el precio de un producto después de aplicarle un descuento. ¿Qué acción corresponde a la fase de **prueba**?

- A) Escribir el código en Python.
- B) Decidir qué datos entran y qué resultado sale.
- C) Ejecutarlo con varios datos distintos y comprobar los resultados.
- D) Ejecutarlo una vez con el ejemplo del enunciado: si el resultado coincide, el programa es correcto.

**Respuesta: C** — Hay que probar con **varios** datos, incluidos casos extremos. A es codificación y B es análisis.

> **Trampa:** la D es lo que se suele hacer, pero un solo ejemplo no demuestra que el programa funcione.

---

## b) Creación de proyectos de desarrollo

### 6. [b · media]
Sobre la consola de Python, ¿cuál de estas afirmaciones es **INCORRECTA**?

- A) Lo que escribes se guarda automáticamente en un archivo `.py` de la carpeta actual.
- B) Se abre escribiendo `python` en una terminal.
- C) Muestra el símbolo `>>>` cuando espera una instrucción.
- D) `help()` muestra la ayuda sin necesidad de internet.

**Respuesta: A** — Lo que escribes en el REPL **no se guarda**. Para conservar un programa hay que escribirlo en un archivo `.py`.

> **Trampa:** como la consola se abre desde una carpeta, parece que guarda en ella.

### 7. [b · avanzada]
Un cuaderno de Jupyter tiene tres celdas:

```python
# Celda 1
descuento = 10
```

```python
# Celda 2
descuento = 25
```

```python
# Celda 3
print(descuento)
```

Las ejecutas en este orden: celda 2, celda 1 y celda 3. ¿Qué muestra la celda 3?

- A) `10`
- B) `25`
- C) `NameError`
- D) `35`

**Respuesta: A** — El cuaderno guarda las variables según el **orden de ejecución**. La última asignación ejecutada fue la de la celda 1.

> **Trampa:** leer las celdas en el orden de la página lleva a responder 25.

### 8. [b · media]
¿Qué lista contiene **solo** fases del desarrollo de un programa?

- A) Análisis, compilación y prueba.
- B) Análisis, diseño y mantenimiento.
- C) Diseño, ejecución y documentación.
- D) Codificación, interpretación y prueba.

**Respuesta: B** — Las fases son análisis, diseño, codificación, prueba, documentación y mantenimiento. Compilación, ejecución e interpretación no son fases de desarrollo.

> **Trampa:** cada opción incorrecta tiene dos fases ciertas y una palabra que «suena» a programar; el mantenimiento se olvida con facilidad.

---

### 9. [c · avanzada]
VS Code subraya en amarillo una línea de tu programa. ¿Cuál de estas afirmaciones es correcta?

- A) El programa no se podrá ejecutar hasta corregirla.
- B) Puede indicar algo que incumple el estilo o un posible problema; el programa puede ejecutarse igualmente.
- C) Significa que esa línea ya se ha ejecutado.
- D) Ninguna es correcta.

**Respuesta: B** — El subrayado es un aviso del editor (con la extensión de Python), no un error de Python. Por ejemplo, avisa cuando no se cumple una anotación de tipo, y el programa se ejecuta igual.

> **Trampa:** asociar cualquier subrayado con «no compila».

### 10. [c · media]
En la consola de Python has escrito `help(round)` y se muestra la ayuda. ¿Qué haces para volver al símbolo `>>>`?

- A) Escribir `exit()`.
- B) Pulsar `Ctrl+Z` y después Enter.
- C) Pulsar la tecla `q`.
- D) Ninguna: hay que cerrar la terminal y abrirla otra vez.

**Respuesta: C** — La `q` sale de la ayuda y vuelve a la consola. `exit()` y `Ctrl+Z` + Enter sirven para salir de la **consola**, no de la ayuda.

> **Trampa:** confundir salir de la ayuda con salir de la consola.

---

## d) Tipos de variables y utilidad de cada uno

### 11. [d · media]
¿Para cuál de estos datos es más adecuado el tipo `str`?

- A) Un número de teléfono.
- B) El número de alumnos matriculados.
- C) El año de nacimiento.
- D) La planta de un edificio (puede ser `-1` para el sótano).

**Respuesta: A** — Con un teléfono no se hacen cálculos y puede llevar prefijo o ceros iniciales. Los otros tres son `int`; la planta también, aunque sea negativa.

> **Trampa:** el teléfono «es un número» y la planta negativa parece un caso raro.

### 12. [d · avanzada]
Sobre los tipos de datos, ¿cuál de estas afirmaciones es **INCORRECTA**?

- A) `5` y `5.0` son de tipos distintos.
- B) El resultado de `9 / 3` es de tipo `int`, porque la división es exacta.
- C) En una operación, `True` vale 1.
- D) `"25"` es de tipo `str`, aunque parezca un número.

**Respuesta: B** — `/` devuelve **siempre** `float`: `9 / 3` es `3.0`.

> **Trampa:** «la división es exacta» parece una buena razón para que salga un entero.

### 13. [d · avanzada]
Sobre la inmutabilidad, ¿cuál de estas afirmaciones es **INCORRECTA**?

- A) Al ejecutar `x += 1`, el número que había en memoria se modifica.
- B) Los tipos `int`, `float`, `bool` y `str` son inmutables.
- C) Tras `x = x + 1`, `id(x)` devuelve un valor distinto al de antes.
- D) Una cadena no se puede modificar carácter a carácter.

**Respuesta: A** — Python crea un objeto **nuevo** con el resultado y hace que `x` apunte a él; el número original no cambia.

> **Trampa:** como el valor de `x` cambia, parece que cambia el objeto.

### 14. [d · media]
¿Qué pareja dato–tipo es la adecuada?

- A) Precio de un ratón, `12.99` → `int`
- B) ¿Está encendido el servidor? → `str` con el valor `"sí"`
- C) Temperatura de la CPU, `67.5` → `float`
- D) Matrícula de un coche, `1234ABC` → `int`

**Respuesta: C** — Una medida con decimales es `float`. El precio también necesita `float`, el «sí/no» es un `bool` y la matrícula, que lleva letras, un `str`.

> **Trampa:** la B funciona en la práctica, pero para un dato de sí o no el tipo adecuado es `bool`.

### 15. [d · avanzada]
Sobre el ámbito y el ciclo de vida de las variables, ¿cuál de estas afirmaciones es correcta?

- A) Una variable local sigue existiendo cuando termina su función, hasta que se cierra el programa.
- B) Antes de asignar un valor a una variable hay que declararla con su tipo.
- C) Todas son correctas.
- D) Una variable creada fuera de cualquier función es global y se puede usar en todo el programa.

**Respuesta: D** — Una local solo existe mientras se ejecuta su función y en Python las variables no se declaran: nacen al asignarles un valor. Como A y B son falsas, la C tampoco es correcta.

> **Trampa:** la A es cierta para las globales, no para las locales.

### 16. [d · media]
Sobre las anotaciones de tipo, por ejemplo `curso: int = 1`, ¿cuál de estas afirmaciones es **INCORRECTA**?

- A) Ayudan a quien lee el código a saber qué tipo se espera.
- B) Si el valor no cumple la anotación, Python detiene el programa con un error.
- C) VS Code puede avisar cuando el valor no encaja con la anotación.
- D) Son una forma de documentación.

**Respuesta: B** — Python **no** las comprueba al ejecutar; solo el editor avisa.

> **Trampa:** la C (el editor avisa) hace pensar que Python también lo impide.

---

## e) Modificación de código para crear y utilizar variables

### 17. [e · media]
Se quiere que el programa muestre `Total: 30`. ¿Qué modificación **NO** funciona en el lugar del comentario?

```python
unidades = 3
precio = 10
# aquí
```

- A) `unidades * precio = total` y `print("Total:", total)`
- B) `total = unidades * precio` y `print("Total:", total)`
- C) `print("Total:", unidades * precio)`
- D) `unidades *= precio` y `print("Total:", unidades)`

**Respuesta: A** — La variable va a la **izquierda** del `=`; escrita así da `SyntaxError`. La D funciona, aunque cambia el valor de `unidades`.

> **Trampa:** la D parece la incorrecta porque «estropea» `unidades`, pero muestra `Total: 30`.

### 18. [e · media]
¿Qué muestra este programa?

```python
visitas = 0
visitas + 1
visitas += 2
print(visitas)
```

- A) `3`
- B) `1`
- C) `2`
- D) `0`

**Respuesta: C** — La segunda línea calcula `1`, pero no lo guarda en ninguna variable. Solo `visitas += 2` cambia su valor.

> **Trampa:** leer `visitas + 1` como si sumara y responder 3.

### 19. [e · avanzada]
¿Qué ocurre al ejecutar este programa?

```python
total_compra = 40
gastos_envio = 5
print(total_compra + gastos_envío)
```

- A) Muestra `45`.
- B) `NameError`, porque `gastos_envío` y `gastos_envio` son nombres distintos.
- C) `SyntaxError`, porque los nombres de variable no pueden llevar tildes.
- D) Muestra `40`, porque la variable con tilde vale 0.

**Respuesta: B** — La tilde de la última línea crea un nombre distinto, que no existe. Se arregla escribiendo `gastos_envio` sin tilde.

> **Trampa:** la C parece lógica, pero Python **sí** admite tildes en los nombres; se evitan porque provocan errores como este.

### 20. [e · avanzada]
Este programa muestra `11.0` cuando la media debería ser `7.0`:

```python
nota_teoria = 8
nota_practica = 6
media = nota_teoria + nota_practica / 2
```

¿Qué modificación **NO** lo arregla?

- A) `media = (nota_teoria + nota_practica) / 2`
- B) `suma = nota_teoria + nota_practica` y `media = suma / 2`
- C) `media = nota_teoria / 2 + nota_practica / 2`
- D) `media = (nota_teoria + nota_practica / 2)`

**Respuesta: D** — El paréntesis rodea toda la expresión, pero dentro sigue dividiéndose antes que sumarse: el resultado sigue siendo `11.0`.

> **Trampa:** la C parece incorrecta y es válida (4 + 3 = 7.0); la D «tiene paréntesis» y parece la solución.

---

### 21. [f · avanzada]
¿Cuánto vale `0o20 + 0b11`?

- A) `31`
- B) `19`
- C) `35`
- D) Ninguna es correcta: da `SyntaxError`.

**Respuesta: B** — `0o20` en octal es 16 y `0b11` en binario es 3: 16 + 3 = 19.

> **Trampa:** la A suma las cifras como si fueran decimales (20 + 11) y la C lee `0o20` como hexadecimal (32 + 3).

### 22. [f · avanzada]
¿Cuántas líneas muestra este `print`?

```python
print("Router\tA\nRouter\\nB")
```

- A) 1
- B) 3
- C) Da error.
- D) Ninguna de las anteriores es correcta.

**Respuesta: D** — Muestra **2** líneas: `\t` es un tabulador, `\n` un salto de línea y `\\n` es una barra invertida seguida de la letra `n`, no un salto.

> **Trampa:** contar los dos `\n` y responder 3.

### 23. [f · media]
¿Cuál de estos nombres es una constante del módulo `math`?

- A) `math.e`
- B) Ninguna
- C) `math.inf`
- D) Todas lo son.

**Respuesta: D** — `math.e` es el número de Euler y `math.inf` es el infinito positivo.

> **Trampa:** solo se recuerda `math.pi` y se descartan las demás.

### 24. [f · avanzada]
Según la regla práctica de los «números mágicos», ¿qué números de este programa conviene convertir en constantes?

```python
horas = float(input("Horas: "))
sueldo = horas * 11.5
extra = sueldo * 0.15
total = sueldo + extra
print(total)
```

- A) Ninguno: cada número aparece una sola vez.
- B) Solo `11.5`.
- C) `11.5` y `0.15`.
- D) Solo `0.15`.

**Respuesta: C** — Los dos tienen un significado propio (precio por hora y porcentaje extra), aunque aparezcan una sola vez: `PRECIO_HORA = 11.5` y `PORCENTAJE_EXTRA = 0.15`.

> **Trampa:** la regla dice «se repite **o** tiene un significado propio»; la A solo se fija en la repetición.

### 25. [f · avanzada]
¿Qué muestra `print(0 and 5 / 0)`?

- A) `ZeroDivisionError`
- B) `False`
- C) `0`
- D) `None`

**Respuesta: C** — Por el cortocircuito, `and` no evalúa la división, porque `0` ya es falso, y devuelve **el propio operando**: `0`.

> **Trampa:** dos a la vez: creer que se calcula `5 / 0` (A) y que `and` siempre devuelve `True` o `False` (B).

### 26. [f · avanzada]
¿Qué muestra `print(not 3 > 5 and 2 == 2.0)`?

- A) `True`
- B) `False`
- C) `TypeError`
- D) `None`

**Respuesta: A** — La comparación va antes que `not`: `not (3 > 5)` es `True`. Además, `2 == 2.0` es `True`, porque se comparan valores. `True and True` da `True`.

> **Trampa:** aplicar `not` solo al `3`, o pensar que `2` y `2.0` no son iguales por ser de tipos distintos.

---

## g) Conversiones de tipo explícitas e implícitas

### 27. [g · avanzada]
¿Cuál de estas operaciones da un resultado de tipo `int`?

- A) `7 / 7`
- B) `True + 0.5`
- C) `9 // 2`
- D) `2 * 1.0`

**Respuesta: C** — La división entera de dos enteros da `int` (`4`). En las demás hay un `float` o una división `/`, y el resultado es `float`.

> **Trampa:** `7 / 7` da un número «redondo» (`1.0`) y parece un entero.

### 28. [g · avanzada]
¿Cuál de estas expresiones **NO** produce ningún error?

- A) `int("7") + 3.5`
- B) `int("siete")`
- C) `"7" + 3`
- D) `float("7,5")`

**Respuesta: A** — `int("7")` da `7`, y `7 + 3.5` se convierte de forma implícita en `10.5`. B y D dan `ValueError` y C da `TypeError`.

> **Trampa:** la A mezcla texto, entero y decimal, y parece la más peligrosa.

### 29. [g · media]
¿Qué valores dan, en este orden, `int(-4.6)`, `round(-4.6)`?

- A) `-4`, `-4`
- B) `-5`, `-5`
- C) `-4`, `-5`,
- D) Ninguna de las anteriores es correcta.

**Respuesta: C** — Dan `-4` y `-5`. `int()` corta los decimales y `round()` redondea al entero más cercano.

> **Trampa:** pensar que `int()` y `round()` hacen lo mismo (opciones A y B).


---

## h) Comentarios en el código

### 30. [h · avanzada]
Sobre los comentarios, ¿cuál de estas afirmaciones es **INCORRECTA**?

- A) Un texto entre triples comillas que no se asigna a nada es el comentario de bloque de Python.
- B) Python ignora todo lo que va después de `#` hasta el final de la línea.
- C) Para comentar varias líneas se pone un `#` en cada una.
- D) Ninguna es incorrecta

**Respuesta: A** — Python no tiene comentarios de bloque. Las triples comillas sueltas son una cadena que no se usa, y por convención se reservan para los docstrings.

> **Trampa:** se usa mucho así y funciona, por eso parece un comentario oficial.

### 31. [h · media]
¿Cuál de estas es una buena práctica al comentar el código?

- A) Comentar cada línea, aunque sea obvia: `x = 5  # x vale 5`.
- B) Dejar comentados los bloques de código antiguos por si vuelven a hacer falta.
- C) Explicar en el comentario por qué se ha tomado una decisión que no es evidente.
- D) Ninguna de las anteriores.

**Respuesta: C** — El comentario debe explicar el **porqué**; el qué ya lo dice el código. El código comentado «por si acaso» ensucia el programa y acaba desactualizado.

> **Trampa:** la B parece una medida prudente y la A, una muestra de buen trabajo.
---

## Hoja de respuestas

| Nº | Crit. | Dificultad | Resp. | Nº | Crit. | Dificultad | Resp. |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | a | media | **D** | 17 | e | media | **A** |
| 2 | a | media | **A** | 18 | e | media | **C** |
| 3 | a | media | **D** | 19 | e | avanzada | **B** |
| 4 | a | avanzada | **B** | 20 | e | avanzada | **D** |
| 5 | a | media | **C** | 21 | f | avanzada | **B** |
| 6 | b | media | **A** | 22 | f | avanzada | **D** |
| 7 | b | avanzada | **A** | 23 | f | media | **D** |
| 8 | b | media | **B** | 24 | f | avanzada | **C** |
| 9 | c | avanzada | **B** | 25 | f | avanzada | **C** |
| 10 | c | media | **C** | 26 | f | avanzada | **A** |
| 11 | d | media | **A** | 27 | g | avanzada | **C** |
| 12 | d | avanzada | **B** | 28 | g | avanzada | **A** |
| 13 | d | avanzada | **A** | 29 | g | media | **C** |
| 14 | d | media | **C** | 30 | h | avanzada | **A** |
| 15 | d | avanzada | **D** | 31 | h | media | **C** |
| 16 | d | media | **B** |  |  |  |  |
