# b) Variables

## 1. ¿Qué es una variable?

Una **variable** es un **nombre** que apunta a un valor guardado en la memoria del ordenador.
Piensa en ella como una etiqueta que pones a un objeto para poder encontrarlo después.

```pycon
>>> edad = 17
>>> edad
17
>>> edad + 1
18
```

En `edad = 17`, el signo `=` **no** significa «es igual a» como en matemáticas. Significa **asigna**: «crea el valor `17` y ponle la etiqueta `edad`».

```text
   edad ────────►  17
  (nombre)       (valor en memoria)
```

## 2. Declaración y asignación

En Python **no se declaran** las variables: se crean en el momento en que les asignas un valor por primera vez.

```python
nombre = "Lucía"
edad = 16
altura = 1.68
es_alumna = True
```

### Reasignación

Una variable puede cambiar de valor cuantas veces quieras, incluso de **tipo**:

```pycon
>>> dato = 10
>>> dato = "diez"
>>> dato
'diez'
```

### Asignación múltiple

```python
x, y, z = 1, 2, 3        # x=1, y=2, z=3
```

### Asignación encadenada

```python
a = b = c = 0            # las tres valen 0
```

### Intercambio de valores

En otros lenguajes hace falta una variable auxiliar; en Python es directo:

```pycon
>>> a, b = 1, 2
>>> a, b = b, a
>>> a, b
(2, 1)
```

!!! warning "El orden importa: la asignación va de derecha a izquierda"
    Primero se calcula lo que hay a la **derecha** del `=` y luego se guarda en la variable de la **izquierda**.
    Por eso es válido `contador = contador + 1`: se calcula `contador + 1` con el valor actual y el resultado se vuelve a guardar en `contador`.

## 3. Reglas de nombrado y buenas prácticas

