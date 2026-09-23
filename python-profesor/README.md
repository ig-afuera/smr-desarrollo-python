# Programación en Python · Repositorio del profesorado

Material **de uso exclusivo del profesor/a**: banco de preguntas tipo test, banco de ejercicios y proyectos de evaluación con solución y rúbrica.
El repositorio del alumnado (apuntes y autoevaluación) está en `../python-alumno`.

> ⚠️ **No compartir este repositorio con el alumnado**: contiene las soluciones de los proyectos de evaluación.

**Unidades disponibles:** UT01 y UT02.

## Estructura

```
python-profesor/
├── README.md
└── utNN/
    ├── preguntas-test.md      Banco de preguntas tipo test (con respuesta y justificación)
    ├── ejercicios.md          Banco de ejercicios de programación (con solución)
    └── proyecto/
        ├── enunciados.md      Proyecto de evaluación: variantes A y B para entregar al alumnado
        ├── rubrica.md         Criterios de calificación y guía de corrección
        ├── pruebas.md         Datos de entrada y salida esperada para probar los proyectos
        ├── solucion_a.py      Solución de referencia de la variante A
        └── solucion_b.py      Solución de referencia de la variante B
```

## Cómo se evalúa

Al final de cada unidad, el alumnado realiza un **proyecto en clase, sin conexión a internet, en un máximo de 1 hora**. El proyecto:

- integra **todo lo visto en la unidad** y puede incluir contenidos de **unidades anteriores**;
- está diseñado para que lo complete en el tiempo indicado una persona **con poca experiencia** que haya seguido la unidad;
- se ofrece en **dos variantes equivalentes (A y B)** para repartirlas entre alumnos contiguos y dificultar las copias;
- se puntúa sobre 10 con la rúbrica de `proyecto/rubrica.md`.

Los bancos de **preguntas tipo test** y de **ejercicios** sirven para pruebas de conocimientos, controles rápidos, refuerzo y recuperación.
No se han creado para el examen final (que es el proyecto), sino como material de apoyo.

## Herramientas

Visual Studio Code, consola de Python (REPL) y Jupyter Notebook. Los enunciados son válidos para trabajar con archivos `.py` o con cuadernos `.ipynb`.

## Consejos para la jornada del proyecto

- **Sin internet**: entrega el enunciado impreso o como archivo local (PDF/Markdown). Recuerda al alumnado que puede usar `help()` en la consola.
- Comprueba antes de la clase que **todos los equipos** tienen VS Code con la extensión de Python (y Jupyter, si se va a usar) y que el intérprete es **3.10 o superior**
  (necesario para `match`, que aparece en UT02).
- Reparte las variantes A/B alternando por filas.
- Indica en la pizarra la hora de inicio y de fin, y avisa cuando queden 15 y 5 minutos.
- Pide que guarden el trabajo con su **nombre** y lo entreguen como te resulte más cómodo (carpeta compartida de red, USB, aula virtual...).

## Formato de las preguntas tipo test

```markdown
### 12. [c · media]
Enunciado de la pregunta.

- A) Opción
- B) Opción
- C) Opción
- D) Opción

**Respuesta: B** — Justificación breve.
```

- `[c · media]` indica el **apartado** del temario (a, b, c...) y la **dificultad** (básica, media, avanzada).
- Cada banco termina con una **hoja de respuestas** en forma de tabla, útil para corregir rápido.
- Para elaborar un examen: elige un número de preguntas por apartado y mezcla las dificultades (por ejemplo, 50 % básicas, 35 % medias, 15 % avanzadas).

## Formato de los ejercicios

Cada ejercicio indica el apartado, la **dificultad** (★ básica · ★★ media · ★★★ avanzada), el enunciado y la **solución** de referencia. Hay soluciones alternativas válidas.

## Añadir una unidad nueva

1. Crea `utNN/` con `preguntas-test.md`, `ejercicios.md` y la carpeta `proyecto/`.
2. Mantén el mismo formato para poder reutilizar las plantillas.
3. Comprueba que todas las soluciones `.py` **se ejecutan** con los datos de `pruebas.md`.
