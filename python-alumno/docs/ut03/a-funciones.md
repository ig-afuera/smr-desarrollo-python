# a) Funciones definidas por el programador

## 1. ¿Qué es una función?

Una **función** es un bloque de código con **nombre** que realiza una tarea concreta. Se escribe **una vez** y se puede usar (**llamar**) tantas veces como haga falta.

Ya has usado muchas funciones sin saberlo: `print()`, `input()`, `int()`, `len()`, `round()`... Son funciones que trae Python. Ahora vas a crear **las tuyas**.

```python
# Sin funciones: el mismo código repetido
print("=" * 30)
print("Informe de ventas")
print("=" * 30)
# ...
print("=" * 30)
print("Informe de gastos")
print("=" * 30)
```

```python
# Con una función: se escribe una vez y se usa dos
def cabecera(titulo):
    print("=" * 30)
    print(titulo)
    print("=" * 30)


cabecera("Informe de ventas")
# ...
cabecera("Informe de gastos")
```

Las funciones aportan tres ventajas:

| Ventaja | Qué significa |
|---|---|
| **Reutilización** | Escribes el código una vez y lo usas muchas. Si hay un fallo, se corrige en **un solo sitio**. |
| **Modularidad** | Divides un problema grande en piezas pequeñas, cada una con su función. Son más fáciles de entender y de probar. |
| **Abstracción** | Para usar una función basta con saber **qué hace**, no **cómo** lo hace. Usas `round()` sin saber cómo está programada por dentro. |

!!! tip "Una función, una tarea"
    Si para explicar lo que hace una función necesitas decir «y además...», probablemente deberían ser dos funciones.

!!! success "Ahora tú"
    **Busca la repetición.** Vuelve a uno de tus programas de la UT02 (por ejemplo, el de la *Cita en el taller* o la *Máquina expendedora*) y responde en un comentario al principio del fichero:

    1. ¿Qué trozos de código se repiten casi iguales?
    2. ¿Qué cambia de una repetición a otra? (Eso serán los **parámetros**.)
    3. ¿Qué nombre le pondrías a una función que hiciera ese trabajo?

    No hace falta que lo programes todavía: lo harás al terminar el apartado 4.

## 2. Definir y llamar a una función

Una función se **define** con `def`, un nombre, paréntesis y dos puntos. El código de la función va **indentado**:

```python
def saludar():
    print("¡Hola!")
    print("Bienvenido/a al programa")
```

Definirla **no la ejecuta**: solo le dice a Python «esto se llama `saludar` y hace esto». Para ejecutarla hay que **llamarla** escribiendo su nombre con paréntesis:

```python
saludar()      # se ejecuta el bloque de la función
saludar()      # y otra vez
```

```text
¡Hola!
Bienvenido/a al programa
¡Hola!
Bienvenido/a al programa
```

Al llamar a una función, el programa **salta** al código de la función, lo ejecuta entero y **vuelve** a la línea siguiente a la llamada.

```python
print("1. Antes de llamar")
saludar()
print("2. Después de llamar")
```

```text
1. Antes de llamar
¡Hola!
Bienvenido/a al programa
2. Después de llamar
```

Reglas para escribir funciones (PEP 8):

- El nombre sigue las mismas reglas que una variable, en `snake_case`. Suele ser un **verbo** que diga qué hace: `calcular_total`, `mostrar_menu`, `pedir_edad`.
- Deja **dos líneas en blanco** antes y después de cada definición de función.
- La función se tiene que **definir antes de llamarla**. Por eso las definiciones suelen ir al principio del fichero.

!!! warning "Errores típicos"
    - **Olvidar los paréntesis**: `saludar` (sin paréntesis) no ejecuta nada; solo nombra la función. `print(saludar)` muestra algo como `<function saludar at 0x...>`.
    - **Llamarla antes de definirla**: da `NameError: name 'saludar' is not defined`.
    - **Olvidar la indentación**: todo lo que pertenece a la función va 4 espacios hacia dentro.

!!! note "`pass` en funciones"
    Si quieres dejar una función preparada pero sin escribir todavía, usa `pass` (lo viste en la UT02):

    ```python
    def calcular_nomina():
        pass       # pendiente de programar
    ```

