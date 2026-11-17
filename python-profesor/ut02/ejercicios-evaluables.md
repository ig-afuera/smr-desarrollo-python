# UT02 · Ejercicios evaluables

Uso de estructuras de control · 5 ejercicios con solución, criterios de corrección y datos de prueba.

Dificultad: ★ básica · ★★ media · ★★★ avanzada.

Los ejercicios son **acumulativos**: cada uno exige lo del anterior y añade un apartado nuevo de la unidad.

| Ejercicio | Caso | Dificultad | a) Selección | b) Repetición | c) Salto | d) Excepciones |
|---|---|---|:-:|:-:|:-:|:-:|
| 1 | Tarifas de mensajería | ★ | ✔ | | | |
| 2 | Cabina de peaje | ★★ | ✔ | ✔ | | |
| 3 | Carga de una furgoneta de reparto | ★★ | ✔ | ✔ | ✔ | |
| 4 | Cronometraje de una carrera popular | ★★★ | ✔ | ✔ | ✔ | ✔ |
| 5 | Tarjeta de transporte | ★★★ | ✔ | ✔ | ✔ | ✔ (completo) |

**Qué se arrastra de un ejercicio a otro**

- Desde el ejercicio 1: `if` / `elif` / `else`, condicional anidado, condición compuesta (`and`, `or`, `not`), expresión condicional (ternario) y `match` con `|` y comodín `_`.
- Desde el ejercicio 2: bucle `for` con `range()`, `while` de validación, contadores, acumuladores, máximo y media.
- Desde el ejercicio 3: `while True` con `break`, `continue` y valor centinela.
- Desde el ejercicio 4: `try` / `except` con varios tipos de error, `finally` y el patrón de validación `while True` + `try` / `except` + `break`.
- Ejercicio 5: añade `raise`, `except ... as error`, excepciones agrupadas, excepciones propias y el módulo `datetime`.

> **Requisitos comunes a todos los ejercicios**
>
> - Los valores fijos (precios, límites...) se guardan en **constantes** en MAYÚSCULAS.
> - Los importes se muestran con **2 decimales** usando f-strings.
> - El código sigue **PEP8** y lleva comentarios donde ayuden a entenderlo.
> - `match` requiere Python 3.10 o superior.

---

## Ejercicio 1 ★ · Tarifas de mensajería

Una empresa de mensajería quiere un programa que calcule el precio de enviar **un paquete**.

**Requisitos**

1. Pide el **peso** del paquete en kg (puede llevar decimales).
    - Si es 0 o negativo, muestra `Peso no válido` y no preguntes nada más.
    - Si pasa de 30 kg, muestra `No se admiten paquetes de más de 30 kg` y no preguntes nada más.
2. La **tarifa base** depende del peso:

    | Peso | Tarifa |
    |---|---|
    | Hasta 2 kg | 4,00 € |
    | Más de 2 kg y hasta 10 kg | 7,50 € |
    | Más de 10 kg y hasta 30 kg | 15,00 € |

3. Pide la **modalidad** y súmale su suplemento usando `match`. Acepta la palabra completa o su inicial:

    | Modalidad | Se acepta | Suplemento |
    |---|---|---|
    | Normal | `normal` | 0 € |
    | Urgente | `urgente` | 5,00 € |
    | Entrega en sábado | `sabado` | 3,00 € |

    Si no es ninguna, muestra `Modalidad no válida` y no preguntes nada más.

4. Pregunta si el destino está **en las islas** (`s`/`n`) y si el cliente es **premium** (`s`/`n`).
5. **Recargo por islas** (con un condicional **anidado**): si el destino está en las islas, se suman 8,00 € cuando el paquete pesa más de 10 kg y 3,00 € en otro caso.
6. **Descuento del 10 %** sobre el precio acumulado si se cumple **alguna** de estas situaciones (escríbelo en **un solo `if`**):
    - El cliente es premium **y no** envía a las islas.
    - El precio acumulado supera los 25 €.

    Si se aplica, muestra `Se aplica un 10 % de descuento`.

7. Con **expresiones condicionales**, calcula:
    - El plazo: `24 h` si es urgente, `48-72 h` en otro caso.
    - El tipo de cliente: `premium` o `estándar`.
8. Muestra el resumen final como en los ejemplos.

**Ejemplos de ejecución**

```text
Peso del paquete (kg): 12
Modalidad (normal/urgente/sabado): u
¿Destino en las islas? (s/n): s
¿Cliente premium? (s/n): n
Se aplica un 10 % de descuento
Cliente estándar | Plazo: 24 h | Total: 25.20 €
```

```text
Peso del paquete (kg): 1.5
Modalidad (normal/urgente/sabado): normal
¿Destino en las islas? (s/n): n
¿Cliente premium? (s/n): s
Se aplica un 10 % de descuento
Cliente premium | Plazo: 48-72 h | Total: 3.60 €
```

```text
Peso del paquete (kg): 5
Modalidad (normal/urgente/sabado): exprés
Modalidad no válida
```

**Criterios de corrección (10 puntos)**

| Criterio | Puntos |
|---|:-:|
| Constantes para tarifas, suplementos, recargos y descuento | 1 |
| Control del peso no válido y del peso máximo | 1,5 |
| Tarifa base con `if` / `elif` / `else` en el orden correcto | 1,5 |
| `match` con `\|` para la modalidad y comodín `_` para la no válida | 2 |
| Recargo por islas con condicional anidado | 1,5 |
| Descuento en un único `if` con `and`, `or` y `not` | 1,5 |
| Plazo y tipo de cliente con ternario; salida con 2 decimales | 1 |

