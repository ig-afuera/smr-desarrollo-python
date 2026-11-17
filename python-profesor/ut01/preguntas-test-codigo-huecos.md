# UT01 · Test sobre un código con huecos

Identificación de los elementos de un programa informático · 50 preguntas de 4 opciones (una correcta).

Todas las preguntas se hacen sobre **el mismo programa**, que tiene **8 huecos**. Hay tres tipos de pregunta:

| Tipo | Qué se pide | Preguntas |
|---|---|---|
| **Completa** | Las opciones son líneas de código: elige la que cumple lo que pide el enunciado. | 1 – 18 |
| **¿Qué pasa si...?** | El enunciado propone una línea o un cambio: elige qué ocurre. | 19 – 35 |
| **Sobre una línea** | Pregunta sobre una línea concreta del programa. | 36 – 50 |

---

## El programa

Una sala de juegos en red cobra por **bloques de 15 minutos** (un bloque empezado se cobra entero). Los clientes con bono tienen un 20 % de descuento.

```python
 1  """Ticket de una sala de juegos en red.
 2
 3  Calcula lo que paga un jugador según los minutos jugados.
 4  """
 5  import math
 6
 7  PRECIO_BLOQUE = 1.25      # euros por cada bloque de 15 minutos
 8  MINUTOS_BLOQUE = 15
 9  DESCUENTO_BONO = 0.2
10  LIMITE_SESION = 180       # minutos seguidos sin descanso
11
12  jugador = input("Nick: ")
13  minutos = «HUECO 1»
14  puesto = input("Puesto (hexadecimal): ")
15  numero_puesto = «HUECO 2»
16  tiene_bono = input("¿Bono? (s/n): ") == "s"
17
18  bloques = minutos // MINUTOS_BLOQUE
19  sobrante = «HUECO 3»
20  bloques += sobrante > 0
21
22  importe = bloques * PRECIO_BLOQUE
23  «HUECO 4»
24  descanso = «HUECO 5»
25  nick_valido = " " not in jugador and len(jugador) >= 3
26
27  print(f"Jugador: «HUECO 6»")
28  print(f"Puesto: {numero_puesto:03d}")
29  print(f"Tiempo: {minutos // 60}h {minutos % 60:02d}min")
30  print(f"Bloques: {bloques}")
31  print(f"Importe: «HUECO 7» €")
32  print("Redondeado:", «HUECO 8», "€")
33  print("Descanso obligatorio:", descanso)
34  print("Nick válido:", nick_valido)
```

**Qué debe hacer cada hueco**

| Hueco | Línea | Debe... |
|:---:|:---:|---|
| 1 | 13 | Pedir los minutos jugados y guardarlos como número **entero**. |
| 2 | 15 | Convertir el puesto, que el usuario teclea en **hexadecimal** (por ejemplo `1A`), en un número entero. |
| 3 | 19 | Calcular los minutos que **no llegan** a completar un bloque. |
| 4 | 23 | Aplicar el descuento del bono **solo** si el jugador tiene bono, sin usar `if`. |
| 5 | 24 | Valer `True` cuando los minutos **superan** el límite de sesión, salvo que el jugador tenga bono. |
| 6 | 27 | Mostrar el nick **centrado** en 12 caracteres. |
| 7 | 31 | Mostrar el importe con **2 decimales**. |
| 8 | 32 | Mostrar el importe redondeado **siempre hacia arriba** al euro (usando el módulo `math`). |

**Datos de referencia.** Salvo que la pregunta diga otra cosa, el usuario teclea: nick `Kira`, minutos `100`, puesto `1A` y bono `s`, y todos los huecos están bien resueltos.

---

## Bloque 1 · Completa

### 1. [hueco 1 · básica]
¿Qué línea va en el **hueco 1**?

- A) `input("Minutos: ")`
- B) `float(input("Minutos: "))`
- C) `int(input("Minutos: "))`
- D) `int("Minutos: ")`

**Respuesta: C** — `input()` devuelve siempre texto, así que hay que convertirlo con `int()`. A deja `"100"` como texto. B lo convierte, pero en `float` (`100.0`), no en entero. D intenta convertir el texto `"Minutos: "` en número (`ValueError`) y además no pide nada al usuario.

> **Trampa:** B «funciona» al leer, pero no cumple lo que pide el hueco: un número entero.

### 2. [hueco 2 · media]
¿Qué línea va en el **hueco 2** para que, si el usuario teclea `1A`, `numero_puesto` valga `26`?