!!! success "Ahora tú"
    **Panel de un ascensor.** Construye un programa con tres funciones sin parámetros:

    - `mostrar_panel()`: dibuja un panel con los botones de las plantas del 0 al 5 usando un `for`, así: `[0] [1] [2] [3] [4] [5]`.
    - `abrir_puertas()`: muestra `<< Puertas abiertas >>`.
    - `cerrar_puertas()`: muestra `>> Puertas cerradas <<`.

    El programa principal debe llamarlas en este orden: abrir, cerrar, mostrar el panel, abrir y cerrar. Comprueba que **las definiciones no muestran nada** hasta que se llaman.

## 3. Parámetros y argumentos

Para que una función trabaje con **datos distintos** en cada llamada, se le pasan valores entre los paréntesis.

```python
def saludar(nombre):          # nombre es un PARÁMETRO
    print(f"¡Hola, {nombre}!")


saludar("Lucía")              # "Lucía" es un ARGUMENTO
saludar("Omar")
```

| Término | Qué es | Dónde aparece |
|---|---|---|
| **Parámetro** | Una variable de la función que recibirá un valor. | En la **definición**: `def saludar(nombre):` |
| **Argumento** | El valor concreto que se envía al llamar. | En la **llamada**: `saludar("Lucía")` |

Una función puede tener varios parámetros, separados por comas:

```python
def mostrar_producto(nombre, precio, unidades):
    total = precio * unidades
    print(f"{unidades} x {nombre} = {total:.2f} €")


mostrar_producto("Bolígrafo", 0.85, 4)
```

```text
4 x Bolígrafo = 3.40 €
```

### Argumentos posicionales y por nombre

Hay dos formas de pasar los argumentos:

```python
# Posicionales: se asignan por ORDEN
mostrar_producto("Cuaderno", 2.50, 3)

# Por nombre: se indica a qué parámetro va cada valor (el orden da igual)
mostrar_producto(unidades=3, nombre="Cuaderno", precio=2.50)

# Mezclados: primero los posicionales y después los por nombre
mostrar_producto("Cuaderno", unidades=3, precio=2.50)
```

Pasarlos **por nombre** hace la llamada más legible, sobre todo cuando hay varios números seguidos y no se sabe qué es cada uno.

!!! warning "Errores típicos con los argumentos"
    - **Cambiar el orden** de los posicionales: `mostrar_producto("Cuaderno", 3, 2.50)` no da error, pero calcula 2,5 unidades a 3 € (**error lógico**).
    - **Faltar o sobrar argumentos**: `mostrar_producto("Cuaderno", 2.50)` da `TypeError: mostrar_producto() missing 1 required positional argument: 'unidades'`.
    - **Un posicional después de uno por nombre**: `mostrar_producto(nombre="Cuaderno", 2.50, 3)` da `SyntaxError`.

### Valores por defecto

Un parámetro puede tener un **valor por defecto**, que se usa si en la llamada no se indica otro. Así el argumento pasa a ser **opcional**:

```python
def precio_con_iva(precio, iva=21):
    return precio + precio * iva / 100


print(precio_con_iva(100))         # usa iva=21 → 121.0
print(precio_con_iva(100, 10))     # usa iva=10 → 110.0
print(precio_con_iva(100, iva=4))  # usa iva=4  → 104.0
```

Ya conoces funciones con valores por defecto: en `print()`, `sep` vale `" "` y `end` vale `"\n"` si no dices otra cosa.

!!! warning "Los parámetros con valor por defecto van al final"
    `def precio_con_iva(iva=21, precio):` da `SyntaxError`. Primero se escriben los parámetros obligatorios y después los opcionales.

### Argumentos solo posicionales y solo por nombre

Con dos símbolos especiales se puede **obligar** a pasar los argumentos de una forma concreta:

- Lo que va **antes de `/`** solo se puede pasar **por posición**.
- Lo que va **después de `*`** solo se puede pasar **por nombre**.

```python
def reservar(fecha, /, personas, *, terraza=False):
    lugar = "terraza" if terraza else "interior"
    print(f"Reserva el {fecha} para {personas} personas en {lugar}")


reservar("12/05", 4)                      # bien
reservar("12/05", personas=4, terraza=True)  # bien
reservar("12/05", 4, True)                # TypeError: terraza solo por nombre
reservar(fecha="12/05", personas=4)       # TypeError: fecha solo por posición
```

