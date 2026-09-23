# UT02 · Banco de ejercicios

Uso de estructuras de control · 22 ejercicios con solución.

Dificultad: ★ básica · ★★ media · ★★★ avanzada.

| Apartado | Ejercicios |
|---|---|
| a) Estructuras de selección | 1 – 6 |
| b) Estructuras de repetición | 7 – 14 |
| c) Estructuras de salto | 15 – 17 |
| d) Control de excepciones | 18 – 22 |

Los ejercicios 20-22 combinan varias estructuras y son adecuados como repaso previo al proyecto.

---

## a) Estructuras de selección

### Ejercicio 1 ★ · Entradas del museo
Pide la edad y muestra el tipo de entrada: infantil (menos de 12 años) 3 €, joven (12-17) 5 €, adulto (18-64) 8 € y jubilado (65 o más) 4 €. Si la edad es negativa, muestra «Edad no válida».

<details>
<summary><b>Ver solución</b></summary>


```python
edad = int(input("Edad: "))

if edad < 0:
    print("Edad no válida")
elif edad < 12:
    print("Entrada infantil: 3 €")
elif edad < 18:
    print("Entrada joven: 5 €")
elif edad < 65:
    print("Entrada adulto: 8 €")
else:
    print("Entrada jubilado: 4 €")
```

Las condiciones van de menor a mayor, así que en cada `elif` ya se sabe que la edad supera el límite anterior.

</details>

### Ejercicio 2 ★★ · Días del mes
Pide un mes (1-12) y un año, y muestra cuántos días tiene ese mes. Febrero tiene 29 días si el año es bisiesto (divisible por 4, salvo los divisibles por 100 que no lo sean por 400). Usa `match`.

<details>
<summary><b>Ver solución</b></summary>


```python
mes = int(input("Mes (1-12): "))
anio = int(input("Año: "))

match mes:
    case 4 | 6 | 9 | 11:
        dias = 30
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        dias = 31
    case 2:
        bisiesto = (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0
        dias = 29 if bisiesto else 28
    case _:
        dias = 0

if dias == 0:
    print("Mes no válido")
else:
    print(f"El mes {mes} del año {anio} tiene {dias} días")
```

Con `2` y `2024` → 29 días; con `2` y `2023` → 28; con `2` y `1900` → 28.

</details>

### Ejercicio 3 ★★ · Tipo de triángulo
Pide los tres lados de un triángulo. Comprueba que sean positivos y que formen un triángulo (cada lado debe ser menor que la suma de los otros dos). Si es válido, indica si es **equilátero**, **isósceles** o **escaleno**.

<details>
<summary><b>Ver solución</b></summary>


```python
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Los lados deben ser positivos")
elif a >= b + c or b >= a + c or c >= a + b:
    print("Esos lados no forman un triángulo")
elif a == b == c:
    print("Triángulo equilátero")
elif a == b or b == c or a == c:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")
```

Pruebas: `3, 3, 3` → equilátero; `3, 3, 5` → isósceles; `3, 4, 5` → escaleno; `1, 2, 3` → no forman triángulo.

</details>

### Ejercicio 4 ★★ · Calculadora con `match`
Pide dos números y una operación (`+`, `-`, `*`, `/`) y muestra el resultado. Si la operación es `/` y el divisor es 0, avisa. Si la operación no existe, avisa.

<details>
<summary><b>Ver solución</b></summary>


```python
a = float(input("Primer número: "))
op = input("Operación (+, -, *, /): ")
b = float(input("Segundo número: "))

match op:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "/":
        if b == 0:
            print("No se puede dividir entre cero")
        else:
            print(f"{a} / {b} = {a / b}")
    case _:
        print("Operación no válida")
```

Con `6`, `/`, `4` → `6.0 / 4.0 = 1.5`.

</details>