- A) `int(puesto)`
- B) `hex(puesto)`
- C) `int("puesto", 16)`
- D) `int(puesto, 16)`

**Respuesta: D** — `int(texto, base)` convierte un texto escrito en otra base a entero. A da `ValueError`: sin base, `"1A"` no es un número válido. B hace lo contrario (de número a texto hexadecimal) y, como `puesto` es un `str`, da `TypeError`. C convierte el texto literal `"puesto"`, no la variable: `ValueError`.

> **Trampa:** C se diferencia de la correcta solo en las comillas. Y B «suena» a hexadecimal, pero va en sentido contrario.

### 3. [hueco 3 · básica]
¿Qué línea va en el **hueco 3**?

- A) `minutos % MINUTOS_BLOQUE`
- B) `minutos // MINUTOS_BLOQUE`
- C) `minutos / MINUTOS_BLOQUE`
- D) `MINUTOS_BLOQUE % minutos`

**Respuesta: A** — El resto de la división (`%`) son los minutos que sobran tras completar bloques: `100 % 15` = 10. B da el cociente (6, los bloques completos), C da `6.666...` y D tiene los operandos al revés: `15 % 100` = 15.

> **Trampa:** D tiene el operador correcto, pero el orden de los operandos importa.

### 4. [hueco 3 · avanzada]
¿Que linea va en el hueco 3?

- A) `minutos - bloques`
- B) `minutos - MINUTOS_BLOQUE`
- C) `minutos - bloques * MINUTOS_BLOQUE`
- D) `(minutos - bloques) * MINUTOS_BLOQUE`

**Respuesta: C** — En la línea 19 `bloques` todavía vale 6 (la línea 20 aún no se ha ejecutado). `6 * 15` = 90 minutos completos, y `100 - 90` = 10. Por precedencia, `*` se calcula antes que `-`. A da 94, B da 85 y D da `94 * 15` = 1410.

> **Trampa:** hay que fijarse en qué vale `bloques` **en ese momento** y en que la multiplicación va antes que la resta.

### 6. [hueco 4 · avanzada]
¿Cuál de estas líneas es **otra forma válida** de resolver el **hueco 4**?

- A) `importe -= importe * (DESCUENTO_BONO or tiene_bono)`
- B) `importe =- importe * DESCUENTO_BONO * tiene_bono`
- C) `importe -= importe * DESCUENTO_BONO`
- D) `importe -= importe * DESCUENTO_BONO * tiene_bono`

**Respuesta: D** — Con bono resta `importe * 0.2 * 1` (el 20 %); sin bono resta `importe * 0.2 * 0` = 0. A: `0.2 or tiene_bono` devuelve siempre `0.2` (el primer operando es *truthy*), así que descuenta a todos. B no es `-=`: es `=` seguido de un signo menos, así que `importe` pasa a valer `-(importe * 0.2 * tiene_bono)`, un número negativo o cero. C descuenta a todos.

> **Trampa:** B tiene los mismos símbolos que D, pero en otro orden: `=-` asigna un valor negativo.

### 7. [hueco 5 · media]
¿Qué línea va en el **hueco 5**?

- A) `minutos > LIMITE_SESION and not tiene_bono`
- B) `minutos >= LIMITE_SESION and not tiene_bono`
- C) `minutos > LIMITE_SESION or not tiene_bono`
- D) `not minutos > LIMITE_SESION and tiene_bono`

**Respuesta: A** — Tienen que cumplirse las dos cosas (`and`): pasarse del límite y no tener bono. B también da `True` con 180 minutos exactos, que no **superan** el límite. C da `True` a cualquiera sin bono, aunque juegue 5 minutos. D se lee como `(not minutos > LIMITE_SESION) and tiene_bono`, porque `not` tiene menos prioridad que `>`: es justo lo contrario.

> **Trampa:** B solo falla en el caso límite (180 minutos), y es fácil pasarlo por alto.

### 8. [hueco 6 · básica]
¿Qué va en el **hueco 6**?

- A) `{jugador:>12}`
- B) `{"jugador":^12}`
- C) `{jugador:^12}`
- D) `{jugador:<12}`

**Respuesta: C** — `^` centra, `>` alinea a la derecha y `<` a la izquierda. B centra el **texto** `"jugador"`, no el valor de la variable: siempre mostraría la palabra «jugador».

> **Trampa:** B tiene el formato correcto, pero las comillas convierten la variable en un literal de cadena.

### 9. [hueco 7 · media]
¿Qué va en el **hueco 7**?

