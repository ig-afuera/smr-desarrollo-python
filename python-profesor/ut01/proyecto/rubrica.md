# Rúbrica y guía de corrección · Proyecto UT01

Válida para las variantes **A** y **B**. Puntuación total: **10 puntos**.

## Criterios

| # | Criterio | Puntos | Qué se valora |
|:-:|---|:-:|---|
| 1 | Documentación | 1 | **Docstring** inicial (0,5) y **comentarios** útiles en el código (0,5). |
| 2 | Constantes | 1 | Las 4 constantes definidas en **MAYÚSCULAS** al inicio y **usadas** en los cálculos; sin «números mágicos». Se restan 0,25 por cada constante ausente o no usada. |
| 3 | Entrada de datos y conversiones | 2 | Se piden todos los datos (0,5). Cada uno se convierte al tipo adecuado: `int` para cantidades y personas, `float` para importes y distancias, `str` para nombres (1,5; se restan 0,25 por conversión errónea). |
| 4 | Cálculos y expresiones | 2 | Todas las operaciones son correctas. Uso adecuado de operadores, precedencia y (A) `//` y `%` para el desglose del cambio / (B) conversión de la duración a horas. |
| 5 | Formato de la salida | 1,5 | f-strings (0,5), 2 decimales en importes (0,5) y alineación/centrado (0,5). |
| 6 | Valores lógicos | 1 | Los dos valores son **expresiones de comparación/lógicas**, correctas y **sin `if`**. Se muestra su valor. |
| 7 | Tipos de dato | 0,5 | Se muestra el `type()` de las tres variables pedidas. |
| 8 | Funcionamiento y estilo | 1 | El programa **se ejecuta sin errores** de principio a fin (0,5) y cumple PEP 8 básico: nombres descriptivos en *snake_case*, indentación de 4 espacios, espacios en operadores (0,5). |
| | **Total** | **10** | |

## Niveles de logro (orientativo)

| Nota | Perfil |
|:-:|---|
| **9-10** | Cumple todos los requisitos, sin errores, con buen formato y estilo cuidado. |
| **7-8,9** | Cumple los requisitos principales. Fallos menores de formato, alguna constante sin usar o algún comentario ausente. |
| **5-6,9** | El programa funciona y calcula bien los datos básicos, pero faltan partes (desglose, valores lógicos, tipos...) o el formato es deficiente. |
| **< 5** | No se ejecuta, no realiza los cálculos principales o faltan varios requisitos. |

## Guía de corrección

1. **Ejecuta** el programa del alumno con los casos de `pruebas.md` (**caso 1 y caso 2**). Compara importes, no el aspecto exacto.
2. Anota los **errores de ejecución** (`NameError`, `TypeError`, `ValueError`...). Un programa que «se rompe» a mitad puede seguir puntuando en los apartados que sí se ejecutan.
3. Revisa el **código**: docstring, comentarios, constantes, tipos convertidos, variables lógicas sin `if`.
4. Aplica los criterios con las **penalizaciones** de la tabla.

### Errores frecuentes y cómo puntuarlos

| Error | Consecuencia |
|---|---|
| No convierte `input()` con `int()`/`float()` | `TypeError` al calcular: criterio 3 y, si impide seguir, parte del criterio 4 y 8. |
| Usa `int()` en importes o distancias (pierde decimales) | Resultados erróneos: criterio 3 y 4. |
| Divide con `/` para el desglose del cambio (A) | Euros con decimales: criterio 4. |
| Olvida convertir la duración a horas (B) | Velocidad media incorrecta (dividir entre minutos): criterio 4. |
| Usa `if` para los valores lógicos | No puntúa el criterio 6 (aunque el resultado sea correcto). |
| Escribe `0.10`, `1.30`... directamente en las fórmulas | Criterio 2: constante definida pero no usada. |
| Muestra los importes sin formatear (`7.6000000000000005`) | Criterio 5. |

## Ampliación opcional para el alumnado avanzado (no puntúa ni penaliza)

- **A**: mostrar también el porcentaje de IVA con `f"{IVA:.0%}"` a partir de la constante.
- **B**: mostrar la hora de llegada si se parte a las 08:00 (con `//` y `%`).

## Temporización orientativa

| Minutos | Tarea |
|:-:|---|
| 0-5 | Lectura del enunciado y planificación |
| 5-20 | Constantes, entrada de datos y conversiones |
| 20-35 | Cálculos |
| 35-50 | Salida con formato, valores lógicos y tipos |
| 50-60 | Revisión, pruebas y entrega |
