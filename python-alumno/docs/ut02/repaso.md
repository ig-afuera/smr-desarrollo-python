# Ejercicios de repaso UT02

Cinco ejercicios para repasar la unidad **de menos a más**. Cada ejercicio usa lo que ya has practicado en el anterior y añade un apartado nuevo, así que **hazlos en orden**.

| Ejercicio | Caso | Dificultad | Repasa |
|---|---|---|---|
| 1 | Pizzería | ★ | a) Selección |
| 2 | Registro semanal de entrenamiento | ★★ | a) Selección · b) Repetición |
| 3 | Taquilla de un concierto | ★★ | a) Selección · b) Repetición · c) Salto |
| 4 | Repostajes de una flota de vehículos | ★★★ | a) Selección · b) Repetición · c) Salto · d) Excepciones |
| 5 | Monedero de un videojuego | ★★★ | Toda la unidad |

!!! tip "Cómo aprovecharlos"
    1. Lee el enunciado entero antes de escribir código. Si te ayuda, dibuja primero el diagrama de flujo.
    2. Guarda los valores fijos (precios, límites...) en **constantes** y muestra los importes con 2 decimales.
    3. Prueba tu programa con el ejemplo **y** con datos raros: cero, negativos, opciones que no existen...
    4. Mira la solución solo cuando tu programa funcione o estés atascado/a.

---

## Ejercicio 1 ★ · Pizzería

!!! abstract "Repasa"
    [a) Estructuras de selección](a-seleccion.md)

Una pizzería quiere un programa que calcule el precio de **un pedido**.

1. Pide el **tamaño** de la pizza y obtén su precio con `match`. Acepta la palabra o su inicial:

    | Tamaño | Se acepta | Precio |
    |---|---|---|
    | Pequeña | `pequena` o `p` | 7,00 € |
    | Mediana | `mediana` o `m` | 9,50 € |
    | Familiar | `familiar` o `f` | 14,00 € |

    Si no es ninguno, muestra `Tamaño no válido` y no preguntes nada más.

2. Pide cuántos **ingredientes extra** quiere (de 0 a 6). Si está fuera de ese rango, muestra `Número de ingredientes no válido` y no preguntes nada más. Si no, suma:
    - 0 extras: nada, pero muestra `Pizza sin ingredientes extra`.
    - 1 o 2 extras: 1,20 € cada uno.
    - 3 o más extras: 0,80 € cada uno (oferta).
3. Pregunta si es **a domicilio** (`s`/`n`) y si el cliente tiene **carné de estudiante** (`s`/`n`).
4. **Gastos de envío** (con un condicional **anidado**): solo si es a domicilio, pide la distancia en km:
    - Más de 10 km: muestra `Fuera de la zona de reparto: tendrás que recogerla` y el pedido pasa a ser para recoger.
    - Más de 3 km: +3,50 €.
    - Hasta 3 km: +1,50 €.
5. **Descuento del 15 %** si se cumple **alguna** de estas situaciones (en **un solo `if`**):
    - Tiene carné de estudiante **y no** es a domicilio.
    - El precio acumulado es de 20 € o más.

    Si se aplica, muestra `Se aplica un 15 % de descuento`.

6. Con **expresiones condicionales**, calcula el tiempo de espera (`45 min` a domicilio, `20 min` para recoger) y el tipo de entrega (`a domicilio` o `para recoger`), y muestra el resumen.

```text
Tamaño (pequena/mediana/familiar): m
Ingredientes extra (0-6): 2
¿Envío a domicilio? (s/n): n
¿Tienes carné de estudiante? (s/n): s
Se aplica un 15 % de descuento
Pedido para recoger | Espera: 20 min | Total: 10.12 €
```

```text
Tamaño (pequena/mediana/familiar): f
Ingredientes extra (0-6): 4
¿Envío a domicilio? (s/n): s
¿Tienes carné de estudiante? (s/n): n
Distancia en km: 2
Pedido a domicilio | Espera: 45 min | Total: 18.70 €
```

```text
Tamaño (pequena/mediana/familiar): p
Ingredientes extra (0-6): 0
Pizza sin ingredientes extra
¿Envío a domicilio? (s/n): s
¿Tienes carné de estudiante? (s/n): s
Distancia en km: 12
Fuera de la zona de reparto: tendrás que recogerla
Se aplica un 15 % de descuento
Pedido para recoger | Espera: 20 min | Total: 5.95 €
```

