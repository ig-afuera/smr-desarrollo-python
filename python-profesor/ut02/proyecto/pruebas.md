# Datos de prueba · Proyecto UT02

Para comprobar el programa de un alumno, escribe los datos de la columna «Entrada» **en el orden indicado**. Las soluciones de referencia son `solucion_a.py` y `solucion_b.py`.

> **Ejecución rápida sin teclear** (PowerShell):
> ```powershell
> "0000`n1234`n1`n4" | python programa_alumno.py
> ```
> Sin tildes en los textos de entrada, para evitar problemas de codificación.

## Variante A · Cajero automático

### Caso 1 · Sesión completa (con datos erróneos)

Entrada, en orden (una por línea):

```text
0000
1234
1
2
abc
200
3
400
3
250
3
1000
9
4
```

| Momento | Resultado esperado |
|---|---|
| PIN `0000` | «PIN incorrecto» |
| PIN `1234` | «Acceso concedido» |
| Opción `1` | Saldo 500.00 € |
| Opción `2`, cantidad `abc` | «Cantidad no válida» y vuelve a pedir |
| Cantidad `200` | Ingreso: saldo 700.00 € |
| Opción `3`, cantidad `400` | Rechazada por superar el límite de 300 € |
| Opción `3`, cantidad `250` | Retirada: saldo 450.00 € |
| Opción `3`, cantidad `1000` | «Saldo insuficiente» |
| Opción `9` | «Opción no válida» |
| Opción `4` | Resumen: **2 operaciones**, saldo final **450.00 €**, variación **-50.00 €** |

### Caso 2 · Tarjeta bloqueada

Entrada: `1111`, `2222`, `3333`.

Resultado esperado: tres veces «PIN incorrecto» y «Tarjeta bloqueada». **No se muestra el menú** y el programa termina.

### Caso 3 · Cantidades no válidas y saldo bajo (ampliación)

Entrada, en orden:

```text
1234
3
300
3
200
3
-5
0
5
4
```

| Momento | Resultado esperado |
|---|---|
| Retiradas de `300` y `200` | Aceptadas: saldo 200.00 € y después 0.00 € |
| Tercera retirada: `-5` y `0` | «Cantidad no válida» (se vuelve a pedir) |
| Cantidad `5` | «Saldo insuficiente» |
| Salir | 2 operaciones, saldo final **0.00 €**, variación **-500.00 €** y, con la ampliación, **Saldo bajo** |

## Variante B · Gestor de notas

### Caso 1 · Datos erróneos mezclados

Entrada, en orden:

```text
x
0
3
Ana
8
7.5
9
Luis
abc
11
4
3.5
5
Marta
10
9
9.5
```

| Momento | Resultado esperado |
|---|---|
| Número de alumnos `x` y `0` | «Escribe un número entero» y «Debe haber al menos un alumno» |
| Ana (8, 7.5, 9) | media **8.17** → Notable |
| Luis: `abc` y `11` en la nota 1 | Avisa y la vuelve a pedir; con 4, 3.5 y 5 → media **4.17** → Suspenso |
| Marta (10, 9, 9.5) | media **9.50** → Sobresaliente |
| Resumen | Aprobados **2**, suspensos **1**, media de la clase **7.28**, mejor alumno **Marta (9.50)** |

### Caso 2 · Tramos frontera

Entrada:

```text
3
A
9
9
9
B
7
7
7
C
5
5
5
```

Esperado: A → **Sobresaliente** (9.00), B → **Notable** (7.00), C → **Aprobado** (5.00). Resumen: aprobados 3, suspensos 0, media de la clase **7.00**, mejor alumno **A (9.00)**.

> Si un alumno obtiene «Notable» para el 9, «Aprobado» para el 7 o «Suspenso» para el 5, sus condiciones usan `>` en lugar de `>=`.

### Caso 3 · Un solo alumno

Entrada: `1`, `Eva`, `5`, `5`, `5`.

Esperado: Eva → **5.00 Aprobado**. Resumen: aprobados 1, suspensos 0, media 5.00, mejor alumno Eva (5.00).
