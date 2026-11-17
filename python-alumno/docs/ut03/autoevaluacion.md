# Autoevaluación UT03

Comprueba **por ti mismo/a** si has entendido la unidad. Las soluciones están ocultas: **inténtalo primero** y despliégalas después.

!!! tip "Cómo usarla"
    1. Contesta las **preguntas** sin mirar los apuntes.
    2. Haz los **ejercicios** en VS Code o Jupyter y **pruébalos** con `assert` y con varios datos (también erróneos).
    3. Al final, haz el **proyecto de práctica** con el formato del examen: **sin internet y con un máximo de 1 hora**.

---

## Parte 1. Preguntas de repaso

### Pregunta 1
¿Qué diferencia hay entre un **parámetro** y un **argumento**?

??? success "Solución"
    El **parámetro** es la variable que aparece en la **definición** de la función (`def saludar(nombre):`). El **argumento** es el valor concreto que se pasa en la **llamada** (`saludar("Lucía")`).

### Pregunta 2
¿Qué devuelve una función que no tiene `return`?

??? success "Solución"
    Devuelve `None`. Por eso, si una función hace `print()` en lugar de `return`, guardar su resultado en una variable da `None`.

### Pregunta 3
¿Qué muestra este código?
```python
def precio(base, iva=21):
    return base + base * iva / 100


print(precio(100), precio(100, 10), precio(iva=4, base=50))
```

??? success "Solución"
    Muestra `121.0 110.0 52.0`.

    - `precio(100)`: usa el valor por defecto, `iva=21`.
    - `precio(100, 10)`: el segundo argumento posicional va a `iva`.
    - `precio(iva=4, base=50)`: por nombre, el orden da igual.

### Pregunta 4
¿Por qué da error `def reservar(personas=2, fecha):`?

??? success "Solución"
    Porque los parámetros **con valor por defecto** tienen que ir **después** de los que no lo tienen. Da `SyntaxError`. Lo correcto es `def reservar(fecha, personas=2):`.

### Pregunta 5
¿Qué muestra este código? ¿Por qué?
```python
x = 10


def cambiar():
    x = 99
    return x


print(cambiar(), x)
```

??? success "Solución"
    Muestra `99 10`. Dentro de `cambiar`, `x = 99` crea una variable **local** que no tiene nada que ver con la `x` global. La global sigue valiendo `10`.

### Pregunta 6
¿Qué muestra este código?
```python
def agregar(lista, valor):
    lista.append(valor)
    valor = 0


numeros = [1, 2]
v = 3
agregar(numeros, v)
print(numeros, v)
```

??? success "Solución"
    Muestra `[1, 2, 3] 3`.

    - La lista es **mutable**: `append` modifica el objeto original y el cambio se ve fuera.
    - `valor = 0` solo cambia la variable local; `v` sigue valiendo `3` (los enteros son **inmutables**).

### Pregunta 7
¿Para qué sirve `if __name__ == "__main__":` al final de un módulo?

??? success "Solución"
    Para que el código de dentro (pruebas, programa principal...) **solo se ejecute al lanzar ese fichero directamente**, y no cuando otro programa lo importa con `import`.

### Pregunta 8
¿Qué diferencia hay entre `import math` y `from math import sqrt`?

??? success "Solución"
    Con `import math` se importa el módulo entero y se usa con su nombre delante: `math.sqrt(9)`. Con `from math import sqrt` solo se importa `sqrt` y se usa directamente: `sqrt(9)`.

### Pregunta 9
¿Qué es el **caso base** de una función recursiva? ¿Qué pasa si no lo tiene?

??? success "Solución"
    Es el caso que se resuelve **directamente, sin volver a llamar** a la función. Sin caso base, la función se llama a sí misma sin fin hasta superar el límite de Python y se produce `RecursionError`.

### Pregunta 10
¿Qué devuelve `f(5)`? ¿Y `f(4)`?
```python
def f(n):
    if n <= 0:
        return 0
    return n + f(n - 2)
```

??? success "Solución"
    - `f(5) = 5 + f(3) = 5 + 3 + f(1) = 5 + 3 + 1 + f(-1) = 5 + 3 + 1 + 0 = 9`.
    - `f(4) = 4 + f(2) = 4 + 2 + f(0) = 4 + 2 + 0 = 6`.

### Pregunta 11
Verdadero o falso: «Las anotaciones de tipo hacen que Python dé error si se pasa un argumento del tipo equivocado».

??? success "Solución"
    **Falso**. Las anotaciones son solo **información** para quien lee el código y para el editor. Python no las comprueba al ejecutar.