??? success "Solución"
    ```python
    PRECIO_PEQUENA = 7.00
    PRECIO_MEDIANA = 9.50
    PRECIO_FAMILIAR = 14.00
    PRECIO_EXTRA = 1.20
    PRECIO_EXTRA_OFERTA = 0.80     # a partir de 3 ingredientes extra
    MAX_EXTRAS = 6
    ENVIO_CERCA = 1.50
    ENVIO_LEJOS = 3.50
    DISTANCIA_MAXIMA = 10          # km
    DESCUENTO = 0.15

    tamano = input("Tamaño (pequena/mediana/familiar): ")

    match tamano:
        case "pequena" | "p":
            precio = PRECIO_PEQUENA
        case "mediana" | "m":
            precio = PRECIO_MEDIANA
        case "familiar" | "f":
            precio = PRECIO_FAMILIAR
        case _:
            precio = 0.0

    if precio == 0:
        print("Tamaño no válido")
    else:
        extras = int(input(f"Ingredientes extra (0-{MAX_EXTRAS}): "))

        if extras < 0 or extras > MAX_EXTRAS:
            print("Número de ingredientes no válido")
        else:
            # Precio de los ingredientes extra
            if extras == 0:
                print("Pizza sin ingredientes extra")
            elif extras <= 2:
                precio += extras * PRECIO_EXTRA
            else:
                precio += extras * PRECIO_EXTRA_OFERTA

            domicilio = input("¿Envío a domicilio? (s/n): ") == "s"
            estudiante = input("¿Tienes carné de estudiante? (s/n): ") == "s"

            # Gastos de envío (condicional anidado)
            if domicilio:
                distancia = float(input("Distancia en km: "))
                if distancia > DISTANCIA_MAXIMA:
                    print("Fuera de la zona de reparto: tendrás que recogerla")
                    domicilio = False
                elif distancia > 3:
                    precio += ENVIO_LEJOS
                else:
                    precio += ENVIO_CERCA

            # Descuento (condición compuesta)
            if (estudiante and not domicilio) or precio >= 20:
                precio -= precio * DESCUENTO
                print("Se aplica un 15 % de descuento")

            espera = "45 min" if domicilio else "20 min"
            entrega = "a domicilio" if domicilio else "para recoger"

            print(f"Pedido {entrega} | Espera: {espera} | "
                  f"Total: {precio:.2f} €")
    ```

    - El `match` deja el precio a `0` cuando el tamaño no es válido; el `if` de después decide si se sigue o no.
    - En el tercer ejemplo, al quedar fuera de la zona, `domicilio` pasa a `False`: por eso luego se aplica el descuento de estudiante.

---

## Ejercicio 2 ★★ · Registro semanal de entrenamiento

!!! abstract "Repasa"
    [a) Estructuras de selección](a-seleccion.md) · [b) Estructuras de repetición](b-repeticion.md)

Una aplicación de deporte registra los entrenamientos de **una semana** y calcula las calorías gastadas.

1. Recorre los **7 días** con un `for` y `range()`, mostrando `Día 1`, `Día 2`...
2. Cada día, pide la **actividad** y obtén las calorías por minuto con `match`:

    | Actividad | Se acepta | kcal por minuto |
    |---|---|---|
    | Correr | `correr` o `c` | 10 |
    | Bicicleta | `bici` o `b` | 7 |
    | Natación | `nadar` o `n` | 9 |

    Cualquier otra respuesta cuenta como **día de descanso**: muestra `Día de descanso` y pasa al día siguiente.

3. Si ha entrenado:
    - Pide los **minutos** (de 1 a 240). Si no son válidos, muestra `Minutos no válidos` y **vuelve a pedirlos** con un `while`.
    - Pregunta si la intensidad ha sido **alta** (`s`/`n`).
    - Calorías = minutos × kcal por minuto. Si la intensidad es alta **y** ha durado 45 minutos o más, las calorías suben un 10 %.
    - Muestra las calorías de ese día sin decimales.
4. Durante el bucle, lleva la cuenta de: días entrenados, minutos totales, sesiones de cada actividad y sesiones intensas (**contadores**); calorías totales (**acumulador**); y el **mejor día** (el de más calorías) con su número (**máximo**).
5. Al terminar, muestra el resumen:
    - `día` o `días` según la cantidad, con un ternario.
    - Una barra de `=` por cada actividad (un `=` por sesión).
    - Calorías totales y, solo si ha entrenado algún día, la media por sesión y el mejor día.

