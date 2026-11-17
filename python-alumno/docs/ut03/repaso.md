# Ejercicios de repaso UT03

Cinco ejercicios para repasar la unidad **de menos a más**. Cada ejercicio usa lo que ya has practicado en el anterior y añade algo nuevo, así que **hazlos en orden**.

| Ejercicio | Caso | Dificultad | Repasa |
|---|---|---|---|
| 1 | Patinetes eléctricos compartidos | ★ | a) Definición, parámetros y `return` |
| 2 | Encuesta de satisfacción de un hotel | ★★ | a) Validación en funciones · Retorno múltiple · Documentación |
| 3 | Planificador de rutas de senderismo | ★★ | a) Módulos propios · `math` · `__name__` · Pruebas |
| 4 | Caja fuerte de un hotel | ★★★ | a) Funciones · b) Recursividad |
| 5 | Hucha digital | ★★★ | Toda la unidad |

!!! tip "Cómo aprovecharlos"
    1. Lee el enunciado entero antes de escribir código. Decide primero **qué funciones** vas a necesitar y qué recibe y devuelve cada una.
    2. Programa y **prueba cada función por separado** antes de escribir el programa principal.
    3. Usa **constantes** para los valores fijos y muestra los importes con 2 decimales.
    4. Mira la solución solo cuando tu programa funcione o estés atascado/a.

---

## Ejercicio 1 ★ · Patinetes eléctricos compartidos

