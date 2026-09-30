# Autoevaluación UT02

Comprueba **por ti mismo/a** si has entendido la unidad. Las soluciones están ocultas: **inténtalo primero** y despliégalas después.

!!! tip "Cómo usarla"
    1. Contesta las **preguntas** sin mirar los apuntes.
    2. Haz los **ejercicios** en VS Code o Jupyter y **ejecútalos** con varios datos de prueba (también con datos erróneos).
    3. Al final, haz el **proyecto de práctica** con el formato del examen: **sin internet y con un máximo de 1 hora**.

---

## Parte 1. Preguntas de repaso

### Pregunta 1
¿Qué diferencia hay entre escribir tres `if` seguidos y escribir un `if` / `elif` / `else`?

??? success "Solución"
    Con `if` separados, **cada condición se evalúa por su cuenta** y pueden ejecutarse varios bloques. Con `if` / `elif` / `else`, se evalúan en orden y **solo se ejecuta el primer bloque** cuya condición sea verdadera.

### Pregunta 2
¿Qué error da este código y por qué?
```python
x = 5
if x = 5:
    print("Cinco")
```

??? success "Solución"
    Da `SyntaxError`: se ha usado `=` (asignación) donde hace falta `==` (comparación). Lo correcto es `if x == 5:`.

### Pregunta 3
¿Qué valores toma `i` en `for i in range(2, 10, 3)`? ¿Cuántas vueltas da?

??? success "Solución"
    Toma los valores `2`, `5` y `8`. Da **3 vueltas** (el siguiente sería 11, que pasa del límite 10).

### Pregunta 4
Verdadero o falso: «`range(1, 10)` incluye el número 10».

??? success "Solución"
    **Falso**. El valor final **no se incluye**: `range(1, 10)` genera del 1 al 9.

### Pregunta 5
¿Cuándo usarías `while` y cuándo `for`?

??? success "Solución"
    `for` cuando sabes **cuántas veces** repetir o recorres una secuencia. `while` cuando repites **hasta que se cumpla algo** y no sabes cuántas vueltas harán falta (por ejemplo, hasta que el usuario teclee un dato válido).

### Pregunta 6
¿Qué muestra este código?
```python
for n in range(1, 8):
    if n % 2 == 0:
        continue
    if n > 5:
        break
    print(n)
```

??? success "Solución"
    Muestra `1`, `3` y `5` (cada uno en una línea).

    - Los pares se saltan con `continue`.
    - Con `n = 7`, no es par, pero `7 > 5` → se ejecuta `break` y el bucle termina sin imprimirlo.

### Pregunta 7
Para **sumar** valores en un bucle, el acumulador empieza en `0`. ¿En qué valor debe empezar si quieres **multiplicarlos**? ¿Por qué?

??? success "Solución"
    En `1`. El valor inicial no debe alterar el resultado: sumar `0` no cambia una suma y multiplicar por `1` no cambia un producto. Si empezara en `0`, el producto daría siempre `0`.

### Pregunta 8
¿Qué muestra este código?
```python
i = 10
while i > 0:
    i -= 3
print(i)
```

??? success "Solución"
    Muestra `-2`. Los valores de `i` son 10 → 7 → 4 → 1 → -2. Cuando `i` vale `-2`, la condición `i > 0` es falsa y el bucle termina.

### Pregunta 9
En un `try` / `except` / `finally`, ¿qué bloque se ejecuta **siempre**? ¿Se ejecuta el `finally` si se produce un error que ningún `except` captura?

??? success "Solución"
    `finally` se ejecuta siempre. Sí: aunque el error no se capture, el `finally` se ejecuta **antes** de que el programa se detenga y muestre la traza.

### Pregunta 10
¿Qué diferencia hay entre un error de sintaxis, una excepción y un error lógico?

??? success "Solución"
    - **Sintaxis**: el código está mal escrito; se detecta **antes** de ejecutar.
    - **Excepción**: el código es correcto pero algo falla **durante** la ejecución (`int("abc")`, `10 / 0`); se puede capturar con `try` / `except`.
    - **Lógico**: el programa se ejecuta sin errores pero **da un resultado equivocado**; Python no avisa, se detecta probando.

### Pregunta 11
¿Por qué no es recomendable escribir `except:` sin indicar el tipo de error?

