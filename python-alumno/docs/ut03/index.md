# UT03. Funciones

Tus programas ya toman decisiones y repiten tareas, pero a medida que crecen aparece un problema: **el mismo código se repite** en varios sitios y cuesta encontrar dónde está cada cosa. En esta unidad aprenderás a **empaquetar** un trozo de código bajo un nombre para usarlo tantas veces como quieras.

## ¿Qué vas a aprender?

Al terminar esta unidad serás capaz de:

- Definir tus propias funciones con `def` y llamarlas desde cualquier parte del programa.
- Pasarles datos (**parámetros**) y recibir resultados (`return`).
- Saber qué variables «ve» cada función (**ámbito**: local, global, `nonlocal`).
- Documentar funciones con docstrings y anotaciones de tipo.
- Usar módulos de la biblioteca estándar (`math`, `random`, `datetime`) y crear los tuyos.
- Probar tus funciones con `assert` y depurarlas paso a paso.
- Resolver problemas con **funciones recursivas**: funciones que se llaman a sí mismas.

## Apartados

| Apartado | Idea clave |
|---|---|
| [a) Funciones definidas por el programador](a-funciones.md) | Empaquetar código: `def`, parámetros, `return`, ámbito, módulos. |
| [b) Recursividad](b-recursividad.md) | Una función que se llama a sí misma: caso base y caso recursivo. |
| [Ejercicios de repaso](repaso.md) | Cinco casos prácticos de dificultad creciente, con soluciones. |
| [Autoevaluación](autoevaluacion.md) | Preguntas, ejercicios y proyecto de práctica, con soluciones. |

!!! info "Esta unidad se apoya en las anteriores"
    Dentro de una función vas a escribir lo mismo que hasta ahora: variables, condicionales, bucles, `try` / `except`...
    La diferencia es **cómo organizas** ese código. **El proyecto de esta unidad también incluye contenidos de la UT01 y la UT02.**

## La idea en un dibujo

```text
 Sin funciones                       Con funciones
 ─────────────                       ─────────────
 pedir nota 1 y validarla            def pedir_nota(): ...   ← se escribe UNA vez
 pedir nota 2 y validarla
 pedir nota 3 y validarla            nota1 = pedir_nota()    ← se usa TRES veces
 (el mismo código tres veces)        nota2 = pedir_nota()
                                     nota3 = pedir_nota()
```