```text
Día 1
Actividad (correr/bici/nadar/descanso): correr
Minutos (1-240): 50
¿Intensidad alta? (s/n): s
Calorías: 550 kcal

Día 2
Actividad (correr/bici/nadar/descanso): descanso
Día de descanso

Día 3
Actividad (correr/bici/nadar/descanso): bici
Minutos (1-240): 300
Minutos no válidos
Minutos (1-240): 90
¿Intensidad alta? (s/n): n
Calorías: 630 kcal

Día 4
Actividad (correr/bici/nadar/descanso): nadar
Minutos (1-240): 30
¿Intensidad alta? (s/n): s
Calorías: 270 kcal

Día 5
Actividad (correr/bici/nadar/descanso): c
Minutos (1-240): 20
¿Intensidad alta? (s/n): n
Calorías: 200 kcal

Día 6
Actividad (correr/bici/nadar/descanso): yoga
Día de descanso

Día 7
Actividad (correr/bici/nadar/descanso): b
Minutos (1-240): 60
¿Intensidad alta? (s/n): s
Calorías: 462 kcal

--- RESUMEN SEMANAL ---
Has entrenado 5 días (250 min) | Sesiones intensas: 2
Correr: ==
Bici:   ==
Nadar:  =
Calorías totales: 2112 kcal
Media por sesión: 422 kcal
Mejor día: el 3 con 630 kcal
```

??? success "Solución"
    ```python
    DIAS = 7
    KCAL_CORRER = 10       # kcal por minuto
    KCAL_BICI = 7
    KCAL_NADAR = 9
    MAX_MINUTOS = 240
    BONUS_INTENSO = 1.10   # +10 % si la sesión es larga e intensa

    total_kcal = 0.0
    minutos_totales = 0
    dias_activos = 0
    correr = 0
    bici = 0
    nadar = 0
    sesiones_intensas = 0
    mejor_kcal = 0.0
    mejor_dia = 0

    for dia in range(1, DIAS + 1):
        print(f"\nDía {dia}")
        actividad = input("Actividad (correr/bici/nadar/descanso): ")

        match actividad:
            case "correr" | "c":
                kcal_minuto = KCAL_CORRER
                correr += 1
            case "bici" | "b":
                kcal_minuto = KCAL_BICI
                bici += 1
            case "nadar" | "n":
                kcal_minuto = KCAL_NADAR
                nadar += 1
            case _:
                kcal_minuto = 0

        if kcal_minuto == 0:
            print("Día de descanso")
        else:
            # Validación de los minutos
            minutos = int(input(f"Minutos (1-{MAX_MINUTOS}): "))
            while minutos < 1 or minutos > MAX_MINUTOS:
                print("Minutos no válidos")
                minutos = int(input(f"Minutos (1-{MAX_MINUTOS}): "))

            intensa = input("¿Intensidad alta? (s/n): ") == "s"

            kcal = minutos * kcal_minuto
            if intensa and minutos >= 45:
                kcal *= BONUS_INTENSO
                sesiones_intensas += 1

            print(f"Calorías: {kcal:.0f} kcal")

            total_kcal += kcal
            minutos_totales += minutos
            dias_activos += 1
            if kcal > mejor_kcal:
                mejor_kcal = kcal
                mejor_dia = dia

    print("\n--- RESUMEN SEMANAL ---")
    palabra = "día" if dias_activos == 1 else "días"
    print(f"Has entrenado {dias_activos} {palabra} "
          f"({minutos_totales} min) | Sesiones intensas: {sesiones_intensas}")
    print(f"Correr: {'=' * correr}")
    print(f"Bici:   {'=' * bici}")
    print(f"Nadar:  {'=' * nadar}")
    print(f"Calorías totales: {total_kcal:.0f} kcal")
    if dias_activos > 0:
        print(f"Media por sesión: {total_kcal / dias_activos:.0f} kcal")
        print(f"Mejor día: el {mejor_dia} con {mejor_kcal:.0f} kcal")
    ```

    - El día 4 tiene intensidad alta, pero dura menos de 45 minutos: no se aplica el 10 %.
    - Si los 7 días son de descanso, `dias_activos` vale `0` y no se calculan la media ni el mejor día (se evita dividir entre cero).

---

## Ejercicio 3 ★★ · Taquilla de un concierto

!!! abstract "Repasa"
    [a) Estructuras de selección](a-seleccion.md) · [b) Estructuras de repetición](b-repeticion.md) · [c) Estructuras de salto](c-salto.md)

Una sala de conciertos tiene **40 butacas** (4 filas de 10). Programa la taquilla, que vende entradas compra a compra hasta que se cierra o se agotan.

1. Usa un bucle `while True`. En cada vuelta pide cuántas entradas se quieren comprar, indicando cuántas quedan:
    - `0` es el **centinela**: cierra la taquilla con `break`.
    - Menos de 1 o más de 6 entradas: muestra `Se pueden comprar de 1 a 6 entradas` y pasa a la siguiente compra con `continue`.
    - Más entradas de las que quedan: muestra `Solo quedan X entradas` y `continue`.