### Pregunta 12
¿En qué casos usarías un bucle en lugar de una función recursiva?

??? success "Solución"
    Cuando el problema se resuelve de forma sencilla con un bucle (sumar, contar, recorrer) o cuando harían falta **muchas** llamadas encadenadas. El bucle es más rápido, gasta menos memoria y no tiene el límite de `RecursionError`. La recursividad se reserva para problemas que se dividen de forma natural en subproblemas iguales, como las torres de Hanói.

---

## Parte 2. Ejercicios

### Ejercicio 1. Rectángulo
Escribe la función `rectangulo(base, altura)`, que **devuelva** el área y el perímetro. En el programa principal, recoge los dos valores en dos variables y muéstralos.

??? success "Solución"
    ```python
    def rectangulo(base, altura):
        """Devuelve el área y el perímetro de un rectángulo."""
        return base * altura, 2 * (base + altura)


    area, perimetro = rectangulo(4, 3)
    print(f"Área: {area} | Perímetro: {perimetro}")
    ```

### Ejercicio 2. Números primos
Escribe `es_primo(n)`, que devuelva `True` o `False`. Úsala para mostrar todos los primos entre 1 y un número pedido al usuario.

??? success "Solución"
    ```python
    def es_primo(n: int) -> bool:
        """Indica si n es primo."""
        if n < 2:
            return False
        for divisor in range(2, n):
            if n % divisor == 0:
                return False
        return True


    limite = int(input("Mostrar primos hasta: "))
    for numero in range(1, limite + 1):
        if es_primo(numero):
            print(numero, end=" ")
    print()
    ```
    El `return False` dentro del bucle termina la función en cuanto aparece un divisor: no hace falta `break` ni variable bandera.

### Ejercicio 3. Contar vocales
Escribe `contar_vocales(texto)`, que devuelva cuántas vocales tiene un texto (con o sin tilde, en mayúsculas o minúsculas). `contar_vocales("Murciélago")` → `5`.

??? success "Solución"
    ```python
    def contar_vocales(texto: str) -> int:
        """Devuelve cuántas vocales tiene el texto."""
        total = 0
        for letra in texto.lower():
            if letra in "aeiouáéíóúü":
                total += 1
        return total


    assert contar_vocales("Murciélago") == 5
    assert contar_vocales("") == 0
    ```

### Ejercicio 4. El mayor de tres
Escribe `mayor_de_tres(a, b, c)` sin usar `max()`, con docstring y anotaciones de tipo. Pruébala con `assert`, incluyendo números repetidos y negativos.

??? success "Solución"
    ```python
    def mayor_de_tres(a: float, b: float, c: float) -> float:
        """Devuelve el mayor de tres números sin usar max()."""
        if a >= b and a >= c:
            return a
        if b >= c:
            return b
        return c


    assert mayor_de_tres(1, 2, 3) == 3
    assert mayor_de_tres(3, 9, 9) == 9
    assert mayor_de_tres(-1, -5, -2) == -1
    ```

### Ejercicio 5. Factorial de dos formas
Escribe `factorial_iterativo(n)` con un bucle y `factorial_recursivo(n)` con recursividad. Comprueba con un bucle y `assert` que dan el mismo resultado para los números del 0 al 9.

??? success "Solución"
    ```python
    def factorial_iterativo(n: int) -> int:
        """Factorial de n con un bucle."""
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


    def factorial_recursivo(n: int) -> int:
        """Factorial de n con recursividad."""
        if n <= 1:
            return 1
        return n * factorial_recursivo(n - 1)


    for numero in range(10):
        assert factorial_iterativo(numero) == factorial_recursivo(numero)
    print("Las dos versiones coinciden")
    ```

### Ejercicio 6. Suma de pares recursiva
Escribe una función **recursiva** `suma_pares(n)` que devuelva la suma de los números pares entre 0 y `n`. `suma_pares(10)` → `30`; `suma_pares(7)` → `12`.

??? success "Solución"
    ```python
    def suma_pares(n: int) -> int:
        """Devuelve la suma de los números pares entre 0 y n."""
        if n <= 0:                       # caso base
            return 0
        if n % 2 != 0:                   # impar: se empieza por el par anterior
            return suma_pares(n - 1)
        return n + suma_pares(n - 2)


    assert suma_pares(10) == 30
    assert suma_pares(7) == 12
    assert suma_pares(0) == 0
    ```