<details>
<summary><b>Ver solución</b></summary>


```python
TARIFA_LIGERO = 4.00      # hasta 2 kg
TARIFA_MEDIO = 7.50       # más de 2 kg y hasta 10 kg
TARIFA_PESADO = 15.00     # más de 10 kg y hasta 30 kg
PESO_MAXIMO = 30
SUPLEMENTO_URGENTE = 5.00
SUPLEMENTO_SABADO = 3.00
RECARGO_ISLAS = 3.00
RECARGO_ISLAS_PESADO = 8.00
DESCUENTO = 0.10

peso = float(input("Peso del paquete (kg): "))

if peso <= 0:
    print("Peso no válido")
elif peso > PESO_MAXIMO:
    print(f"No se admiten paquetes de más de {PESO_MAXIMO} kg")
else:
    # Tarifa base según el peso
    if peso <= 2:
        precio = TARIFA_LIGERO
    elif peso <= 10:
        precio = TARIFA_MEDIO
    else:
        precio = TARIFA_PESADO

    modalidad = input("Modalidad (normal/urgente/sabado): ")

    match modalidad:
        case "normal" | "n":
            suplemento = 0.0
        case "urgente" | "u":
            suplemento = SUPLEMENTO_URGENTE
        case "sabado" | "s":
            suplemento = SUPLEMENTO_SABADO
        case _:
            suplemento = -1

    if suplemento < 0:
        print("Modalidad no válida")
    else:
        precio += suplemento

        islas = input("¿Destino en las islas? (s/n): ") == "s"
        premium = input("¿Cliente premium? (s/n): ") == "s"

        # Recargo por islas (condicional anidado)
        if islas:
            if peso > 10:
                precio += RECARGO_ISLAS_PESADO
            else:
                precio += RECARGO_ISLAS

        # Descuento (condición compuesta)
        if (premium and not islas) or precio > 25:
            precio -= precio * DESCUENTO
            print("Se aplica un 10 % de descuento")

        es_urgente = suplemento == SUPLEMENTO_URGENTE
        plazo = "24 h" if es_urgente else "48-72 h"
        tipo_cliente = "premium" if premium else "estándar"

        print(f"Cliente {tipo_cliente} | Plazo: {plazo} | "
              f"Total: {precio:.2f} €")
```

**Datos de prueba**

| Entradas (peso, modalidad, islas, premium) | Resultado esperado |
|---|---|
| `0` | `Peso no válido` |
| `40` | `No se admiten paquetes de más de 30 kg` |
| `5`, `x` | `Modalidad no válida` |
| `1.5`, `n`, `n`, `n` | Sin descuento · `Total: 4.00 €` |
| `1.5`, `n`, `n`, `s` | Descuento (premium sin islas) · `Total: 3.60 €` |
| `8`, `s`, `s`, `s` | Premium pero a las islas y 13,50 € no supera 25 → sin descuento · `Total: 13.50 €` |
| `12`, `u`, `s`, `n` | 15 + 5 + 8 = 28 € > 25 → descuento · `Total: 25.20 €` |

</details>

---

## Ejercicio 2 ★★ · Cabina de peaje

Una cabina de peaje de una autopista necesita un programa que cobre a **todos los vehículos de un turno** y al final muestre un resumen.

**Requisitos**

1. Pide cuántos vehículos han pasado por la cabina y recórrelos con un `for` y `range()`, mostrando `Vehículo 1`, `Vehículo 2`...
2. Para cada vehículo, pide el **tipo** y obtén el precio con `match`:

    | Tipo | Precio |
    |---|---|
    | `moto` | 1,80 € |
    | `turismo` | 3,20 € |
    | `camion` o `autobus` | 7,50 € |

    Si el tipo no es válido, muestra `Tipo no válido: el vehículo no se cobra` y pasa al siguiente vehículo (sin pedir nada más de ese).

3. Para cada vehículo válido:
    - Pide la **hora de paso** (0-23). Si está fuera de rango, muestra `Hora no válida` y **vuelve a pedirla** con un `while` hasta que sea correcta.
    - Pregunta si lleva **telepeaje** (`s`/`n`).
    - **Hora punta** (de 7 a 9 o de 18 a 20, ambas incluidas, en un solo `if`): el precio sube un 20 %.
    - **Telepeaje**: después del recargo, el precio baja un 10 %.
    - Muestra el importe de ese vehículo.
4. Durante el bucle, lleva la cuenta de:
    - Vehículos cobrados, cuántos de cada tipo (motos, turismos y pesados) y cuántos en hora punta (**contadores**).
    - Total recaudado (**acumulador**).
    - Importe más alto (**máximo**).
5. Al terminar, muestra el resumen:
    - `vehículo` o `vehículos` según la cantidad.
    - Una barra de asteriscos por cada tipo (un `*` por vehículo).
    - Total recaudado, importe medio e importe más alto. Si no se ha cobrado ningún vehículo, **no** se muestran la media ni el máximo.

**Ejemplo de ejecución**

