# Rúbrica y guía de corrección · Proyecto UT02

Válida para las variantes **A** y **B**. Puntuación total: **10 puntos**.

## Criterios

| # | Criterio | Puntos | Qué se valora |
|:-:|---|:-:|---|
| 1 | Documentación y constantes | 1 | **Docstring** y comentarios útiles (0,5). Las 4 constantes definidas en MAYÚSCULAS y **usadas** en el código, sin «números mágicos» (0,5). |
| 2 | Conversiones y formato (UT01) | 1 | Datos leídos convertidos al tipo correcto (`int`/`float`/`str`) (0,5). Salida con f-strings y 2 decimales en importes y medias (0,5). |
| 3 | Validación con `try` / `except` | 2 | Captura una excepción **concreta** (`ValueError`), no un `except:` genérico (0,5). **Repite la pregunta** hasta obtener un dato válido (1). Rechaza también los valores válidos pero **fuera de rango** (0 o negativos en A; fuera de 0-10 en B) (0,5). |
| 4 | Selección | 1,5 | Uso correcto de `if` / `elif` / `else` (o `match`) para: (A) opciones del menú, rechazo de retiradas por saldo/límite y avisos; (B) calificación por tramos, con los **tramos frontera** correctos (9, 7 y 5). |
| 5 | Repetición y control de flujo | 2 | Bucle correcto para el menú (A) o para el recorrido de alumnos y notas (B), con condición de parada adecuada, sin bucles infinitos involuntarios (1,5). (A) límite de 3 intentos del PIN con bloqueo / (B) bucle anidado (alumnos → notas); uso adecuado de `break` / `continue` / `else` (0,5). |
| 6 | Contadores, acumuladores y resumen | 1,5 | (A) contador de operaciones exitosas (solo ingresos y retiradas), saldo y variación. (B) aprobados/suspensos, media de la clase y **mejor alumno**. Las variables se **inicializan** correctamente. |
| 7 | Funcionamiento | 1 | Se ejecuta sin errores de principio a fin con los casos de `pruebas.md` (0,5) y **no se rompe** con datos erróneos (0,5). |
| | **Total** | **10** | |

## Niveles de logro (orientativo)

| Nota | Perfil |
|:-:|---|
| **9-10** | Cumple todos los requisitos, con validación robusta y código claro. |
| **7-8,9** | Cumple los requisitos principales. Fallos menores: algún tramo frontera, un mensaje, una constante sin usar. |
| **5-6,9** | El flujo principal funciona (menú o lectura de datos y cálculos), pero falta la validación, el resumen o hay errores lógicos. |
| **< 5** | No se ejecuta, o faltan estructuras esenciales (bucle de menú o de lectura, decisiones...). |

## Guía de corrección

1. **Ejecuta** el programa con los casos de `pruebas.md`, **incluyendo el de datos erróneos**. Compara el comportamiento, no el texto exacto.
2. Anota los **errores de ejecución** (`ValueError`, `NameError`, bucles infinitos...). Un programa que «se rompe» a mitad puede seguir puntuando en lo que sí funciona.
3. Revisa el **código**: docstring, constantes, `except` concreto, inicialización de acumuladores, condiciones de los `if`.
4. Aplica los criterios con las **penalizaciones** de la tabla.

### Errores frecuentes y cómo puntuarlos

| Error | Consecuencia |
|---|---|
| `except:` a secas | Criterio 3: se pierden los 0,5 del `except` concreto. |
| Valida el tipo (`float`) pero no el rango | Criterio 3: se pierden los 0,5 del rango. |
| Pide el dato solo dos veces en lugar de repetir hasta que sea válido (sin bucle) | Criterio 3: no puntúa el «repite hasta válido». |
| (A) Cuenta las consultas o los rechazos como operaciones | Criterio 6. |
| (A) Tras el bloqueo por PIN sigue mostrando el menú | Criterios 5 y 4. |
| (A) Comprueba el límite antes que el saldo | Válido si el mensaje es coherente; no se penaliza. |
| (B) Condiciones de calificación en orden incorrecto (`>= 5` primero) | Criterio 4: todas las notas salen «Aprobado». |
| (B) Inicializa `suma_notas` fuera del bucle de alumnos | La media acumula notas de alumnos anteriores: criterio 6. |
| (B) `mejor_media` inicializada a `0` con un alumno de media 0 | No se penaliza (caso extremo). |
| No cierra el `break` del menú → bucle infinito | Criterio 5 y 7. |
| Variables mal nombradas (`a`, `x1`), sin comentarios | Criterio 1. |

## Ampliación opcional para el alumnado avanzado (no puntúa ni penaliza)

- **A**: expresión condicional para el aviso «Saldo bajo».
- **B**: porcentaje de aprobados con `f"{...:.1%}"`.

## Temporización orientativa

| Minutos | Tarea |
|:-:|---|
| 0-5 | Lectura del enunciado y planificación |
| 5-15 | Constantes, PIN (A) / número de alumnos (B) |
| 15-35 | Menú y operaciones (A) / lectura de alumnos y notas (B) |
| 35-50 | Validación con `try` / `except`, resumen final |
| 50-60 | Revisión, pruebas con datos erróneos y entrega |