- A) `{round(importe, 2)}`
- B) `{importe:.2f}`
- C) `{importe:.2%}`
- D) `{importe:,}`

**Respuesta: B** — `:.2f` muestra siempre dos decimales: con los datos de referencia, `7.00`. A redondea el valor, pero no obliga a mostrar dos decimales: se ve `7.0`. C lo muestra como porcentaje (`700.00%`). D solo añade separador de miles (`7.0`).

> **Trampa:** A redondea a dos decimales, pero un número no «guarda» ceros finales: para mostrar `7.00` hace falta dar formato.

### 10. [hueco 8 · media]
¿Qué va en el **hueco 8**?

- A) `round(importe)`
- B) `math.floor(importe)`
- C) `int(importe)`
- D) `math.ceil(importe)`

**Respuesta: D** — `math.ceil()` redondea hacia arriba. Con un importe de `8.10`: A da 8 (redondea al más cercano), B da 8 (hacia abajo), C da 8 (trunca) y D da 9.

> **Trampa:** con los datos de referencia (importe `7.0`) las cuatro dan 7: hay que pensar en el caso general.

### 11. [línea 20 · avanzada]
¿Qué línea puede **sustituir a la línea 20** sin cambiar el resultado del programa?

- A) `bloques += bool(sobrante)`
- B) `bloques += bool("sobrante")`
- C) `bloques = bloques + sobrante > 0`
- D) `bloques += sobrante`

**Respuesta: A** — `bool(sobrante)` es `False` si `sobrante` es 0 y `True` en otro caso: suma 1 solo si hay minutos sueltos, igual que `sobrante > 0`. B convierte el texto `"sobrante"`, que no está vacío: siempre suma 1. C, por precedencia, calcula `(bloques + sobrante) > 0`, y `bloques` pasa a valer `True`. D suma los minutos sueltos (10), no un bloque.

> **Trampa:** en C, `+` tiene más prioridad que `>`, así que el resultado es un `bool` y no un número.

### 12. [línea 16 · avanzada]
Se quiere aceptar también la `S` mayúscula. La línea 16 se cambia por estas dos:

```python
respuesta = input("¿Bono? (s/n): ")
tiene_bono = ______
```

¿Qué va en el hueco para que `tiene_bono` sea `True` con `s` o con `S`, y `False` en cualquier otro caso?

- A) `respuesta == "s" or "S"`
- B) `respuesta == ("s" or "S")`
- C) `respuesta == "s" or respuesta == "S"`
- D) `respuesta == "s" and respuesta == "S"`

**Respuesta: C** — Hay que comparar `respuesta` con cada letra. A se lee como `(respuesta == "s") or "S"`: si el usuario escribe `n`, devuelve el texto `"S"`, no `False`. B: `"s" or "S"` vale `"s"`, así que solo acepta la minúscula. D nunca es `True`: un texto no puede ser `"s"` y `"S"` a la vez.

> **Trampa:** A se «lee» bien en castellano, pero `or` devuelve uno de sus operandos.

### 13. [línea 28 · media]
Se quiere que la línea 28 muestre el puesto en hexadecimal, en mayúsculas y sin prefijo (`Puesto: 1A`). ¿Qué va entre las llaves?

- A) `{numero_puesto:X}`
- B) `{hex(numero_puesto)}`
- C) `{numero_puesto:b}`
- D) `{numero_puesto:o}`

**Respuesta: A** — El formato `:X` muestra el número en hexadecimal con mayúsculas y sin prefijo. B muestra `0x1a` (con prefijo y en minúsculas). C lo muestra en binario (`11010`) y D en octal (`32`).

> **Trampa:** B es la función de hexadecimal, pero añade el prefijo `0x`.

### 14. [línea 25 · media]
Se quiere una variable `nick_escrito` que valga `True` solo si el jugador ha escrito **algo** como nick. ¿Qué línea lo consigue?

- A) `nick_escrito = bool("jugador")`
- B) `nick_escrito = jugador == " "`
- C) `nick_escrito = len(jugador) > 1`
- D) `nick_escrito = bool(jugador)`

**Respuesta: D** — El texto vacío `""` es *falsy* y cualquier otro texto es *truthy*. A convierte el literal `"jugador"`: siempre `True`. B solo es `True` si el nick es un espacio. C da `False` con un nick de una sola letra, que sí es algo escrito.

> **Trampa:** C parece correcta, pero exige al menos 2 caracteres.

### 15. [línea 12 · avanzada]
Si el usuario pulsa Enter sin escribir nada, el nick debe ser `"Invitado"`. ¿Qué línea sustituye a la 12?