```text
¿Cuántos vehículos pasan por la cabina? 4

Vehículo 1
Tipo (moto/turismo/camion/autobus): turismo
Hora de paso (0-23): 8
¿Lleva telepeaje? (s/n): n
Importe: 3.84 €

Vehículo 2
Tipo (moto/turismo/camion/autobus): bici
Tipo no válido: el vehículo no se cobra

Vehículo 3
Tipo (moto/turismo/camion/autobus): camion
Hora de paso (0-23): 25
Hora no válida
Hora de paso (0-23): 19
¿Lleva telepeaje? (s/n): s
Importe: 8.10 €

Vehículo 4
Tipo (moto/turismo/camion/autobus): moto
Hora de paso (0-23): 12
¿Lleva telepeaje? (s/n): s
Importe: 1.62 €

--- RESUMEN DEL TURNO ---
Cobrados: 3 vehículos | En hora punta: 2
Motos:     *
Turismos:  *
Pesados:   *
Total recaudado: 13.56 €
Importe medio: 4.52 €
Importe más alto: 8.10 €
```

**Criterios de corrección (10 puntos)**

| Criterio | Puntos |
|---|:-:|
| Constantes para precios, recargo y descuento | 0,5 |
| `for` con `range()` que recorre todos los vehículos y los numera desde 1 | 1,5 |
| `match` con `\|` y comodín; el vehículo no válido no se cobra ni pide más datos | 1,5 |
| Validación de la hora con `while` | 1,5 |
| Hora punta en un solo `if` con condición compuesta; recargo y descuento en el orden correcto | 1,5 |
| Contadores, acumulador y máximo correctamente inicializados y actualizados | 2 |
| Resumen: ternario, barras, media y máximo solo si hay vehículos cobrados | 1,5 |

<details>
<summary><b>Ver solución</b></summary>


```python
PRECIO_MOTO = 1.80
PRECIO_TURISMO = 3.20
PRECIO_PESADO = 7.50
RECARGO_PUNTA = 0.20
DESCUENTO_TELEPEAJE = 0.10

total = 0.0
cobrados = 0
motos = 0
turismos = 0
pesados = 0
en_punta = 0
importe_mayor = 0.0

vehiculos = int(input("¿Cuántos vehículos pasan por la cabina? "))

for i in range(1, vehiculos + 1):
    print(f"\nVehículo {i}")
    tipo = input("Tipo (moto/turismo/camion/autobus): ")

    match tipo:
        case "moto":
            precio = PRECIO_MOTO
            motos += 1
        case "turismo":
            precio = PRECIO_TURISMO
            turismos += 1
        case "camion" | "autobus":
            precio = PRECIO_PESADO
            pesados += 1
        case _:
            precio = 0.0

    if precio == 0:
        print("Tipo no válido: el vehículo no se cobra")
    else:
        # Validación de la hora
        hora = int(input("Hora de paso (0-23): "))
        while hora < 0 or hora > 23:
            print("Hora no válida")
            hora = int(input("Hora de paso (0-23): "))

        telepeaje = input("¿Lleva telepeaje? (s/n): ") == "s"

        if 7 <= hora <= 9 or 18 <= hora <= 20:
            precio += precio * RECARGO_PUNTA
            en_punta += 1

        if telepeaje:
            precio -= precio * DESCUENTO_TELEPEAJE

        print(f"Importe: {precio:.2f} €")

        total += precio
        cobrados += 1
        if precio > importe_mayor:
            importe_mayor = precio

print("\n--- RESUMEN DEL TURNO ---")
palabra = "vehículo" if cobrados == 1 else "vehículos"
print(f"Cobrados: {cobrados} {palabra} | En hora punta: {en_punta}")
print(f"Motos:     {'*' * motos}")
print(f"Turismos:  {'*' * turismos}")
print(f"Pesados:   {'*' * pesados}")
print(f"Total recaudado: {total:.2f} €")
if cobrados > 0:
    print(f"Importe medio: {total / cobrados:.2f} €")
    print(f"Importe más alto: {importe_mayor:.2f} €")
```

**Datos de prueba**

| Entradas | Resultado esperado |
|---|---|
| Las del ejemplo | `Total recaudado: 13.56 €` · `Importe medio: 4.52 €` |
| `turismo`, hora `8`, sin telepeaje | 3,20 × 1,2 = `3.84 €` |
| `camion`, hora `19`, con telepeaje | 7,50 × 1,2 × 0,9 = `8.10 €` |
| `0` vehículos | El bucle no se ejecuta · `Cobrados: 0 vehículos` · no se muestran media ni máximo |
| `1` vehículo cobrado | `Cobrados: 1 vehículo` (singular) |

</details>

---

## Ejercicio 3 ★★ · Carga de una furgoneta de reparto

Un almacén va cargando paquetes en una furgoneta que admite como máximo **300 kg** y **8 paquetes**. El programa decide, paquete a paquete, si se carga o se rechaza.

**Requisitos**

1. Usa un bucle `while True`. En cada vuelta pide el **peso** del paquete:
    - `0` es el **centinela**: termina la carga con `break`.
    - Un peso negativo muestra `Peso no válido` y pasa al siguiente paquete con `continue`.
