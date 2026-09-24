# d) Literales

Un **literal** es un valor escrito directamente en el código, tal cual. En `edad = 17`, `edad` es la variable y `17` es el literal.

## 1. Literales numéricos

### Enteros

Un entero se puede escribir en varias **bases**:

| Base | Prefijo | Ejemplo | Valor decimal |
|---|---|---|---|
| Decimal | (ninguno) | `255` | 255 |
| Binaria | `0b` | `0b1010` | 10 |
| Octal | `0o` | `0o17` | 15 |
| Hexadecimal | `0x` | `0xFF` | 255 |

```pycon
>>> 0b1010
10
>>> 0o17
15
>>> 0xFF
255
```

Para leer mejor los números grandes puedes separar con guion bajo (no cambia el valor):

```pycon
>>> 1_000_000
1000000
```

### Reales (decimales) y notación científica

```pycon
>>> 3.14
3.14
>>> .5
0.5
>>> 2.
2.0
>>> 1.5e3          # 1,5 × 10³
1500.0
>>> 2e-4           # 2 × 10⁻⁴
0.0002
```

## 2. Literales de cadena

Se pueden escribir con comillas **simples** o **dobles**; es indiferente, pero hay que cerrar con las mismas que abriste.

```pycon
>>> 'Hola'
'Hola'
>>> "Hola"
'Hola'
>>> "Es la casa de Ana's"       # comillas simples dentro de dobles: sin problema
"Es la casa de Ana's"
```

!!! success "Ahora tú"
    Prueba en la consola estos dos ejemplos y explica qué ocurre en cada uno.

    1. Mezclando comillas dobles y simples (un tipo de comillas dentro del otro):

        ```python
        frase_1 = "Es la casa de Ana's"
        frase_2 = 'Ana dijo "hola"'
        print(frase_1)
        print(frase_2)
        ```

    2. Cerrando mal a propósito (abres con comillas simples y cierras con dobles):

        ```python
        frase_3 = 'Hola mundo"
        ```

    ¿Por qué el primer caso funciona y el segundo da error?

### Comillas triples: varias líneas

```python
poema = """Rosas son rojas,
violetas azules,
Python es genial."""
print(poema)
```

### Secuencias de escape

La barra invertida `\` da un significado especial al carácter siguiente:

| Secuencia | Significado |
|---|---|
| `\n` | Salto de línea |
| `\t` | Tabulador |
| `\\` | Una barra invertida |
| `\'` | Comilla simple |
| `\"` | Comilla doble |

```pycon
>>> print("Línea 1\nLínea 2")
Línea 1
Línea 2
>>> print("Nombre:\tAna")
Nombre:	Ana
>>> print("Ruta: C:\\Users\\Ana")
Ruta: C:\Users\Ana
```

### Cadenas *raw* (crudas)

Con una `r` delante, las barras invertidas **no** se interpretan. Muy útil con rutas de Windows:

```pycon
>>> print(r"C:\nuevo\tabla")
C:\nuevo\tabla
>>> print("C:\nuevo\tabla")       # sin r: \n y \t se interpretan como escapes
C:
uevo	abla
```

### f-strings: cadenas con formato

Con una `f` delante puedes incluir **variables y expresiones entre llaves** `{ }`:

```pycon
>>> nombre = "Ana"
>>> edad = 16
>>> f"{nombre} tiene {edad} años"
'Ana tiene 16 años'
>>> f"El año que viene tendrá {edad + 1}"
'El año que viene tendrá 17'
```

Después de los dos puntos `:` puedes indicar el **formato**:

| Formato | Efecto | Ejemplo | Resultado |
|---|---|---|---|
| `:.2f` | 2 decimales | `f"{3.14159:.2f}"` | `'3.14'` |
| `:05d` | Entero con ceros a la izquierda hasta 5 cifras | `f"{42:05d}"` | `'00042'` |
| `:>8` | Alinear a la derecha en 8 espacios | `f"{'ab':>8}"` | `'      ab'` |
| `:<8` | Alinear a la izquierda | `f"{'ab':<8}"` | `'ab      '` |
| `:^8` | Centrar | `f"{'ab':^8}"` | `'   ab   '` |
| `:,` | Separador de miles | `f"{1234567:,}"` | `'1,234,567'` |
| `:.1%` | Porcentaje | `f"{0.256:.1%}"` | `'25.6%'` |

```pycon
>>> precio = 4.5
>>> f"Total: {precio:.2f} €"
'Total: 4.50 €'
>>> f"{precio * 3:>10.2f}"
'     13.50'
```

!!! tip "Consejo"
    `:.2f` es la forma habitual de mostrar **dinero**. Úsala siempre en tickets y facturas.

!!! success "Ahora tú"
    Prueba en la consola este código y comprueba qué hace cada formato:

    ```python
    producto = "Ratón"
    unidades = 7
    precio = 12.5
    descuento = 0.15

    print(f"Producto: {producto:>10}")
    print(f"Código:   {unidades:05d}")
    print(f"Precio:   {precio:.2f} €")
    print(f"Total:    {unidades * precio:,.2f} €")
    print(f"Descuento: {descuento:.0%}")
    ```

    Ahora modifica los valores y los formatos:

    1. Cambia `producto` por un nombre más largo y prueba `:<10` y `:^10`.
    2. Pon `unidades = 1200` y `precio = 999.99`. ¿Cómo se ve el total con `:,.2f`?
    3. Muestra el precio con 3 decimales y el descuento con 1 decimal.

## 3. Literales lógicos

Solo hay dos: `True` y `False`. Se escriben siempre con la primera letra mayúscula (`true` no existe en Python).

```python
es_mayor = True
tiene_carnet = False
```

## Resumen

- Un literal es un valor escrito directamente en el código.
- Enteros en decimal, binario (`0b`), octal (`0o`) y hexadecimal (`0x`); reales con punto y notación científica (`1.5e3`).
- Cadenas con comillas simples, dobles o triples; `\n`, `\t`, `\\` como escapes; `r"..."` para rutas.
- Las **f-strings** (`f"..."`) insertan valores y permiten dar formato: `{precio:.2f}`.
- Literales lógicos: `True` y `False`.