- A) `jugador = input("Nick: ") and "Invitado"`
- B) `jugador = input("Nick: ") or "Invitado"`
- C) `jugador = "Invitado" or input("Nick: ")`
- D) `jugador = input("Nick: " or "Invitado")`

**Respuesta: B** — Si el texto está vacío (*falsy*), `or` devuelve el segundo operando, `"Invitado"`; si no, devuelve lo escrito. A hace lo contrario: con nick vacío da `""` y con nick escrito da `"Invitado"`. C devuelve siempre `"Invitado"` y, por el cortocircuito, ni siquiera llega a pedir el nick. D solo afecta al mensaje de la pregunta.

> **Trampa:** C tiene las mismas piezas que B; el orden decide qué se evalúa.

### 16. [constantes · básica]
El `60` de la línea 29 es un «número mágico». ¿Qué línea añadirías junto a las constantes, siguiendo la convención?

- A) `minutos_hora = 60`
- B) `MINUTOS_HORA = 60`
- C) `MINUTOS HORA = 60`
- D) `60_MINUTOS = 60`

**Respuesta: B** — Las constantes se escriben en MAYÚSCULAS, separando palabras con guion bajo. A funciona, pero por su nombre parece una variable. C tiene un espacio en el nombre y D empieza por un dígito: ninguno es un identificador válido.

> **Trampa:** A no da ningún error; lo que falla es la convención.

### 17. [nueva línea · básica]
Entre las líneas 27 y 28 se quiere mostrar una línea de 20 guiones. ¿Qué instrucción lo hace?

- A) `print("-" + 20)`
- B) `print("-", 20)`
- C) `print("-" * "20")`
- D) `print("-" * 20)`

**Respuesta: D** — `*` entre un texto y un número repite el texto. A intenta unir texto y número: `TypeError`. B muestra `- 20`. C multiplica dos textos: `TypeError`.

> **Trampa:** en C el 20 va entre comillas: es texto, no un número.

### 18. [nueva línea · media]
Al final del programa se quiere mostrar cuántos minutos le quedan al jugador hasta el límite (con los datos de referencia, `Quedan 80 min`). ¿Qué línea lo consigue?

- A) `print(f"Quedan {LIMITE_SESION - minutos} min")`
- B) `print("Quedan {LIMITE_SESION - minutos} min")`
- C) `print(f"Quedan {LIMITE_SESION} - {minutos} min")`
- D) `print("Quedan " + LIMITE_SESION - minutos + " min")`

**Respuesta: A** — Dentro de las llaves de una f-string se puede poner una expresión. B no tiene la `f`: muestra las llaves tal cual. C muestra `Quedan 180 - 100 min`: la resta queda fuera de las llaves. D intenta sumar un texto y un número: `TypeError`.

> **Trampa:** B solo se diferencia de A en una letra, la `f`.

---

## Bloque 2 · ¿Qué pasa si...?

### 19. [hueco 1 · media]
En el hueco 1 se escribe `input("Minutos: ")`. Con los datos de referencia, ¿qué ocurre?

- A) Funciona: `minutos` vale `"100"` y `bloques` vale 6.
- B) `ValueError` en la línea 13.
- C) `TypeError` en la línea 18.
- D) `TypeError` en la línea 13.

**Respuesta: C** — La línea 13 funciona: guarda el texto `"100"`. El error llega en la línea 18, al intentar `"100" // 15`: la división entera no admite un texto (`TypeError`).

> **Trampa:** el error no aparece donde está el fallo (línea 13), sino donde se usa el dato.

### 20. [hueco 1 · avanzada]
En el hueco 1 se escribe `float(input("Minutos: "))` y el usuario teclea `100.5`. ¿Cuánto vale `bloques` después de la línea 20?

- A) `7.0`
- B) `7`
- C) `6.7`
- D) `ValueError` en la línea 13.

**Respuesta: A** — `100.5 // 15` da `6.0`: la división entera de un `float` sigue siendo `float`. Sobran 10.5 minutos, así que se suma `True` (1): `7.0`.

> **Trampa:** se cuentan bien los bloques (7), pero el tipo se arrastra desde la línea 13.

### 21. [hueco 1 · media]
En el hueco 1 se escribe `int(float(input("Minutos: ")))` y el usuario teclea `90.9`. ¿Qué muestra la línea 30?

- A) `Bloques: 7`
- B) `Bloques: 6`
- C) `Bloques: 6.06`
- D) `ValueError` en la línea 13.