2. Pregunta si el paquete es **frágil** (`s`/`n`). Un paquete frágil de más de **20 kg** se rechaza.
3. Si el paquete **no cabe** (la carga superaría los 300 kg), se rechaza indicando cuántos kg quedan libres.
4. Pide la **zona de reparto** y cuéntala con `match`: `norte`/`n`, `sur`/`s`, `centro`/`c`. Cualquier otra zona se rechaza.
5. Cada rechazo (frágil pesado, no cabe o zona desconocida) se cuenta y salta al siguiente paquete con `continue`.
6. Si el paquete se carga: actualiza la carga total, el número de paquetes, los frágiles y el paquete más pesado, y muestra `Cargado. Paquetes: X/8 | Carga: Y kg`.
7. Al llegar a 8 paquetes, muestra `La furgoneta está completa` y termina la carga con `break`.
8. Muestra la **hoja de carga**:
    - Paquetes cargados (y cuántos frágiles), rechazados y reparto por zonas.
    - Carga total, paquete más pesado y peso medio (solo si se ha cargado alguno).
    - Porcentaje de ocupación (carga / 300 × 100) con 1 decimal.
    - Una **barra de 10 posiciones** dibujada con un `for`: un `#` por cada 10 % de ocupación completo y un `.` en el resto (usa un ternario).
    - Estado con un ternario: `SALE A REPARTO` si la ocupación es del 50 % o más; si no, `ESPERA MÁS CARGA`.

**Ejemplo de ejecución**

```text
Peso del paquete en kg (0 para cerrar): 25
¿Es frágil? (s/n): s
Rechazado: un paquete frágil no puede pasar de 20.0 kg

Peso del paquete en kg (0 para cerrar): 40
¿Es frágil? (s/n): n
Zona de reparto (norte/sur/centro): norte
Cargado. Paquetes: 1/8 | Carga: 40.0 kg

Peso del paquete en kg (0 para cerrar): -3
Peso no válido

Peso del paquete en kg (0 para cerrar): 120
¿Es frágil? (s/n): n
Zona de reparto (norte/sur/centro): sur
Cargado. Paquetes: 2/8 | Carga: 160.0 kg

Peso del paquete en kg (0 para cerrar): 12
¿Es frágil? (s/n): s
Zona de reparto (norte/sur/centro): oeste
Rechazado: zona desconocida

Peso del paquete en kg (0 para cerrar): 90
¿Es frágil? (s/n): n
Zona de reparto (norte/sur/centro): c
Cargado. Paquetes: 3/8 | Carga: 250.0 kg

Peso del paquete en kg (0 para cerrar): 80
¿Es frágil? (s/n): n
Rechazado: no cabe. Quedan 50.0 kg libres

Peso del paquete en kg (0 para cerrar): 18.5
¿Es frágil? (s/n): s
Zona de reparto (norte/sur/centro): centro
Cargado. Paquetes: 4/8 | Carga: 268.5 kg

Peso del paquete en kg (0 para cerrar): 0

--- HOJA DE CARGA ---
Paquetes cargados: 4 (1 frágiles) | Rechazados: 3
Por zonas -> norte: 1 | sur: 1 | centro: 2
Carga total: 268.5 kg | Paquete más pesado: 120.0 kg
Peso medio: 67.1 kg
Ocupación: 89.5 %
########..
Estado: SALE A REPARTO
```

**Criterios de corrección (10 puntos)**

| Criterio | Puntos |
|---|:-:|
| `while True` con centinela `0` y `break` | 1,5 |
| `continue` en peso negativo y en cada rechazo, sin código duplicado | 2 |
| Rechazo de frágil pesado con condición compuesta y control de capacidad | 1,5 |
| `match` de zonas con `\|` y comodín que rechaza | 1 |
| Parada automática con `break` al completar los 8 paquetes | 1 |
| Contadores, acumulador, máximo y media (sin dividir entre cero) | 1,5 |
| Barra con `for` + ternario y estado final con ternario | 1,5 |

<details>
<summary><b>Ver solución</b></summary>


```python
CARGA_MAXIMA = 300.0      # kg
MAX_PAQUETES = 8
PESO_MAX_FRAGIL = 20.0    # kg

carga = 0.0
paquetes = 0
fragiles = 0
rechazados = 0
paquete_mayor = 0.0
norte = 0
sur = 0
centro = 0

while True:
    peso = float(input("\nPeso del paquete en kg (0 para cerrar): "))

    if peso == 0:
        break

    if peso < 0:
        print("Peso no válido")
        continue

    fragil = input("¿Es frágil? (s/n): ") == "s"

    if fragil and peso > PESO_MAX_FRAGIL:
        print("Rechazado: un paquete frágil no puede pasar de "
              f"{PESO_MAX_FRAGIL} kg")
        rechazados += 1
        continue

    if carga + peso > CARGA_MAXIMA:
        libre = CARGA_MAXIMA - carga
        print(f"Rechazado: no cabe. Quedan {libre:.1f} kg libres")
        rechazados += 1
        continue

    zona = input("Zona de reparto (norte/sur/centro): ")

    match zona:
        case "norte" | "n":
            norte += 1
        case "sur" | "s":
            sur += 1
        case "centro" | "c":
            centro += 1
        case _:
            print("Rechazado: zona desconocida")
            rechazados += 1
            continue

    # El paquete se carga
    carga += peso
    paquetes += 1
    if fragil:
        fragiles += 1
    if peso > paquete_mayor:
        paquete_mayor = peso

    print(f"Cargado. Paquetes: {paquetes}/{MAX_PAQUETES} | "
          f"Carga: {carga:.1f} kg")

    if paquetes == MAX_PAQUETES:
        print("La furgoneta está completa")
        break

# Resumen
ocupacion = carga / CARGA_MAXIMA * 100
print("\n--- HOJA DE CARGA ---")
print(f"Paquetes cargados: {paquetes} ({fragiles} frágiles) | "
      f"Rechazados: {rechazados}")
print(f"Por zonas -> norte: {norte} | sur: {sur} | centro: {centro}")
print(f"Carga total: {carga:.1f} kg | "
      f"Paquete más pesado: {paquete_mayor:.1f} kg")
if paquetes > 0:
    print(f"Peso medio: {carga / paquetes:.1f} kg")

print(f"Ocupación: {ocupacion:.1f} %")
for i in range(1, 11):
    print("#" if i * 10 <= ocupacion else ".", end="")
print()

estado = "SALE A REPARTO" if ocupacion >= 50 else "ESPERA MÁS CARGA"
print(f"Estado: {estado}")
```

