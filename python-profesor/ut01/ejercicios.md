# UT01 · Banco de ejercicios

Identificación de los elementos de un programa informático · 22 ejercicios con solución.

Dificultad: ★ básica · ★★ media · ★★★ avanzada.

| Apartado | Ejercicios |
|---|---|
| a) Estructura y bloques | 1 – 2 |
| b) Variables | 3 – 4 |
| c) Tipos de datos | 5 – 6 |
| d) Literales | 7 – 9 |
| e) Constantes | 10 – 11 |
| f) Operadores y expresiones | 12 – 16 |
| g) Conversiones de tipo | 17 – 19 |
| h) Comentarios | 20 |
| Integradores (varios apartados) | 21 – 22 |

---

## a) Estructura y bloques fundamentales

### Ejercicio 1 ★ · Saludo personalizado
Escribe un programa que pregunte el nombre y muestre `Hola, <nombre>. ¡Bienvenido a Python!`.

<details>
<summary><b>Ver solución</b></summary>


```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}. ¡Bienvenido a Python!")
```

</details>

### Ejercicio 2 ★★ · Fases de desarrollo: IMC
Aplica las fases de desarrollo al problema «calcular el índice de masa corporal (IMC = peso / altura²)»:
a) Análisis: entradas y salidas. b) Diseño: pseudocódigo. c) Codificación. d) Prueba: un caso con resultado conocido.

<details>
<summary><b>Ver solución</b></summary>


**a) Análisis.** Entradas: peso (kg) y altura (m). Salida: el IMC con dos decimales.

**b) Diseño.**
```text
1. Pedir peso
2. Pedir altura
3. imc = peso / altura al cuadrado
4. Mostrar imc
```

**c) Codificación.**
```python
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / altura ** 2
print(f"Tu IMC es {imc:.2f}")
```

**d) Prueba.** Peso 70 y altura 1,75 → IMC = 70 / 3,0625 = 22,857… → se muestra `22.86`.

</details>

---

## b) Variables

### Ejercicio 3 ★ · Intercambio con variable auxiliar
Intercambia el valor de dos variables `a = 10` y `b = 20` **sin** usar la asignación múltiple (con una variable auxiliar). Después, hazlo de la forma «pythónica».

<details>
<summary><b>Ver solución</b></summary>


```python
a = 10
b = 20

# Con variable auxiliar
aux = a
a = b
b = aux
print(a, b)         # 20 10

# Forma pythónica (volvemos a intercambiar)
a, b = b, a
print(a, b)         # 10 20
```

</details>

### Ejercicio 4 ★★ · ¿Cuánto valen?
Sin ejecutar, indica los valores finales de `a`, `b`, `c` y `d`:

```python
a = b = 3
c, d = 1, 2
a += 4
c, d = d, c + d
b = b * a
```

<details>
<summary><b>Ver solución</b></summary>


Paso a paso:

| Línea | a | b | c | d |
|---|:-:|:-:|:-:|:-:|
| `a = b = 3` | 3 | 3 | | |
| `c, d = 1, 2` | 3 | 3 | 1 | 2 |
| `a += 4` | 7 | 3 | 1 | 2 |
| `c, d = d, c + d` | 7 | 3 | 2 | 3 |
| `b = b * a` | 7 | 21 | 2 | 3 |

Resultado final: `a = 7`, `b = 21`, `c = 2`, `d = 3`. (En `c, d = d, c + d` se evalúa primero todo el lado derecho con los valores antiguos: `(2, 1 + 2)`.)

</details>

---

## c) Tipos de datos

### Ejercicio 5 ★ · ¿De qué tipo es?
Indica el tipo (`int`, `float`, `str` o `bool`) de cada valor y comprueba tus respuestas con `type()`.

```text
a) 42          b) 42.0        c) "42"        d) 4 > 2
e) 7 / 7       f) 7 // 7      g) "a" + "b"   h) 3 == 3.0
```

<details>
<summary><b>Ver solución</b></summary>


| | Tipo | Motivo |
|---|---|---|
| a | `int` | Entero |
| b | `float` | Tiene punto decimal |
| c | `str` | Entre comillas |
| d | `bool` | Resultado de una comparación |
| e | `float` | `/` siempre devuelve `float` (`1.0`) |
| f | `int` | `//` con enteros da entero (`1`) |
| g | `str` | Concatenación: `'ab'` |
| h | `bool` | `3 == 3.0` es `True` |

</details>

### Ejercicio 6 ★★ · Verdadero o falso
Predice el valor de `bool(...)` en cada caso:

```text
a) bool(0)      b) bool(0.0)     c) bool("")      d) bool(" ")
e) bool("0")    f) bool(-5)      g) bool("False") h) bool(1 - 1)
```

<details>
<summary><b>Ver solución</b></summary>


| | Resultado | Motivo |
|---|:-:|---|
| a | `False` | El cero es *falsy* |
| b | `False` | `0.0` es *falsy* |
| c | `False` | Cadena vacía |
| d | `True` | Un espacio ya es contenido: no está vacía |
| e | `True` | Cadena no vacía |
| f | `True` | Cualquier número distinto de 0 |
| g | `True` | Cadena no vacía |
| h | `False` | `1 - 1` es `0` |

</details>

---

## d) Literales

### Ejercicio 7 ★ · Cambio de base con literales
Sin usar `int()`, `bin()` ni funciones: escribe en una línea `print(...)` la suma de `0b1101`, `0o17` y `0xA`. ¿Cuánto da? Calcula a mano cada valor.

<details>
<summary><b>Ver solución</b></summary>


```python
print(0b1101 + 0o17 + 0xA)      # 13 + 15 + 10 = 38
```

- `0b1101` = 8 + 4 + 0 + 1 = 13
- `0o17` = 1·8 + 7 = 15
- `0xA` = 10

</details>

### Ejercicio 8 ★★ · Tabla con f-strings
Guarda en variables los datos de tres productos y muestra esta tabla **con f-strings** (nombre alineado a la izquierda en 10 posiciones, precio a la derecha en 8 posiciones con 2 decimales):

```text
Producto    Precio
Teclado      19.90
Ratón         8.50
Monitor     129.99
```

<details>
<summary><b>Ver solución</b></summary>


```python
p1, precio1 = "Teclado", 19.90
p2, precio2 = "Ratón", 8.5
p3, precio3 = "Monitor", 129.99

print(f"{'Producto':<10}{'Precio':>8}")
print(f"{p1:<10}{precio1:>8.2f}")
print(f"{p2:<10}{precio2:>8.2f}")
print(f"{p3:<10}{precio3:>8.2f}")
```

Se usan comillas simples dentro de la f-string para no cerrar las dobles. Para la cabecera, `:>8` alinea el texto a la derecha.

</details>

### Ejercicio 9 ★ · Escapes y cadenas *raw*
Muestra por pantalla exactamente esto usando **un solo `print`** con escapes (`\n`, `\t`) y otro con una cadena *raw*:

```text
Nombre:	Ana
Ciudad:	Sevilla
```
(con un tabulador tras los dos puntos) y, después, la ruta `C:\Users\ana\notas.txt`.

<details>
<summary><b>Ver solución</b></summary>


```python
print("Nombre:\tAna\nCiudad:\tSevilla")
print(r"C:\Users\ana\notas.txt")
```

Sin la `r`, `\n` en `\notas.txt` se interpretaría como un salto de línea.

</details>

---

## e) Constantes

### Ejercicio 10 ★ · Círculo
Con `math.pi`, pide el radio de un círculo y muestra su **longitud** (2πr) y su **área** (πr²) con 2 decimales.

<details>
<summary><b>Ver solución</b></summary>


```python
import math

radio = float(input("Radio: "))

longitud = 2 * math.pi * radio
area = math.pi * radio ** 2

print(f"Longitud: {longitud:.2f}")
print(f"Área: {area:.2f}")
```

Con radio `1` → longitud `6.28`, área `3.14`.

</details>

### Ejercicio 11 ★★ · Factura con constantes
Define las constantes `IVA = 0.21` y `DESCUENTO = 0.05`. Pide el precio de un producto y la cantidad. Calcula y muestra: subtotal, descuento (en €), IVA (sobre el subtotal con descuento) y total. Todos con 2 decimales.

<details>
<summary><b>Ver solución</b></summary>


```python
IVA = 0.21
DESCUENTO = 0.05

precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
importe_descuento = subtotal * DESCUENTO
base = subtotal - importe_descuento
importe_iva = base * IVA
total = base + importe_iva

print(f"Subtotal:  {subtotal:>9.2f} €")
print(f"Descuento: {importe_descuento:>9.2f} €")
print(f"IVA:       {importe_iva:>9.2f} €")
print(f"Total:     {total:>9.2f} €")
```

Con precio `10` y cantidad `4`: subtotal 40.00, descuento 2.00, IVA 7.98, total 45.98.

</details>

---

## f) Operadores y expresiones

### Ejercicio 12 ★ · Minutos a días, horas y minutos
Pide un número de minutos y muéstralo como días, horas y minutos. Ejemplo: `3000` minutos → `2 días, 2 horas y 0 minutos`.