### Ejercicio 5 ★★ · Tarifa de aparcamiento
Un aparcamiento cobra `0.03` € por minuto, pero los **primeros 15 minutos son gratis** y el importe **máximo diario es 8 €**. Pide los minutos de estancia y muestra el importe. Usa constantes.

<details>
<summary><b>Ver solución</b></summary>


```python
TARIFA_MINUTO = 0.03
MINUTOS_GRATIS = 15
MAXIMO_DIARIO = 8.0

minutos = int(input("Minutos de estancia: "))

if minutos <= MINUTOS_GRATIS:
    importe = 0.0
else:
    importe = (minutos - MINUTOS_GRATIS) * TARIFA_MINUTO
    if importe > MAXIMO_DIARIO:
        importe = MAXIMO_DIARIO

print(f"Importe: {importe:.2f} €")
```

Pruebas: `10` → `0.00 €`; `75` → `1.80 €`; `600` → `8.00 €`.

</details>

### Ejercicio 6 ★ · Día de la semana
Pide un número del 1 al 7 y muestra el nombre del día (1 = lunes) y si es «laborable» o «fin de semana». Usa `match` para el nombre.

<details>
<summary><b>Ver solución</b></summary>


```python
n = int(input("Número del día (1-7): "))

match n:
    case 1:
        nombre = "lunes"
    case 2:
        nombre = "martes"
    case 3:
        nombre = "miércoles"
    case 4:
        nombre = "jueves"
    case 5:
        nombre = "viernes"
    case 6:
        nombre = "sábado"
    case 7:
        nombre = "domingo"
    case _:
        nombre = ""

if nombre == "":
    print("Número no válido")
else:
    tipo = "fin de semana" if n >= 6 else "laborable"
    print(f"El día {n} es {nombre} ({tipo})")
```

</details>

---

## b) Estructuras de repetición

### Ejercicio 7 ★ · Cuenta atrás
Pide un número `n` y muestra la cuenta atrás desde `n` hasta 1, y al final `¡Despegue!`.

<details>
<summary><b>Ver solución</b></summary>


```python
n = int(input("Cuenta atrás desde: "))

for i in range(n, 0, -1):
    print(i)

print("¡Despegue!")
```

</details>

### Ejercicio 8 ★ · Suma de los pares
Pide un número `n` y calcula la suma de los números pares desde 2 hasta `n` (incluido, si es par).

<details>
<summary><b>Ver solución</b></summary>


```python
n = int(input("Hasta: "))

suma = 0
for i in range(2, n + 1, 2):
    suma += i

print(f"La suma de los pares hasta {n} es {suma}")
```

Con `10` → `30` (2 + 4 + 6 + 8 + 10).

</details>

### Ejercicio 9 ★★ · Factorial
Pide un número entero y calcula su factorial (`n! = 1 × 2 × … × n`; `0! = 1`). Si es negativo, avisa.

<details>
<summary><b>Ver solución</b></summary>


```python
n = int(input("Número: "))

if n < 0:
    print("No existe el factorial de un número negativo")
else:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")
```

Con `5` → `5! = 120`. Con `0` el bucle no se ejecuta y queda `0! = 1`.

</details>

### Ejercicio 10 ★★ · Fibonacci
Pide un número `n` y muestra los `n` primeros términos de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, …), en una sola línea.

<details>
<summary><b>Ver solución</b></summary>


```python
n = int(input("¿Cuántos términos? "))

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

Con `8` → `0 1 1 2 3 5 8 13`.

</details>

### Ejercicio 11 ★★ · Estadísticas de una serie
Pide cuántos números se van a introducir (al menos 1) y después cada uno de ellos. Muestra el **mayor**, el **menor** y la **media**.

<details>
<summary><b>Ver solución</b></summary>


```python
cantidad = int(input("¿Cuántos números? "))

primero = float(input("Número 1: "))
suma = mayor = menor = primero

