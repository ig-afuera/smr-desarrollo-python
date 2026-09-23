# Autoevaluación UT01

Esta página es para que compruebes **por ti mismo/a** si has entendido la unidad. Las soluciones están ocultas: **inténtalo primero** y despliégalas después.

!!! tip "Cómo usarla"
    1. Contesta las **preguntas** sin mirar los apuntes.
    2. Haz los **ejercicios** en VS Code o en un cuaderno de Jupyter y ejecútalos: no vale con «creer» que funcionan.
    3. Al final, haz el **proyecto de práctica** con el formato del examen: **sin internet y con un máximo de 1 hora**.

---

## Parte 1. Preguntas de repaso

### Pregunta 1
¿Qué diferencia hay entre un lenguaje **compilado** y uno **interpretado**? ¿Cuál es Python?

??? success "Solución"
    Un lenguaje compilado se traduce **entero** a código máquina antes de ejecutarse. Uno interpretado se traduce y ejecuta **línea a línea** mediante un intérprete.
    Python es **interpretado**.

### Pregunta 2
Verdadero o falso: «En Python los bloques de código se delimitan con llaves `{ }`».

??? success "Solución"
    **Falso**. Se delimitan mediante la **indentación** (4 espacios) tras una línea que termina en dos puntos `:`.

### Pregunta 3
¿Cuáles de estos nombres son identificadores válidos? Explica los que no lo sean.
`_temp`, `2x`, `mi-variable`, `class`, `Total`

??? success "Solución"
    - `_temp` ✅ válido.
    - `2x` ❌ empieza por un dígito.
    - `mi-variable` ❌ el guion es el operador resta.
    - `class` ❌ es una palabra reservada.
    - `Total` ✅ válido (y distinto de `total`).

### Pregunta 4
¿Qué diferencia hay entre `=` y `==`?

??? success "Solución"
    `=` es el operador de **asignación** (guarda un valor en una variable). `==` es el operador de **comparación** (devuelve `True` si los dos valores son iguales).

### Pregunta 5
¿Qué tipo de dato devuelve siempre `input()`? ¿Qué consecuencia tiene?

??? success "Solución"
    Devuelve siempre `str` (texto), aunque el usuario teclee un número. Para calcular hay que convertirlo antes con `int()` o `float()`.

### Pregunta 6
¿De qué tipo es el resultado de `3 / 1`? ¿Y el de `3 // 1`?

??? success "Solución"
    `3 / 1` es `3.0` (**`float`**: la división `/` siempre da `float`). `3 // 1` es `3` (**`int`**).

### Pregunta 7
Verdadero o falso: «Si escribo una constante en mayúsculas (`IVA = 0.21`), Python impide que la modifique».

??? success "Solución"
    **Falso**. Las mayúsculas son solo una **convención** para avisar a quien lea el código. Python permite reasignarla, pero no se debe hacer.

### Pregunta 8
¿Cuánto vale `bool("False")`? ¿Por qué?

??? success "Solución"
    Vale `True`. Cualquier cadena **no vacía** es *truthy*; `bool` no interpreta el contenido del texto, solo mira si está vacío.

### Pregunta 9
Escribe el número 255 como literal binario y como literal hexadecimal.

??? success "Solución"
    Binario: `0b11111111`. Hexadecimal: `0xFF`.

### Pregunta 10
¿Por qué `0.1 + 0.2 == 0.3` da `False`? ¿Cómo se comparan correctamente dos decimales?

??? success "Solución"
    Los decimales se guardan en binario con precisión limitada y `0.1 + 0.2` vale en realidad `0.30000000000000004`.
    Se comparan con `math.isclose(0.1 + 0.2, 0.3)`, que admite una pequeña tolerancia.

### Pregunta 11
¿Qué es un *docstring* y dónde se escribe?

??? success "Solución"
    Es una cadena entre triples comillas (`"""..."""`) que documenta un módulo, una función o una clase. Se escribe **justo al principio** de lo que documenta y se puede consultar con `help()` o `__doc__`.

### Pregunta 12
Explica la diferencia entre `int(3.9)` y `round(3.9)`.

??? success "Solución"
    `int(3.9)` **trunca** (corta los decimales) y da `3`. `round(3.9)` **redondea** al entero más cercano y da `4`.

---

## Parte 2. Ejercicios

### Ejercicio 1. Presentación
Pide el nombre y la edad y muestra: `Hola, Ana. Tienes 16 años y el año que viene tendrás 17.`

??? success "Solución"
    ```python
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    print(f"Hola, {nombre}. Tienes {edad} años y el año que viene tendrás {edad + 1}.")
    ```

### Ejercicio 2. Intercambio
Pide dos números enteros, **intercámbialos** y muéstralos.

??? success "Solución"
    ```python
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    a, b = b, a
    print(f"Ahora a vale {a} y b vale {b}")
    ```