2. Pide el **tipo de entrada** con `match`: `general`/`g` (18 €), `reducida`/`r` (12 €) o `vip`/`v` (35 €). Si no es ninguno, avisa y `continue`.
3. Importe = entradas × precio. Se suman **1,50 € de gastos de gestión**, salvo que la compra sea de 4 entradas o más, o sea VIP (escríbelo en **un solo `if`**).
4. Actualiza las entradas vendidas, el número de compras, lo recaudado, las entradas de cada tipo y la compra más alta. Muestra `X entrada(s): Y €`, con `entrada` o `entradas` según la cantidad (ternario).
5. Si se venden todas las butacas, muestra `¡Entradas agotadas!` y sal con `break`.
6. Al cerrar, muestra el resumen (vendidas por tipo, recaudado, compra más alta y, si hay compras, el importe medio) y un **mapa de la sala** con **bucles anidados**: una línea por fila y, en cada una, `X` si la butaca está vendida y `_` si está libre. Las butacas se van ocupando en orden, de la primera de la fila 1 en adelante.

```text
Entradas (quedan 40, 0 para cerrar): 3
Tipo (general/reducida/vip): g
3 entradas: 55.50 €

Entradas (quedan 37, 0 para cerrar): 8
Se pueden comprar de 1 a 6 entradas

Entradas (quedan 37, 0 para cerrar): 6
Tipo (general/reducida/vip): vip
6 entradas: 210.00 €

Entradas (quedan 31, 0 para cerrar): 5
Tipo (general/reducida/vip): r
5 entradas: 60.00 €

Entradas (quedan 26, 0 para cerrar): 4
Tipo (general/reducida/vip): butaca
Tipo de entrada no válido

Entradas (quedan 26, 0 para cerrar): 1
Tipo (general/reducida/vip): v
1 entrada: 35.00 €

Entradas (quedan 25, 0 para cerrar): 0

--- TAQUILLA CERRADA ---
Vendidas: 15 | General: 3 | Reducida: 5 | VIP: 7
Recaudado: 360.50 € | Compra más alta: 210.00 €
Importe medio por compra: 90.12 €
Fila 1: X X X X X X X X X X
Fila 2: X X X X X _ _ _ _ _
Fila 3: _ _ _ _ _ _ _ _ _ _
Fila 4: _ _ _ _ _ _ _ _ _ _
```

??? success "Solución"
    ```python
    AFORO = 40
    FILAS = 4
    ASIENTOS_POR_FILA = 10
    MAX_POR_COMPRA = 6
    PRECIO_GENERAL = 18.00
    PRECIO_REDUCIDA = 12.00
    PRECIO_VIP = 35.00

    vendidas = 0
    compras = 0
    recaudado = 0.0
    general = 0
    reducida = 0
    vip = 0
    compra_mayor = 0.0

    while True:
        libres = AFORO - vendidas
        cantidad = int(input(f"\nEntradas (quedan {libres}, 0 para cerrar): "))

        if cantidad == 0:
            break

        if cantidad < 0 or cantidad > MAX_POR_COMPRA:
            print(f"Se pueden comprar de 1 a {MAX_POR_COMPRA} entradas")
            continue

        if cantidad > libres:
            print(f"Solo quedan {libres} entradas")
            continue

        tipo = input("Tipo (general/reducida/vip): ")

        match tipo:
            case "general" | "g":
                precio = PRECIO_GENERAL
                general += cantidad
            case "reducida" | "r":
                precio = PRECIO_REDUCIDA
                reducida += cantidad
            case "vip" | "v":
                precio = PRECIO_VIP
                vip += cantidad
            case _:
                print("Tipo de entrada no válido")
                continue

        importe = cantidad * precio

        # Gastos de gestión: gratis si la compra es grande o es VIP
        if cantidad < 4 and precio != PRECIO_VIP:
            importe += 1.50

        vendidas += cantidad
        compras += 1
        recaudado += importe
        if importe > compra_mayor:
            compra_mayor = importe

        palabra = "entrada" if cantidad == 1 else "entradas"
        print(f"{cantidad} {palabra}: {importe:.2f} €")

        if vendidas == AFORO:
            print("¡Entradas agotadas!")
            break

    print("\n--- TAQUILLA CERRADA ---")
    print(f"Vendidas: {vendidas} | General: {general} | Reducida: {reducida} "
          f"| VIP: {vip}")
    print(f"Recaudado: {recaudado:.2f} € | Compra más alta: {compra_mayor:.2f} €")
    if compras > 0:
        print(f"Importe medio por compra: {recaudado / compras:.2f} €")

    # Mapa de la sala: X vendido, _ libre
    asiento = 1
    for fila in range(1, FILAS + 1):
        print(f"Fila {fila}: ", end="")
        for _ in range(ASIENTOS_POR_FILA):
            print("X" if asiento <= vendidas else "_", end=" ")
            asiento += 1
        print()
    ```

    - Cada `continue` descarta la compra y vuelve a preguntar, sin anidar el resto del código dentro de `else`.
    - Hay dos formas de salir del bucle: el centinela `0` y las entradas agotadas. Las dos usan `break`.
    - En el mapa, la variable `asiento` cuenta las butacas de 1 a 40 a lo largo de los dos bucles.