for i in range(2, cantidad + 1):
    n = float(input(f"Número {i}: "))
    suma += n
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print(f"Mayor: {mayor} | Menor: {menor} | Media: {suma / cantidad:.2f}")
```

Se lee el primer número **antes** del bucle para inicializar el mayor y el menor con un dato real. Con `3, 8, -2, 5` → mayor `8.0`, menor `-2.0`, media `3.50`.

</details>

### Ejercicio 12 ★★ · Tablas de multiplicar
Muestra las tablas de multiplicar del 1 al 9 en forma de cuadrícula (9 filas × 9 columnas), con cada número alineado a la derecha en 3 posiciones.

<details>
<summary><b>Ver solución</b></summary>


```python
for fila in range(1, 10):
    for col in range(1, 10):
        print(f"{fila * col:3d}", end="")
    print()
```

</details>

### Ejercicio 13 ★★★ · Cifras de un número
Pide un entero positivo y, **sin convertirlo a texto**, muestra cuántas cifras tiene, cuánto suman y cómo queda al revés. Con `12345`: 5 cifras, suman 15 y al revés es `54321`.

<details>
<summary><b>Ver solución</b></summary>


```python
n = int(input("Número entero positivo: "))
original = n

cantidad = 0
suma = 0
invertido = 0

while n > 0:
    cifra = n % 10               # última cifra
    suma += cifra
    invertido = invertido * 10 + cifra
    cantidad += 1
    n //= 10                     # quitamos la última cifra

print(f"{original} tiene {cantidad} cifras, suman {suma} y al revés es {invertido}")
```

</details>

### Ejercicio 14 ★★★ · Números primos
Pide un límite y muestra todos los números primos desde 2 hasta ese límite, en una sola línea.

<details>
<summary><b>Ver solución</b></summary>


```python
limite = int(input("Primos hasta: "))

for n in range(2, limite + 1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=" ")
print()
```

Con `20` → `2 3 5 7 11 13 17 19`. El `else` del bucle interno se ejecuta solo si no se encontró ningún divisor.

</details>

---

## c) Estructuras de salto

### Ejercicio 15 ★ · Primer múltiplo
Encuentra y muestra el primer múltiplo de 7 mayor que 100 usando un `while True` con `break`.

<details>
<summary><b>Ver solución</b></summary>


```python
n = 101

while True:
    if n % 7 == 0:
        break
    n += 1

print("El primer múltiplo de 7 mayor que 100 es", n)
```

Resultado: `105`.

</details>

### Ejercicio 16 ★★ · Suma de positivos
Pide números enteros hasta que se teclee `0`. Los **negativos se ignoran** (avisando) y no se suman. Al terminar, muestra la suma de los positivos. Usa `continue` y `break`.

<details>
<summary><b>Ver solución</b></summary>


```python
suma = 0

while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0:
        break
    if n < 0:
        print("Los negativos se ignoran")
        continue
    suma += n

print("Suma de los positivos:", suma)
```

Con `5, -3, 7, 0` → `12`.

</details>

### Ejercicio 17 ★★ · Conversor con menú
Crea un menú que se repita: `1` kilómetros → millas, `2` millas → kilómetros, `3` salir. Usa la constante `MILLAS_POR_KM = 0.621371`. Si la opción no es válida, avisa y vuelve al menú.

<details>
<summary><b>Ver solución</b></summary>


```python
MILLAS_POR_KM = 0.621371

while True:
    print("\n1. Kilómetros a millas")
    print("2. Millas a kilómetros")
    print("3. Salir")
    opcion = input("Opción: ")

    if opcion == "3":
        break
    if opcion != "1" and opcion != "2":
        print("Opción no válida")
        continue

    valor = float(input("Valor: "))
    if opcion == "1":
        print(f"{valor} km = {valor * MILLAS_POR_KM:.2f} millas")
    else:
        print(f"{valor} millas = {valor / MILLAS_POR_KM:.2f} km")
