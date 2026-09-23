# Datos de prueba · Proyecto UT01

Para comprobar el programa de un alumno, escribe los datos de la columna «Entrada» **en el orden indicado** y compara con los resultados esperados.
Las soluciones de referencia son `solucion_a.py` y `solucion_b.py` (ejecútalas con `python solucion_a.py`).

## Variante A · Ticket de la cafetería

### Caso 1

| Entrada (en orden) | |
|---|---|
| Nombre | `Lucía` |
| Cafés | `3` |
| Bollos | `2` |
| Dinero entregado | `20` |

| Resultado esperado | Valor |
|---|---|
| Importe de cafés | 3.90 € |
| Importe de bollos | 3.70 € |
| Subtotal | 7.60 € |
| IVA | 0.76 € |
| Total | 8.36 € |
| Cambio | 11.64 € |
| Cambio desglosado | 11 € y 64 cts |
| `pago_suficiente` | `True` |
| `pedido_grande` | `True` (5 artículos) |
| Tipos | `int`, `float`, `str` |

### Caso 2

| Entrada (en orden) | |
|---|---|
| Nombre | `Pablo` |
| Cafés | `1` |
| Bollos | `0` |
| Dinero entregado | `5` |

| Resultado esperado | Valor |
|---|---|
| Subtotal | 1.30 € |
| IVA | 0.13 € |
| Total | 1.43 € |
| Cambio | 3.57 € |
| Cambio desglosado | 3 € y 57 cts |
| `pago_suficiente` | `True` |
| `pedido_grande` | `False` |

## Variante B · Ficha de un viaje

### Caso 1

| Entrada (en orden) | |
|---|---|
| Destino | `Valencia` |
| Distancia | `350` |
| Consumo | `6.5` |
| Personas | `3` |
| Horas / Minutos | `3` / `30` |

| Resultado esperado | Valor |
|---|---|
| Litros | 22.75 l |
| Coste total | 37.54 € |
| Coste por persona | 12.51 € |
| Duración | 3 h 30 min |
| Velocidad media | 100.0 km/h |
| CO₂ | 52.55 kg |
| `viaje_largo` | `True` |
| `viaje_economico` | `False` |

### Caso 2

| Entrada (en orden) | |
|---|---|
| Destino | `Toledo` |
| Distancia | `75` |
| Consumo | `5.2` |
| Personas | `2` |
| Horas / Minutos | `1` / `5` |

| Resultado esperado | Valor |
|---|---|
| Litros | 3.90 l |
| Coste total | 6.43 € |
| Coste por persona | 3.22 € |
| Duración | 1 h 05 min |
| Velocidad media | 69.2 km/h |
| CO₂ | 9.01 kg |
| `viaje_largo` | `False` |
| `viaje_economico` | `True` |

> **Ejecución rápida sin teclear** (PowerShell), útil para corregir muchos programas:
> ```powershell
> "Ana`n3`n2`n20" | python programa_alumno.py
> ```
> (Usa nombres sin tildes al canalizar la entrada en PowerShell para evitar problemas de codificación.)