### Ejercicio 3. Temperatura
Pide una temperatura en grados Celsius y muéstrala en Fahrenheit con un decimal. Fórmula: `F = C × 9/5 + 32`.

??? success "Solución"
    ```python
    celsius = float(input("Grados Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius} °C son {fahrenheit:.1f} °F")
    ```
    Con `100` se obtiene `100.0 °C son 212.0 °F`.

### Ejercicio 4. Segundos a horas, minutos y segundos
Pide un número de segundos y muestra el tiempo en formato `h:mm:ss`. Por ejemplo, `3725` segundos → `1:02:05`.

??? success "Solución"
    ```python
    total = int(input("Segundos: "))

    horas = total // 3600
    resto = total % 3600
    minutos = resto // 60
    segundos = resto % 60

    print(f"{horas}:{minutos:02d}:{segundos:02d}")
    ```
    `//` da el cociente y `%` el resto. El formato `:02d` rellena con un cero a la izquierda.

### Ejercicio 5. Precio con IVA
Define una **constante** `IVA = 0.21`. Pide el precio sin IVA y muestra el importe del IVA y el precio final, con dos decimales.

??? success "Solución"
    ```python
    IVA = 0.21

    precio = float(input("Precio sin IVA: "))
    importe_iva = precio * IVA
    total = precio + importe_iva

    print(f"IVA:   {importe_iva:.2f} €")
    print(f"Total: {total:.2f} €")
    ```

### Ejercicio 6. Predice la salida
**Sin ejecutar nada**, ¿qué valor tiene cada expresión?

```text
a) 7 // 2 + 7 % 2
b) 2 ** 3 ** 2
c) -7 // 2
d) not True or True
e) "ab" * 2 + "c"
f) bool("0")
g) 10 / 5
h) int(3.99) + round(3.5)
```

??? success "Solución"
    | | Resultado | Por qué |
    |---|---|---|
    | a | `4` | `7 // 2` = 3 y `7 % 2` = 1 |
    | b | `512` | `**` se evalúa de derecha a izquierda: `2 ** 9` |
    | c | `-4` | La división entera redondea hacia abajo |
    | d | `True` | `not True` es `False`; `False or True` es `True` |
    | e | `'ababc'` | Primero `*` (`'abab'`) y luego `+ "c"` |
    | f | `True` | Es un texto no vacío |
    | g | `2.0` | `/` siempre devuelve `float` |
    | h | `7` | `int(3.99)` = 3 y `round(3.5)` = 4 |

    Compruébalo después en la consola de Python.

### Ejercicio 7. Detecta los errores
Cada trozo de código tiene un error. Indica cuál y corrígelo.

```python
# a)
2nombre = "Ana"

# b)
edad = input("Edad: ")
print(edad + 1)

# c)
x = 5
  y = 6

# d)
radio = float(input("Radio: "))
area = pi * radio ** 2

# e)
precio = float("3,50")
```

??? success "Solución"
    - **a)** `SyntaxError`: un nombre no puede empezar por un dígito. → `nombre2 = "Ana"` o `nombre = "Ana"`.
    - **b)** `TypeError`: `input()` devuelve texto y no se puede sumar `1` a un `str`. → `edad = int(input("Edad: "))`.
    - **c)** `IndentationError`: la segunda línea tiene una indentación sin motivo. → alinea `y = 6` con `x = 5`.
    - **d)** `NameError`: `pi` no está definido. → `import math` al principio y usar `math.pi`.
    - **e)** `ValueError`: `float` solo entiende el punto decimal. → `float("3.50")`.

### Ejercicio 8. Hipotenusa
Pide los dos catetos de un triángulo rectángulo y calcula la hipotenusa (usa el módulo `math`). Muestra el resultado con 2 decimales.

??? success "Solución"
    ```python
    import math

    cateto_a = float(input("Cateto a: "))
    cateto_b = float(input("Cateto b: "))

    hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
    print(f"La hipotenusa mide {hipotenusa:.2f}")
    ```
    Otra forma: `math.hypot(cateto_a, cateto_b)`. Con catetos 3 y 4, la salida es `La hipotenusa mide 5.00`.

---

## Parte 3. Proyecto de práctica

!!! abstract "Formato del examen"
    **Tiempo: 45 minutos.** Sin internet ni apuntes. Usa VS Code (`.py`) o Jupyter, como prefieras.
    El proyecto real tiene esta misma forma: un enunciado con requisitos numerados.

### Presupuesto de reparación de un ordenador

Un taller de informática quiere un programa que calcule presupuestos.

**Requisitos**

