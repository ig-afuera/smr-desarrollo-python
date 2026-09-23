# Proyecto de evaluación UT02

**Uso de estructuras de control**

> Este documento contiene **dos variantes equivalentes (A y B)** para repartir en el aula. Imprime o entrega **una sola variante por alumno/a**.
> Cada variante empieza en una página nueva y es autocontenida.

| | |
|---|---|
| **Duración máxima** | 1 hora (el proyecto está pensado para unos 50 minutos) |
| **Conexión a internet** | No |
| **Herramientas** | Visual Studio Code, consola de Python y/o Jupyter Notebook |
| **Entrega** | Un único archivo `.py` o `.ipynb` con tu nombre, en la carpeta indicada por el profesor/a |
| **Contenidos** | Todos los de la UT02 y los de la UT01 (constantes, conversiones de tipo, operadores, f-strings, comentarios...) |

---

<div style="page-break-after: always;"></div>

# VARIANTE A · Cajero automático

Nombre: ______________________________  Fecha: ______________

Programa el funcionamiento de un **cajero automático** sencillo.

## Requisitos

1. Al inicio del archivo, escribe un **docstring** que explique qué hace el programa. Añade **comentarios** donde ayuden a entender el código.
2. Define estas **constantes** (nombres en MAYÚSCULAS):
    - `PIN_CORRECTO`: `"1234"`
    - `MAX_INTENTOS`: `3`
    - `SALDO_INICIAL`: `500.0` €
    - `LIMITE_RETIRADA`: `300.0` € (máximo por cada retirada)
3. **Autenticación.** Pide el PIN, con un máximo de `MAX_INTENTOS` intentos.
    - Si es correcto, muestra `Acceso concedido` y continúa.
    - Si falla todas las veces, muestra `Tarjeta bloqueada` y **el programa termina** sin mostrar el menú.
4. **Menú.** Se muestra y **se repite** hasta que el usuario elija salir:
    ```text
    1. Consultar saldo
    2. Ingresar dinero
    3. Retirar dinero
    4. Salir
    ```
    Si la opción no es válida, se avisa y se vuelve a mostrar el menú.
5. **Consultar saldo**: muestra el saldo actual con 2 decimales.
6. **Ingresar y retirar**: se pide la **cantidad**, que debe ser un número **mayor que 0**. Si el usuario escribe otra cosa (texto, cero, negativos), se avisa y se **vuelve a pedir** (usa `try` / `except`).
7. **Retirar** se rechaza, avisando del motivo, si la cantidad es **mayor que el saldo** («Saldo insuficiente») o **mayor que el límite por retirada**. Si no, se descuenta del saldo.
8. **Resumen final** al salir: número de **operaciones realizadas con éxito** (ingresos y retiradas; no cuentan las consultas ni los rechazos), **saldo final** y **variación** respecto al saldo inicial (con signo: `+50.00` o `-50.00`).

**Ampliación (solo si te sobra tiempo):** al final, muestra el aviso `Saldo bajo` si el saldo final es inferior a 50 € y `Saldo correcto` en caso contrario, usando una **expresión condicional** (`a if condición else b`).

## Ejemplo de ejecución

Lo que teclea el usuario va detrás de los dos puntos. Los menús se han abreviado con `(menú)`.

```text
PIN (intento 1/3): 0000
PIN incorrecto
PIN (intento 2/3): 1234
Acceso concedido

(menú)
Elige una opción: 1
Saldo actual: 500.00 €

(menú)
Elige una opción: 2
Cantidad (€): abc
Cantidad no válida
Cantidad (€): 200
Ingreso realizado. Nuevo saldo: 700.00 €

(menú)
Elige una opción: 3
Cantidad (€): 400
No se puede retirar más de 300.00 € por operación

(menú)
Elige una opción: 3
Cantidad (€): 250
Retirada realizada. Nuevo saldo: 450.00 €

(menú)
Elige una opción: 3
Cantidad (€): 1000
Saldo insuficiente

(menú)
Elige una opción: 9
Opción no válida

(menú)
Elige una opción: 4

--- RESUMEN DE LA SESIÓN ---
Operaciones realizadas: 2
Saldo final: 450.00 €
Variación: -50.00 €
```

