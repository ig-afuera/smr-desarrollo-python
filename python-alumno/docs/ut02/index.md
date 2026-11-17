# UT02. Uso de estructuras de control

Hasta ahora tus programas se ejecutaban **de arriba abajo, una línea tras otra**. En esta unidad aprenderás a que el programa **tome decisiones**, **repita tareas** y **reaccione ante los errores**.

## ¿Qué vas a aprender?

Al terminar esta unidad serás capaz de:

- Hacer que el programa siga un camino u otro según una condición (`if`, `elif`, `else`, `match`).
- Repetir instrucciones con `while` y `for`, y controlar cuántas veces.
- Alterar el flujo de un bucle con `break`, `continue` y `pass`.
- Evitar que el programa se «rompa» ante datos incorrectos con `try` / `except`.
- Resolver problemas típicos: menús, validación de datos, contadores, acumuladores, búsquedas...

## Apartados

| Apartado | Idea clave |
|---|---|
| [a) Estructuras de selección](a-seleccion.md) | Decidir: `if`, `elif`, `else`, `match`. |
| [b) Estructuras de repetición](b-repeticion.md) | Repetir: `while`, `for`, `range()`. |
| [c) Estructuras de salto](c-salto.md) | Controlar el bucle: `break`, `continue`, `pass`. |
| [d) Control de excepciones](d-excepciones.md) | Anticipar errores: `try`, `except`, `raise`. |
| [Ejercicios de repaso](repaso.md) | Cinco casos prácticos de dificultad creciente, con soluciones. |
| [Autoevaluación](autoevaluacion.md) | Preguntas, ejercicios y proyecto de práctica, con soluciones. |

!!! info "Esta unidad se apoya en la anterior"
    Vas a usar constantemente lo aprendido en la UT01: variables, operadores de comparación y lógicos, conversiones de tipo, f-strings...
    Si algo te suena borroso, repásalo antes. **El proyecto de esta unidad también incluye contenidos de la UT01.**

## Las tres formas de ejecutar un programa

```text
 Secuencia               Selección                Repetición
 ─────────               ─────────                ──────────
 instrucción 1           ¿condición?              ¿condición?
 instrucción 2            ├─ sí → bloque A         ├─ sí → bloque ─┐
 instrucción 3            └─ no → bloque B         │               │
                                                  └─ no → sigue ◄─┘
```