**Respuesta: B** — `float("90.9")` da `90.9` e `int()` lo **trunca** a 90. Son 6 bloques exactos y no sobra nada.

> **Trampa:** si se redondea en lugar de truncar, salen 91 minutos y 7 bloques.

### 22. [hueco 2 · básica]
Con el hueco 2 bien resuelto, el usuario teclea `ff` como puesto. ¿Qué muestra la línea 28?

- A) `Puesto: ff`
- B) `Puesto: 0ff`
- C) `Puesto: 255`
- D) `Puesto: 25`

**Respuesta: C** — `ff` en hexadecimal es 255. El formato `:03d` rellena con ceros **hasta** 3 cifras; si el número ya tiene 3, no añade nada ni lo recorta.

> **Trampa:** pensar que la línea 28 muestra el texto tecleado, o que `:03d` recorta a 3 cifras.

### 23. [hueco 2 · media]
En el hueco 2 se escribe `int(puesto, 8)` y el usuario teclea `17`. ¿Qué muestra la línea 28?

- A) `Puesto: 017`
- B) `Puesto: 015`
- C) `Puesto: 15`
- D) `ValueError`, porque `17` no es un número octal.

**Respuesta: B** — `17` en octal es 15 (1·8 + 7) y `:03d` lo rellena hasta 3 cifras: `015`.

> **Trampa:** C olvida el formato de la línea 28; A olvida el cambio de base.

### 24. [hueco 3 · avanzada]
En el hueco 3 se escribe `minutos / MINUTOS_BLOQUE` y el jugador juega 90 minutos. ¿Qué muestra la línea 30?

- A) `Bloques: 6`
- B) `Bloques: 6.0`
- C) `Bloques: 7`
- D) `TypeError`: no se puede sumar un `int` y un `bool`.

**Respuesta: C** — `sobrante` vale `6.0`, que es mayor que 0, así que se suma un bloque: 6 + 1 = 7. Se cobra un bloque de más aunque no ha sobrado ningún minuto.

> **Trampa:** con 100 minutos este error no se nota (también da 7). Solo aparece con un número exacto de bloques: por eso hay que probar con varios datos.

### 25. [hueco 4 · avanzada]
En el hueco 4 se escribe `importe *= 1 - DESCUENTO_BONO and tiene_bono`. El jugador juega 100 minutos y responde `n` al bono. ¿Cuánto vale `importe` después de la línea 23?

- A) `8.75`
- B) `0.0`
- C) `7.0`
- D) `TypeError`

**Respuesta: B** — La resta va antes que `and`: `(1 - 0.2) and False`. Como `0.8` es *truthy*, `and` devuelve el segundo operando, `False`. Después, `8.75 * False` = `8.75 * 0` = `0.0`. El jugador sin bono no paga nada.

> **Trampa:** con bono el resultado es `8.75` (no descuenta) y sin bono es `0.0` (gratis): justo al revés de lo que se quería.

### 26. [hueco 4 · media]
Con el hueco 4 bien resuelto, el jugador juega 100 minutos y responde `S` (mayúscula) al bono. ¿Cuánto vale `importe` después de la línea 23?

- A) `8.75`
- B) `7.0`
- C) `0.0`
- D) Se produce un error en la línea 16.

**Respuesta: A** — `"S" == "s"` es `False`: Python distingue mayúsculas de minúsculas. Sin bono no hay descuento: 7 bloques × 1.25 = `8.75`.

> **Trampa:** para una persona `S` y `s` significan lo mismo; para Python son textos distintos.

### 27. [hueco 5 · media]
Con el hueco 5 bien resuelto, el jugador juega exactamente 180 minutos y no tiene bono. ¿Qué muestra la línea 33?

- A) `Descanso obligatorio: True`
- B) `Descanso obligatorio: False`
- C) `Descanso obligatorio: 180`
- D) `Descanso obligatorio: 0`

**Respuesta: B** — El descanso es obligatorio cuando se **supera** el límite: `180 > 180` es `False`, y `False and ...` es `False`.

> **Trampa:** «llegar al límite» no es «superarlo».

### 28. [hueco 6 · avanzada]
En el hueco 6 se escribe `{jugador:>12}`. Con el nick `Kira`, ¿cuántos espacios hay en pantalla entre los dos puntos de `Jugador:` y la `K`?

- A) 8
- B) 12
- C) 1
- D) 9