> No hace falta que los mensajes sean **idénticos** a los del ejemplo: importa que el programa se comporte igual.

## Recomendaciones

- Lee todo el enunciado antes de empezar y **prueba a menudo**. Empieza por lo básico: constantes, PIN y menú con «Salir».
- Añade las opciones del menú **de una en una**, comprobando que funcionan.
- Prueba también con **datos erróneos** (letras, cero, negativos): el programa no debe «romperse».
- Si te atascas, lee el mensaje de error y prueba la instrucción que falla en la consola de Python. `help()` funciona sin internet.

<div style="page-break-after: always;"></div>

# VARIANTE B · Gestor de notas de la clase

Nombre: ______________________________  Fecha: ______________

Programa un **gestor de notas** para un profesor: pide las notas de cada alumno, calcula su media y muestra un resumen de la clase.

## Requisitos

1. Al inicio del archivo, escribe un **docstring** que explique qué hace el programa. Añade **comentarios** donde ayuden a entender el código.
2. Define estas **constantes** (nombres en MAYÚSCULAS):
    - `NOTAS_POR_ALUMNO`: `3`
    - `NOTA_MIN`: `0`
    - `NOTA_MAX`: `10`
    - `NOTA_APROBADO`: `5`
3. Pide el **número de alumnos**. Debe ser un entero **mayor que 0**; si no, se avisa y se **vuelve a pedir** (usa `try` / `except`).
4. Para **cada alumno**, pide su **nombre** y sus `NOTAS_POR_ALUMNO` **notas** (admiten decimales). Cada nota debe ser un número entre `NOTA_MIN` y `NOTA_MAX`; si el usuario escribe otra cosa (texto o fuera de rango), se avisa y se **vuelve a pedir esa nota**.
5. Tras leer las notas de un alumno, calcula su **media** y su **calificación**:

    | Media | Calificación |
    |---|---|
    | 9 o más | Sobresaliente |
    | de 7 a menos de 9 | Notable |
    | de `NOTA_APROBADO` a menos de 7 | Aprobado |
    | menos de `NOTA_APROBADO` | Suspenso |

   y muestra: `Nombre: media 8.17 (Notable)` (media con 2 decimales).
6. **Resumen final** de la clase: número de **aprobados** (media ≥ `NOTA_APROBADO`), número de **suspensos**, **media de la clase** (media de las medias) y el **mejor alumno** con su media.

**Ampliación (solo si te sobra tiempo):** muestra también el **porcentaje de aprobados** de la clase con un decimal.

## Ejemplo de ejecución

Lo que teclea el usuario va detrás de los dos puntos.

```text
Número de alumnos: x
Escribe un número entero
Número de alumnos: 0
Debe haber al menos un alumno
Número de alumnos: 3

Alumno 1
Nombre: Ana
  Nota 1: 8
  Nota 2: 7.5
  Nota 3: 9
Ana: media 8.17 (Notable)

Alumno 2
Nombre: Luis
  Nota 1: abc
Escribe un número
  Nota 1: 11
  La nota debe estar entre 0 y 10
  Nota 1: 4
  Nota 2: 3.5
  Nota 3: 5
Luis: media 4.17 (Suspenso)

Alumno 3
Nombre: Marta
  Nota 1: 10
  Nota 2: 9
  Nota 3: 9.5
Marta: media 9.50 (Sobresaliente)

--- RESUMEN DE LA CLASE ---
Aprobados: 2
Suspensos: 1
Media de la clase: 7.28
Mejor alumno: Marta (9.50)
```

> No hace falta que los mensajes sean **idénticos** a los del ejemplo: importa que el programa se comporte igual.

## Recomendaciones

- Lee todo el enunciado antes de empezar y **prueba a menudo**. Empieza por un solo alumno y una sola nota, y amplía después.
- Prueba también con **datos erróneos** (letras, notas fuera de rango): el programa no debe «romperse».
- Piensa qué **variables** necesitas para el resumen final (contadores, acumuladores...) y **cuándo** hay que inicializarlas.
- Si te atascas, lee el mensaje de error y prueba la instrucción que falla en la consola de Python. `help()` funciona sin internet.