!!! abstract "Repasa"
    [a) Definir y llamar](a-funciones.md#2-definir-y-llamar-a-una-funcion) · [Parámetros](a-funciones.md#3-parametros-y-argumentos) · [`return`](a-funciones.md#4-valor-de-retorno-return)

Una empresa de patinetes eléctricos quiere calcular el precio de cada viaje.

1. Define estas **constantes**: desbloqueo 1,00 €, minuto 0,25 €, minuto con abono 0,18 € y 60 minutos como límite de la tarifa normal.
2. Escribe la función `coste_viaje(minutos, abonado=False)`, que **devuelva** el precio del viaje:
    - Se usa el precio del minuto con abono o sin él según el parámetro `abonado` (ternario).
    - A partir del minuto 61, cada minuto cuesta **la mitad**.
    - Los abonados **no pagan** el desbloqueo.
3. Escribe la función `formatear_duracion(minutos)`, que **devuelva** un texto con la duración, usando **varios `return`** y sin `elif`:
    - Menos de una hora: `45 min`.
    - Horas exactas: `2 h`.
    - En otro caso: `1 h 15 min`.

    Pista: `divmod(minutos, 60)` devuelve las horas y los minutos sobrantes.

4. Escribe la función `mostrar_ticket(minutos, abonado=False)`, que **muestre** el ticket usando las dos funciones anteriores.
5. El programa principal pide los minutos. Si no son mayores que 0, muestra `Duración no válida`. Si no, pregunta si tiene abono y muestra el ticket, pasando `abonado` **por nombre**. Si el cliente **no** es abonado, muestra además cuánto se ahorraría con abono.

```text
Minutos de viaje: 25
¿Tienes abono? (s/n): n
Viaje de 25 min (ocasional): 7.25 €
Con abono te ahorrarías 2.75 €
```

```text
Minutos de viaje: 75
¿Tienes abono? (s/n): s
Viaje de 1 h 15 min (abonado): 12.15 €
```

```text
Minutos de viaje: 120
¿Tienes abono? (s/n): n
Viaje de 2 h (ocasional): 23.50 €
Con abono te ahorrarías 7.30 €
```

??? success "Solución"
    ```python
    DESBLOQUEO = 1.00
    PRECIO_MINUTO = 0.25
    PRECIO_MINUTO_ABONO = 0.18
    MINUTOS_TARIFA_LARGA = 60      # a partir de aquí, el minuto cuesta la mitad


    def coste_viaje(minutos, abonado=False):
        """Devuelve el coste de un viaje en patinete."""
        precio_minuto = PRECIO_MINUTO_ABONO if abonado else PRECIO_MINUTO

        if minutos <= MINUTOS_TARIFA_LARGA:
            coste = minutos * precio_minuto
        else:
            minutos_extra = minutos - MINUTOS_TARIFA_LARGA
            coste = (MINUTOS_TARIFA_LARGA * precio_minuto
                     + minutos_extra * precio_minuto / 2)

        if not abonado:
            coste += DESBLOQUEO
        return coste


    def formatear_duracion(minutos):
        """Devuelve la duración como texto: '45 min', '2 h' o '1 h 15 min'."""
        horas, resto = divmod(minutos, 60)
        if horas == 0:
            return f"{resto} min"
        if resto == 0:
            return f"{horas} h"
        return f"{horas} h {resto} min"


    def mostrar_ticket(minutos, abonado=False):
        """Muestra el ticket de un viaje."""
        tipo = "abonado" if abonado else "ocasional"
        coste = coste_viaje(minutos, abonado)
        print(f"Viaje de {formatear_duracion(minutos)} ({tipo}): {coste:.2f} €")


    minutos = int(input("Minutos de viaje: "))

    if minutos <= 0:
        print("Duración no válida")
    else:
        abonado = input("¿Tienes abono? (s/n): ") == "s"
        mostrar_ticket(minutos, abonado=abonado)

        if not abonado:
            ahorro = coste_viaje(minutos) - coste_viaje(minutos, abonado=True)
            print(f"Con abono te ahorrarías {ahorro:.2f} €")
    ```

    - `coste_viaje` **devuelve** el precio en lugar de mostrarlo: por eso se puede llamar dos veces y restar los resultados para calcular el ahorro.
    - `mostrar_ticket` es la única función que usa `print`: su trabajo es precisamente mostrar.
    - En `formatear_duracion`, cada `return` termina la función, así que no hacen falta `elif` ni `else`.

---

## Ejercicio 2 ★★ · Encuesta de satisfacción de un hotel

!!! abstract "Repasa"
    [Parámetros](a-funciones.md#3-parametros-y-argumentos) · [Retorno múltiple](a-funciones.md#devolver-varios-valores) · [Ámbito](a-funciones.md#6-ambito-de-las-variables) · [Documentación](a-funciones.md#7-documentacion-de-funciones)

Un hotel pide a sus huéspedes que valoren de 1 a 5 la limpieza, la atención y la comida. Programa la encuesta. **Todas las funciones** deben tener docstring y anotaciones de tipo.

1. `pedir_entero(mensaje, minimo, maximo)`: pide un entero con el patrón `while True` + `try` / `except` hasta que esté entre `minimo` y `maximo`, y lo **devuelve**. Muestra `Escribe un número entero` o `Debe estar entre X y Y` según el error. Es el patrón de validación de la UT02, pero escrito **una sola vez**.
2. `media_valoracion(limpieza, atencion, comida)`: devuelve la media de las tres notas.
3. `calificar(media)`: devuelve `Excelente` (4,5 o más), `Buena` (3,5 o más), `Mejorable` (2,5 o más) o `Mala`.
4. `actualizar_extremos(media, mejor, peor)`: devuelve **dos valores**, la mejor y la peor media teniendo en cuenta la nueva.
5. `main()`: el programa principal. **No uses variables globales**: todas las variables viven dentro de `main()`.
    - Pide el número de huéspedes (de 1 a 20).
    - Para cada huésped, pide las tres notas y muestra su media con 2 decimales y su calificación.
    - Al final, muestra la media del hotel con su calificación, la mejor y la peor valoración y, si hay alguna, cuántas valoraciones han sido `Mala`.

```text
Número de huéspedes (1-20): cuatro
Escribe un número entero
Número de huéspedes (1-20): 30
Debe estar entre 1 y 20
Número de huéspedes (1-20): 3

Huésped 1
Limpieza (1-5): 5
Atención (1-5): 4
Comida (1-5): 5
Media: 4.67 → Excelente

Huésped 2
Limpieza (1-5): seis
Escribe un número entero
Limpieza (1-5): 2
Atención (1-5): 1
Comida (1-5): 3
Media: 2.00 → Mala

Huésped 3
Limpieza (1-5): 3
Atención (1-5): 4
Comida (1-5): 9
Debe estar entre 1 y 5
Comida (1-5): 4
Media: 3.67 → Buena

--- RESULTADO DE LA ENCUESTA ---
Media del hotel: 3.44 (Mejorable)
Mejor valoración: 4.67 | Peor valoración: 2.00
Atención: 1 valoración(es) mala(s)
```

??? success "Solución"
    ```python
    """Encuesta de satisfacción de los huéspedes de un hotel."""

    MAX_HUESPEDES = 20


    def pedir_entero(mensaje: str, minimo: int, maximo: int) -> int:
        """Pide un entero hasta que esté entre minimo y maximo (incluidos)."""
        while True:
            try:
                numero = int(input(mensaje))
                if minimo <= numero <= maximo:
                    return numero
                print(f"Debe estar entre {minimo} y {maximo}")
            except ValueError:
                print("Escribe un número entero")


    def media_valoracion(limpieza: int, atencion: int, comida: int) -> float:
        """Devuelve la media de las tres notas."""
        return (limpieza + atencion + comida) / 3


    def calificar(media: float) -> str:
        """Devuelve la calificación en texto según la media."""
        if media >= 4.5:
            return "Excelente"
        if media >= 3.5:
            return "Buena"
        if media >= 2.5:
            return "Mejorable"
        return "Mala"


    def actualizar_extremos(media: float, mejor: float,
                            peor: float) -> tuple[float, float]:
        """Devuelve la mejor y la peor media teniendo en cuenta la nueva."""
        if media > mejor:
            mejor = media
        if media < peor:
            peor = media
        return mejor, peor


    def main() -> None:
        """Programa principal."""
        huespedes = pedir_entero(f"Número de huéspedes (1-{MAX_HUESPEDES}): ",
                                 1, MAX_HUESPEDES)
        suma_medias = 0.0
        malas = 0
        mejor = 0.0          # cualquier media será mayor
        peor = 5.0           # cualquier media será menor o igual

        for huesped in range(1, huespedes + 1):
            print(f"\nHuésped {huesped}")
            limpieza = pedir_entero("Limpieza (1-5): ", 1, 5)
            atencion = pedir_entero("Atención (1-5): ", 1, 5)
            comida = pedir_entero("Comida (1-5): ", 1, 5)

            media = media_valoracion(limpieza, atencion, comida)
            calificacion = calificar(media)
            print(f"Media: {media:.2f} → {calificacion}")

            suma_medias += media
            if calificacion == "Mala":
                malas += 1
            mejor, peor = actualizar_extremos(media, mejor, peor)

        print("\n--- RESULTADO DE LA ENCUESTA ---")
        media_global = suma_medias / huespedes
        print(f"Media del hotel: {media_global:.2f} ({calificar(media_global)})")
        print(f"Mejor valoración: {mejor:.2f} | Peor valoración: {peor:.2f}")
        if malas > 0:
            print(f"Atención: {malas} valoración(es) mala(s)")


    main()
    ```

    - En `pedir_entero`, el `return` sale a la vez del bucle y de la función: no hace falta `break`.
    - `calificar` se usa dos veces, para cada huésped y para la media del hotel. Si cambian los límites, se cambian en un solo sitio.
    - `actualizar_extremos` no modifica `mejor` ni `peor` de `main()` (son números, inmutables): devuelve los nuevos valores y `main()` los asigna.
    - No hay que comprobar que `huespedes` sea mayor que 0 antes de dividir: `pedir_entero` ya garantiza que vale al menos 1.

---

## Ejercicio 3 ★★ · Planificador de rutas de senderismo

!!! abstract "Repasa"
    [Módulos](a-funciones.md#8-funciones-predefinidas-y-modulos) · [Módulos propios](a-funciones.md#9-modulos-propios-y-organizacion-del-codigo) · [Pruebas](a-funciones.md#10-pruebas-y-depuracion-de-funciones)

Un club de montaña quiere planificar rutas por etapas. El programa se divide en **dos ficheros** en la misma carpeta.

**Fichero `ruta.py`** (módulo con los cálculos, sin `input` ni `print` fuera de las pruebas):

1. Constantes: velocidad en llano 4 km/h; 10 minutos extra por cada 100 m de subida; 0,5 L de agua por hora (0,75 L si hace calor).
2. `tiempo_etapa(km, desnivel)`: devuelve los minutos de la etapa (tiempo andando + tiempo extra por la subida), **redondeados hacia arriba** con `math.ceil`.
3. `dificultad(km, desnivel)`: calcula `puntos = km + desnivel / 100` y devuelve `fácil` (menos de 10), `moderada` (menos de 20) o `difícil`.
4. `formatear_hora(minutos)`: convierte minutos en texto `HH:MM` con dos cifras: `545` → `09:05`.
5. `agua_necesaria(minutos, calor=False)`: devuelve los litros, redondeados hacia arriba **al medio litro** (1,2 L → 1,5 L). Pista: `math.ceil(litros * 2) / 2`.
6. Dentro de `if __name__ == "__main__":`, escribe **al menos 8 pruebas** con `assert` y muestra `Pruebas de ruta.py superadas`.

**Fichero `principal.py`** (programa principal):

1. `pedir_numero(mensaje, minimo, maximo, entero=False)`: pide un número hasta que sea válido. Si `entero` es `True` lo convierte con `int()`, si no, con `float()`.
2. `main()`:
    - Pide la hora (5-12) y el minuto (0-59) de salida, y si hace calor.
    - Pide etapas hasta que los km sean `0` (máximo 40 km y 2000 m de subida por etapa). Para cada etapa, muestra los minutos, la dificultad y la hora de llegada.
    - Al final, muestra la distancia y el tiempo total, el agua recomendada y, con un ternario, si se llegará de noche (después de las 20:00) o con luz de día.

```text
> python ruta.py
Pruebas de ruta.py superadas
```

```text
> python principal.py
Hora de salida (5-12): 8
Minuto de salida (0-59): 30
¿Hace calor? (s/n): s

Etapa 1 - km (0 para terminar): 12.5
Desnivel de subida (m): 600
Etapa 1: 248 min | moderada | llegada a las 12:38

Etapa 2 - km (0 para terminar): 7,5
Valor no válido
Etapa 2 - km (0 para terminar): 7.5
Desnivel de subida (m): abc
Valor no válido
Desnivel de subida (m): 350
Etapa 2: 148 min | moderada | llegada a las 15:06

Etapa 3 - km (0 para terminar): 0

--- RESUMEN DE LA RUTA ---
Distancia: 20.0 km | Tiempo: 06:36 h
Agua recomendada: 5.0 L
Llegarás con luz de día
```

```text
> python principal.py
Hora de salida (5-12): 14
Debe estar entre 5 y 12
Hora de salida (5-12): 11
Minuto de salida (0-59): 15
¿Hace calor? (s/n): n

Etapa 1 - km (0 para terminar): 18
Desnivel de subida (m): 900
Etapa 1: 360 min | difícil | llegada a las 17:15

Etapa 2 - km (0 para terminar): 16
Desnivel de subida (m): 1500
Etapa 2: 390 min | difícil | llegada a las 23:45

Etapa 3 - km (0 para terminar): 0

--- RESUMEN DE LA RUTA ---
Distancia: 34.0 km | Tiempo: 12:30 h
Agua recomendada: 6.5 L
¡Llegarás de noche! Adelanta la salida
```

??? success "Solución"
    **`ruta.py`**

    ```python
    """Cálculos para planificar rutas de senderismo."""

    import math

    VELOCIDAD = 4               # km/h en llano
    MINUTOS_POR_100M = 10       # minutos extra por cada 100 m de subida
    LITROS_HORA = 0.5
    LITROS_HORA_CALOR = 0.75


    def tiempo_etapa(km: float, desnivel: int) -> int:
        """Devuelve los minutos de una etapa, redondeados hacia arriba."""
        minutos = km / VELOCIDAD * 60 + desnivel / 100 * MINUTOS_POR_100M
        return math.ceil(minutos)


    def dificultad(km: float, desnivel: int) -> str:
        """Clasifica una etapa según su distancia y su desnivel."""
        puntos = km + desnivel / 100
        if puntos < 10:
            return "fácil"
        if puntos < 20:
            return "moderada"
        return "difícil"


    def formatear_hora(minutos: int) -> str:
        """Convierte minutos en un texto con formato HH:MM."""
        horas, resto = divmod(minutos, 60)
        return f"{horas:02d}:{resto:02d}"


    def agua_necesaria(minutos: int, calor: bool = False) -> float:
        """Devuelve los litros de agua, redondeados hacia arriba al medio litro."""
        litros_hora = LITROS_HORA_CALOR if calor else LITROS_HORA
        litros = minutos / 60 * litros_hora
        return math.ceil(litros * 2) / 2


    if __name__ == "__main__":
        # Pruebas: solo se ejecutan al lanzar ruta.py directamente
        assert tiempo_etapa(8, 0) == 120
        assert tiempo_etapa(6, 450) == 135
        assert dificultad(5, 200) == "fácil"
        assert dificultad(10, 0) == "moderada"
        assert dificultad(12, 800) == "difícil"
        assert formatear_hora(545) == "09:05"
        assert agua_necesaria(120) == 1.0
        assert agua_necesaria(130) == 1.5
        assert agua_necesaria(120, calor=True) == 1.5
        print("Pruebas de ruta.py superadas")
    ```

    **`principal.py`**

    ```python
    """Planificador de una ruta de senderismo por etapas."""

    import ruta

    HORA_ANOCHECER = 20 * 60    # 20:00 en minutos


    def pedir_numero(mensaje: str, minimo: float, maximo: float,
                     entero: bool = False) -> float:
        """Pide un número entre minimo y maximo hasta que sea válido."""
        while True:
            try:
                texto = input(mensaje)
                numero = int(texto) if entero else float(texto)
                if minimo <= numero <= maximo:
                    return numero
                print(f"Debe estar entre {minimo} y {maximo}")
            except ValueError:
                print("Valor no válido")


    def main() -> None:
        """Programa principal."""
        hora = pedir_numero("Hora de salida (5-12): ", 5, 12, entero=True)
        minuto = pedir_numero("Minuto de salida (0-59): ", 0, 59, entero=True)
        calor = input("¿Hace calor? (s/n): ") == "s"

        reloj = hora * 60 + minuto       # hora actual en minutos
        total_km = 0.0
        total_minutos = 0
        etapa = 1

        while True:
            print()
            km = pedir_numero(f"Etapa {etapa} - km (0 para terminar): ", 0, 40)
            if km == 0:
                break
            desnivel = pedir_numero("Desnivel de subida (m): ", 0, 2000,
                                    entero=True)

            minutos = ruta.tiempo_etapa(km, desnivel)
            reloj += minutos
            total_km += km
            total_minutos += minutos
            print(f"Etapa {etapa}: {minutos} min | "
                  f"{ruta.dificultad(km, desnivel)} | "
                  f"llegada a las {ruta.formatear_hora(reloj)}")
            etapa += 1

        print("\n--- RESUMEN DE LA RUTA ---")
        if total_km == 0:
            print("No has añadido ninguna etapa")
        else:
            print(f"Distancia: {total_km:.1f} km | "
                  f"Tiempo: {ruta.formatear_hora(total_minutos)} h")
            agua = ruta.agua_necesaria(total_minutos, calor)
            print(f"Agua recomendada: {agua} L")
            aviso = ("¡Llegarás de noche! Adelanta la salida"
                     if reloj > HORA_ANOCHECER else "Llegarás con luz de día")
            print(aviso)


    if __name__ == "__main__":
        main()
    ```

    - `ruta.py` solo **calcula**; `principal.py` se encarga de **pedir y mostrar**. Así las funciones de `ruta.py` se pueden reutilizar en otro programa y probar con `assert`.
    - Al ejecutar `principal.py` **no** aparece `Pruebas de ruta.py superadas`: al importar `ruta`, su `__name__` vale `"ruta"`, no `"__main__"`.
    - `formatear_hora` sirve tanto para la hora del reloj (`12:38`) como para la duración total (`06:36 h`).
    - El parámetro `entero=False` permite usar la misma función para pedir números enteros y decimales.

---

## Ejercicio 4 ★★★ · Caja fuerte de un hotel

!!! abstract "Repasa"
    [a) Funciones](a-funciones.md) · [b) Recursividad](b-recursividad.md): [caso base y caso recursivo](b-recursividad.md#2-estructura-de-una-funcion-recursiva) · [ejemplos clásicos](b-recursividad.md#3-ejemplos-clasicos)

La caja fuerte de las habitaciones de un hotel pide al huésped que elija un código. Para que sea seguro, debe cumplir unas reglas.

**Funciones recursivas** (sin bucles):

1. `contar_cifras(n)`: cuántas cifras tiene `n`.
2. `suma_cifras(n)`: suma de las cifras de `n`.
3. `raiz_digital(n)`: suma las cifras **una y otra vez** hasta que queda una sola: `4721` → `14` → `5`. Usa `suma_cifras`.
4. `contar_digito(n, digito)`: cuántas veces aparece `digito` en `n`: `contar_digito(1213, 1)` → `2`.
5. `invertir(texto)`: el texto al revés.

**Funciones normales**:

6. `comprobar_codigo(codigo)`: devuelve **dos valores**: si el código es seguro (`True`/`False`) y un texto con el motivo. Un código es seguro si:
    - Tiene entre 4 y 6 cifras.
    - No es **capicúa** (se lee igual al revés, como `4554`).
    - Ninguna cifra aparece **más de 2 veces**.
7. `pedir_codigo(mensaje)`: pide un código entero positivo hasta que lo sea.
8. `probar()`: al menos **10 pruebas** con `assert` de las funciones anteriores (todas menos `pedir_codigo`).
9. `main()`:
    - Llama a `probar()` antes de nada.
    - **Configurar**: pide códigos hasta que uno sea seguro, mostrando el motivo de cada rechazo. Al guardarlo, muestra la raíz digital como **dígito de control**.
    - **Abrir**: da **3 intentos** para escribir el código. Si acierta, `Caja abierta`; si falla los tres, `Caja bloqueada. Llama a recepción` (usa el `else` del `for`).

```text
--- CONFIGURAR LA CAJA FUERTE ---
Nuevo código: 123
Código rechazado: Debe tener entre 4 y 6 cifras
Nuevo código: 12a4
El código solo puede tener cifras
Nuevo código: 45754
Código rechazado: No puede ser capicúa
Nuevo código: 707170
Código rechazado: La cifra 7 se repite demasiado
Nuevo código: 849302
Código guardado. Dígito de control: 8

--- ABRIR LA CAJA FUERTE ---
Código (intento 1/3): 849320
Código incorrecto
Código (intento 2/3): -5
El código debe ser positivo
Código (intento 2/3): 849302
Caja abierta
```

```text
--- CONFIGURAR LA CAJA FUERTE ---
Nuevo código: 2580
Código guardado. Dígito de control: 6

--- ABRIR LA CAJA FUERTE ---
Código (intento 1/3): 1111
Código incorrecto
Código (intento 2/3): 0258
Código incorrecto
Código (intento 3/3): 2085
Código incorrecto
Caja bloqueada. Llama a recepción
```

??? success "Solución"
    ```python
    """Caja fuerte de la habitación de un hotel."""

    MIN_CIFRAS = 4
    MAX_CIFRAS = 6
    MAX_REPETICIONES = 2     # una cifra puede aparecer como mucho 2 veces
    INTENTOS = 3


    # --- Funciones recursivas (sin bucles) ---

    def contar_cifras(n: int) -> int:
        """Devuelve cuántas cifras tiene n (n >= 0)."""
        if n < 10:
            return 1
        return 1 + contar_cifras(n // 10)


    def suma_cifras(n: int) -> int:
        """Devuelve la suma de las cifras de n (n >= 0)."""
        if n < 10:
            return n
        return n % 10 + suma_cifras(n // 10)


    def raiz_digital(n: int) -> int:
        """Suma las cifras una y otra vez hasta que queda una sola."""
        if n < 10:
            return n
        return raiz_digital(suma_cifras(n))


    def contar_digito(n: int, digito: int) -> int:
        """Devuelve cuántas veces aparece digito en n."""
        coincide = 1 if n % 10 == digito else 0
        if n < 10:
            return coincide
        return coincide + contar_digito(n // 10, digito)


    def invertir(texto: str) -> str:
        """Devuelve el texto al revés."""
        if len(texto) <= 1:
            return texto
        return invertir(texto[1:]) + texto[0]


    # --- Funciones normales ---

    def comprobar_codigo(codigo: int) -> tuple[bool, str]:
        """Indica si el código es seguro y, si no lo es, el motivo."""
        if not MIN_CIFRAS <= contar_cifras(codigo) <= MAX_CIFRAS:
            return False, f"Debe tener entre {MIN_CIFRAS} y {MAX_CIFRAS} cifras"
        if invertir(str(codigo)) == str(codigo):
            return False, "No puede ser capicúa"
        for digito in range(10):
            if contar_digito(codigo, digito) > MAX_REPETICIONES:
                return False, f"La cifra {digito} se repite demasiado"
        return True, "Código seguro"


    def pedir_codigo(mensaje: str) -> int:
        """Pide un código numérico positivo hasta que lo sea."""
        while True:
            try:
                codigo = int(input(mensaje))
                if codigo > 0:
                    return codigo
                print("El código debe ser positivo")
            except ValueError:
                print("El código solo puede tener cifras")


    def probar() -> None:
        """Pruebas de las funciones recursivas y de comprobar_codigo."""
        assert contar_cifras(7) == 1
        assert contar_cifras(90210) == 5
        assert suma_cifras(4721) == 14
        assert raiz_digital(4721) == 5           # 4721 → 14 → 5
        assert raiz_digital(9) == 9
        assert contar_digito(1213, 1) == 2
        assert contar_digito(5000, 0) == 3
        assert invertir("hotel") == "letoh"
        assert invertir("") == ""
        assert comprobar_codigo(123)[0] is False
        assert comprobar_codigo(4554)[0] is False
        assert comprobar_codigo(70007)[0] is False
        assert comprobar_codigo(2580) == (True, "Código seguro")


    def main() -> None:
        """Programa principal."""
        probar()
        print("--- CONFIGURAR LA CAJA FUERTE ---")

        while True:
            codigo = pedir_codigo("Nuevo código: ")
            seguro, motivo = comprobar_codigo(codigo)
            if seguro:
                break
            print(f"Código rechazado: {motivo}")

        print(f"Código guardado. Dígito de control: {raiz_digital(codigo)}")

        print("\n--- ABRIR LA CAJA FUERTE ---")
        for intento in range(1, INTENTOS + 1):
            if pedir_codigo(f"Código (intento {intento}/{INTENTOS}): ") == codigo:
                print("Caja abierta")
                break
            print("Código incorrecto")
        else:
            print("Caja bloqueada. Llama a recepción")


    main()
    ```

    - Todas las funciones recursivas trabajan con números usando `n % 10` (última cifra) y `n // 10` (el número sin la última cifra). El caso base es un número de **una cifra** (`n < 10`).
    - `raiz_digital` es recursiva y además llama a otra función recursiva, `suma_cifras`.
    - `comprobar_codigo[0]` se queda con el primer valor de los dos devueltos, el `True`/`False`.
    - Al escribir `0258`, `int()` lo convierte en `258`: por eso no coincide con `2580`.

---

## Ejercicio 5 ★★★ · Hucha digital

!!! abstract "Repasa"
    Toda la unidad: [a) Funciones](a-funciones.md) · [b) Recursividad](b-recursividad.md), y también excepciones propias y `match` de la UT02.