??? success "Solución"
    Porque captura **cualquier** error, incluso los inesperados, y los esconde. Es mejor capturar solo los que sabes tratar (`except ValueError:`).

### Pregunta 12
En dos bucles anidados, ¿a qué bucle afecta un `break`?

??? success "Solución"
    Solo al **bucle más interno**, el que lo contiene. El bucle externo sigue su curso.

---

## Parte 2. Ejercicios

### Ejercicio 1. Signo y paridad
Pide un número entero y muestra si es **par o impar** y si es **positivo, negativo o cero**. Ejemplo: `-4 es par y negativo`.

??? success "Solución"
    ```python
    n = int(input("Número: "))

    if n > 0:
        signo = "positivo"
    elif n < 0:
        signo = "negativo"
    else:
        signo = "cero"

    paridad = "par" if n % 2 == 0 else "impar"

    print(f"{n} es {paridad} y {signo}")
    ```

### Ejercicio 2. El mayor de tres
Pide tres números y muestra cuál es el mayor (sin usar `max()`).

??? success "Solución"
    ```python
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    c = int(input("Tercer número: "))

    if a >= b and a >= c:
        mayor = a
    elif b >= c:
        mayor = b
    else:
        mayor = c

    print("El mayor es", mayor)
    ```

### Ejercicio 3. Calificación
Pide una nota entre 0 y 10 y muestra: *Sobresaliente* (9-10), *Notable* (7-8,99), *Bien* (6-6,99), *Suficiente* (5-5,99) o *Insuficiente* (menos de 5). Si la nota no está entre 0 y 10, muestra «Nota no válida».

??? success "Solución"
    ```python
    nota = float(input("Nota (0-10): "))

    if nota < 0 or nota > 10:
        print("Nota no válida")
    elif nota >= 9:
        print("Sobresaliente")
    elif nota >= 7:
        print("Notable")
    elif nota >= 6:
        print("Bien")
    elif nota >= 5:
        print("Suficiente")
    else:
        print("Insuficiente")
    ```
    Primero se descartan las notas no válidas y después se ordenan las condiciones de la más restrictiva a la más general.

### Ejercicio 4. Tabla de multiplicar
Pide un número y muestra su tabla de multiplicar del 1 al 10, alineada.

??? success "Solución"
    ```python
    n = int(input("Tabla del: "))

    for i in range(1, 11):
        print(f"{n} x {i:2d} = {n * i:3d}")
    ```

### Ejercicio 5. Suma con centinela
Pide números hasta que se teclee `0`. Al terminar, muestra la **suma**, la **cantidad** de números y la **media**. Si no se ha introducido ninguno, avísalo (evita dividir entre cero).

??? success "Solución"
    ```python
    suma = 0
    cantidad = 0

    numero = int(input("Número (0 para terminar): "))
    while numero != 0:
        suma += numero
        cantidad += 1
        numero = int(input("Número (0 para terminar): "))

    if cantidad > 0:
        print(f"Suma: {suma} | Cantidad: {cantidad} | Media: {suma / cantidad:.2f}")
    else:
        print("No has introducido ningún número")
    ```

### Ejercicio 6. ¿Es primo?
Pide un número entero y di si es primo. Recuerda que los menores que 2 no lo son.

??? success "Solución"
    ```python
    n = int(input("Número: "))

    if n < 2:
        print("No es primo")
    else:
        es_primo = True
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break
        print("Es primo" if es_primo else "No es primo")
    ```
    La variable `es_primo` hace de bandera: empieza en `True` y pasa a `False` en cuanto aparece un divisor.

### Ejercicio 7. Adivina el número
El programa tiene un número secreto (constante `SECRETO = 42`). El usuario tiene **5 intentos**. Tras cada fallo, indica si el número secreto es mayor o menor. Si lo adivina, se felicita y termina; si agota los intentos, se revela el número.

??? success "Solución"
    ```python
    SECRETO = 42
    MAX_INTENTOS = 5

    for intento in range(1, MAX_INTENTOS + 1):
        numero = int(input(f"Intento {intento}/{MAX_INTENTOS}: "))

        if numero == SECRETO:
            print(f"¡Acertaste en el intento {intento}!")
            break
        elif numero < SECRETO:
            print("El número secreto es mayor")
        else:
            print("El número secreto es menor")
    else:
        print(f"Has agotado los intentos. Era el {SECRETO}")
    ```

