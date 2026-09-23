# a) Estructura y bloques fundamentales

## 1. Introducción a la programación

Un **programa** es un conjunto de instrucciones que el ordenador ejecuta para resolver un problema.
Antes de escribir el programa hace falta un **algoritmo**: los pasos ordenados, precisos y finitos que resuelven ese problema.

!!! example "Un algoritmo de la vida real"
    Preparar un té:

    1. Llenar el cazo con agua.
    2. Calentar el agua hasta que hierva.
    3. Poner la bolsita en la taza.
    4. Verter el agua en la taza.
    5. Esperar tres minutos y retirar la bolsita.

    Es un algoritmo porque los pasos son claros, están ordenados y terminan.

El ordenador solo entiende código máquina (ceros y unos). Un **lenguaje de programación** nos permite escribir las instrucciones de forma
que sean comprensibles para las personas, y un programa especial se encarga de traducirlas a código maquina. Dependiendo del lenguaje, este programa recibe el nombre de **interprete** o **compilador**

| | Compilado | Interpretado |
|---|---|---|
| Cómo funciona | Se traduce **todo** el programa a código máquina antes de ejecutarlo. Genera un archivo **ejecutable**| Un **intérprete** traduce y ejecuta el programa **línea a línea**. No se genera nada|
| Ejemplos | C, C++ | **Python**, JavaScript |
| Ventaja | Suele ejecutarse más rápido. | Puedes probar código al instante. |

## 2. Python

**Python** es un lenguaje de alto nivel (cercano al lenguaje humano) e interpretado.

- **Sintaxis clara y legible**: el código se parece mucho a un texto en inglés.
- **Multiplataforma**: funciona en Windows, Linux y macOS.
- **Tipado dinámico**: no hace falta declarar el tipo de las variables (lo veremos en el [apartado c](c-tipos.md)).
- **Biblioteca estándar muy amplia**: matemáticas, fechas, ficheros, redes...
- Es gratuito y tiene una comunidad enorme.

**Versiones.** Vamos a trabajar con **Python 3** (versión 3.10 o superior). Python 2 está obsoleto y no se usa. Para saber qué versión tienes:

```text
python --version
```

**¿Dónde se usa?** Automatización de tareas y administración de sistemas (muy útil en SMR), desarrollo web, análisis de datos,
inteligencia artificial, ciberseguridad, educación...

## 3. Entorno de trabajo

Vamos a usar tres herramientas. Todas ejecutan el mismo Python; cambia la forma de trabajar con él.

=== "Consola de Python (REPL)"

    **REPL** significa *Read-Eval-Print Loop*: lee una instrucción, la evalúa, muestra el resultado y vuelve a esperar.
    Es perfecta para probar cosas rápidas.

    Se abre escribiendo `python` en una terminal. Verás el símbolo `>>>`:

    ```text
    >>> 2 + 3
    5
    >>> print("Hola")
    Hola
    >>> exit()
    ```

    - `exit()` (o `Ctrl+Z` y Enter en Windows) cierra la consola.
    - `help(len)` muestra la ayuda de una función. **Funciona sin internet**, así que la usarás mucho en los proyectos de clase.
    - Lo que escribes en el REPL **no se guarda**.