Obligar a escribir `terraza=True` evita llamadas confusas como `reservar("12/05", 4, True)`, donde no se sabe qué significa ese `True`.

!!! note "No lo usarás a menudo"
    En tus programas no es obligatorio usar `/` ni `*`, pero los verás en la documentación de Python. Por ejemplo, `sorted()` (UT04) tiene el parámetro `reverse` **solo por nombre**.

!!! success "Ahora tú"
    **Calculadora de propinas.** Construye la función `mostrar_propina(importe, porcentaje=10, personas=1)` que muestre la propina y lo que paga cada persona, con 2 decimales:

    ```text
    Cuenta: 48.00 € | Propina (10 %): 4.80 € | Por persona: 52.80 €
    ```

    Llámala **cuatro veces** de formas distintas:

    1. Solo con el importe.
    2. Con importe y porcentaje, por posición.
    3. Con importe y número de personas, pasando las personas **por nombre** (y dejando el porcentaje por defecto).
    4. Con los tres argumentos por nombre y en otro orden.

    Después, cambia la definición para que `personas` sea **solo por nombre** y comprueba qué llamadas dejan de funcionar.

## 4. Valor de retorno: `return`

Las funciones de los ejemplos anteriores **muestran** resultados con `print()`. Pero muchas veces lo que necesitas es que la función **calcule** un valor y te lo **devuelva** para seguir usándolo. Para eso está `return`:

```python
def area_rectangulo(base, altura):
    return base * altura


salon = area_rectangulo(5, 4)
cocina = area_rectangulo(3, 2.5)
print(f"Superficie total: {salon + cocina} m²")
```

```text
Superficie total: 27.5 m²
```

La llamada `area_rectangulo(5, 4)` **se sustituye** por el valor devuelto (`20`), así que se puede guardar en una variable, usar en una expresión o pasar a otra función.

### `return` termina la función

En cuanto se ejecuta un `return`, la función **acaba** y vuelve al punto de la llamada. Lo que haya debajo no se ejecuta. Esto permite varios `return`, uno por cada caso:

```python
def clasificar_imc(imc):
    if imc < 18.5:
        return "bajo peso"
    if imc < 25:
        return "normal"
    if imc < 30:
        return "sobrepeso"
    return "obesidad"
```

No hace falta `elif` ni `else`: si se cumple la primera condición, el `return` ya ha terminado la función.

### Devolver varios valores

Separando los valores con comas, la función devuelve una **tupla** (UT04). Al recibirla se puede **desempaquetar** en varias variables:

```python
def dividir(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto


cajas, sueltos = dividir(50, 12)
print(f"{cajas} cajas completas y {sueltos} huevos sueltos")
```

```text
4 cajas completas y 2 huevos sueltos
```

### Funciones sin `return`

Si una función no tiene `return` (o tiene un `return` sin valor), devuelve el valor especial **`None`**, que significa «nada»:

```pycon
>>> def saludar():
...     print("Hola")
...
>>> resultado = saludar()
Hola
>>> print(resultado)
None
```

### `print` frente a `return`

| | `print()` | `return` |
|---|---|---|
| Qué hace | **Muestra** el valor en pantalla. | **Devuelve** el valor a quien llamó a la función. |
| ¿Se puede usar el valor después? | No. | Sí: guardarlo, operar con él, compararlo... |
| ¿Termina la función? | No. | Sí. |

!!! warning "El error más frecuente de la unidad"
    ```python
    def doble(n):
        print(n * 2)       # MAL: lo muestra, pero no lo devuelve


    resultado = doble(5) + 1   # TypeError: None + 1
    ```

    Si el resultado se va a **usar** después, la función tiene que **devolverlo** con `return`. Deja los `print` para el programa principal o para funciones cuyo trabajo sea mostrar algo.

