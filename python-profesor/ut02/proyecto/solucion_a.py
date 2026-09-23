"""Cajero automático.

Autentica al usuario con un PIN (3 intentos) y permite consultar el saldo,
ingresar y retirar dinero. Al salir muestra un resumen de la sesión.

Autor: (solución de referencia)
"""

PIN_CORRECTO = "1234"
MAX_INTENTOS = 3
SALDO_INICIAL = 500.0
LIMITE_RETIRADA = 300.0     # máximo por operación
SALDO_BAJO = 50.0           # por debajo de este saldo se muestra un aviso

saldo = SALDO_INICIAL
operaciones = 0             # ingresos y retiradas realizados con éxito

# --- Autenticación ---
autenticado = False
for intento in range(1, MAX_INTENTOS + 1):
    pin = input(f"PIN (intento {intento}/{MAX_INTENTOS}): ")
    if pin == PIN_CORRECTO:
        autenticado = True
        break
    print("PIN incorrecto")

if not autenticado:
    print("Tarjeta bloqueada. Contacte con su banco.")
else:
    print("Acceso concedido")

    # --- Menú principal ---
    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar saldo")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "4":
            break

        if opcion == "1":
            print(f"Saldo actual: {saldo:.2f} €")
        elif opcion == "2" or opcion == "3":
            # Pedir una cantidad positiva (se repite hasta que sea válida)
            while True:
                try:
                    cantidad = float(input("Cantidad (€): "))
                    if cantidad <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cantidad no válida")

            if opcion == "2":
                saldo += cantidad
                operaciones += 1
                print(f"Ingreso realizado. Nuevo saldo: {saldo:.2f} €")
            elif cantidad > saldo:
                print("Saldo insuficiente")
            elif cantidad > LIMITE_RETIRADA:
                print(f"No se puede retirar más de {LIMITE_RETIRADA:.2f} € por operación")
            else:
                saldo -= cantidad
                operaciones += 1
                print(f"Retirada realizada. Nuevo saldo: {saldo:.2f} €")
        else:
            print("Opción no válida")

    # --- Resumen de la sesión ---
    print("\n--- RESUMEN DE LA SESIÓN ---")
    print(f"Operaciones realizadas: {operaciones}")
    print(f"Saldo final: {saldo:.2f} €")
    print(f"Variación: {saldo - SALDO_INICIAL:+.2f} €")
    print("Saldo bajo" if saldo < SALDO_BAJO else "Saldo correcto")