**Respuesta: D** — `Kira` tiene 4 caracteres; alineado a la derecha en 12, lleva 8 espacios delante. Además, en la línea 27 ya hay un espacio escrito entre `Jugador:` y la llave: 1 + 8 = 9.

> **Trampa:** el espacio que hay en el propio texto de la f-string.

### 29. [hueco 8 · avanzada]
En el hueco 8 se escribe `round(importe)`. El jugador juega 30 minutos y no tiene bono. ¿Qué muestra la línea 32?

- A) `Redondeado: 3 €`
- B) `Redondeado: 2 €`
- C) `Redondeado: 2.5 €`
- D) `Redondeado:3€`

**Respuesta: B** — 30 minutos son 2 bloques: `importe` = 2.5. `round()` redondea los «medios» al **par** más cercano: `round(2.5)` es 2. `print()` separa cada dato con un espacio.

> **Trampa:** se espera que 2.5 suba a 3. D, además, olvida los espacios que pone `print()` entre los datos.

### 30. [línea 5 · media]
Con todos los huecos bien resueltos, se borra la línea 5. ¿Qué ocurre?

- A) El programa pide los datos y da `NameError` al llegar a la línea 32.
- B) El programa funciona igual, porque `math` está siempre disponible.
- C) El programa funciona igual, porque `math` solo se usa para redondear.
- D) `SyntaxError` en la línea 1, porque falta el `import`.

**Respuesta: A** — Sin `import math`, el nombre `math` no existe. El programa se ejecuta con normalidad hasta que lo usa, en el hueco 8: `NameError: name 'math' is not defined`.

> **Trampa:** el error no aparece al principio, sino en la primera línea que usa `math`.

### 31. [constantes · media]
En la línea 21 (que está vacía) se escribe `PRECIO_BLOQUE = 2`. ¿Qué ocurre?

- A) Error: una constante no se puede reasignar.
- B) Python ignora la línea porque el nombre está en mayúsculas.
- C) El programa se ejecuta sin errores y el importe se calcula a 2 € por bloque.
- D) `SyntaxError`, porque las constantes solo se pueden definir al principio.

**Respuesta: C** — Python no tiene constantes reales: las mayúsculas son solo una convención. La reasignación es válida y la línea 22 ya usa el nuevo valor.

> **Trampa:** A y D son cosas que **no se deben** hacer, pero Python las permite.

### 32. [línea 22 · media]
Se añaden 4 espacios al principio de la línea 22. ¿Qué ocurre?

- A) Nada: la sangría solo sirve para que el código se lea mejor.
- B) `IndentationError`.
- C) La línea 22 pasa a formar parte de la línea 20 y solo se ejecuta si sobran minutos.
- D) VS Code la subraya en amarillo, pero el programa se ejecuta igual.

**Respuesta: B** — Un bloque solo empieza tras una línea que termina en dos puntos `:`. La línea 20 no termina en `:`, así que sangrar la 22 es un error.

> **Trampa:** C «inventa» un bloque donde no lo hay.

### 33. [línea 25 · básica]
El jugador escribe `Neo` como nick. ¿Qué muestra la línea 34?

- A) `Nick válido: True`
- B) `Nick válido: False`
- C) `Nick válido: Neo`
- D) `TypeError` en la línea 25.

**Respuesta: A** — `Neo` no tiene espacios (`True`) y su longitud es 3, que cumple `>= 3` (`True`). `True and True` es `True`.

> **Trampa:** leer `>=` como `>` y pensar que hacen falta más de 3 letras.

### 34. [línea 30 · básica]
La línea 30 se cambia por `print("Bloques: " + bloques)`. ¿Qué ocurre?

- A) Muestra `Bloques: 7`.
- B) Muestra `Bloques:7`.
- C) `TypeError`.
- D) `ValueError`.

**Respuesta: C** — `+` entre un texto y un número no está permitido: Python nunca convierte un número en texto por su cuenta. Haría falta `str(bloques)`.

> **Trampa:** D: el problema no es el contenido del dato, sino que la operación no admite ese tipo.

### 35. [línea 20 · avanzada]
Justo después de la línea 20 se añade `print(type(bloques))`. Con los datos de referencia, ¿qué muestra?

- A) `<class 'bool'>`
- B) `<class 'float'>`
- C) `<class 'str'>`
- D) `<class 'int'>`

**Respuesta: D** — `bloques` era un `int` (6) y se le suma un `bool` (`True`). En una operación `bool` + `int` el resultado toma el tipo más amplio: `int`.

> **Trampa:** como en la línea 20 se suma una comparación, parece que `bloques` pasa a ser `bool`.

---