!!! success "Ahora tú"
    **Conversor de temperaturas.** Construye estas funciones (ninguna debe usar `print`):

    1. `celsius_a_fahrenheit(c)`: devuelve `c * 9 / 5 + 32`.
    2. `convertir(c)`: devuelve **dos** valores, los grados Fahrenheit (usando la función anterior) y los Kelvin (`c + 273.15`).
    3. `sensacion(c)`: devuelve `"helada"` (menos de 0), `"frío"` (menos de 15), `"agradable"` (menos de 25) o `"calor"`, usando **varios `return`** y sin `elif`.

    El programa principal pide una temperatura en grados Celsius y muestra:

    ```text
    Temperatura: 18.0 °C
    En Fahrenheit: 64.4 °F | En Kelvin: 291.15 K
    Sensación: agradable
    ```

    Para terminar, vuelve a la respuesta del «Ahora tú» del apartado 1 y programa la función que propusiste.

## 5. Paso de argumentos: mutables e inmutables

Cuando llamas a una función, el parámetro pasa a ser **otro nombre para el mismo objeto** que enviaste (recuerda de la UT01 que las variables son **referencias** a objetos). Lo que ocurra después depende de si el objeto se puede modificar o no.

### Objetos inmutables (`int`, `float`, `str`, `bool`, tuplas)

No se pueden modificar. Si dentro de la función se asigna otro valor al parámetro, solo cambia la variable **local**; la de fuera sigue igual:

```python
def sumar_punto(puntos):
    puntos = puntos + 1          # crea un objeto nuevo solo para la función
    print("Dentro:", puntos)


marcador = 10
sumar_punto(marcador)
print("Fuera:", marcador)
```

```text
Dentro: 11
Fuera: 10
```

Si quieres que el cambio llegue fuera, **devuelve** el nuevo valor y asígnalo: `marcador = sumar_punto(marcador)`.

### Objetos mutables (listas, diccionarios...)

Las **listas** las verás a fondo en la UT04. Por ahora basta con saber que una lista guarda varios valores entre corchetes y que `append()` le añade uno al final. Las listas **sí se pueden modificar**, y la modificación se ve **fuera** de la función, porque las dos variables apuntan al **mismo** objeto:

```python
def anadir_tarea(tareas, nueva):
    tareas.append(nueva)         # modifica el objeto original


pendientes = ["comprar pan"]
anadir_tarea(pendientes, "llamar al médico")
print(pendientes)
```

```text
['comprar pan', 'llamar al médico']
```

| Tipo de objeto | ¿La función puede cambiarlo? | Cómo hacer llegar el cambio fuera |
|---|---|---|
| Inmutable (`int`, `str`...) | No | Devolver el valor con `return` y asignarlo. |
| Mutable (lista, diccionario...) | Sí, con sus métodos (`append`...) | Ya llega: es el mismo objeto. |

!!! danger "Nunca uses una lista como valor por defecto"
    El valor por defecto se crea **una sola vez**, al definir la función, y se comparte entre todas las llamadas:

    ```python
    def anadir(elemento, lista=[]):      # MAL
        lista.append(elemento)
        return lista


    print(anadir("a"))   # ['a']
    print(anadir("b"))   # ['a', 'b']  ← ¡sigue ahí la 'a'!
    ```

    Usa `None` como valor por defecto y crea la lista dentro: `if lista is None: lista = []`.

!!! success "Ahora tú"
    **Predice la salida.** Antes de ejecutar este programa, escribe en un papel qué mostrará cada `print`. Después ejecútalo y comprueba.

    ```python
    def modificar(numero, texto, lista):
        numero += 100
        texto = texto.upper()
        lista.append(numero)


    n = 5
    t = "hola"
    datos = [1, 2]

    modificar(n, t, datos)
    print(n)
    print(t)
    print(datos)
    ```

    Después, cambia la función para que **devuelva** `numero` y `texto`, y el programa principal actualice `n` y `t` con lo devuelto.

## 6. Ámbito de las variables

El **ámbito** (*scope*) de una variable es la parte del programa donde existe y se puede usar.

### Variables locales

Las variables creadas **dentro** de una función (incluidos los parámetros) son **locales**: nacen al llamar a la función y **desaparecen** al terminar. Desde fuera no se pueden ver:

```python
def calcular_descuento(precio):
    descuento = precio * 0.15        # variable local
    return precio - descuento


print(calcular_descuento(40))        # 34.0
print(descuento)                     # NameError: 'descuento' no existe aquí
```

Gracias a esto, dos funciones pueden usar variables con el **mismo nombre** sin interferir entre sí.