**Datos de prueba**

| Entradas | Resultado esperado |
|---|---|
| Las del ejemplo | 4 cargados, 3 rechazados · `Ocupación: 89.5 %` · `########..` |
| `0` nada más empezar | Hoja vacía: `Ocupación: 0.0 %`, barra `..........`, sin peso medio, `ESPERA MÁS CARGA` |
| Ocho paquetes de `10` kg | Se detiene solo con `La furgoneta está completa` · `Ocupación: 26.7 %` |
| `20`, frágil | Se carga (el límite es «más de 20 kg») |
| `abc` como peso | El programa se detiene con `ValueError` (las excepciones se controlan a partir del ejercicio 4) |

</details>

---

## Ejercicio 4 ★★★ · Cronometraje de una carrera popular

La organización de una carrera popular quiere registrar los tiempos de los corredores al llegar a meta. Hay tres pruebas: 5 km, 10 km y 21 km. **El programa nunca debe detenerse con una traza**, aunque se escriban datos incorrectos.

**Requisitos**

1. Un bucle `while True` registra corredores uno a uno. En cada vuelta:
2. Pide el **dorsal** (entero del 1 al 500; `0` para terminar). Valídalo con el patrón `while True` + `try` / `except` + `break`:
    - Si no es un entero: `El dorsal debe ser un número entero`.
    - Si está fuera de rango: `Dorsal fuera de rango`.
    - Si es `0`, termina el registro con `break`.
3. Pide la **prueba** con `match`: `5k`/`5`, `10k`/`10`, `21k`/`21`/`media`. Si no es ninguna, muestra `Prueba desconocida. Corredor no registrado` y pasa al siguiente con `continue`.
4. Pide el tiempo en **minutos** (entero, no negativo) y **segundos** (entero de 0 a 59), y los **kilómetros completados** (decimal entre 0 y la distancia de la prueba). Valida los tres con el mismo patrón y un mensaje claro en cada caso.
5. Calcula el **ritmo** en segundos por km (tiempo total en segundos / km) dentro de un `try`:
    - Muestra el ritmo en formato `m:ss min/km` (por ejemplo, `4:15 min/km`).
    - Si los km son **menores** que la distancia: `Estado: abandono`.
    - Si los completa: `Estado: finaliza` y su **nivel** según el ritmo: menos de 4:00 → `élite`; menos de 5:30 → `avanzado`; menos de 7:00 → `popular`; resto → `paseo`.
    - Si los km son **0**, se produce `ZeroDivisionError`: captúralo y muestra `No ha completado ningún kilómetro: no se calcula el ritmo` (cuenta como abandono).
    - En un `finally`, muestra siempre `--- Dorsal X registrado ---`.
6. Lleva la cuenta de corredores registrados, que finalizan y que abandonan, y guarda el **mejor ritmo** (el más bajo) entre los que finalizan, con su dorsal.
7. Al terminar, muestra la clasificación. Si nadie ha terminado su prueba, indícalo.

**Ejemplo de ejecución**

```text
Dorsal (1-500, 0 para terminar): abc
El dorsal debe ser un número entero

Dorsal (1-500, 0 para terminar): 600
Dorsal fuera de rango

Dorsal (1-500, 0 para terminar): 17
Prueba (5k/10k/21k): 10k
Minutos: 42
Segundos: 30
Kilómetros completados (0-10): 10
Ritmo: 4:15 min/km
Estado: finaliza | Nivel: avanzado
--- Dorsal 17 registrado ---

Dorsal (1-500, 0 para terminar): 23
Prueba (5k/10k/21k): maraton
Prueba desconocida. Corredor no registrado

Dorsal (1-500, 0 para terminar): 88
Prueba (5k/10k/21k): 5k
Minutos: treinta
Escribe un número entero
Minutos: 31
Segundos: 75
Los segundos van de 0 a 59
Segundos: 5
Kilómetros completados (0-5): 5
Ritmo: 6:13 min/km
Estado: finaliza | Nivel: popular
--- Dorsal 88 registrado ---

Dorsal (1-500, 0 para terminar): 140
Prueba (5k/10k/21k): 21
Minutos: 50
Segundos: 0
Kilómetros completados (0-21): 0
No ha completado ningún kilómetro: no se calcula el ritmo
--- Dorsal 140 registrado ---

Dorsal (1-500, 0 para terminar): 205
Prueba (5k/10k/21k): 21k
Minutos: 120
Segundos: 0
Kilómetros completados (0-21): 12.5
Ritmo: 9:36 min/km
Estado: abandono
--- Dorsal 205 registrado ---

Dorsal (1-500, 0 para terminar): 0

--- CLASIFICACIÓN ---
Registrados: 4 | Finalizan: 2 | Abandonan: 2
Mejor ritmo: dorsal 17 con 4:15 min/km
```