Una aplicación ayuda a ahorrar dinero para conseguir un objetivo (una bici, un viaje...) antes de una fecha. Programa la hucha de **una sesión**, organizada en funciones, con docstrings y anotaciones de tipo en todas ellas.

1. **Importaciones y constantes.** Importa `math` y `date` de `datetime`. Constantes: importe máximo por operación 1000 € y ancho de la barra de progreso 20.
2. **Excepción propia.** `ImporteNoValidoError`, que hereda de `Exception`.
3. **Entrada de datos.**
    - `pedir_numero(mensaje, minimo=0, maximo=IMPORTE_MAXIMO)`: pide un decimal hasta que esté en el rango.
    - `pedir_fecha()`: pide día, mes y año, y devuelve un objeto `date`. Si la fecha no existe (`date(2027, 2, 31)` lanza `ValueError`) o no es posterior a hoy, la vuelve a pedir.
4. **Operaciones**:
    - `ingresar(saldo, importe)` y `retirar(saldo, importe)`: **devuelven** el nuevo saldo. Lanzan `ImporteNoValidoError` si el importe no es mayor que 0 o, al retirar, si no hay saldo suficiente.
    - `barra_progreso(actual, objetivo, ancho=ANCHO_BARRA)`: devuelve un texto como `[#######.............] 38 %`. El porcentaje no pasa de 100. La barra se construye con un `for`.
    - `ahorro_diario(saldo, objetivo, fecha)`: devuelve **dos valores**, los días que faltan hasta la fecha y cuánto hay que ahorrar al día, redondeado **hacia arriba** al céntimo.