### Variables globales

Las variables creadas **fuera** de cualquier función son **globales**: se pueden **leer** desde cualquier función.

```python
IVA = 21                             # constante global


def con_iva(precio):
    return precio + precio * IVA / 100   # se lee la global sin problema
```

Pero si dentro de una función se **asigna** un valor a una variable, Python la considera **local** en toda la función:

```python
visitas = 0


def registrar_visita():
    visitas = visitas + 1            # UnboundLocalError
```

Python ve la asignación y decide que `visitas` es local; al intentar leerla en `visitas + 1`, todavía no tiene valor.

### La palabra clave `global`

Con `global` se indica que se quiere **modificar** la variable global:

```python
visitas = 0


def registrar_visita():
    global visitas
    visitas += 1


registrar_visita()
registrar_visita()
print(visitas)                       # 2
```

!!! warning "Evita `global`"
    Una función que modifica variables globales es difícil de seguir y de probar: su resultado depende de cosas que pasan **fuera** de ella. Casi siempre es mejor **recibir** el valor como parámetro y **devolver** el nuevo:

    ```python
    def registrar_visita(visitas):
        return visitas + 1


    visitas = 0
    visitas = registrar_visita(visitas)
    ```

    Las **constantes** globales (en MAYÚSCULAS) sí son una buena práctica: se leen, pero nunca se modifican.


| Palabra clave | Permite modificar... |
|---|---|
| (ninguna) | Solo variables locales. Las de fuera se pueden **leer**. |
| `global` | Una variable del programa principal. |

!!! info "Orden de búsqueda: regla LEGB"
    Cuando usas un nombre, Python lo busca por este orden: **L**ocal (la función actual) → **E**nclosing (la función que la contiene) → **G**lobal (el programa) → **B**uilt-in (las funciones de Python, como `print`). Por eso, si llamas `print` a una variable tuya, «tapas» la función `print`.

!!! success "Ahora tú"
    **Contador de un torno.** Un torno de entrada a un museo cuenta las personas que pasan.

    1. Escribe una versión con una variable global `aforo_actual` y dos funciones, `entrar()` y `salir()`, que la modifiquen con `global`. `salir()` no debe dejar el aforo por debajo de 0.
    2. Haz un menú (`e` entrar, `s` salir, `f` fin) que muestre el aforo tras cada acción.
    3. Reescríbelo **sin `global`**: las funciones reciben el aforo como parámetro y devuelven el nuevo valor.

    ¿Qué versión te resulta más fácil de leer? Explícalo en un comentario.

## 7. Documentación de funciones

### Docstrings

Un **docstring** es una cadena entre triples comillas justo debajo del `def` que explica **qué hace** la función, qué recibe y qué devuelve (PEP 257, que viste en la UT01):

```python
def precio_final(precio, descuento=0):
    """Calcula el precio después de aplicar un descuento.

    Recibe el precio original y el porcentaje de descuento (0 por defecto).
    Devuelve el precio rebajado redondeado a 2 decimales.
    """
    return round(precio - precio * descuento / 100, 2)
```

- Si cabe en una línea, se escribe en una línea: `"""Devuelve el doble de n."""`.
- Si es largo, una primera línea de resumen, una línea en blanco y el resto de la explicación.

El docstring es lo que muestra `help()` y lo que enseña VS Code al pasar el ratón por encima de la función:

```pycon
>>> help(precio_final)
Help on function precio_final in module __main__:

precio_final(precio, descuento=0)
    Calcula el precio después de aplicar un descuento.
    ...
```

### Anotaciones de tipo

Las **anotaciones de tipo** (*type hints*), que conociste en la UT01, indican de qué tipo son los parámetros y el valor devuelto:

```python
def precio_final(precio: float, descuento: float = 0) -> float:
    """Calcula el precio después de aplicar un descuento."""
    return round(precio - precio * descuento / 100, 2)


def es_mayor_de_edad(edad: int) -> bool:
    """Indica si la edad corresponde a una persona adulta."""
    return edad >= 18


def mostrar_ticket(total: float) -> None:
    """Muestra el total del ticket. No devuelve nada."""
    print(f"TOTAL: {total:.2f} €")
```