**Criterios de corrección (10 puntos)**

| Criterio | Puntos |
|---|:-:|
| Patrón `while True` + `try` / `except ValueError` + `break` en las cuatro entradas numéricas | 2,5 |
| Fin con dorsal `0` (`break`) y prueba desconocida con `continue` | 1 |
| `match` de la prueba con `\|` y comodín | 1 |
| Cálculo del ritmo y formato `m:ss` con `:02d` | 1 |
| `ZeroDivisionError` capturado y `finally` que se ejecuta siempre | 1,5 |
| Estado y nivel con `if` / `elif` / `else` en el orden correcto | 1,5 |
| Contadores y mejor ritmo (mínimo) con su dorsal; aviso si nadie termina | 1,5 |

<details>
<summary><b>Ver solución</b></summary>


```python
MAX_DORSAL = 500

registrados = 0
finalizan = 0
abandonan = 0
mejor_ritmo = -1        # -1: todavía no hay ningún ritmo
mejor_dorsal = 0

while True:
    # Dorsal (0 para terminar)
    while True:
        try:
            texto = f"\nDorsal (1-{MAX_DORSAL}, 0 para terminar): "
            dorsal = int(input(texto))
            if 0 <= dorsal <= MAX_DORSAL:
                break
            print("Dorsal fuera de rango")
        except ValueError:
            print("El dorsal debe ser un número entero")

    if dorsal == 0:
        break

    prueba = input("Prueba (5k/10k/21k): ")
    match prueba:
        case "5k" | "5":
            distancia = 5
        case "10k" | "10":
            distancia = 10
        case "21k" | "21" | "media":
            distancia = 21
        case _:
            print("Prueba desconocida. Corredor no registrado")
            continue

    # Tiempo: minutos y segundos
    while True:
        try:
            minutos = int(input("Minutos: "))
            if minutos >= 0:
                break
            print("Los minutos no pueden ser negativos")
        except ValueError:
            print("Escribe un número entero")

    while True:
        try:
            segundos = int(input("Segundos: "))
            if 0 <= segundos <= 59:
                break
            print("Los segundos van de 0 a 59")
        except ValueError:
            print("Escribe un número entero")

    # Kilómetros completados
    while True:
        try:
            km = float(input(f"Kilómetros completados (0-{distancia}): "))
            if 0 <= km <= distancia:
                break
            print(f"Debe estar entre 0 y {distancia}")
        except ValueError:
            print("Escribe un número (usa punto decimal)")

    registrados += 1

    try:
        ritmo = (minutos * 60 + segundos) / km      # segundos por km
        ritmo_min = int(ritmo // 60)
        ritmo_seg = int(ritmo % 60)
        print(f"Ritmo: {ritmo_min}:{ritmo_seg:02d} min/km")

        if km < distancia:
            print("Estado: abandono")
            abandonan += 1
        else:
            finalizan += 1
            if ritmo < 240:
                nivel = "élite"
            elif ritmo < 330:
                nivel = "avanzado"
            elif ritmo < 420:
                nivel = "popular"
            else:
                nivel = "paseo"
            print(f"Estado: finaliza | Nivel: {nivel}")

            if mejor_ritmo < 0 or ritmo < mejor_ritmo:
                mejor_ritmo = ritmo
                mejor_dorsal = dorsal
    except ZeroDivisionError:
        print("No ha completado ningún kilómetro: no se calcula el ritmo")
        abandonan += 1
    finally:
        print(f"--- Dorsal {dorsal} registrado ---")

print("\n--- CLASIFICACIÓN ---")
print(f"Registrados: {registrados} | Finalizan: {finalizan} | "
      f"Abandonan: {abandonan}")
if mejor_ritmo < 0:
    print("Nadie ha terminado su prueba")
else:
    print(f"Mejor ritmo: dorsal {mejor_dorsal} con "
          f"{int(mejor_ritmo // 60)}:{int(mejor_ritmo % 60):02d} min/km")
```

**Datos de prueba**

| Entradas | Resultado esperado |
|---|---|
| Las del ejemplo | `Registrados: 4 \| Finalizan: 2 \| Abandonan: 2` · mejor: dorsal 17 |
| `0` nada más empezar | `Registrados: 0 ...` · `Nadie ha terminado su prueba` |
| Cualquier texto en dorsal, minutos, segundos o km | Mensaje de aviso y se vuelve a preguntar; nunca aparece una traza |
| km = `0` | Se captura `ZeroDivisionError` y aun así se muestra `--- Dorsal X registrado ---` |
| 10 km en `40:00` | Ritmo `4:00` → nivel `avanzado` (élite es **menos** de 4:00) |

</details>

---

## Ejercicio 5 ★★★ · Tarjeta de transporte

Una red de autobuses usa tarjetas recargables. Programa el funcionamiento de **una tarjeta**: recargas, viajes y consulta de saldo. Este ejercicio reúne **toda la unidad**.

**Requisitos**

1. **Excepciones propias.** Define tres excepciones que hereden de `Exception`, cada una con un docstring:
    - `RecargaNoValidaError`: el importe de la recarga no está permitido.
    - `LimiteSaldoError`: la recarga haría superar el saldo máximo.
    - `ViajeRechazadoError`: el saldo no alcanza para pagar el viaje.