### Ejercicio 7. Palíndromos
Escribe una función **recursiva** `es_palindromo(texto)`: un texto es palíndromo si la primera y la última letra son iguales **y** lo de en medio también es palíndromo. `texto[0]` es la primera letra, `texto[-1]` la última y `texto[1:-1]` el texto sin ellas (UT04).

??? success "Solución"
    ```python
    def es_palindromo(texto: str) -> bool:
        """Indica si el texto se lee igual al revés."""
        if len(texto) <= 1:              # caso base: vacío o una letra
            return True
        if texto[0] != texto[-1]:
            return False
        return es_palindromo(texto[1:-1])


    assert es_palindromo("reconocer")
    assert not es_palindromo("python")
    assert es_palindromo("")
    ```

### Ejercicio 8. Decimal a binario
Escribe una función **recursiva** `binario(n)` que devuelva un texto con el número `n` en binario. Pista: el binario de `n` es el binario de `n // 2` seguido de la cifra `n % 2`. Compruébala con la función `bin()` de la UT01.

??? success "Solución"
    ```python
    def binario(n: int) -> str:
        """Devuelve la representación en binario de n (n >= 0)."""
        if n < 2:                        # caso base: 0 o 1
            return str(n)
        return binario(n // 2) + str(n % 2)


    for numero in range(50):
        assert binario(numero) == bin(numero)[2:]   # bin(5) es '0b101'
    print(binario(13))                               # 1101
    ```

### Ejercicio 9. Mi módulo de utilidades
Crea un módulo `utilidades.py` con las funciones `es_primo` (ejercicio 2) y `binario` (ejercicio 8), y sus pruebas dentro de `if __name__ == "__main__":`. Después, crea `principal.py` en la misma carpeta, que pida un número y diga si es primo y cuál es su representación en binario.

??? success "Solución"
    ```python
    # utilidades.py
    """Funciones matemáticas de uso general."""


    def es_primo(n: int) -> bool:
        """Indica si n es primo."""
        if n < 2:
            return False
        for divisor in range(2, n):
            if n % divisor == 0:
                return False
        return True


    def binario(n: int) -> str:
        """Devuelve la representación en binario de n (n >= 0)."""
        if n < 2:
            return str(n)
        return binario(n // 2) + str(n % 2)


    if __name__ == "__main__":
        assert es_primo(13) and not es_primo(1)
        assert binario(13) == "1101"
        print("Pruebas superadas")
    ```

    ```python
    # principal.py
    import utilidades

    numero = int(input("Número: "))
    texto = "es primo" if utilidades.es_primo(numero) else "no es primo"
    print(f"{numero} {texto} y en binario es {utilidades.binario(numero)}")
    ```

### Ejercicio 10. Encuentra los fallos
Cada fragmento tiene un fallo. Explícalo y corrígelo.

```python
# a) Quiere guardar el doble de 5 en la variable resultado
def doble(n):
    print(n * 2)


resultado = doble(5)

# b) Quiere clasificar la temperatura
def clasificar(grados):
    if grados > 30:
        return "calor"
    elif grados < 10:
        return "frío"


print(clasificar(20).upper())

# c) Quiere sumar del 1 al n
def suma(n):
    return n + suma(n - 1)

# d) Quiere mostrar el menú
def mostrar_menu():
    print("1. Jugar  2. Salir")


mostrar_menu
```

??? success "Solución"
    - **a)** La función **muestra** el doble pero no lo **devuelve**: `resultado` vale `None`. Hay que cambiar `print(n * 2)` por `return n * 2`.
    - **b)** Si la temperatura está entre 10 y 30, ninguna condición se cumple y la función devuelve `None`. `None.upper()` da `AttributeError`. Falta un `return` para el resto de casos:
      ```python
      def clasificar(grados):
          if grados > 30:
              return "calor"
          if grados < 10:
              return "frío"
          return "templado"
      ```
    - **c)** Falta el **caso base**: se produce `RecursionError`.
      ```python
      def suma(n):
          if n <= 1:
              return n
          return n + suma(n - 1)
      ```
    - **d)** Faltan los **paréntesis** en la llamada: `mostrar_menu` solo nombra la función, no la ejecuta. Lo correcto es `mostrar_menu()`.

---

## Parte 3. Proyecto de práctica

!!! abstract "Formato del examen"
    **Tiempo: 50 minutos.** Sin internet ni apuntes. Usa VS Code (`.py`) o Jupyter, como prefieras.
    Este proyecto también repasa la UT01 y la UT02 (constantes, f-strings, `match`, bucles, `try` / `except`...).

### Servicio técnico de móviles

Un servicio técnico de móviles necesita un programa para calcular presupuestos de reparación.