<details>
<summary><b>Ver solución</b></summary>


```python
total = int(input("Minutos: "))

dias = total // (24 * 60)
resto = total % (24 * 60)
horas = resto // 60
minutos = resto % 60

print(f"{dias} días, {horas} horas y {minutos} minutos")
```

Comprobación con 3000: `3000 // 1440 = 2`, `3000 % 1440 = 120`, `120 // 60 = 2`, `120 % 60 = 0`.

</details>

### Ejercicio 13 ★★ · Cifras de un número
Pide un número de exactamente tres cifras y muestra sus tres cifras por separado y su suma. Ejemplo: `472` → `4 7 2 (suma: 13)`.

<details>
<summary><b>Ver solución</b></summary>


```python
n = int(input("Número de tres cifras: "))

unidades = n % 10
decenas = (n // 10) % 10
centenas = n // 100

print(centenas, decenas, unidades, f"(suma: {centenas + decenas + unidades})")
```

</details>

### Ejercicio 14 ★★ · Devolver el cambio en monedas
Pide una cantidad de **céntimos** (entero, menor de 100) y muestra cuántas monedas de 50, 20, 10, 5, 2 y 1 céntimos hacen falta, usando las menos monedas posibles.

<details>
<summary><b>Ver solución</b></summary>


```python
cents = int(input("Céntimos a devolver (0-99): "))

m50 = cents // 50
cents %= 50
m20 = cents // 20
cents %= 20
m10 = cents // 10
cents %= 10
m5 = cents // 5
cents %= 5
m2 = cents // 2
cents %= 2
m1 = cents

print(f"50c: {m50} | 20c: {m20} | 10c: {m10} | 5c: {m5} | 2c: {m2} | 1c: {m1}")
```

Con `88`: 1 de 50, 1 de 20, 1 de 10, 1 de 5, 1 de 2 y 1 de 1.

</details>

### Ejercicio 15 ★★ · Expresiones lógicas
Pide la edad (entero) y si tiene carné (`s` o `n`). Sin usar `if`, calcula y muestra estas variables lógicas:

- `es_adulto`: edad ≥ 18
- `puede_conducir`: es adulto **y** tiene carné
- `es_joven_sin_carne`: edad entre 18 y 25 (ambos incluidos) **y** no tiene carné

<details>
<summary><b>Ver solución</b></summary>


```python
edad = int(input("Edad: "))
tiene_carne = input("¿Tienes carné? (s/n): ") == "s"

es_adulto = edad >= 18
puede_conducir = es_adulto and tiene_carne
es_joven_sin_carne = 18 <= edad <= 25 and not tiene_carne

print("Adulto:", es_adulto)
print("Puede conducir:", puede_conducir)
print("Joven sin carné:", es_joven_sin_carne)
```

Con edad `20` y `n`: `True`, `False`, `True`.

</details>

### Ejercicio 16 ★★ · Precedencia
Calcula a mano el valor de cada expresión y comprueba después con Python:

```text
a) 2 + 3 * 4 ** 2 - 1
b) (2 + 3) * 4 ** 2 - 1
c) 20 / 4 * 2
d) 20 // 3 % 4
e) -3 ** 2
f) 5 > 3 and 2 > 4 or not False
g) 10 - 2 - 3 * 2
h) 2 ** -1
```

<details>
<summary><b>Ver solución</b></summary>


| | Resultado | Pasos |
|---|---|---|
| a | `49` | `4 ** 2` = 16; `3 * 16` = 48; `2 + 48 - 1` = 49 |
| b | `79` | `(5) * 16 - 1` = 79 |
| c | `10.0` | `/` y `*` van de izquierda a derecha: `5.0 * 2` |
| d | `2` | `20 // 3` = 6; `6 % 4` = 2 |
| e | `-9` | La potencia va antes que el signo: `-(3 ** 2)` |
| f | `True` | `(True and False) or True` → `False or True` |
| g | `2` | `10 - 2 - 6` = 2 |
| h | `0.5` | Exponente negativo: `1 / 2` |

</details>

---

## g) Conversiones de tipo

### Ejercicio 17 ★ · Sumar o concatenar
Pide dos valores con `input()`. Muestra su **concatenación** como texto y su **suma** como números. Con `12` y `30` debe mostrar `1230` y `42`.

<details>
<summary><b>Ver solución</b></summary>


```python
a = input("Primer valor: ")
b = input("Segundo valor: ")

print("Concatenación:", a + b)
print("Suma:", int(a) + int(b))
```