2. **Alta de la tarjeta.** Pide la edad del titular con el patrón de validación. Si no está entre 0 y 120, **lanza** un `ValueError` con el mensaje `La edad debe estar entre 0 y 120`. Captúralo con `except ValueError as error` y muestra `Dato no válido:` seguido del mensaje.
    - Menores de 26 años tienen tarjeta `JOVEN`; el resto, `GENERAL` (ternario). Muestra `Tarjeta X activada`.
3. **Menú** que se repite con `while True` y se resuelve con `match`:

    ```text
    1. Recargar  2. Viajar  3. Consultar  4. Salir
    ```

4. **Recargar.** Pide un importe entero. Solo se admiten 5, 10, 15 o 20 € y el saldo nunca puede pasar de **50 €**.
    - Texto no numérico → `Escribe un importe entero`.
    - Importe no permitido → lanza `RecargaNoValidaError`.
    - Se superaría el máximo → lanza `LimiteSaldoError`.
    - Captura las dos excepciones propias **en un mismo `except`** y muestra `Recarga rechazada:` seguido del mensaje.
    - En un `finally`, muestra siempre el saldo.
5. **Viajar.** Pide la zona de destino con `match` (`1`: 1,50 €, `2`: 2,00 €, `3`: 2,80 €). Si no es válida, avisa y vuelve al menú con `continue`. Después:
    - **Hora punta** (de 7 a 9 o de 17 a 19, ambas incluidas): +0,30 €. La hora se obtiene del reloj del ordenador con `datetime`.
    - Tarjeta **joven**: después del recargo, el precio se reduce un 50 %.
    - **Cada 10 viajes, uno gratis**: si el viaje que se va a hacer es el 10, el 20, el 30..., cuesta 0 € y se muestra `¡Este viaje es gratis!`.
    - Si el saldo no alcanza, lanza `ViajeRechazadoError` con un mensaje como `Necesitas 2.15 € y tienes 1.00 €`, captúralo y muestra `Acceso denegado:` seguido del mensaje.
    - Si alcanza, descuenta el precio y muestra `Viaje validado (HH h): X €`.
    - En un `finally`, muestra siempre el saldo.
6. **Consultar.** Muestra tipo de tarjeta, saldo y viajes, y una barra de progreso hacia el viaje gratis, dibujada con un `for` y un ternario: `●` por cada viaje hecho de la tanda actual de 10 y `○` por cada uno pendiente.
7. **Salir** con la opción `4`. Si se eligen **3 opciones no válidas seguidas**, muestra `Demasiados errores seguidos. Tarjeta bloqueada` y sal también del menú. Una opción válida pone el contador de errores a cero.
8. Al salir, muestra el **resumen**: viajes, dinero gastado y saldo final.

> **Para probar la hora punta.** Como en la teoría, cambia temporalmente `datetime.now().hour` por un valor fijo (`hora = 8`, `hora = 12`...) para comprobar todos los casos.

**Ejemplo de ejecución** (realizado a las 8 h, en hora punta)

```text
Edad del titular: abc
Dato no válido: invalid literal for int() with base 10: 'abc'
Edad del titular: 150
Dato no válido: La edad debe estar entre 0 y 120
Edad del titular: 20
Tarjeta JOVEN activada

1. Recargar  2. Viajar  3. Consultar  4. Salir
Opción: 2
Zona de destino (1/2/3): 1
Acceso denegado: Necesitas 0.90 € y tienes 0.00 €
Saldo: 0.00 €

1. Recargar  2. Viajar  3. Consultar  4. Salir
Opción: 1
Importe a recargar (5, 10, 15 o 20 €): 7
Recarga rechazada: Solo se admiten 5, 10, 15 o 20 €
Saldo: 0.00 €

1. Recargar  2. Viajar  3. Consultar  4. Salir
Opción: 1
Importe a recargar (5, 10, 15 o 20 €): 20
Recarga de 20 € realizada
Saldo: 20.00 €

1. Recargar  2. Viajar  3. Consultar  4. Salir
Opción: 1
Importe a recargar (5, 10, 15 o 20 €): 20
Recarga de 20 € realizada
Saldo: 40.00 €

1. Recargar  2. Viajar  3. Consultar  4. Salir
Opción: 1
Importe a recargar (5, 10, 15 o 20 €): 20
Recarga rechazada: El saldo no puede pasar de 50.00 €
Saldo: 40.00 €

1. Recargar  2. Viajar  3. Consultar  4. Salir
Opción: 2
Zona de destino (1/2/3): 3
Viaje validado (08 h): 1.55 €
Saldo: 38.45 €

1. Recargar  2. Viajar  3. Consultar  4. Salir
Opción: 3
Tarjeta JOVEN | Saldo: 38.45 € | Viajes: 1
Hacia el viaje gratis: ● ○ ○ ○ ○ ○ ○ ○ ○ ○

1. Recargar  2. Viajar  3. Consultar  4. Salir
Opción: 4

--- RESUMEN ---
Viajes: 1 | Gastado: 1.55 € | Saldo final: 38.45 €
```

**Criterios de corrección (10 puntos)**

| Criterio | Puntos |
|---|:-:|
| Tres excepciones propias heredando de `Exception`, con docstring | 1 |
| Edad validada con `raise ValueError(...)` y `except ... as error`; tipo de tarjeta con ternario | 1,5 |
| Menú con `while True` + `match`; salida con `break`; bloqueo tras 3 errores seguidos | 1,5 |
| Recarga: `raise` de las dos excepciones propias, `except` agrupado y `finally` | 2 |
| Viaje: `match` de zonas con `continue`, hora punta con `datetime` y condición compuesta, descuento joven | 1,5 |
| Viaje gratis cada 10 con `%` y `ViajeRechazadoError` lanzada y capturada | 1,5 |
| Consulta con barra `for` + ternario y resumen final con 2 decimales | 1 |