**Requisitos**

1. Un **docstring** inicial que explique qué hace el programa, y **comentarios** donde sean útiles.
2. **Constantes**: precio de la hora de trabajo `30.00`, pantalla `89.90`, batería `45.00`, IVA `21` %, descuento de cliente habitual `10` % y máximo de `8` horas.
3. Estas **funciones**, todas con docstring y anotaciones de tipo:
    - `pedir_entero(mensaje, minimo, maximo)`: pide un entero hasta que sea válido (`try` / `except`).
    - `precio_pieza(tipo)`: devuelve el precio de la pieza (`software` no tiene pieza: `0`).
    - `aplicar_descuento(importe, habitual=False)`: devuelve el importe con el descuento, si corresponde.
    - `con_iva(importe, iva=IVA)`: devuelve el importe con IVA.
    - `presupuesto(tipo, horas, habitual=False)`: devuelve **dos valores**, la base (pieza + horas de trabajo, con el descuento aplicado) y el total con IVA.
    - `probar()`: al menos 5 pruebas con `assert` de las funciones de cálculo.
    - `main()`: el programa principal. No se usan variables globales (salvo las constantes).
4. Un **menú** que se repite hasta elegir salir:
    ```text
    --- SERVICIO TÉCNICO ---
    1. Pantalla  2. Batería  3. Software  4. Salir
    ```
5. Si la opción **no es válida**, se avisa y se vuelve a mostrar el menú.
6. Tras elegir la reparación, se piden las **horas** (de 1 a 8) y si es **cliente habitual**, y se muestran la base y el total con 2 decimales.
7. Al salir, se muestra un **resumen** con el número de presupuestos y el total facturado.
8. El programa principal se lanza con `if __name__ == "__main__":`.

**Ampliación (solo si te sobra tiempo):** mueve las funciones de cálculo a un módulo `taller.py` y deja en `principal.py` solo `pedir_entero` y `main()`. Las pruebas pasan a `taller.py`, dentro de su propio `if __name__ == "__main__":`.

**Ejemplo de ejecución** (lo tecleado por el usuario va tras los dos puntos)

```text
--- SERVICIO TÉCNICO ---
1. Pantalla  2. Batería  3. Software  4. Salir
Reparación: 1
Horas de trabajo (1-8): 2
¿Cliente habitual? (s/n): n
Reparación de pantalla | Base: 149.90 € | Total con IVA: 181.38 €

--- SERVICIO TÉCNICO ---
1. Pantalla  2. Batería  3. Software  4. Salir
Reparación: 6
Opción no válida

--- SERVICIO TÉCNICO ---
1. Pantalla  2. Batería  3. Software  4. Salir
Reparación: 3
Horas de trabajo (1-8): dos
Escribe un número entero
Horas de trabajo (1-8): 1
¿Cliente habitual? (s/n): s
Reparación de software | Base: 27.00 € | Total con IVA: 32.67 €

--- SERVICIO TÉCNICO ---
1. Pantalla  2. Batería  3. Software  4. Salir
Reparación: 2
Horas de trabajo (1-8): 12
Debe estar entre 1 y 8
Horas de trabajo (1-8): 3
¿Cliente habitual? (s/n): n
Reparación de batería | Base: 135.00 € | Total con IVA: 163.35 €

--- SERVICIO TÉCNICO ---
1. Pantalla  2. Batería  3. Software  4. Salir
Reparación: 4

--- RESUMEN DEL DÍA ---
Presupuestos: 3
Total facturado: 377.40 €
```

**Criterios de autocorrección**

- [ ] El programa se ejecuta sin errores con los datos del ejemplo **y** con datos incorrectos (letras, números fuera de rango).
- [ ] Hay docstrings en el programa y en todas las funciones, y constantes en MAYÚSCULAS.
- [ ] Las funciones de cálculo **devuelven** valores con `return` y no usan `print` ni `input`.
- [ ] Se usan valores por defecto (`habitual=False`, `iva=IVA`) y al menos una llamada con argumentos por nombre.
- [ ] `presupuesto` devuelve dos valores y se recogen desempaquetando.
- [ ] Las pruebas con `assert` se superan.
- [ ] No hay variables globales salvo las constantes.