1. Al inicio del archivo, un **docstring** que explique qué hace el programa. Añade **comentarios** donde sea útil.
2. Define dos **constantes**: `IVA` (0,21) y `TARIFA_REVISION` (15 €, un cargo fijo por la revisión del equipo).
3. Pide por teclado: nombre del cliente, horas de mano de obra, precio por hora, coste de las piezas y porcentaje de descuento.
   Convierte cada dato al **tipo adecuado**.
4. Calcula:
    - la mano de obra (horas × precio por hora),
    - la base = mano de obra + piezas + tarifa de revisión,
    - el descuento (importe en euros) y la base con el descuento aplicado,
    - el importe del IVA y el **total**.
5. Muestra el presupuesto con un formato cuidado: importes con **2 decimales**, alineados a la derecha, y el nombre del cliente en mayúsculas.
6. Calcula y muestra dos valores lógicos, **sin usar `if`**:
    - `presupuesto_alto`: el total supera los 200 €.
    - `reparacion_rapida`: se ha trabajado 1 hora o menos **y** no se han usado piezas.
7. Muestra también el total **redondeado hacia arriba** al euro (usa el módulo `math`).

**Ejemplo de ejecución**

```text
Nombre del cliente: Ana
Horas de mano de obra: 2.5
Precio por hora (€): 30
Coste de las piezas (€): 45.50
Descuento (%): 10

PRESUPUESTO PARA ANA
----------------------------------
Mano de obra:          75.00 €
Piezas:                45.50 €
Revisión:              15.00 €
Descuento:            -13.55 €
Base imponible:       121.95 €
IVA (21%):             25.61 €
----------------------------------
TOTAL:                147.56 €

Total redondeado al euro superior: 148 €
¿Presupuesto alto (más de 200 €)? False
¿Reparación rápida? False
```

**Criterios de autocorrección**

- [ ] El programa se ejecuta de principio a fin sin errores.
- [ ] Hay docstring, comentarios y constantes con nombre en MAYÚSCULAS (no hay «números mágicos»).
- [ ] Los datos numéricos se convierten con `float()`.
- [ ] Los cálculos dan los mismos resultados que el ejemplo.
- [ ] Todos los importes salen con 2 decimales.
- [ ] Los dos valores lógicos son correctos con otros datos (prueba con `1` hora y `0` de piezas).

??? success "Solución"
    ```python
    """Presupuesto de reparación de un ordenador.

    Pide los datos del trabajo y muestra el presupuesto con IVA.
    """
    import math

    IVA = 0.21
    TARIFA_REVISION = 15.0      # coste fijo de la revisión, en euros

    # --- Entrada de datos ---
    cliente = input("Nombre del cliente: ")
    horas = float(input("Horas de mano de obra: "))
    precio_hora = float(input("Precio por hora (€): "))
    piezas = float(input("Coste de las piezas (€): "))
    descuento_pct = float(input("Descuento (%): "))

    # --- Cálculos ---
    mano_obra = horas * precio_hora
    base = mano_obra + piezas + TARIFA_REVISION
    descuento = base * descuento_pct / 100
    base_final = base - descuento
    importe_iva = base_final * IVA
    total = base_final + importe_iva

    # --- Valores lógicos ---
    presupuesto_alto = total > 200
    reparacion_rapida = horas <= 1 and piezas == 0

    # --- Salida ---
    print()
    print(f"PRESUPUESTO PARA {cliente.upper()}")
    print("-" * 34)
    print(f"Mano de obra:   {mano_obra:>12.2f} €")
    print(f"Piezas:         {piezas:>12.2f} €")
    print(f"Revisión:       {TARIFA_REVISION:>12.2f} €")
    print(f"Descuento:      {-descuento:>12.2f} €")
    print(f"Base imponible: {base_final:>12.2f} €")
    print(f"IVA ({IVA:.0%}):      {importe_iva:>12.2f} €")
    print("-" * 34)
    print(f"TOTAL:          {total:>12.2f} €")
    print()
    print(f"Total redondeado al euro superior: {math.ceil(total)} €")
    print(f"¿Presupuesto alto (más de 200 €)? {presupuesto_alto}")
    print(f"¿Reparación rápida? {reparacion_rapida}")
    ```

    **Puntos clave**

    - `cliente.upper()` pasa a mayúsculas (método de cadenas; se estudia en la UT04, pero puedes averiguarlo con `help(str)`).
    - `f"{IVA:.0%}"` muestra `0.21` como `21%`.
    - Los valores lógicos son **expresiones de comparación** guardadas en variables: no hace falta `if`.
    - `math.ceil()` redondea siempre hacia arriba.

---

## ¿Cómo voy?

| Si has acertado... | Qué hacer |
|---|---|
| Casi todo | Estás listo/a. Repasa los errores que hayas tenido. |
| La mitad | Vuelve a los apartados donde fallaste y repite los ejemplos en la consola. |
| Poco | Repasa la unidad con calma, escribiendo los ejemplos, y pide ayuda al profesor o profesora antes del proyecto. |