---

## Ejercicio 4 ★★★ · Repostajes de una flota de vehículos

!!! abstract "Repasa"
    [a) Estructuras de selección](a-seleccion.md) · [b) Estructuras de repetición](b-repeticion.md) · [c) Estructuras de salto](c-salto.md) · [d) Control de excepciones](d-excepciones.md)

Una empresa de alquiler de vehículos anota cada repostaje de su flota para controlar el gasto y el consumo. **El programa nunca debe detenerse con una traza**, aunque se escriban datos incorrectos.

1. Un bucle `while True` registra repostajes uno a uno.
2. Pide el **número de vehículo** (entero del 1 al 99; `0` para terminar). Valídalo con el patrón `while True` + `try` / `except` + `break`, con un mensaje distinto si no es un entero o si está fuera de rango. Con `0`, termina con `break`.
3. Pide el **combustible** con `match`: `gasolina`/`g` (1,62 €/L) o `diesel`/`d` (1,54 €/L). Si no es ninguno, muestra `Combustible desconocido. Repostaje no registrado` y `continue`.
4. Pide los **litros** (mayor que 0 y hasta 80) y los **km recorridos desde el último repostaje** (0 o más). Valida los dos con el mismo patrón.
5. Calcula y muestra el **importe** (litros × precio por litro).
6. Calcula el **consumo** en litros cada 100 km (`litros / km * 100`) dentro de un `try`:
    - Clasifícalo: menos de 5 → `eficiente`; menos de 8 → `normal`; menos de 12 → `alto`; resto → `revisar el vehículo`.
    - Si los km son **0**, se produce `ZeroDivisionError`: captúralo y muestra `Sin kilómetros recorridos: no se calcula el consumo`.
    - En un `finally`, muestra siempre `--- Repostaje del vehículo X guardado ---`.
7. Lleva la cuenta de repostajes, repostajes sin consumo calculado, litros y gasto total, y guarda el **vehículo más eficiente** (el de consumo más bajo).
8. Al terminar, muestra el informe. Si no hay ningún consumo calculado, indícalo.

```text
Vehículo (1-99, 0 para terminar): dos
El número de vehículo debe ser un entero

Vehículo (1-99, 0 para terminar): 150
Número de vehículo fuera de rango

Vehículo (1-99, 0 para terminar): 12
Combustible (gasolina/diesel): g
Litros (hasta 80): 40
Km desde el último repostaje: 650
Importe: 64.80 €
Consumo: 6.2 L/100 km (normal)
--- Repostaje del vehículo 12 guardado ---

Vehículo (1-99, 0 para terminar): 7
Combustible (gasolina/diesel): electrico
Combustible desconocido. Repostaje no registrado

Vehículo (1-99, 0 para terminar): 31
Combustible (gasolina/diesel): d
Litros (hasta 80): cero
Escribe un número (usa punto decimal)
Litros (hasta 80): 0
Los litros deben ser mayores que 0 y hasta 80
Litros (hasta 80): 55.5
Km desde el último repostaje: -20
Los kilómetros no pueden ser negativos
Km desde el último repostaje: 0
Importe: 85.47 €
Sin kilómetros recorridos: no se calcula el consumo
--- Repostaje del vehículo 31 guardado ---

Vehículo (1-99, 0 para terminar): 8
Combustible (gasolina/diesel): diesel
Litros (hasta 80): 30
Km desde el último repostaje: 240
Importe: 46.20 €
Consumo: 12.5 L/100 km (revisar el vehículo)
--- Repostaje del vehículo 8 guardado ---

Vehículo (1-99, 0 para terminar): 0

--- INFORME DE LA FLOTA ---
Repostajes: 3 | Sin consumo calculado: 1
Litros: 125.50 | Gasto: 196.47 €
Gasto medio por repostaje: 65.49 €
Vehículo más eficiente: 12 con 6.2 L/100 km
```