Las reglas del [apartado a](a-estructura.md#5-palabras-reservadas-e-identificadores) siguen vigentes. Además:

| Haz | Evita |
|---|---|
| `precio_final`, `numero_alumnos` | `x`, `pf`, `a1` (no explican nada) |
| `minusculas_con_guion_bajo` | `PrecioFinal`, `precioFinal` (otros estilos) |
| Nombres en el idioma del proyecto y sin tildes ni ñ (`anio`, `contrasenia`) | Caracteres especiales: aunque Python los admite, dan problemas |
| Un nombre corto si su uso es muy local (`i` en un contador) | Nombres que se parecen mucho: `total` y `totall` |
| Un nombre que **no** coincida con una función de Python | `print = 5`, `len = 3`, `type = "x"` (pisan funciones útiles) |

!!! failure "Cuidado con pisar funciones"
    ```pycon
    >>> print = 5
    >>> print("hola")
    Traceback (most recent call last):
      ...
    TypeError: 'int' object is not callable
    ```
    Si te ocurre en Jupyter o en la consola, ejecuta `del print` para recuperar la función.

## 4. Ámbito y ciclo de vida de una variable

El **ámbito** es la zona del programa donde una variable existe y se puede usar. El **ciclo de vida** es el tiempo durante el que existe.

- Una variable **nace** cuando se le asigna un valor por primera vez.
- Una variable creada fuera de cualquier función es **global**: se puede usar en todo el programa.
- Una variable creada **dentro de una función** es **local**: solo existe mientras se ejecuta esa función.
- Usar una variable que aún no existe provoca un `NameError`.

```pycon
>>> print(saldo)
Traceback (most recent call last):
  ...
NameError: name 'saldo' is not defined
```

```python
mensaje = "Hola"              # variable global

def saludar():
    destinatario = "Ana"      # variable local: solo existe dentro de la función
    print(mensaje, destinatario)

saludar()
# print(destinatario)         # daría NameError: aquí ya no existe
```

!!! success "Prueba tu"
    Antes de ejecutar cada ejemplo, **apunta en un papel qué crees que va a mostrar**. Después cópialo en tu editor, ejecútalo y compara.

    **Ejemplo 1: una variable creada dentro de una función**

    ```python
    def preparar_mochila():
        objeto = "cuaderno"
        print("Dentro:", objeto)


    preparar_mochila()
    print("Fuera:", objeto)
    ```

    - ¿Qué línea se ejecuta bien y cuál falla? ¿Qué error aparece?
    - Borra la última línea y vuelve a ejecutar. ¿Qué deduces sobre dónde «vive» `objeto`?

    **Ejemplo 2: una variable creada fuera de la función**

    ```python
    temperatura = 22


    def mostrar_tiempo():
        print("Hace", temperatura, "grados")


    mostrar_tiempo()
    temperatura = 30
    mostrar_tiempo()
    ```

    - ¿Puede la función usar `temperatura` aunque no se haya creado dentro de ella?
    - ¿Por qué la segunda llamada muestra un valor distinto a la primera?
    - Mueve la línea `temperatura = 22` para que quede **debajo** de la primera llamada a `mostrar_tiempo()`. ¿Qué ocurre ahora y por qué?

    **Ejemplo 3: el mismo nombre dentro y fuera**

    ```python
    puntos = 100


    def perder_vida():
        puntos = 50
        print("Dentro de la función:", puntos)


    perder_vida()
    print("Fuera de la función:", puntos)
    ```

    - ¿Cuánto valen los `puntos` de fuera después de llamar a `perder_vida()`?
    - ¿Son la misma variable las dos `puntos`? Compruébalo añadiendo `print(id(puntos))` dentro y fuera de la función.

    **Ejemplo 4: leer una variable antes de asignarla (reto)**

    ```python
    nivel = 1


    def mostrar_nivel():
        print("Nivel actual:", nivel)


    def subir_nivel():
        print("Nivel antes:", nivel)
        nivel = 2
        print("Nivel después:", nivel)


    mostrar_nivel()
    subir_nivel()
    print("Nivel fuera:", nivel)
    ```

    - ¿Qué muestra `mostrar_nivel()`? ¿Cómo puede usar `nivel` si no se creó dentro de ella?
    - `subir_nivel()` falla en su primera línea, que es idéntica a la de `mostrar_nivel()`. ¿Qué error aparece? Fíjate en la palabra que acompaña a *variable* en el mensaje.
    - Cuando se produce el error, ¿existe un `nivel` global? Entonces, ¿por qué Python no lo usa?
    - Borra la línea `print("Nivel antes:", nivel)` y vuelve a ejecutar. ¿Qué muestra ahora la función? ¿Cuánto vale `nivel` fuera?
    - Recupera esa línea y cambia `nivel = 2` por `nuevo_nivel = 2` (y el último `print` de la función para que muestre `nuevo_nivel`). ¿Por qué ya no falla?

    Con lo que has observado, escribe con tus palabras **tres reglas**: una sobre lo que puede ver una función, otra sobre lo que ocurre al asignar un valor dentro de ella y otra sobre qué pasa si usas una variable dentro de una función antes de asignarle un valor.

!!! note "Adelanto"
    Las funciones se estudian en la [UT03](../index.md). Por ahora, todas tus variables serán globales. Lo importante es que sepas que las locales existen.

## 5. Eliminar variables y conocerlas: `del`, `id()` y `type()`

| Función | Qué hace |
|---|---|
| `type(x)` | Dice de qué **tipo** es el valor de `x`. |
| `id(x)` | Devuelve un número que **identifica** el objeto en memoria. |
| `del x` | **Elimina** el nombre `x` (deja de existir). |

```pycon
>>> precio = 9.99
>>> type(precio)
<class 'float'>
>>> a = 1000
>>> b = a
>>> id(a) == id(b)
True
>>> del a
>>> a
Traceback (most recent call last):
  ...
NameError: name 'a' is not defined
>>> b
1000
```

Observa que tras `b = a` **las dos variables apuntan al mismo objeto** (`id` idéntico). Al borrar `a` solo se elimina esa etiqueta; el valor sigue vivo mientras `b` lo use.

## Resumen

- Una variable es un **nombre que apunta a un valor**; se crea al asignar con `=`.
- Se puede reasignar, y también cambiar de tipo.
- Asignación múltiple (`a, b = 1, 2`), encadenada (`a = b = 0`) e intercambio (`a, b = b, a`).
- Nombres en *snake_case*, descriptivos y sin pisar funciones de Python.
- Existen variables **globales** y **locales**; usar una inexistente da `NameError`.
- `type()`, `id()` y `del` sirven para inspeccionar y eliminar.