5. **Funciones recursivas**:
    - `capital_final(capital, interes, anios)`: capital tras `anios` años con un interés anual compuesto (cada año el capital se multiplica por `1 + interes / 100`).
    - `anios_hasta(capital, objetivo, interes)`: cuántos años hacen falta para llegar al objetivo solo con intereses. Si el capital o el interés son 0, lanza `ValueError` (nunca se llegaría).
6. **`probar()`**: pruebas con `assert` de las funciones que no piden datos, incluida una que compruebe que `retirar` lanza la excepción.
7. **`main()`**: llama a `probar()`, pide para qué se ahorra, el objetivo (de 1 a 100 000 €) y la fecha. Después, un menú con `while True` y `match`:
    - `1` Ingresar y `2` Retirar: piden el importe y capturan `ImporteNoValidoError` mostrando `Operación cancelada:` y el mensaje. Escríbelos en **un solo `case`**.
    - `3` Progreso: muestra la barra y, si no se ha llegado al objetivo, los días que faltan y el ahorro diario necesario. Si se ha llegado, felicita.
    - `4` Simular intereses: pide un interés (0-20 %) y unos años (0-30), muestra el capital final y los intereses ganados, y cuántos años harían falta para llegar al objetivo. Captura el `ValueError` de `anios_hasta` y también el `RecursionError` si hicieran falta demasiados años.
    - `5` Salir: muestra el saldo final y el número de operaciones realizadas (`operación` u `operaciones`, con un ternario).

