# Programación en Python — Índice de contenidos

## Índice general

- [UT01. Identificación de los elementos de un programa informático](#ut01-identificación-de-los-elementos-de-un-programa-informático)
- [UT02. Uso de estructuras de control](#ut02-uso-de-estructuras-de-control)
- [UT03. Funciones](#ut03-funciones)
- [UT04. Cadenas de caracteres, listas, tuplas y diccionarios](#ut04-cadenas-de-caracteres-listas-tuplas-y-diccionarios)
- [UT05. Lectura y escritura de información](#ut05-lectura-y-escritura-de-información)
- [UT06. Programación orientada a objetos](#ut06-programación-orientada-a-objetos)

---

## UT01. Identificación de los elementos de un programa informático

### a) Estructura y bloques fundamentales
1. Introducción a la programación: concepto de programa, algoritmo y lenguaje de programación.
2. Python: características, versiones y ámbito de uso.
3. Entorno de trabajo: instalación del intérprete, IDE/editores, consola interactiva (REPL) y ejecución de scripts.
4. Estructura de un programa en Python:
   1. Sentencias y líneas de código.
   2. Indentación y bloques de código.
5. Palabras reservadas e identificadores: reglas y convenciones de nombrado (PEP 8).
6. Fases de desarrollo: análisis, diseño, codificación, prueba y documentación.

### b) Variables
1. Concepto de variable y de referencia a un objeto en memoria.
2. Declaración y asignación (asignación simple, múltiple y encadenada).
3. Reglas de nombrado y buenas prácticas.
4. Ámbito y ciclo de vida de una variable (introducción: local y global).
5. Eliminación de variables (`del`) y funciones `id()` y `type()`.

### c) Tipos de datos
1. Tipado dinámico y fuerte en Python.
2. Tipos numéricos: `int`, `float`.
3. Tipo lógico: `bool` (valores *truthy* y *falsy*).
4. Tipo cadena: `str` (introducción).
7. Mutabilidad e inmutabilidad.
8. Anotaciones de tipo (*type hints*): introducción.

### d) Literales
1. Literales numéricos: enteros (decimal, binario, octal, hexadecimal), reales y notación científica, complejos.
2. Literales de cadena: comillas simples, dobles y triples; secuencias de escape; cadenas *raw*; f-strings.
3. Literales lógicos: `True` y `False`.

### e) Constantes
1. Concepto de constante y diferencia con variable.
2. Convención de constantes en Python (mayúsculas) y ausencia de constantes reales.
3. Constantes del módulo `math` (`pi`, `e`) y otras constantes predefinidas.
4. Uso de constantes para mejorar la legibilidad y el mantenimiento.

### f) Operadores y expresiones
1. Operadores aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
2. Operadores de asignación y asignación aumentada (`+=`, `-=`, etc.).
3. Operadores de comparación (relacionales).
4. Operadores lógicos: `and`, `or`, `not` (evaluación en cortocircuito).
6. Operadores de identidad (`is`, `is not`) y de pertenencia (`in`, `not in`).
7. Precedencia y asociatividad de operadores; uso de paréntesis.
8. Expresiones: concepto, evaluación y expresiones compuestas.
9. Operador *walrus* (`:=`): introducción.
10. Uso del módulo `math` en expresiones matemáticas.

### g) Conversiones de tipo
1. Conversión implícita (coerción) de tipos.
2. Conversión explícita (*casting*): `int()`, `float()`, `str()`, `bool()`, `complex()`.
3. Conversión entre sistemas de numeración: `bin()`, `oct()`, `hex()`.
4. Errores habituales en conversiones (`ValueError`, `TypeError`).
5. Comprobación de tipos: `type()` e `isinstance()`.

### h) Comentarios
1. Comentarios de una línea (`#`) y de varias líneas.
2. *Docstrings* (cadenas de documentación).
3. Buenas prácticas: qué comentar y qué no.
4. Documentación y estilo de código (PEP 8 y PEP 257).

---

## UT02. Uso de estructuras de control

### a) Estructuras de selección
1. Concepto de flujo de control y diagramas de flujo.
2. Condicional simple: `if`.
3. Condicional doble: `if … else`.
4. Condicional múltiple: `if … elif … else`.
5. Condiciones compuestas y anidamiento de condicionales.
6. Expresión condicional (operador ternario).
7. Selección múltiple con `match … case` (Python 3.10+).
8. Errores comunes: indentación, `=` frente a `==`, condiciones mal formuladas.

### b) Estructuras de repetición
1. Concepto de bucle, iteración y condición de parada.
2. Bucle `while`: sintaxis, bucles controlados por condición y por centinela, bucles infinitos.
3. Bucle `for`: iteración sobre secuencias e iterables.
4. Función `range()` y sus parámetros (inicio, fin, paso).
5. Bucles anidados.
6. Cláusula `else` en bucles.
7. Patrones típicos: contadores, acumuladores, búsqueda de máximos y mínimos, validación de entradas.

### c) Estructuras de salto
1. Sentencia `break`: salida anticipada de un bucle.
2. Sentencia `continue`: salto a la siguiente iteración.
3. Sentencia `pass`: bloque vacío.
4. Uso adecuado de las sentencias de salto y alternativas para un código más legible.

### d) Control de excepciones
1. Concepto de error, excepción y traza de error (*traceback*).
2. Tipos de errores: sintaxis, ejecución y lógicos.
3. Excepciones más comunes: `ValueError`, `TypeError`, `ZeroDivisionError`, `IndexError`, `KeyError`, `FileNotFoundError`, etc.
4. Estructura `try … except`: captura de una o varias excepciones.
5. Cláusulas `else` y `finally`.
6. Lanzamiento de excepciones con `raise`.
7. Aserciones con `assert`.
8. Validación de entradas de usuario con excepciones.
9. Introducción a las excepciones personalizadas.
10. Depuración básica: uso del depurador y mensajes de traza.

---

## UT03. Funciones

### a) Definición de funciones definidas por el programador
1. Concepto de función: reutilización, modularidad y abstracción.
2. Definición y llamada de funciones (`def`).
3. Parámetros y argumentos:
   1. Parámetros posicionales y por nombre.
   2. Valores por defecto.
   4. Argumentos solo posicionales y solo por nombre.
4. Valor de retorno (`return`): retorno único y múltiple (tuplas), funciones sin retorno.
5. Paso de argumentos: referencia a objetos y efecto en objetos mutables e inmutables.
6. Ámbito de las variables: local, global (`global`) y `nonlocal`.
7. Documentación de funciones: docstrings y anotaciones de tipo.
10. Funciones predefinidas (*built-in*) y uso de módulos: `import`, `from … import`, módulos de la biblioteca estándar (`math`, `random`, `datetime`).
11. Creación de módulos propios y organización del código.
12. Pruebas y depuración de funciones.

### b) Recursividad
1. Concepto de recursividad y comparación con la iteración.
2. Estructura de una función recursiva: caso base y caso recursivo.
3. Ejemplos clásicos: factorial, sucesión de Fibonacci, potencia, suma de dígitos, inversión de cadenas, torres de Hanoi.
4. Pila de llamadas y límite de recursión (`RecursionError`).
5. Ventajas, inconvenientes y cuándo usar recursividad.

---

## UT04. Cadenas de caracteres, listas, tuplas y diccionarios

### a) Cadenas de caracteres
1. Concepto de cadena y su carácter inmutable.
2. Creación de cadenas y secuencias de escape.
3. Acceso a caracteres: indexación (positiva y negativa) y *slicing* (rebanado).
4. Operaciones básicas: concatenación, repetición, longitud (`len()`), pertenencia (`in`) y comparación.
5. Recorrido de cadenas.
6. Métodos de cadena:
   1. Mayúsculas y minúsculas: `upper()`, `lower()`, `capitalize()`, `title()`.
   2. Búsqueda y sustitución: `find()`, `count()`, `replace()`, `startswith()`, `endswith()`.
   3. Limpieza: `strip()`, `lstrip()`, `rstrip()`.
   4. División y unión: `split()`, `join()`.
   5. Comprobación: `isdigit()`, `isalpha()`, `isalnum()`, etc.
7. Formateo de cadenas: operador `%`, `format()` y f-strings.

### b) Listas
1. Concepto de lista: colección ordenada y mutable.
2. Creación de listas y listas heterogéneas.
3. Acceso a elementos: indexación y *slicing*.
4. Modificación de elementos.
5. Métodos de listas: `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `clear()`, `index()`, `count()`, `sort()`, `reverse()`.
6. Operaciones: concatenación, repetición, pertenencia y `del`.
7. Funciones asociadas: `len()`, `min()`, `max()`, `sum()`, `sorted()`.
8. Recorrido de listas (`for`, `enumerate()`).
9. Copia de listas: referencia, copia superficial y copia profunda.
10. Listas anidadas y matrices.
11. Listas por comprensión.
12. Algoritmos básicos: búsqueda (lineal) y ordenación.
13. Introducción a los conjuntos (`set`) como estructura complementaria.

### c) Tuplas
1. Concepto de tupla: colección ordenada e inmutable.
2. Creación de tuplas y tuplas de un solo elemento.
3. Acceso a elementos e *slicing*.
4. Operaciones y métodos: `count()`, `index()`, concatenación y repetición.
5. Empaquetado y desempaquetado de tuplas.
6. Tuplas como valores de retorno en funciones.
7. Conversión entre listas y tuplas.
8. Comparativa: cuándo usar tuplas y cuándo listas.

### d) Diccionarios
1. Concepto de diccionario: pares clave-valor.
2. Creación de diccionarios y requisitos de las claves (tipos hashables).
3. Acceso a valores: `[]` y `get()`.
4. Inserción, modificación y eliminación de elementos: `pop()`, `popitem()`, `del`, `clear()`.
5. Métodos principales: `keys()`, `values()`, `items()`, `update()`, `setdefault()`.
6. Recorrido de diccionarios.
7. Comprobación de pertenencia de claves (`in`).
8. Diccionarios anidados.
9. Diccionarios por comprensión.
10. Combinación de estructuras: listas de diccionarios, diccionarios de listas.
11. Ejemplos de uso: contadores de frecuencia, agendas, inventarios.

---

## UT05. Lectura y escritura de información

### a) Entrada desde teclado
1. Función `input()`: lectura de cadenas.
2. Conversión de los datos leídos a otros tipos.
3. Validación de entradas y tratamiento de errores.
4. Lectura de varios datos en una misma línea.

### b) Salida a pantalla
1. Función `print()`: parámetros `sep`, `end` y `file`.
2. Formateo de la salida: f-strings, `format()` y alineación de texto y números.
3. Salida de errores (`sys.stderr`).
4. Buenas prácticas en la presentación de datos.

### c) Ficheros de datos
1. Concepto de fichero y almacenamiento persistente.
2. Ficheros de texto y ficheros binarios.
3. Formatos habituales: TXT, CSV, JSON.
4. Codificación de caracteres (UTF-8) y saltos de línea.

### d) Registros
1. Concepto de registro y campo.
2. Representación de registros: tuplas, diccionarios y clases sencillas.
3. Registros de longitud fija y variable; uso de delimitadores.
4. Almacenamiento de colecciones de registros (ejemplos: agenda, inventario).

### e) Apertura y cierre de ficheros. Modos de acceso
1. Función `open()` y objeto fichero.
2. Modos de acceso: lectura (`r`), escritura (`w`), añadir (`a`), creación exclusiva (`x`), texto (`t`), binario (`b`) y actualización (`+`).
3. Cierre de ficheros: `close()`.
4. Gestión de recursos con la sentencia `with`.
5. Acceso secuencial y acceso aleatorio: `seek()` y `tell()`.
6. Excepciones asociadas: `FileNotFoundError`, `PermissionError`, `IOError`.

### f) Escritura y lectura de información en ficheros
1. Lectura: `read()`, `readline()`, `readlines()` y recorrido línea a línea.
2. Escritura: `write()` y `writelines()`.
3. Ficheros CSV: módulo `csv` (`reader`, `writer`, `DictReader`, `DictWriter`).
4. Ficheros JSON: módulo `json` (`load`, `dump`, `loads`, `dumps`).
6. Operaciones típicas: añadir, buscar, modificar y borrar registros en un fichero.

### g) Utilización de los sistemas de ficheros
1. Estructura de un sistema de ficheros: rutas absolutas y relativas, separadores según el sistema operativo.
2. Módulo `os`: directorio de trabajo, listado de contenidos, información de ficheros.
3. Módulo `os.path`: `exists()`, `isfile()`, `isdir()`, `join()`, `basename()`, `splitext()`, etc.
4. Módulo `pathlib`: manejo de rutas orientado a objetos.
5. Recorrido de directorios (`os.walk()`, `glob`).
6. Permisos y atributos de ficheros.

### h) Creación y eliminación de ficheros y directorios
1. Creación de ficheros.
2. Creación de directorios: `os.mkdir()`, `os.makedirs()`.
3. Eliminación de ficheros: `os.remove()`.
4. Eliminación de directorios: `os.rmdir()`, `shutil.rmtree()`.
5. Renombrado, copia y movimiento: `os.rename()`, `shutil.copy()`, `shutil.move()`.
6. Comprobaciones previas y tratamiento de errores.
7. Precauciones al eliminar datos y trabajo con ficheros temporales.

---

## UT06. Programación orientada a objetos

### Introducción a la programación orientada a objetos
1. Paradigmas de programación: comparativa entre programación estructurada y orientada a objetos.
2. Conceptos básicos: clase, objeto, atributo, método e instancia.
3. Definición de clases (`class`), constructor (`__init__`) y el parámetro `self`.
4. Atributos de instancia y atributos de clase.
5. Métodos de instancia, de clase (`@classmethod`) y estáticos (`@staticmethod`).
6. Métodos especiales: `__str__()`, `__repr__()`, `__eq__()`, `__len__()`, etc.
7. Representación de clases con diagramas UML.

### a) Encapsulación
1. Concepto de encapsulación y ocultación de información.
2. Convenciones de visibilidad en Python: público, protegido (`_x`) y privado (`__x`).
3. *Name mangling*.
4. Métodos *getter* y *setter*.
5. Propiedades con `@property` y `@x.setter`.
6. Validación de datos en atributos.
7. Ventajas de la encapsulación: seguridad, mantenimiento y coherencia de los datos.

### b) Herencia
1. Concepto de herencia y jerarquía de clases (relación «es un»).
2. Clase base (superclase) y clase derivada (subclase).
3. Uso de `super()` y llamada al constructor de la clase padre.
4. Sobrescritura de métodos.
5. Herencia múltiple y orden de resolución de métodos (MRO).
6. Funciones `isinstance()` e `issubclass()`.
7. Composición frente a herencia (relación «tiene un»).
8. Clases abstractas: módulo `abc` (`ABC`, `@abstractmethod`).

### c) Polimorfismo
1. Concepto de polimorfismo.
2. Polimorfismo por herencia y sobrescritura de métodos.
3. Polimorfismo por *duck typing* (tipado de pato).
4. Sobrecarga de operadores mediante métodos especiales (`__add__`, `__lt__`, etc.).
5. Ausencia de sobrecarga clásica de métodos en Python y alternativas (argumentos por defecto, `*args`).
6. Ejemplos integradores: jerarquía de figuras geométricas, cuentas bancarias, empleados, animales.

### Cierre de la unidad
1. Diseño de un pequeño proyecto orientado a objetos que integre las seis unidades (estructuras de control, funciones, colecciones, persistencia en ficheros y clases).
2. Buenas prácticas de diseño y organización del código en módulos.
