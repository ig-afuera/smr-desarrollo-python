# Proyecto de evaluación UT01

**Identificación de los elementos de un programa informático**

> Este documento contiene **dos variantes equivalentes (A y B)** para repartir en el aula. Imprime o entrega **una sola variante por alumno/a**.
> Cada variante empieza en una página nueva y es autocontenida.

| | |
|---|---|
| **Duración máxima** | 1 hora (el proyecto está pensado para unos 45-50 minutos) |
| **Conexión a internet** | No |
| **Herramientas** | Visual Studio Code, consola de Python y/o Jupyter Notebook |
| **Entrega** | Un único archivo `.py` o `.ipynb` con tu nombre, en la carpeta indicada por el profesor/a |
| **Contenidos** | Todos los de la UT01 |

---

<div style="page-break-after: always;"></div>

# VARIANTE A · Ticket de la cafetería

Nombre: ______________________________  Fecha: ______________

La **Cafetería El Rincón** necesita un programa que genere el ticket de cada cliente.

## Requisitos

1. Al inicio del archivo, escribe un **docstring** que explique qué hace el programa. Añade **comentarios** allí donde ayuden a entender el código.
2. Define estas **constantes** (nombres en MAYÚSCULAS):
    - `NOMBRE_LOCAL`: `"Cafetería El Rincón"`
    - `IVA`: `0.10`
    - `PRECIO_CAFE`: `1.30` €
    - `PRECIO_BOLLO`: `1.85` €

   Los precios no incluyen IVA.
3. Pide por teclado, **convirtiendo cada dato al tipo adecuado**:
    - el nombre del cliente,
    - el número de cafés,
    - el número de bollos,
    - el dinero entregado (admite decimales).
4. Calcula: el importe de los cafés, el importe de los bollos, el **subtotal**, el **importe del IVA**, el **total** y el **cambio** (dinero entregado − total).
5. Muestra un **ticket con formato cuidado**: el nombre del local **centrado**, los importes con **2 decimales** y **alineados a la derecha**.
6. Muestra el **cambio desglosado en euros y céntimos**, por ejemplo `11 € y 64 cts`. Suponemos que el dinero entregado siempre es suficiente.
   *Pista: trabaja con el cambio en céntimos (como número entero) y usa `//` y `%`.*
7. Calcula y muestra estos dos valores lógicos (**sin usar `if`**):
    - `pago_suficiente`: el dinero entregado cubre el total.
    - `pedido_grande`: entre cafés y bollos hay **5 o más** artículos.
8. Muestra el **tipo de dato** (`type`) de las variables que contienen el número de cafés, el total y el nombre del cliente.

## Ejemplo de ejecución

Lo que teclea el usuario va detrás de los dos puntos.

```text
Nombre del cliente: Lucía
Número de cafés: 3
Número de bollos: 2
Dinero entregado (€): 20

       Cafetería El Rincón        
----------------------------------
Cliente: Lucía
----------------------------------
3 x Café   1.30             3.90 €
2 x Bollo  1.85             3.70 €
----------------------------------
Subtotal                    7.60 €
IVA (10%)                   0.76 €
TOTAL                       8.36 €
Entregado                  20.00 €
Cambio                     11.64 €
----------------------------------
Cambio a devolver: 11 € y 64 cts

Pago suficiente: True
Pedido grande (5 o más artículos): True
Tipo de 'cafes': <class 'int'>
Tipo de 'total': <class 'float'>
Tipo de 'cliente': <class 'str'>
```

> No hace falta que tu ticket sea **idéntico** al del ejemplo: importa que muestre la misma información, con importes de 2 decimales y bien alineados.

## Recomendaciones

- Lee todo el enunciado antes de empezar y prueba el programa **a menudo**.
- Primero haz que **funcione**; después, mejora el formato.
- Si algo te falla, lee el mensaje de error y usa la consola de Python para probar esa instrucción por separado. `help()` funciona sin internet.

<div style="page-break-after: always;"></div>

# VARIANTE B · Ficha de un viaje en coche

Nombre: ______________________________  Fecha: ______________

Una aplicación de viajes compartidos necesita un programa que calcule la **ficha de un viaje en coche**.

## Requisitos

1. Al inicio del archivo, escribe un **docstring** que explique qué hace el programa. Añade **comentarios** allí donde ayuden a entender el código.
2. Define estas **constantes** (nombres en MAYÚSCULAS):
    - `PRECIO_LITRO`: `1.65` € por litro de gasolina
    - `EMISION_CO2_LITRO`: `2.31` kg de CO₂ por litro
    - `UMBRAL_VIAJE_LARGO`: `300` km
    - `UMBRAL_ECONOMICO`: `10` € por persona
3. Pide por teclado, **convirtiendo cada dato al tipo adecuado**:
    - el destino,
    - la distancia en km (admite decimales),
    - el consumo del coche en litros cada 100 km (admite decimales),
    - el número de personas que viajan,
    - la duración: primero las **horas** y después los **minutos** (enteros).
4. Calcula:
    - los **litros** consumidos (`distancia × consumo / 100`),
    - el **coste total** del combustible,
    - el **coste por persona**,
    - la **velocidad media** en km/h (convierte la duración a horas),
    - las **emisiones de CO₂** en kg.
5. Muestra una **ficha con formato cuidado**: etiquetas alineadas a la izquierda, valores **alineados a la derecha** y con el número de decimales adecuado (combustible, costes y emisiones: 2; velocidad y distancia: 1). La duración se muestra como `3 h 05 min` (los minutos siempre con dos cifras).
6. Calcula y muestra estos dos valores lógicos (**sin usar `if`**):
    - `viaje_largo`: la distancia **supera** el umbral de viaje largo.
    - `viaje_economico`: el coste por persona es **menor** que el umbral económico.
7. Muestra el **tipo de dato** (`type`) de las variables que contienen el número de personas, la distancia y el destino.

## Ejemplo de ejecución

Lo que teclea el usuario va detrás de los dos puntos.

```text
Destino: Valencia
Distancia (km): 350
Consumo del coche (litros/100 km): 6.5
Número de personas: 3
Duración: horas: 3
Duración: minutos: 30

FICHA DEL VIAJE A Valencia
====================================
Distancia:                 350.0 km
Combustible:               22.75 l
Coste total:               37.54 €
Coste por persona:         12.51 €
Duración:                  3 h 30 min
Velocidad media:           100.0 km/h
Emisiones de CO2:          52.55 kg
====================================
¿Viaje largo (más de 300 km)? True
¿Viaje económico (menos de 10 € por persona)? False
Tipo de 'personas': <class 'int'>
Tipo de 'distancia': <class 'float'>
Tipo de 'destino': <class 'str'>
```

> No hace falta que tu ficha sea **idéntica** a la del ejemplo: importa que muestre la misma información, con los decimales pedidos y bien alineada.

## Recomendaciones

- Lee todo el enunciado antes de empezar y prueba el programa **a menudo**.
- Primero haz que **funcione**; después, mejora el formato.
- Si algo te falla, lee el mensaje de error y usa la consola de Python para probar esa instrucción por separado. `help()` funciona sin internet.