`a + b` con textos los une; para sumar hay que convertir antes.

</details>

### Ejercicio 18 ★★ · Media de tres notas
Pide tres notas (con decimales). Muestra la media con 2 decimales, la media **truncada** con `int()` y la media **redondeada** con `round()`.

<details>
<summary><b>Ver solución</b></summary>


```python
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1 + n2 + n3) / 3

print(f"Media: {media:.2f}")
print("Truncada:", int(media))
print("Redondeada:", round(media))
```

Con `6`, `7` y `8.5`: media `7.17`, truncada `7`, redondeada `7`. Con `9`, `9` y `8.5`: media `8.83`, truncada `8`, redondeada `9`.

</details>

### Ejercicio 19 ★★ · Bases numéricas
Pide un entero (0-255) y muestra su representación en binario, octal y hexadecimal **sin prefijo**, y en binario de 8 dígitos. Con `200`: `11001000`, `310`, `C8`, `11001000`.

<details>
<summary><b>Ver solución</b></summary>


```python
n = int(input("Número (0-255): "))

print("Binario:", f"{n:b}")
print("Octal:", f"{n:o}")
print("Hexadecimal:", f"{n:X}")
print("Binario (8 bits):", f"{n:08b}")
```

Alternativa con las funciones: `bin(n)[2:]`, `oct(n)[2:]` y `hex(n)[2:]`.

</details>

---

## h) Comentarios

### Ejercicio 20 ★ · Documenta y mejora
Mejora este código: pon nombres significativos, una constante para el número mágico, un docstring inicial y comentarios útiles.

```python
a = float(input())
b = a * 1.21
print(b)
```

<details>
<summary><b>Ver solución</b></summary>


```python
"""Calcula el precio final de un producto aplicando el IVA general."""

IVA = 0.21

precio_sin_iva = float(input("Precio sin IVA: "))
precio_final = precio_sin_iva * (1 + IVA)   # precio con el IVA incluido
print(f"Precio final: {precio_final:.2f} €")
```

Cambios: nombres descriptivos, constante `IVA` en lugar del «número mágico» `1.21`, mensaje en el `input`, formato de salida y un docstring que explica qué hace el programa.

</details>

---

## Integradores

### Ejercicio 21 ★★★ · Distancia entre dos puntos
Pide las coordenadas de dos puntos del plano `(x1, y1)` y `(x2, y2)`, y muestra la **distancia** entre ellos con 3 decimales (`√((x2−x1)² + (y2−y1)²)`) y si están **en el mismo eje vertical** (misma `x`), como `True` o `False`.

<details>
<summary><b>Ver solución</b></summary>


```python
import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
misma_vertical = x1 == x2

print(f"Distancia: {distancia:.3f}")
print("Misma vertical:", misma_vertical)
```

Puntos `(0, 0)` y `(3, 4)`: distancia `5.000`, `False`. Alternativa: `math.hypot(x2 - x1, y2 - y1)`.

</details>

### Ejercicio 22 ★★★ · Consumo de una impresora
Una impresora usa un cartucho de tinta de `PAGINAS_CARTUCHO = 400` páginas que cuesta `PRECIO_CARTUCHO = 24.90` €. Pide el número de páginas de un trabajo de impresión. Muestra:

1. Cuántos cartuchos **completos** se consumen (división entera) y qué fracción del siguiente se usa (en %, con 1 decimal).
2. El coste del trabajo con 2 decimales.
3. Si el trabajo cuesta más de 10 € (`True`/`False`).

Con 1000 páginas: 2 cartuchos y `50.0%` del siguiente; coste `62.25 €`; `True`.

<details>
<summary><b>Ver solución</b></summary>


```python
"""Coste de imprimir un trabajo según el consumo del cartucho."""

PAGINAS_CARTUCHO = 400
PRECIO_CARTUCHO = 24.90
LIMITE_COSTE = 10

paginas = int(input("Páginas del trabajo: "))

cartuchos_completos = paginas // PAGINAS_CARTUCHO
resto_paginas = paginas % PAGINAS_CARTUCHO
fraccion_siguiente = resto_paginas / PAGINAS_CARTUCHO

coste = paginas / PAGINAS_CARTUCHO * PRECIO_CARTUCHO
es_caro = coste > LIMITE_COSTE

print(f"Cartuchos completos: {cartuchos_completos}")
print(f"Uso del siguiente cartucho: {fraccion_siguiente:.1%}")
print(f"Coste: {coste:.2f} €")
print("¿Más de 10 €?", es_caro)
```

`f"{0.5:.1%}"` muestra `50.0%` (el `%` va pegado al número).

</details>