## Bloque 3 · Sobre una línea

### 36. [líneas 1–4 · básica]
¿Qué son las líneas 1 a 4?

- A) Un comentario de varias líneas que Python descarta al ejecutar.
- B) El docstring del módulo: documenta el programa y Python lo conserva.
- C) Un texto que se muestra en pantalla al ejecutar el programa.
- D) Un error, porque es una cadena que no se asigna a ninguna variable.

**Respuesta: B** — Una cadena entre triples comillas al principio del archivo es el docstring del módulo. A diferencia de un comentario, Python lo conserva y se puede consultar con `help()`.

> **Trampa:** A: las triples comillas no son un comentario, aunque a veces se usen como tal.

### 37. [línea 7 · media]
En la línea 7, ¿qué es `1.25`?

- A) Una constante de tipo `float`.
- B) Una variable de tipo `float`.
- C) Un literal de tipo `str`.
- D) Un literal de tipo `float`.

**Respuesta: D** — `1.25` es un valor escrito tal cual en el código: un literal. La constante es `PRECIO_BLOQUE`, el nombre que lo guarda.

> **Trampa:** A confunde el valor con el nombre de la constante.

### 38. [líneas 7–10 · básica]
¿Por qué los nombres de las líneas 7 a 10 están en MAYÚSCULAS?

- A) Para que Python impida cambiar su valor.
- B) Porque es obligatorio para las variables que se crean antes del primer `input()`.
- C) Para que sean variables globales.
- D) Es una convención para avisar de que su valor no debe cambiar.

**Respuesta: D** — Las mayúsculas son un aviso para las personas que leen el código. Python no las protege (A), no es una norma ligada a `input()` (B) y cualquier variable creada fuera de una función ya es global (C).

> **Trampa:** C es cierto que son globales, pero no **por** estar en mayúsculas.

### 39. [línea 16 · media]
¿De qué tipo es `tiene_bono`?

- A) `str`, porque `input()` siempre devuelve texto.
- B) Depende de lo que escriba el usuario.
- C) `bool`
- D) `int`

**Respuesta: C** — `input()` devuelve un `str`, pero la línea guarda el resultado de la comparación `== "s"`, que siempre es `True` o `False`.

> **Trampa:** A: es cierto que `input()` devuelve texto, pero no es lo que se guarda.

### 40. [línea 18 · básica]
Con los datos de referencia, ¿cuánto vale `bloques` justo después de la línea 18?

- A) `6.67`
- B) `7`
- C) `6.0`
- D) `6`

**Respuesta: D** — `100 // 15` es la división entera: 6. Entre dos `int` da un `int`.

> **Trampa:** B es el valor tras la línea 20, no tras la 18. C confunde `//` con `/`.

### 41. [línea 20 · media]
Antes de la línea 20, `bloques` vale 6 y `sobrante` vale 10. ¿Cuánto vale `bloques` después?

- A) `16`
- B) `True`
- C) `7`
- D) `TypeError`

**Respuesta: C** — Primero se calcula la derecha: `10 > 0` es `True`. Después `bloques += True` equivale a `bloques = 6 + True`, y `True` vale 1.

> **Trampa:** A suma `sobrante` en vez de la comparación; B cree que la comparación sustituye el valor.

### 42. [línea 25 · básica]
¿Qué tipo de operador es `not in` en la línea 25?

- A) De pertenencia.
- B) Lógico.
- C) De identidad.
- D) De comparación.

**Respuesta: A** — `in` y `not in` comprueban si un elemento está dentro de otro: aquí, si hay un espacio dentro del nick.

> **Trampa:** la palabra `not` hace pensar en un operador lógico.

### 43. [línea 25 · avanzada]
El jugador escribe `Ana Mar`. Al ejecutar la línea 25, ¿llega Python a calcular `len(jugador) >= 3`?

- A) Sí, Python siempre evalúa las dos partes de un `and`.
- B) Sí, porque `>=` tiene más prioridad que `and`.
- C) No: la primera parte es `False` y `and` ya no mira la segunda.
- D) No: la línea da error por el espacio del nick.

**Respuesta: C** — `" " not in "Ana Mar"` es `False`. Por la evaluación en cortocircuito, `and` ya sabe que el resultado es `False` y no evalúa la segunda parte.

> **Trampa:** B: la prioridad indica cómo se agrupa la expresión, no obliga a calcular la parte de la derecha.

### 44. [línea 28 · básica]
¿Qué indica `:03d` en la línea 28?