??? success "Solución"
    ```python
    MAX_VEHICULO = 99
    PRECIO_GASOLINA = 1.62     # € por litro
    PRECIO_DIESEL = 1.54
    MAX_LITROS = 80

    repostajes = 0
    sin_consumo = 0
    litros_totales = 0.0
    gasto_total = 0.0
    mejor_consumo = -1         # -1: todavía no hay ningún consumo
    mejor_vehiculo = 0

    while True:
        # Número de vehículo (0 para terminar)
        while True:
            try:
                texto = f"\nVehículo (1-{MAX_VEHICULO}, 0 para terminar): "
                vehiculo = int(input(texto))
                if 0 <= vehiculo <= MAX_VEHICULO:
                    break
                print("Número de vehículo fuera de rango")
            except ValueError:
                print("El número de vehículo debe ser un entero")

        if vehiculo == 0:
            break

        combustible = input("Combustible (gasolina/diesel): ")
        match combustible:
            case "gasolina" | "g":
                precio_litro = PRECIO_GASOLINA
            case "diesel" | "d":
                precio_litro = PRECIO_DIESEL
            case _:
                print("Combustible desconocido. Repostaje no registrado")
                continue

        # Litros repostados
        while True:
            try:
                litros = float(input(f"Litros (hasta {MAX_LITROS}): "))
                if 0 < litros <= MAX_LITROS:
                    break
                print(f"Los litros deben ser mayores que 0 y hasta {MAX_LITROS}")
            except ValueError:
                print("Escribe un número (usa punto decimal)")

        # Kilómetros desde el último repostaje
        while True:
            try:
                km = float(input("Km desde el último repostaje: "))
                if km >= 0:
                    break
                print("Los kilómetros no pueden ser negativos")
            except ValueError:
                print("Escribe un número (usa punto decimal)")

        importe = litros * precio_litro
        repostajes += 1
        litros_totales += litros
        gasto_total += importe
        print(f"Importe: {importe:.2f} €")

        try:
            consumo = litros / km * 100        # litros cada 100 km
            if consumo < 5:
                nivel = "eficiente"
            elif consumo < 8:
                nivel = "normal"
            elif consumo < 12:
                nivel = "alto"
            else:
                nivel = "revisar el vehículo"
            print(f"Consumo: {consumo:.1f} L/100 km ({nivel})")

            if mejor_consumo < 0 or consumo < mejor_consumo:
                mejor_consumo = consumo
                mejor_vehiculo = vehiculo
        except ZeroDivisionError:
            print("Sin kilómetros recorridos: no se calcula el consumo")
            sin_consumo += 1
        finally:
            print(f"--- Repostaje del vehículo {vehiculo} guardado ---")

    print("\n--- INFORME DE LA FLOTA ---")
    print(f"Repostajes: {repostajes} | Sin consumo calculado: {sin_consumo}")
    print(f"Litros: {litros_totales:.2f} | Gasto: {gasto_total:.2f} €")
    if repostajes > 0:
        print(f"Gasto medio por repostaje: {gasto_total / repostajes:.2f} €")
    if mejor_consumo < 0:
        print("No hay consumos calculados")
    else:
        print(f"Vehículo más eficiente: {mejor_vehiculo} "
              f"con {mejor_consumo:.1f} L/100 km")
    ```

    - Cada dato numérico tiene su propio bucle de validación: si falla, solo se repite **esa** pregunta.
    - `mejor_consumo` empieza en `-1` para saber que todavía no hay ningún consumo con el que comparar.
    - El `finally` se ejecuta tanto si el consumo se calcula como si salta el `ZeroDivisionError`.

---

## Ejercicio 5 ★★★ · Monedero de un videojuego

!!! abstract "Repasa"
    Toda la unidad: [a) Selección](a-seleccion.md) · [b) Repetición](b-repeticion.md) · [c) Salto](c-salto.md) · [d) Excepciones](d-excepciones.md), incluidos `raise` y las excepciones propias.

Un videojuego tiene una tienda donde se compran **gemas** con dinero real y, con las gemas, objetos para el personaje. Programa el monedero de **una sesión de juego**.

1. **Excepciones propias.** Define tres excepciones que hereden de `Exception`, cada una con su docstring:
    - `PackNoPermitidoError`: la cuenta no puede comprar ese pack de gemas.
    - `LimiteGastoError`: la compra supera el gasto máximo de la sesión.
    - `CompraRechazadaError`: no hay gemas suficientes para el objeto.
2. **Alta de la cuenta.** Pide la edad del jugador con el patrón de validación. Si no está entre 0 y 120, **lanza** un `ValueError` con el mensaje `La edad debe estar entre 0 y 120`. Captúralo con `except ValueError as error` y muestra `Dato no válido:` seguido del mensaje.
    - Menores de 14 años tienen cuenta `INFANTIL`; el resto, `ESTÁNDAR` (ternario). Muestra `Cuenta X creada`.
3. **Menú** que se repite con `while True` y se resuelve con `match`:

    ```text
    1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
    ```