<details>
<summary><b>Ver solución</b></summary>


```python
from datetime import datetime

SALDO_MAXIMO = 50.0
TARIFA_ZONA_1 = 1.50
TARIFA_ZONA_2 = 2.00
TARIFA_ZONA_3 = 2.80
RECARGO_PUNTA = 0.30
DESCUENTO_JOVEN = 0.50
VIAJES_PARA_GRATIS = 10
MAX_ERRORES = 3


class RecargaNoValidaError(Exception):
    """El importe de la recarga no está permitido."""


class LimiteSaldoError(Exception):
    """La recarga haría superar el saldo máximo."""


class ViajeRechazadoError(Exception):
    """El saldo no alcanza para pagar el viaje."""


# Edad del titular
while True:
    try:
        edad = int(input("Edad del titular: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
        break
    except ValueError as error:
        print("Dato no válido:", error)

joven = edad < 26
tipo_tarjeta = "JOVEN" if joven else "GENERAL"
print(f"Tarjeta {tipo_tarjeta} activada")

saldo = 0.0
viajes = 0
gastado = 0.0
errores = 0

while True:
    print("\n1. Recargar  2. Viajar  3. Consultar  4. Salir")
    opcion = input("Opción: ")

    match opcion:
        case "1":
            errores = 0
            try:
                importe = int(input("Importe a recargar (5, 10, 15 o 20 €): "))
                if importe % 5 != 0 or not 5 <= importe <= 20:
                    raise RecargaNoValidaError(
                        "Solo se admiten 5, 10, 15 o 20 €"
                    )
                if saldo + importe > SALDO_MAXIMO:
                    raise LimiteSaldoError(
                        f"El saldo no puede pasar de {SALDO_MAXIMO:.2f} €"
                    )
                saldo += importe
                print(f"Recarga de {importe} € realizada")
            except ValueError:
                print("Escribe un importe entero")
            except (RecargaNoValidaError, LimiteSaldoError) as error:
                print("Recarga rechazada:", error)
            finally:
                print(f"Saldo: {saldo:.2f} €")

        case "2":
            errores = 0
            zona = input("Zona de destino (1/2/3): ")
            match zona:
                case "1":
                    precio = TARIFA_ZONA_1
                case "2":
                    precio = TARIFA_ZONA_2
                case "3":
                    precio = TARIFA_ZONA_3
                case _:
                    print("Zona no válida")
                    continue

            hora = datetime.now().hour
            if 7 <= hora <= 9 or 17 <= hora <= 19:
                precio += RECARGO_PUNTA
            if joven:
                precio -= precio * DESCUENTO_JOVEN
            if (viajes + 1) % VIAJES_PARA_GRATIS == 0:
                precio = 0.0
                print("¡Este viaje es gratis!")

            try:
                if precio > saldo:
                    raise ViajeRechazadoError(
                        f"Necesitas {precio:.2f} € y tienes {saldo:.2f} €"
                    )
                saldo -= precio
                gastado += precio
                viajes += 1
                print(f"Viaje validado ({hora:02d} h): {precio:.2f} €")
            except ViajeRechazadoError as error:
                print("Acceso denegado:", error)
            finally:
                print(f"Saldo: {saldo:.2f} €")

        case "3":
            errores = 0
            print(f"Tarjeta {tipo_tarjeta} | Saldo: {saldo:.2f} € | "
                  f"Viajes: {viajes}")
            print("Hacia el viaje gratis: ", end="")
            for i in range(1, VIAJES_PARA_GRATIS + 1):
                hecho = i <= viajes % VIAJES_PARA_GRATIS
                print("●" if hecho else "○", end=" ")
            print()

        case "4":
            break

        case _:
            errores += 1
            print(f"Opción no válida ({errores}/{MAX_ERRORES})")
            if errores == MAX_ERRORES:
                print("Demasiados errores seguidos. Tarjeta bloqueada")
                break

print("\n--- RESUMEN ---")
print(f"Viajes: {viajes} | Gastado: {gastado:.2f} € | "
      f"Saldo final: {saldo:.2f} €")
```

**Datos de prueba** (con la hora fijada a 8, en hora punta)

| Entradas | Resultado esperado |
|---|---|
| Edad `abc`, `150`, `20` | Dos avisos y tarjeta `JOVEN` |
| Recarga `abc` | `Escribe un importe entero` y `Saldo: ...` (el `finally` se ejecuta) |
| Recarga `7` o `25` | `Recarga rechazada: Solo se admiten 5, 10, 15 o 20 €` |
| Con 40 € de saldo, recarga `20` | `Recarga rechazada: El saldo no puede pasar de 50.00 €` |
| Joven, zona 3, hora 8 | (2,80 + 0,30) × 0,5 = `1.55 €` |
| Adulto, 10 viajes a zona 1, hora 8 | 9 × 1,80 = `16.20 €` gastados; el décimo es gratis y la barra vuelve a empezar |
| Opciones `x`, `y`, `z` seguidas | `Tarjeta bloqueada` y se muestra el resumen |
| Opciones `x`, `3`, `y`, `z` | **No** se bloquea: la opción válida reinicia el contador |

</details>