- A) Que se muestran 3 decimales.
- B) Que el número se muestra en octal con 3 cifras.
- C) Que se dejan 3 espacios a la izquierda.
- D) Que se muestra un entero rellenando con ceros a la izquierda hasta 3 cifras.

**Respuesta: D** — Con los datos de referencia, 26 se muestra como `026`.

> **Trampa:** el `0` inicial recuerda al prefijo de los literales octales (`0o`).

### 45. [línea 29 · media]
Con los datos de referencia, ¿qué muestra la línea 29?

- A) `Tiempo: 1h 40min`
- B) `Tiempo: 1.67h 40min`
- C) `Tiempo: 1h 4min`
- D) `Tiempo: 1h 40.0min`

**Respuesta: A** — `100 // 60` = 1 y `100 % 60` = 40. El formato `:02d` solo añade un cero si el número tiene una cifra; 40 ya tiene dos.

> **Trampa:** B usa `/`, y D cree que el resto es `float`.

### 46. [línea 33 · básica]
Con los datos de referencia, ¿qué muestra la línea 33?

- A) `Descanso obligatorio:False`
- B) `Descanso obligatorio: False`
- C) `Descanso obligatorio: 'False'`
- D) `Descanso obligatorio: True`

**Respuesta: B** — 100 minutos no superan el límite: `descanso` es `False`. `print()` separa los datos con un espacio y muestra los valores sin comillas.

> **Trampa:** A olvida el espacio que añade `print()`; C muestra el valor como si fuera un texto.

### 47. [línea 5 · media]
¿Por qué `import math` está en la línea 5 y no, por ejemplo, justo antes de la línea 32?

- A) Porque Python da error si el `import` no es la primera línea de código.
- B) Porque el docstring obliga a que el `import` vaya detrás.
- C) Porque PEP 8 recomienda poner los `import` al principio del archivo.
- D) Porque `math` solo funciona si se importa antes de definir las constantes.

**Respuesta: C** — Es una norma de estilo de PEP 8. Si se importara justo antes de la línea 32 el programa también funcionaría.

> **Trampa:** A, B y D convierten una recomendación de estilo en una obligación.

### 48. [línea 24 · media]
¿Qué tipo de variable es `descanso`?

- A) Local, porque se crea después de pedir los datos.
- B) Una constante, porque no cambia de valor después de la línea 24.
- C) Solo existe mientras se ejecuta la línea 24.
- D) Global.

**Respuesta: D** — Se crea fuera de cualquier función, así que es global y se puede usar en el resto del programa (como hace la línea 33).

> **Trampa:** A: que una variable sea local no depende de cuándo se crea, sino de que esté dentro de una función.

### 49. [línea 9 · media]
¿Qué literal podría sustituir a `0.2` en la línea 9 sin cambiar su valor?

- A) `2e1`
- B) `0.2e1`
- C) `2e-1`
- D) `.2e-1`

**Respuesta: C** — `2e-1` es 2 × 10⁻¹ = 0.2. A vale 20.0, B vale 2.0 y D vale 0.02.

> **Trampa:** el signo del exponente y el punto de D.

### 50. [línea 10 · avanzada]
¿Qué literal podría sustituir a `180` en la línea 10 sin cambiar su valor?

- A) `0x180`
- B) `0b1011`
- C) `0o226`
- D) `0xB4`

**Respuesta: D** — `0xB4` = 11 × 16 + 4 = 180. A vale 384, B vale 11 y C vale 150.

> **Trampa:** A contiene las mismas cifras que 180, pero en hexadecimal.

---

## Hoja de respuestas

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| C | D | A | C | B | D | A | C | B | D |

| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | C | A | D | B | B | D | A | C | A |

| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| B | C | B | C | B | A | B | D | B | A |

| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| C | B | A | C | D | B | D | D | C | D |

| 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| C | A | C | D | A | B | C | D | C | D |

**Solución completa de los huecos**

| Hueco | Línea correcta |
|:---:|---|
| 1 | `minutos = int(input("Minutos: "))` |
| 2 | `numero_puesto = int(puesto, 16)` |
| 3 | `sobrante = minutos % MINUTOS_BLOQUE` |
| 4 | `importe *= 1 - DESCUENTO_BONO * tiene_bono` |
| 5 | `descanso = minutos > LIMITE_SESION and not tiene_bono` |
| 6 | `print(f"Jugador: {jugador:^12}")` |
| 7 | `print(f"Importe: {importe:.2f} €")` |
| 8 | `print("Redondeado:", math.ceil(importe), "€")` |