- Detrás de cada parámetro: `: tipo`. Si tiene valor por defecto, con espacios: `descuento: float = 0`.
- Detrás del paréntesis: `-> tipo` del valor devuelto (`-> None` si no devuelve nada).

!!! note "Python no las comprueba"
    Las anotaciones son **información** para quien lee el código y para el editor (VS Code te avisa si pasas un tipo que no encaja), pero Python **no** da error si no se cumplen: `es_mayor_de_edad("hola")` se ejecuta igual.

!!! success "Ahora tú"
    **Documenta tu conversor.** Vuelve a las funciones del conversor de temperaturas del apartado 4:

    1. Añade a cada una un docstring y anotaciones de tipo. En `convertir`, el tipo devuelto es `tuple[float, float]`.
    2. Desde la consola de Python (o una celda de Jupyter), importa o pega las funciones y ejecuta `help()` sobre cada una.
    3. En VS Code, pasa el ratón por encima de una llamada a `sensacion()`: ¿qué aparece?

## 8. Funciones predefinidas y módulos

### Funciones predefinidas (*built-in*)

Python trae funciones listas para usar sin importar nada. Algunas que ya conoces y otras nuevas:

| Función | Qué hace | Ejemplo | Resultado |
|---|---|---|---|
| `abs(x)` | Valor absoluto | `abs(-7)` | `7` |
| `round(x, n)` | Redondea a `n` decimales | `round(3.14159, 2)` | `3.14` |
| `max(a, b, ...)` | El mayor | `max(4, 9, 2)` | `9` |
| `min(a, b, ...)` | El menor | `min(4, 9, 2)` | `2` |
| `pow(x, y)` | Potencia | `pow(2, 5)` | `32` |
| `len(s)` | Longitud | `len("python")` | `6` |
| `divmod(a, b)` | Cociente y resto | `divmod(17, 5)` | `(3, 2)` |

Para consultar la ayuda de cualquiera: `help(round)`.

### Módulos: `import`

Un **módulo** es un fichero `.py` con funciones (y constantes) que puedes usar en tu programa. Python incluye muchos en su **biblioteca estándar**. Hay varias formas de importarlos:

```python
import math                       # todo el módulo: se usa math.sqrt()
print(math.sqrt(81))              # 9.0

from math import sqrt, pi         # solo lo que se indica: se usa sqrt()
print(sqrt(81) * pi)

import random as rd               # con un alias más corto
print(rd.randint(1, 6))
```

| Forma | Cómo se usa | Cuándo |
|---|---|---|
| `import math` | `math.sqrt(9)` | Por defecto: queda claro de dónde viene cada función. |
| `from math import sqrt` | `sqrt(9)` | Cuando usas mucho una o dos funciones. |
| `import random as rd` | `rd.randint(1, 6)` | Cuando el nombre del módulo es largo. |

!!! warning "Evita `from módulo import *`"
    Importa **todo** sin que se vea qué, y puede tapar tus propias variables o funciones con el mismo nombre. Los `import` van siempre **al principio** del fichero.

### Tres módulos muy útiles

**`math`**: funciones matemáticas.

| Función | Ejemplo | Resultado |
|---|---|---|
| `math.sqrt(x)` | `math.sqrt(2)` | `1.4142...` |
| `math.ceil(x)` | `math.ceil(4.1)` | `5` (redondea hacia arriba) |
| `math.floor(x)` | `math.floor(4.9)` | `4` (redondea hacia abajo) |
| `math.hypot(a, b)` | `math.hypot(3, 4)` | `5.0` (hipotenusa) |
| `math.pi`, `math.e` | | Constantes |

**`random`**: números al azar.

| Función | Qué devuelve |
|---|---|
| `random.randint(a, b)` | Un entero entre `a` y `b`, **ambos incluidos**. |
| `random.random()` | Un decimal entre 0 y 1 (sin llegar a 1). |
| `random.uniform(a, b)` | Un decimal entre `a` y `b`. |
| `random.choice(secuencia)` | Un elemento al azar: `random.choice("AEIOU")` → una vocal. |

**`datetime`**: fechas y horas.

```python
from datetime import date, datetime

hoy = date.today()
print(hoy)                         # 2026-11-17
print(hoy.year, hoy.month, hoy.day)

ahora = datetime.now()
print(ahora.hour, ahora.minute)    # hora y minutos actuales

examen = date(2026, 12, 18)
dias = (examen - hoy).days         # restar fechas da los días entre ellas
print(f"Faltan {dias} días para el examen")
```