4. **Comprar gemas.** Pide el pack con `match` (`1`: 100 gemas por 1,99 €; `2`: 550 gemas por 9,99 €; `3`: 1200 gemas por 19,99 €). Si no existe, avisa y vuelve al menú con `continue`. Después:
    - Una cuenta infantil no puede comprar el pack 3 → lanza `PackNoPermitidoError`.
    - En una sesión no se pueden gastar más de **30 €** → lanza `LimiteGastoError` indicando cuánto se puede gastar todavía.
    - Captura las dos excepciones **en un mismo `except`** y muestra `Compra cancelada:` seguido del mensaje.
    - En un `finally`, muestra siempre las gemas.
5. **Comprar objeto.** Pide el objeto con `match`: `espada` (300 gemas), `escudo` (200) o `pocion`/`poción` (50). Si no existe, avisa y `continue`. Después:
    - **Hora feliz** (de 13 a 14 o de 20 a 22, ambas incluidas): el objeto cuesta un 20 % menos (redondea a un número entero de gemas con `int()`). La hora se obtiene con `datetime`.
    - Si no hay gemas suficientes, lanza `CompraRechazadaError` con un mensaje como `Necesitas 300 gemas y tienes 0`, captúralo y muestra `Compra rechazada:` seguido del mensaje.
    - Si hay gemas, réstalas y muestra el objeto conseguido. **Cada 5 objetos** se regalan 25 gemas de bonus.
    - En un `finally`, muestra siempre las gemas.
6. **Inventario.** Muestra tipo de cuenta, gemas, objetos y dinero gastado, y una barra hacia el próximo bonus dibujada con un `for` y un ternario: `★` por cada objeto conseguido de la tanda actual de 5 y `☆` por cada uno pendiente.
7. **Salir** con la opción `4`. Si se eligen **3 opciones no válidas seguidas**, muestra `Demasiados errores seguidos. Sesión cerrada` y sal también. Una opción válida pone el contador de errores a cero.
8. Al salir, muestra el resumen: objetos, gemas y dinero gastado.

!!! tip "Para probar la hora feliz"
    Cambia temporalmente `datetime.now().hour` por un valor fijo (`hora = 21`, `hora = 10`...) para comprobar los dos casos.

Ejemplo realizado a las 10 h (fuera de la hora feliz):

```text
Edad del jugador: abc
Dato no válido: invalid literal for int() with base 10: 'abc'
Edad del jugador: 200
Dato no válido: La edad debe estar entre 0 y 120
Edad del jugador: 12
Cuenta INFANTIL creada

1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
Opción: 2
Objeto (espada/escudo/pocion): espada
Compra rechazada: Necesitas 300 gemas y tienes 0
Gemas: 0

1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
Opción: 1
Pack (1: 100 gemas, 2: 550 gemas, 3: 1200 gemas): 3
Compra cancelada: Las cuentas infantiles no pueden comprar este pack
Gemas: 0

1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
Opción: 1
Pack (1: 100 gemas, 2: 550 gemas, 3: 1200 gemas): 2
Has comprado 550 gemas por 9.99 €
Gemas: 550

1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
Opción: 1
Pack (1: 100 gemas, 2: 550 gemas, 3: 1200 gemas): 2
Has comprado 550 gemas por 9.99 €
Gemas: 1100

1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
Opción: 2
Objeto (espada/escudo/pocion): espada
Has conseguido: espada (300 gemas)
Gemas: 800

1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
Opción: 2
Objeto (espada/escudo/pocion): lanza
Ese objeto no está en la tienda

1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
Opción: 3
Cuenta INFANTIL | Gemas: 800 | Objetos: 1 | Gastado: 19.98 €
Próximo bonus: ★ ☆ ☆ ☆ ☆

1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir
Opción: 4

--- FIN DE LA SESIÓN ---
Objetos: 1 | Gemas: 800 | Gastado: 19.98 €
```