??? success "Solución"
    ```python
    """Servicio técnico de móviles.

    Calcula presupuestos de reparación (pieza + mano de obra), aplica el
    descuento de cliente habitual y el IVA, y al salir muestra un resumen.
    """

    PRECIO_HORA = 30.00          # mano de obra, € por hora
    PRECIO_PANTALLA = 89.90
    PRECIO_BATERIA = 45.00
    IVA = 21                     # %
    DESCUENTO_HABITUAL = 10      # %
    MAX_HORAS = 8


    def pedir_entero(mensaje: str, minimo: int, maximo: int) -> int:
        """Pide un entero hasta que esté entre minimo y maximo."""
        while True:
            try:
                numero = int(input(mensaje))
                if minimo <= numero <= maximo:
                    return numero
                print(f"Debe estar entre {minimo} y {maximo}")
            except ValueError:
                print("Escribe un número entero")


    def precio_pieza(tipo: str) -> float:
        """Devuelve el precio de la pieza según el tipo de reparación."""
        if tipo == "pantalla":
            return PRECIO_PANTALLA
        if tipo == "batería":
            return PRECIO_BATERIA
        return 0.0                       # software: no hay pieza


    def aplicar_descuento(importe: float, habitual: bool = False) -> float:
        """Aplica el descuento de cliente habitual, si corresponde."""
        if habitual:
            return importe - importe * DESCUENTO_HABITUAL / 100
        return importe


    def con_iva(importe: float, iva: int = IVA) -> float:
        """Devuelve el importe con el IVA incluido."""
        return importe + importe * iva / 100


    def presupuesto(tipo: str, horas: int,
                    habitual: bool = False) -> tuple[float, float]:
        """Devuelve la base imponible y el total con IVA de una reparación."""
        base = precio_pieza(tipo) + horas * PRECIO_HORA
        base = aplicar_descuento(base, habitual)
        return base, con_iva(base)


    def probar() -> None:
        """Pruebas de las funciones de cálculo."""
        assert precio_pieza("software") == 0
        assert aplicar_descuento(100) == 100
        assert aplicar_descuento(100, habitual=True) == 90
        assert con_iva(100) == 121
        assert con_iva(100, iva=10) == 110
        assert presupuesto("software", 2) == (60, 72.6)


    def main() -> None:
        """Programa principal: menú de reparaciones."""
        probar()
        presupuestos = 0
        facturado = 0.0

        while True:
            print("\n--- SERVICIO TÉCNICO ---")
            print("1. Pantalla  2. Batería  3. Software  4. Salir")
            opcion = input("Reparación: ")

            match opcion:
                case "1":
                    tipo = "pantalla"
                case "2":
                    tipo = "batería"
                case "3":
                    tipo = "software"
                case "4":
                    break
                case _:
                    print("Opción no válida")
                    continue

            horas = pedir_entero(f"Horas de trabajo (1-{MAX_HORAS}): ",
                                 1, MAX_HORAS)
            habitual = input("¿Cliente habitual? (s/n): ") == "s"

            base, total = presupuesto(tipo, horas, habitual=habitual)
            print(f"Reparación de {tipo} | Base: {base:.2f} € | "
                  f"Total con IVA: {total:.2f} €")
            presupuestos += 1
            facturado += total

        print("\n--- RESUMEN DEL DÍA ---")
        print(f"Presupuestos: {presupuestos}")
        print(f"Total facturado: {facturado:.2f} €")


    if __name__ == "__main__":
        main()
    ```

    **Puntos clave**

    - Las funciones de cálculo **no** usan `print` ni `input`: reciben datos y devuelven resultados. Por eso se pueden probar con `assert`.
    - `presupuesto` reutiliza `precio_pieza`, `aplicar_descuento` y `con_iva`: si cambia el IVA o el descuento, solo se toca una constante.
    - `pedir_entero` sustituye al bucle de validación que en la UT02 tenías que repetir para cada dato.
    - `presupuestos` y `facturado` son variables **locales** de `main()`, no globales.

    **Ampliación con módulo**

    `taller.py` contiene las constantes, `precio_pieza`, `aplicar_descuento`, `con_iva`, `presupuesto` y las pruebas dentro de `if __name__ == "__main__":`. `principal.py` empieza con `import taller` y llama a `taller.presupuesto(...)`. Al ejecutar `principal.py`, las pruebas de `taller.py` no se ejecutan; para lanzarlas, ejecuta `python taller.py`.

---

## ¿Cómo voy?

| Si has acertado... | Qué hacer |
|---|---|
| Casi todo | Estás listo/a. Repasa los errores que hayas tenido. |
| La mitad | Vuelve a los apartados donde fallaste y repite los ejemplos en la consola. |
| Poco | Repasa la unidad con calma, escribiendo los ejemplos, y pide ayuda al profesor o profesora antes del proyecto. |
