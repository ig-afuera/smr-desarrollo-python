# c) Estructuras de salto

Las sentencias de salto **alteran el funcionamiento normal de un bucle**: salir de él antes de tiempo, saltarse una vuelta o dejar un hueco vacío.

## 1. `break`: salir del bucle

`break` **termina el bucle inmediatamente** y el programa continúa con la primera instrucción posterior.

```python
# Buscar el primer múltiplo de 7 entre 50 y 100
for n in range(50, 101):
    if n % 7 == 0:
        print("El primero es", n)
        break
```

```text
El primero es 56
```

En el diagrama de flujo, la flecha del `break` **sale del bucle** y se une al camino de salida, aunque queden valores por recorrer.

![Diagrama de flujo de break en un bucle for](img/fd-break.svg)

!!! warning "`break` solo sale del bucle más interno"
    En bucles anidados, `break` termina **únicamente el bucle en el que está**, no todos.

!!! success "Ahora tú"
    **Robot aspirador.** Un robot aspirador empieza con la batería al 100 % y tiene que limpiar las habitaciones de la 1 a la 8. Construye un programa que:

    1. Recorra las habitaciones con un `for`.
    2. Antes de limpiar cada habitación, calcule al azar cuánta batería gastará en ella (entre 10 y 25).
    3. Si la batería **no llega** para esa habitación, muestre `Batería insuficiente para la habitación X. Vuelvo a la base.` y termine el bucle con `break`.
    4. Si llega, reste el gasto y muestre `Habitación X limpia. Batería: Y %`.
    5. Al final, si ha limpiado todas, muestre `¡Casa limpia!`.

    Para el gasto al azar usa el módulo **`random`** que viste en el [condicional doble](a-seleccion.md#3-condicional-doble-if-else): `random.randint(10, 25)` devuelve un entero al azar entre 10 y 25, ambos incluidos.

## 2. `continue`: saltar a la siguiente iteración

`continue` **se salta el resto del bloque** en la vuelta actual y pasa directamente a la siguiente iteración.

```python
# Mostrar solo los números impares del 1 al 10
for n in range(1, 11):
    if n % 2 == 0:
        continue          # los pares se saltan
    print(n)
```

```text
1
3
5
7
9
```

Cuando se llega al `continue`, el resto del cuerpo (`print(n)`) se salta y la flecha vuelve al inicio del bucle, con el siguiente valor:

![Diagrama de flujo de continue](img/fd-continue.svg)

Con `while` hay que tener cuidado de actualizar el contador **antes** del `continue`, o el bucle se quedará atascado:

```python
i = 0
while i < 10:
    i += 1                # ← actualizamos antes del continue
    if i % 2 == 0:
        continue
    print(i)
```

!!! success "Ahora tú"
    **El juego del número prohibido.** En este juego se cuenta del 1 al 50, pero está prohibido decir los números que:

    - son **múltiplos de 3**, o
    - **terminan en 3** (como el 13 o el 43).

    En su lugar se dice `¡Pum!`. Construye un programa que muestre la secuencia completa usando `continue` para saltar el `print` del número cuando esté prohibido:

    ```text
    1
    2
    ¡Pum!
    4
    5
    ¡Pum!
    ...
    ```

    Al final muestra cuántos `¡Pum!` ha habido. Pista: la última cifra de un número es `n % 10`.

## 3. Uso adecuado de las sentencias de salto

`break` y `continue` son útiles, pero abusar de ellos complica seguir el flujo del programa.

| Situación | Recomendación |
|---|---|
| Buscar algo y parar al encontrarlo | `break` es adecuado. |
| Menú que se repite hasta elegir «salir» | `while True` + `break`. |
| Saltar elementos que no interesan | `continue` va bien si evita anidar demasiado. |
| Varios `break`/`continue` en el mismo bucle | Replantea la condición del bucle: quizá se lea mejor. |

Alternativas que a veces dan un código más claro:

**Usar una variable «bandera»** (*flag*) que controle el bucle:

```python
salir = False
while not salir:
    opcion = input("Opción (s para salir): ")
    if opcion == "s":
        salir = True
    else:
        print("Has elegido", opcion)
```

**Poner la condición de parada en el propio `while`:**

```python
# En lugar de while True + break
texto = input("Texto (fin para terminar): ")
while texto != "fin":
    print("Recibido:", texto)
    texto = input("Texto (fin para terminar): ")
```

**Usar `continue` con moderación**, mejor un `if` positivo:

```python
# Con continue
for n in range(1, 11):
    if n % 2 == 0:
        continue
    print(n)

# Sin continue (igual de claro)
for n in range(1, 11):
    if n % 2 != 0:
        print(n)
```

!!! success "Ahora tú"
    **Reproductor de música sin `break`.** Construye el menú de un reproductor que se repita hasta que el usuario quiera salir, **sin usar `break`**, controlándolo con una variable bandera:

    | Tecla | Acción |
    |---|---|
    | `p` | Muestra `▶ Reproduciendo canción X` |
    | `s` | Pasa a la siguiente canción (hay 10; después de la 10 vuelve a la 1) y la muestra |
    | `a` | Vuelve a la canción anterior (antes de la 1 va a la 10) y la muestra |
    | `q` | Muestra `Apagando reproductor` y termina |

    La canción actual se guarda en una variable que empieza en 1. Si la tecla no es válida, avisa.

## Resumen

| Sentencia | Efecto |
|---|---|
| `break` | Sale del bucle actual. |
| `continue` | Salta a la siguiente iteración. |
| `pass` | No hace nada (marcador de posición). |

Úsalas cuando simplifiquen el código, no como sustituto de una buena condición de bucle.