??? success "Solución"
    ```python
    from datetime import datetime

    LIMITE_GASTO = 30.00         # € como máximo por sesión
    EDAD_INFANTIL = 14
    GEMAS_PEQUENO = 100
    PRECIO_PEQUENO = 1.99
    GEMAS_MEDIANO = 550
    PRECIO_MEDIANO = 9.99
    GEMAS_GRANDE = 1200
    PRECIO_GRANDE = 19.99
    COSTE_ESPADA = 300           # gemas
    COSTE_ESCUDO = 200
    COSTE_POCION = 50
    DESCUENTO_HORA_FELIZ = 0.20
    OBJETOS_PARA_BONUS = 5
    GEMAS_BONUS = 25
    MAX_ERRORES = 3


    class PackNoPermitidoError(Exception):
        """La cuenta no puede comprar ese pack de gemas."""


    class LimiteGastoError(Exception):
        """La compra supera el gasto máximo de la sesión."""


    class CompraRechazadaError(Exception):
        """No hay gemas suficientes para el objeto."""


    # Edad del jugador
    while True:
        try:
            edad = int(input("Edad del jugador: "))
            if edad < 0 or edad > 120:
                raise ValueError("La edad debe estar entre 0 y 120")
            break
        except ValueError as error:
            print("Dato no válido:", error)

    infantil = edad < EDAD_INFANTIL
    tipo_cuenta = "INFANTIL" if infantil else "ESTÁNDAR"
    print(f"Cuenta {tipo_cuenta} creada")

    gemas = 0
    gastado = 0.0
    objetos = 0
    errores = 0

    while True:
        print("\n1. Comprar gemas  2. Comprar objeto  3. Inventario  4. Salir")
        opcion = input("Opción: ")

        match opcion:
            case "1":
                errores = 0
                pack = input("Pack (1: 100 gemas, 2: 550 gemas, 3: 1200 gemas): ")
                match pack:
                    case "1":
                        cantidad, precio = GEMAS_PEQUENO, PRECIO_PEQUENO
                    case "2":
                        cantidad, precio = GEMAS_MEDIANO, PRECIO_MEDIANO
                    case "3":
                        cantidad, precio = GEMAS_GRANDE, PRECIO_GRANDE
                    case _:
                        print("Pack no válido")
                        continue

                try:
                    if infantil and pack == "3":
                        raise PackNoPermitidoError(
                            "Las cuentas infantiles no pueden comprar este pack"
                        )
                    if gastado + precio > LIMITE_GASTO:
                        disponible = LIMITE_GASTO - gastado
                        raise LimiteGastoError(
                            f"Solo puedes gastar {disponible:.2f} € más"
                        )
                    gemas += cantidad
                    gastado += precio
                    print(f"Has comprado {cantidad} gemas por {precio:.2f} €")
                except (PackNoPermitidoError, LimiteGastoError) as error:
                    print("Compra cancelada:", error)
                finally:
                    print(f"Gemas: {gemas}")

            case "2":
                errores = 0
                objeto = input("Objeto (espada/escudo/pocion): ")
                match objeto:
                    case "espada":
                        coste = COSTE_ESPADA
                    case "escudo":
                        coste = COSTE_ESCUDO
                    case "pocion" | "poción":
                        coste = COSTE_POCION
                    case _:
                        print("Ese objeto no está en la tienda")
                        continue

                hora = datetime.now().hour
                if 13 <= hora <= 14 or 20 <= hora <= 22:
                    coste = int(coste - coste * DESCUENTO_HORA_FELIZ)
                    print("¡Hora feliz! 20 % de descuento")

                try:
                    if coste > gemas:
                        raise CompraRechazadaError(
                            f"Necesitas {coste} gemas y tienes {gemas}"
                        )
                    gemas -= coste
                    objetos += 1
                    print(f"Has conseguido: {objeto} ({coste} gemas)")
                    if objetos % OBJETOS_PARA_BONUS == 0:
                        gemas += GEMAS_BONUS
                        print(f"¡Bonus por {objetos} objetos: "
                              f"+{GEMAS_BONUS} gemas!")
                except CompraRechazadaError as error:
                    print("Compra rechazada:", error)
                finally:
                    print(f"Gemas: {gemas}")

            case "3":
                errores = 0
                print(f"Cuenta {tipo_cuenta} | Gemas: {gemas} | "
                      f"Objetos: {objetos} | Gastado: {gastado:.2f} €")
                print("Próximo bonus: ", end="")
                for i in range(1, OBJETOS_PARA_BONUS + 1):
                    conseguido = i <= objetos % OBJETOS_PARA_BONUS
                    print("★" if conseguido else "☆", end=" ")
                print()

            case "4":
                break

            case _:
                errores += 1
                print(f"Opción no válida ({errores}/{MAX_ERRORES})")
                if errores == MAX_ERRORES:
                    print("Demasiados errores seguidos. Sesión cerrada")
                    break

    print("\n--- FIN DE LA SESIÓN ---")
    print(f"Objetos: {objetos} | Gemas: {gemas} | Gastado: {gastado:.2f} €")
    ```

    - Las tres excepciones propias hacen que cada problema tenga un nombre claro y se pueda capturar por separado o agrupado.
    - `raise` corta el `try` en ese punto: si salta, las gemas no se suman ni se restan.
    - Prueba a comprar 5 pociones a las 21 h: cada una cuesta 40 gemas y, al conseguir la quinta, aparece el bonus de 25 gemas.

---

!!! info "¿Y ahora?"
    Si has resuelto los cinco ejercicios, haz la [autoevaluación](autoevaluacion.md) y su proyecto de práctica con el formato del examen.