```

Con `1`, `10` → `10.0 km = 6.21 millas`; con `2`, `10` → `10.0 millas = 16.09 km`.

</details>

---

## d) Control de excepciones

### Ejercicio 18 ★ · Precio válido
Pide un precio (número decimal **mayor que 0**). Si el usuario escribe algo que no es un número o un valor no positivo, avisa y **vuelve a preguntar**.

<details>
<summary><b>Ver solución</b></summary>


```python
while True:
    try:
        precio = float(input("Precio (€): "))
        if precio <= 0:
            raise ValueError
        break
    except ValueError:
        print("Introduce un número mayor que cero (con punto decimal)")

print(f"Precio registrado: {precio:.2f} €")
```

Con `abc`, `-5`, `12.5` → avisa dos veces y acepta `12.5`.

</details>

### Ejercicio 19 ★★ · División segura
Pide dos números y muestra el resultado de dividirlos. Controla con `try` / `except` los textos no numéricos y la división entre cero. Usa `else` para mostrar el resultado y `finally` para mostrar siempre «Fin de la operación».

<details>
<summary><b>Ver solución</b></summary>


```python
try:
    a = float(input("Dividendo: "))
    b = float(input("Divisor: "))
    resultado = a / b
except ValueError:
    print("Debes escribir números")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print(f"Resultado: {resultado:.2f}")
finally:
    print("Fin de la operación")
```

Con `7` y `0` → «No se puede dividir entre cero» y «Fin de la operación».

</details>

### Ejercicio 20 ★★ · Edad con `raise`
Pide una edad. Si no está entre 0 y 120, **lanza** un `ValueError` con un mensaje explicativo y **captúralo** para mostrarlo. Si el texto ni siquiera es un entero, también debe controlarse.

<details>
<summary><b>Ver solución</b></summary>


```python
try:
    edad = int(input("Edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120")
    print("Edad registrada:", edad)
except ValueError as error:
    print("Error:", error)
```

Con `150` → `Error: La edad debe estar entre 0 y 120`. Con `abc` → se muestra el mensaje automático de `int()`. Para un mensaje propio en ese caso, se pueden separar los dos `except` con excepciones distintas (idea de ampliación).

</details>

### Ejercicio 21 ★★ · Tres intentos
Pide un número entero con un **máximo de 3 intentos**. Si escribe un entero, muéstralo y termina. Si agota los intentos, muestra «Demasiados intentos fallidos». Usa `for ... else`.

<details>
<summary><b>Ver solución</b></summary>


```python
MAX_INTENTOS = 3

for intento in range(1, MAX_INTENTOS + 1):
    try:
        numero = int(input(f"Número entero (intento {intento}/{MAX_INTENTOS}): "))
    except ValueError:
        print("No es un entero")
    else:
        print("Has escrito", numero)
        break
else:
    print("Demasiados intentos fallidos")
```

El `else` del `for` solo se ejecuta si el bucle acabó sin `break`, es decir, si ninguno de los intentos fue válido.

</details>

### Ejercicio 22 ★★★ · Suma y media con validación
Pide cuántos números se van a introducir (entero **mayor que 0**) y después cada número (decimal). Todas las entradas deben **validarse**: si son incorrectas, se vuelve a preguntar. Al final, muestra la suma y la media con 2 decimales.

<details>
<summary><b>Ver solución</b></summary>


```python
# Cantidad de números (entero > 0)
while True:
    try:
        cantidad = int(input("¿Cuántos números vas a introducir? "))
        if cantidad > 0:
            break
        print("Debe ser mayor que 0")
    except ValueError:
        print("Escribe un número entero")

# Lectura y suma de los números
suma = 0
for i in range(1, cantidad + 1):
    while True:
        try:
            n = float(input(f"Número {i}: "))
            break
        except ValueError:
            print("Número no válido")
    suma += n

print(f"Suma: {suma:.2f} | Media: {suma / cantidad:.2f}")
```

Con `x`, `0`, `3`, y luego `2`, `abc`, `4`, `6` → `Suma: 12.00 | Media: 4.00`.

</details>