### Ejercicio 8. Lectura segura
Pide un número entero entre 1 y 10. Si el usuario escribe algo que no es un entero, o un número fuera de rango, muestra un aviso y **vuelve a preguntar** hasta que sea correcto.

??? success "Solución"
    ```python
    while True:
        try:
            numero = int(input("Número del 1 al 10: "))
            if 1 <= numero <= 10:
                break
            print("Fuera de rango")
        except ValueError:
            print("Debes escribir un número entero")

    print("Has elegido el", numero)
    ```

### Ejercicio 9. Patrón numérico
Pide un número `n` y dibuja `n` filas. La fila `k` muestra los números del 1 al `k`. Con `n = 4`:

```text
1
12
123
1234
```

??? success "Solución"
    ```python
    n = int(input("Filas: "))

    for fila in range(1, n + 1):
        for numero in range(1, fila + 1):
            print(numero, end="")
        print()
    ```
    El bucle interno escribe una fila sin salto de línea (`end=""`) y el `print()` final salta a la siguiente.

### Ejercicio 10. Encuentra los fallos
Cada fragmento tiene un fallo. Explícalo y corrígelo.

```python
# a) Quiere mostrar del 1 al 10
i = 1
while i < 10:
    print(i)

# b) Quiere clasificar la nota
if nota >= 5:
    print("Aprobado")
elif nota >= 9:
    print("Sobresaliente")

# c)
edad = input("Edad: ")
if edad >= 18:
    print("Mayor de edad")
```

??? success "Solución"
    - **a)** Dos fallos: no se actualiza `i` (**bucle infinito**) y la condición `i < 10` no llega a mostrar el 10.
      ```python
      i = 1
      while i <= 10:
          print(i)
          i += 1
      ```
    - **b)** El orden de las condiciones: un 9,5 cumple `nota >= 5` y **nunca se llega** al `elif`. La condición más restrictiva debe ir primero.
      ```python
      if nota >= 9:
          print("Sobresaliente")
      elif nota >= 5:
          print("Aprobado")
      ```
    - **c)** `input()` devuelve texto y no se puede comparar con un número (`TypeError`). Hay que convertir: `edad = int(input("Edad: "))`.

---

## Parte 3. Proyecto de práctica

!!! abstract "Formato del examen"
    **Tiempo: 50 minutos.** Sin internet ni apuntes. Usa VS Code (`.py`) o Jupyter, como prefieras.
    Este proyecto también repasa la UT01 (constantes, conversiones, f-strings...).

### Máquina expendedora

Una máquina expendedora vende tres bebidas. Programa su funcionamiento.

**Requisitos**

1. Un **docstring** inicial que explique qué hace el programa, y **comentarios** donde sean útiles.
2. Tres **constantes** con los precios: café `1.20`, té `1.00` y agua `0.80`.
3. Un **menú** que se repite hasta que el usuario elija salir:
    ```text
    --- MÁQUINA EXPENDEDORA ---
    1. Café  (1.20 €)
    2. Té    (1.00 €)
    3. Agua  (0.80 €)
    4. Salir
    ```
4. Si la opción **no es válida**, se avisa y se vuelve a mostrar el menú.
5. Tras elegir una bebida, se pide el **dinero introducido**. Debe ser un número **positivo**; si el usuario teclea otra cosa (texto, cero o un valor negativo), se avisa y se **vuelve a pedir** (usa `try` / `except`).
6. Si el dinero **no alcanza**, se avisa y se **devuelve todo el dinero**. Si alcanza, se entrega la bebida y se muestra el **cambio**.
7. Al salir, se muestra un **resumen**: bebidas vendidas y dinero recaudado (por las ventas, sin contar el cambio), con 2 decimales.

**Ampliación (solo si te sobra tiempo):** la máquina tiene **3 unidades** de cada bebida. Cuando una se agota, se avisa y no se puede vender más.

**Ejemplo de ejecución** (lo tecleado por el usuario va tras los dos puntos)