!!! success "Ahora tú"
    **Asistente de viaje.** Construye un programa con estas funciones, importando lo necesario al principio:

    1. `dias_hasta(dia, mes, anio)`: devuelve los días que faltan desde hoy hasta esa fecha (usa `datetime`).
    2. `depositos_necesarios(km, autonomia)`: devuelve cuántas veces hay que llenar el depósito para recorrer `km` kilómetros, **redondeando hacia arriba** (usa `math.ceil`).
    3. `codigo_reserva()`: devuelve un código de 4 letras mayúsculas al azar, construido con un `for` y `random.choice("ABCDEFGHJKLMNPQRSTUVWXYZ")`.

    El programa principal pide la fecha del viaje, los km y la autonomía del coche, y muestra:

    ```text
    Faltan 32 días para tu viaje
    Tendrás que llenar el depósito 3 veces
    Código de reserva: KTQB
    ```

## 9. Módulos propios y organización del código

Cualquier fichero `.py` que escribas es un módulo, y sus funciones se pueden importar desde **otro fichero de la misma carpeta**.

```python
# Fichero: conversiones.py
"""Funciones para convertir unidades."""

KM_POR_MILLA = 1.609344


def millas_a_km(millas):
    """Convierte millas a kilómetros."""
    return millas * KM_POR_MILLA


def km_a_millas(km):
    """Convierte kilómetros a millas."""
    return km / KM_POR_MILLA
```

```python
# Fichero: principal.py (en la misma carpeta)
import conversiones

distancia = float(input("Distancia en millas: "))
print(f"Son {conversiones.millas_a_km(distancia):.2f} km")
```

```text
mi_proyecto/
├── conversiones.py     ← módulo con las funciones
└── principal.py        ← programa que las usa
```

### `if __name__ == "__main__":`

Al importar un módulo, Python **ejecuta todo su código**. Si `conversiones.py` tuviera pruebas o un `input()` sueltos, se ejecutarían al importarlo. Para evitarlo, el código que solo debe ejecutarse **al lanzar el fichero directamente** se pone dentro de este `if`:

```python
# Al final de conversiones.py
if __name__ == "__main__":
    # Solo se ejecuta con: python conversiones.py
    # NO se ejecuta al hacer: import conversiones
    print(millas_a_km(26.2))
```

`__name__` es una variable especial: vale `"__main__"` en el fichero que se ejecuta y el nombre del módulo (`"conversiones"`) en los ficheros importados.

### Cómo organizar un programa

A partir de ahora, tus programas seguirán este orden:

```python
"""Docstring del programa: qué hace."""

# 1. Importaciones
import math

# 2. Constantes
PRECIO_BASE = 3.50


# 3. Funciones
def calcular_precio(distancia):
    """Precio del trayecto según la distancia."""
    return PRECIO_BASE + math.ceil(distancia) * 0.40


def main():
    """Programa principal."""
    km = float(input("Km: "))
    print(f"Precio: {calcular_precio(km):.2f} €")


# 4. Punto de entrada
if __name__ == "__main__":
    main()
```

Meter el programa principal en una función `main()` tiene una ventaja: **todas** sus variables son locales, así que ninguna función puede usarlas «por accidente» como globales.

!!! success "Ahora tú"
    **Tu primer módulo.** Crea una carpeta `geometria` con dos ficheros:

    1. `figuras.py`, con un docstring de módulo y las funciones `area_circulo(radio)`, `area_triangulo(base, altura)` y `perimetro_circulo(radio)` (usa `math.pi`). Al final, dentro de `if __name__ == "__main__":`, muestra el área de un círculo de radio 1 como prueba.
    2. `principal.py`, con una función `main()` que muestre un menú para elegir la figura, pida los datos y muestre el resultado con 2 decimales usando las funciones de `figuras`.

    Ejecuta `figuras.py` y después `principal.py`. ¿Aparece la prueba de `figuras.py` al ejecutar `principal.py`? ¿Por qué?

## 10. Pruebas y depuración de funciones

### Probar funciones con `assert`