!!! tip "Para probar los casos extremos"
    - Con 1 € de saldo, un objetivo de 90 000 € y un interés de 0,05 %, `anios_hasta` necesitaría más de 1000 llamadas encadenadas: comprueba que se captura el `RecursionError`.
    - Para comprobar la felicitación, ingresa más dinero del objetivo.

Ejemplo realizado el 17/11/2026 (los días que faltan dependen de la fecha en que lo ejecutes):

```text
--- NUEVA HUCHA ---
¿Para qué ahorras?: bicicleta
Objetivo (€): 450
Fecha en la que lo quieres conseguir
Día: 31
Mes: 2
Año: 2027
Fecha no válida
Día: 28
Mes: 2
Año: 2027

[bicicleta] 1. Ingresar  2. Retirar  3. Progreso  4. Simular intereses  5. Salir
Opción: 1
Importe (€): 120
Saldo: 120.00 €

[bicicleta] 1. Ingresar  2. Retirar  3. Progreso  4. Simular intereses  5. Salir
Opción: 2
Importe (€): 200
Operación cancelada: Solo tienes 120.00 € en la hucha

[bicicleta] 1. Ingresar  2. Retirar  3. Progreso  4. Simular intereses  5. Salir
Opción: 2
Importe (€): 0
Operación cancelada: El importe debe ser mayor que 0

[bicicleta] 1. Ingresar  2. Retirar  3. Progreso  4. Simular intereses  5. Salir
Opción: 1
Importe (€): 50,5
Escribe un número (usa punto decimal)
Importe (€): 50.5
Saldo: 170.50 €

[bicicleta] 1. Ingresar  2. Retirar  3. Progreso  4. Simular intereses  5. Salir
Opción: 3
[#######.............] 38 %
Faltan 103 días: ahorra 2.72 € al día

[bicicleta] 1. Ingresar  2. Retirar  3. Progreso  4. Simular intereses  5. Salir
Opción: 4
Interés anual (%): 3
Años: 5
En 5 años tendrías 197.66 € (+27.16 € de intereses)
Solo con intereses llegarías al objetivo en 33 años

[bicicleta] 1. Ingresar  2. Retirar  3. Progreso  4. Simular intereses  5. Salir
Opción: 7
Opción no válida

[bicicleta] 1. Ingresar  2. Retirar  3. Progreso  4. Simular intereses  5. Salir
Opción: 5

Hucha cerrada con 170.50 € tras 2 operaciones
```