```text
--- MÁQUINA EXPENDEDORA ---
1. Café  (1.20 €)
2. Té    (1.00 €)
3. Agua  (0.80 €)
4. Salir
Elige una opción: 1
Introduce el dinero (€): 0.5
Dinero insuficiente. Se devuelven 0.50 €

(… se vuelve a mostrar el menú …)
Elige una opción: 2
Introduce el dinero (€): abc
Cantidad no válida
Introduce el dinero (€): 2
Aquí tienes tu té. Cambio: 1.00 €

(… se vuelve a mostrar el menú …)
Elige una opción: 9
Opción no válida

(… se vuelve a mostrar el menú …)
Elige una opción: 3
Introduce el dinero (€): 1
Aquí tienes tu agua. Cambio: 0.20 €

(… se vuelve a mostrar el menú …)
Elige una opción: 4

--- RESUMEN ---
Bebidas vendidas: 2
Total recaudado: 1.80 €
```

**Criterios de autocorrección**

- [ ] El programa se ejecuta sin errores con los datos del ejemplo **y** con datos incorrectos (letras, cero, negativos).
- [ ] Hay docstring, comentarios y constantes en MAYÚSCULAS.
- [ ] El menú se repite y solo termina con la opción 4.
- [ ] La entrada de dinero se valida con `try` / `except` y no «rompe» el programa.
- [ ] El cambio y el resumen salen con 2 decimales.
- [ ] El total recaudado no incluye el dinero devuelto.

??? success "Solución"
    ```python
    """Máquina expendedora de bebidas.

    Muestra un menú, cobra la bebida elegida y devuelve el cambio.
    Al salir, muestra un resumen de las ventas.
    """

    PRECIO_CAFE = 1.20
    PRECIO_TE = 1.00
    PRECIO_AGUA = 0.80

    ventas = 0            # bebidas vendidas
    recaudado = 0.0       # dinero ingresado por las ventas

    while True:
        print("\n--- MÁQUINA EXPENDEDORA ---")
        print(f"1. Café  ({PRECIO_CAFE:.2f} €)")
        print(f"2. Té    ({PRECIO_TE:.2f} €)")
        print(f"3. Agua  ({PRECIO_AGUA:.2f} €)")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                nombre, precio = "café", PRECIO_CAFE
            case "2":
                nombre, precio = "té", PRECIO_TE
            case "3":
                nombre, precio = "agua", PRECIO_AGUA
            case "4":
                break
            case _:
                print("Opción no válida")
                continue

        # Pedir el dinero hasta que sea un número positivo
        while True:
            try:
                dinero = float(input("Introduce el dinero (€): "))
                if dinero <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Cantidad no válida")

        if dinero < precio:
            print(f"Dinero insuficiente. Se devuelven {dinero:.2f} €")
        else:
            cambio = dinero - precio
            ventas += 1
            recaudado += precio
            print(f"Aquí tienes tu {nombre}. Cambio: {cambio:.2f} €")

    print("\n--- RESUMEN ---")
    print(f"Bebidas vendidas: {ventas}")
    print(f"Total recaudado: {recaudado:.2f} €")
    ```

    **Puntos clave**

    - `while True` + `break` para el menú; `continue` vuelve a mostrarlo si la opción no es válida (el `break` dentro del `match` sale del `while`).
    - Un segundo `while True` con `try` / `except` valida el dinero. `raise ValueError` reutiliza el mismo `except` para el caso de `dinero <= 0`.
    - Se guardan `nombre` y `precio` en el `match` para no repetir el código de cobro tres veces.
    - Si prefieres, sustituye el `match` por `if` / `elif` / `else`: es equivalente.

    **Ampliación con stock**

    Con lo visto hasta ahora se resuelve con tres variables (`stock_cafe`, `stock_te`, `stock_agua`, todas a `3`). Dentro de cada `case`, antes de pedir el dinero, se comprueba si el stock de esa bebida es `0` (avisar y `continue`), y tras cada venta se resta `1` al stock correspondiente.
    En la UT04 verás una forma más cómoda con diccionarios.

---

## ¿Cómo voy?

| Si has acertado... | Qué hacer |
|---|---|
| Casi todo | Estás listo/a. Repasa los errores que hayas tenido. |
| La mitad | Vuelve a los apartados donde fallaste y repite los ejemplos en la consola. |
| Poco | Repasa la unidad con calma, escribiendo los ejemplos, y pide ayuda al profesor o profesora antes del proyecto. |