Una ventaja de las funciones que **devuelven** un valor es que son muy fáciles de **probar**: se llaman con unos datos de los que conoces el resultado y se comprueba con [`assert`](../ut02/d-excepciones.md#7-aserciones-assert) que coincide.

```python
def es_bisiesto(anio):
    """Indica si un año es bisiesto."""
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


# Pruebas
assert es_bisiesto(2024), "2024 es bisiesto"
assert not es_bisiesto(2023), "2023 no es bisiesto"
assert not es_bisiesto(1900), "1900 no es bisiesto (múltiplo de 100)"
assert es_bisiesto(2000), "2000 es bisiesto (múltiplo de 400)"
print("Todas las pruebas superadas")
```

Si alguna prueba falla, el `AssertionError` te dice **cuál**. Cada vez que cambies la función, vuelve a ejecutar las pruebas para comprobar que no has roto nada.

!!! tip "Qué casos probar"
    - Un caso **normal** (2024).
    - Los **límites**: el primer y el último valor válidos (en un rango del 1 al 10, prueba el 1 y el 10).
    - Los casos **especiales**: cero, negativos, cadenas vacías... y los que la función trata aparte (1900 y 2000).

Para probar una función que **lanza una excepción** con datos incorrectos, se usa `try` / `except`:

```python
def pedir_divisor(n):
    if n == 0:
        raise ValueError("El divisor no puede ser 0")
    return n


try:
    pedir_divisor(0)
    assert False, "Debería haber lanzado ValueError"
except ValueError:
    pass                           # es lo esperado: la prueba se supera
```

### Depurar funciones en VS Code

Con el depurador (UT02) puedes seguir la ejecución **dentro** de las funciones:

| Tecla | Acción con funciones |
|---|---|
| `F10` (*Paso por encima*) | Ejecuta la llamada **entera** sin entrar en la función. |
| `F11` (*Paso al interior*) | **Entra** en la función y la recorre línea a línea. |
| `Shift+F11` (*Paso al exterior*) | Termina la función actual y **vuelve** a donde se llamó. |

Fíjate en dos paneles:

- **Variables**: muestra las variables **locales** de la función en la que estás y, aparte, las globales.
- **Pila de llamadas** (*Call Stack*): muestra qué función ha llamado a cuál. Lo usarás mucho en la [recursividad](b-recursividad.md).

!!! success "Ahora tú"
    **Letra del DNI.** La letra del DNI se obtiene dividiendo el número entre 23 y usando el resto como posición en la cadena `"TRWAGMYFPDXBNJZSQVHLCKE"` (posición 0 → `T`, 1 → `R`...).

    1. Escribe `letra_dni(numero)`, que devuelva la letra. Si el número es negativo o tiene más de 8 cifras, lanza `ValueError`.
    2. Escribe al menos **cinco pruebas** con `assert`: `letra_dni(12345678)` debe dar `"Z"` y `letra_dni(0)` debe dar `"T"`. Añade una prueba para un número que dé resto 22 (por ejemplo, `22`) y otras dos que comprueben que se lanza `ValueError`.
    3. Introduce un error a propósito (por ejemplo, divide entre 24) y comprueba qué prueba falla.
    4. Pon un punto de interrupción en la llamada a `letra_dni` y entra en la función con `F11`. Observa el panel **Variables**.

## Resumen

- Una **función** agrupa código bajo un nombre: se **define** con `def` y se **ejecuta** al **llamarla** con paréntesis.
- Los **parámetros** reciben los **argumentos**: por posición, por nombre o con valor por defecto. `/` y `*` obligan a una forma concreta.
- `return` **devuelve** un valor y termina la función. Sin `return`, la función devuelve `None`. Varios valores se devuelven como tupla.
- Las funciones pueden **modificar** objetos mutables (listas), pero no inmutables: para estos, devuelve el nuevo valor.
- Las variables de una función son **locales**. Evita `global`; usa parámetros y `return`. `nonlocal` modifica variables de la función que la contiene.
- Documenta con **docstrings** y **anotaciones de tipo**.
- Importa módulos con `import` o `from ... import`; crea los tuyos y protege su código de prueba con `if __name__ == "__main__":`.
- Prueba las funciones con `assert` y entra en ellas con `F11` en el depurador.