??? success "Solución"
    ```python
    """Hucha digital: ahorro para conseguir un objetivo."""

    import math
    from datetime import date

    IMPORTE_MAXIMO = 1000.00  # máximo por operación
    ANCHO_BARRA = 20


    class ImporteNoValidoError(Exception):
        """El importe de la operación no se puede aceptar."""


    # --- Entrada de datos ---

    def pedir_numero(mensaje: str, minimo: float = 0,
                     maximo: float = IMPORTE_MAXIMO) -> float:
        """Pide un número entre minimo y maximo hasta que sea válido."""
        while True:
            try:
                numero = float(input(mensaje))
                if minimo <= numero <= maximo:
                    return numero
                print(f"Debe estar entre {minimo:.2f} y {maximo:.2f}")
            except ValueError:
                print("Escribe un número (usa punto decimal)")


    def pedir_fecha() -> date:
        """Pide una fecha futura (día, mes y año) hasta que sea válida."""
        while True:
            try:
                dia = int(input("Día: "))
                mes = int(input("Mes: "))
                anio = int(input("Año: "))
                fecha = date(anio, mes, dia)   # ValueError si no existe
                if fecha > date.today():
                    return fecha
                print("La fecha tiene que ser futura")
            except ValueError:
                print("Fecha no válida")


    # --- Operaciones ---

    def ingresar(saldo: float, importe: float) -> float:
        """Devuelve el saldo tras ingresar el importe."""
        if importe <= 0:
            raise ImporteNoValidoError("El importe debe ser mayor que 0")
        return saldo + importe


    def retirar(saldo: float, importe: float) -> float:
        """Devuelve el saldo tras retirar el importe."""
        if importe <= 0:
            raise ImporteNoValidoError("El importe debe ser mayor que 0")
        if importe > saldo:
            raise ImporteNoValidoError(f"Solo tienes {saldo:.2f} € en la hucha")
        return saldo - importe


    def barra_progreso(actual: float, objetivo: float,
                       ancho: int = ANCHO_BARRA) -> str:
        """Devuelve una barra de texto con el porcentaje conseguido."""
        porcentaje = min(actual / objetivo * 100, 100)
        llenos = int(porcentaje * ancho / 100)
        barra = ""
        for posicion in range(ancho):
            barra += "#" if posicion < llenos else "."
        return f"[{barra}] {porcentaje:.0f} %"


    def ahorro_diario(saldo: float, objetivo: float,
                      fecha: date) -> tuple[int, float]:
        """Devuelve los días que faltan y cuánto hay que ahorrar cada día."""
        dias = (fecha - date.today()).days
        falta = max(objetivo - saldo, 0)
        return dias, math.ceil(falta / dias * 100) / 100   # redondeo hacia arriba


    # --- Funciones recursivas ---

    def capital_final(capital: float, interes: float, anios: int) -> float:
        """Capital tras 'anios' años a un interés anual compuesto (en %)."""
        if anios == 0:
            return capital
        return capital_final(capital * (1 + interes / 100), interes, anios - 1)


    def anios_hasta(capital: float, objetivo: float, interes: float) -> int:
        """Años necesarios para que el capital llegue al objetivo con intereses."""
        if capital >= objetivo:
            return 0
        if capital <= 0 or interes <= 0:
            raise ValueError("Sin capital o sin interés no se llega al objetivo")
        return 1 + anios_hasta(capital * (1 + interes / 100), objetivo, interes)


    def probar() -> None:
        """Pruebas de las funciones que no piden datos."""
        assert ingresar(10, 5) == 15
        assert retirar(10, 4) == 6
        assert barra_progreso(50, 100, ancho=10) == "[#####.....] 50 %"
        assert barra_progreso(300, 100, ancho=4) == "[####] 100 %"
        assert capital_final(100, 10, 0) == 100
        assert round(capital_final(100, 10, 2), 2) == 121.00
        assert anios_hasta(100, 100, 5) == 0
        assert anios_hasta(100, 121, 10) == 2
        try:
            retirar(10, 50)
            assert False, "Debería lanzar ImporteNoValidoError"
        except ImporteNoValidoError:
            pass


    # --- Programa principal ---

    def main() -> None:
        """Programa principal."""
        probar()

        print("--- NUEVA HUCHA ---")
        nombre = input("¿Para qué ahorras?: ")
        objetivo = pedir_numero("Objetivo (€): ", 1, 100000)
        print("Fecha en la que lo quieres conseguir")
        fecha = pedir_fecha()
        saldo = 0.0
        operaciones = 0

        while True:
            print(f"\n[{nombre}] 1. Ingresar  2. Retirar  3. Progreso  "
                  "4. Simular intereses  5. Salir")
            opcion = input("Opción: ")

            match opcion:
                case "1" | "2":
                    importe = pedir_numero("Importe (€): ")
                    try:
                        if opcion == "1":
                            saldo = ingresar(saldo, importe)
                        else:
                            saldo = retirar(saldo, importe)
                        operaciones += 1
                        print(f"Saldo: {saldo:.2f} €")
                    except ImporteNoValidoError as error:
                        print("Operación cancelada:", error)
                case "3":
                    print(barra_progreso(saldo, objetivo))
                    if saldo >= objetivo:
                        print(f"¡Objetivo conseguido! Ya puedes comprar: {nombre}")
                    else:
                        dias, diario = ahorro_diario(saldo, objetivo, fecha)
                        print(f"Faltan {dias} días: ahorra {diario:.2f} € al día")
                case "4":
                    interes = pedir_numero("Interés anual (%): ", 0, 20)
                    anios = int(pedir_numero("Años: ", 0, 30))
                    final = capital_final(saldo, interes, anios)
                    print(f"En {anios} años tendrías {final:.2f} € "
                          f"(+{final - saldo:.2f} € de intereses)")
                    try:
                        necesarios = anios_hasta(saldo, objetivo, interes)
                        print(f"Solo con intereses llegarías al objetivo "
                              f"en {necesarios} años")
                    except ValueError as error:
                        print(error)
                    except RecursionError:
                        print("Harían falta demasiados años: no se puede calcular")
                case "5":
                    break
                case _:
                    print("Opción no válida")

        palabra = "operación" if operaciones == 1 else "operaciones"
        print(f"\nHucha cerrada con {saldo:.2f} € tras {operaciones} {palabra}")


    if __name__ == "__main__":
        main()
    ```

    - Las funciones `ingresar` y `retirar` **no** modifican el saldo: lo reciben y **devuelven** el nuevo. Si lanzan la excepción, la asignación `saldo = ...` no llega a hacerse y el saldo no cambia.
    - El importe se pide con `pedir_numero`, que acepta el 0. Así se comprueba que la excepción de `ingresar`/`retirar` funciona.
    - `capital_final` y `anios_hasta` se acercan a su caso base en cada llamada: `anios` baja de 1 en 1 y el capital crece. Si el interés es 0, el capital no crece nunca, y por eso `anios_hasta` lanza un `ValueError` antes de entrar en una recursión infinita.
    - Aunque esté bien escrita, una recursión **demasiado profunda** también falla: por eso se captura `RecursionError`.

---

!!! info "¿Y ahora?"
    Si has resuelto los cinco ejercicios, haz la [autoevaluación](autoevaluacion.md) y su proyecto de práctica con el formato del examen.