=== "Visual Studio Code"

    Es el editor con el que escribirás **programas completos** guardados en archivos `.py`.

    **Preparación (una sola vez)**

    1. Instala la extensión **Python** (de Microsoft) desde el panel de extensiones (`Ctrl+Shift+X`).
    2. Instala también la extensión **Jupyter** si vas a trabajar con cuadernos.

    **Tu primer programa**

    1. `Archivo → Abrir carpeta...` y elige una carpeta para tus prácticas.
    2. Crea un archivo nuevo llamado `hola.py`.
    3. Escribe:

        ```python
        print("¡Hola, mundo!")
        ```

    4. Ejecútalo con el botón ▶ (arriba a la derecha) o, en la terminal integrada (`` Ctrl+` ``):

        ```text
        python hola.py
        ```

    !!! tip "Elige bien el intérprete"
        Abajo a la derecha, VS Code muestra la versión de Python que usa. Si no aparece o no es la 3.10+,
        pulsa `Ctrl+Shift+P` y elige **Python: Select Interpreter**.

=== "Jupyter Notebook"

    Un **cuaderno** (`.ipynb`) está formado por **celdas**. Hay celdas de **código** (se ejecutan) y celdas de **texto** en Markdown
    (se leen). El resultado aparece justo debajo de la celda.

    **En VS Code**

    1. `Ctrl+Shift+P` → **Jupyter: Create New Jupyter Notebook**.
    2. Botón **+ Código** para añadir una celda de código y **+ Markdown** para una de texto.
    3. Escribe en una celda y ejecútala con `Shift+Enter`.
    4. Arriba a la derecha elige el **kernel** (el Python que ejecuta las celdas).

    ```python
    nombre = "Ana"
    print("Hola,", nombre)
    ```

    !!! warning "El orden de ejecución importa"
        Un cuaderno recuerda las variables **en el orden en que ejecutas las celdas**, no en el orden en que aparecen.
        Si algo se comporta de forma rara, usa **Reiniciar** el kernel y **Ejecutar todo** para empezar desde cero.

    !!! note "`input()` en un cuaderno"
        Al ejecutar `input()`, aparece una **caja de texto en la parte superior** de la ventana. Escribe ahí y pulsa Enter.

### ¿Cuándo uso cada una?

| Quiero... | Uso |
|---|---|
| Probar una instrucción suelta o comprobar qué hace una función | Consola (REPL) |
| Escribir un programa completo que se pueda guardar y ejecutar entero | VS Code (`.py`) |
| Experimentar paso a paso, mezclando código, resultados y explicaciones | Jupyter Notebook |

### Dos funciones para empezar

Antes de nada necesitas mostrar y leer datos. Se estudian a fondo en la UT05; ahora solo lo imprescindible:

```python
nombre = input("¿Cómo te llamas? ")     # pide un dato por teclado y lo guarda
print("Encantado de conocerte,", nombre)  # muestra un mensaje por pantalla
```

## 4. Estructura de un programa en Python

Un programa es una **secuencia de sentencias** que se ejecutan de arriba abajo, una tras otra.

### Sentencias y líneas de código

- Normalmente hay **una sentencia por línea**. No hace falta punto y coma al final.
- Una sentencia muy larga se puede partir dentro de paréntesis:

```python
total = (10 + 20 +
         30 + 40)
print(total)
```

### Indentación y bloques de código

En otros lenguajes los bloques se marcan con llaves `{ }`. **En Python se marcan con la indentación** (los espacios al comienzo de la línea).
Un bloque empieza tras una línea que termina en dos puntos `:` y todas sus líneas van con el mismo sangrado (por convención, **4 espacios**).

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")     # dentro del bloque
    print("Puedes votar")           # dentro del bloque
print("Fin del programa")           # fuera del bloque
```

!!! note "Adelanto"
    `if` se estudia en la [UT02](../ut02/a-seleccion.md). Aquí solo interesa ver cómo se forma un bloque.

!!! warning "Error típico: `IndentationError`"
    Mezclar espacios y tabuladores, o sangrar líneas de más o de menos, produce un `IndentationError`.
    VS Code inserta 4 espacios al pulsar `Tab`; deja que lo haga él.

## 5. Palabras reservadas e identificadores

Un **identificador** es el nombre que damos a una variable, función, etc. Reglas:

- Puede contener letras, dígitos y guion bajo `_`.
- **No** puede empezar por un dígito.
- Distingue mayúsculas de minúsculas: `edad` y `Edad` son nombres distintos.
- **No** puede ser una **palabra reservada**.

Las palabras reservadas son las que Python usa para su propia sintaxis. Puedes verlas todas:

```text
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

| Nombre | ¿Válido? | Motivo |
|---|:---:|---|
| `edad` | ✅ | |
| `nota_final` | ✅ | |
| `_temporal` | ✅ | Empieza por guion bajo, permitido. |
| `precio2` | ✅ | Los dígitos valen si no van al principio. |
| `2precio` | ❌ | Empieza por un dígito. |
| `mi-variable` | ❌ | El guion `-` es el operador resta. |
| `mi variable` | ❌ | Los espacios no están permitidos. |
| `class` | ❌ | Palabra reservada. |
| `Edad` | ✅ | Válido, pero distinto de `edad`. |

**Convención (PEP 8):** nombres en minúsculas y separando palabras con guion bajo (*snake_case*): `precio_final`, `numero_alumnos`.
Elige nombres que **expliquen qué guardan**: `precio_final` es mejor que `x` o `pf`.

## 6. Fases de desarrollo

Programar no es solo escribir código. El desarrollo de un programa sigue unas fases:

```text
Análisis → Diseño → Codificación → Prueba → Documentación (→ Mantenimiento)
```

| Fase | Pregunta que responde | Ejemplo: «calcular el área de un rectángulo» |
|---|---|---|
| **Análisis** | ¿Qué hay que resolver? ¿Qué datos entran y qué sale? | Entradas: base y altura. Salida: el área. |
| **Diseño** | ¿Cómo lo resuelvo? (pasos, pseudocódigo) | 1. Pedir base. 2. Pedir altura. 3. área = base × altura. 4. Mostrar. |
| **Codificación** | Escribir el algoritmo en Python. | Ver código más abajo. |
| **Prueba** | ¿Funciona? Probar con varios datos. | Base 4 y altura 3 → 12. Base 0 → 0. |
| **Documentación** | Explicar qué hace y cómo se usa. | Comentarios y descripción al inicio del programa. |

```python
base = float(input("Base: "))
altura = float(input("Altura: "))
area = base * altura
print("El área es", area)
```

!!! tip "Consejo"
    Cuanto mejor pienses el problema (análisis y diseño), menos tiempo perderás corrigiendo. En los proyectos de clase,
    dedica los **primeros 5 minutos a leer y planificar**.

## Resumen

- Un programa es un algoritmo escrito en un lenguaje de programación. Python es interpretado, legible y multiplataforma.
- Usamos la **consola** para probar, **VS Code** para programas `.py` y **Jupyter** para experimentar con celdas.
- En Python los bloques se marcan con **indentación** (4 espacios) tras los dos puntos `:`.
- Los identificadores no pueden empezar por número, ni contener espacios o guiones, ni ser palabras reservadas.
- Fases: análisis, diseño, codificación, prueba y documentación.
