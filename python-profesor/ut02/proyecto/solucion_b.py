"""Gestor de notas de una clase.

Pide las notas de cada alumno, calcula su media y su calificación y,
al final, muestra un resumen de la clase.

Autor: (solución de referencia)
"""

NOTA_MIN = 0
NOTA_MAX = 10
NOTAS_POR_ALUMNO = 3
NOTA_APROBADO = 5

# --- Número de alumnos (entero mayor que 0) ---
while True:
    try:
        num_alumnos = int(input("Número de alumnos: "))
        if num_alumnos > 0:
            break
        print("Debe haber al menos un alumno")
    except ValueError:
        print("Escribe un número entero")

aprobados = 0
suma_medias = 0.0
mejor_media = -1.0
mejor_alumno = ""

# --- Datos de cada alumno ---
for i in range(1, num_alumnos + 1):
    print(f"\nAlumno {i}")
    nombre = input("Nombre: ")

    suma_notas = 0.0
    for n in range(1, NOTAS_POR_ALUMNO + 1):
        # Pedir la nota hasta que sea un número entre NOTA_MIN y NOTA_MAX
        while True:
            try:
                nota = float(input(f"  Nota {n}: "))
                if NOTA_MIN <= nota <= NOTA_MAX:
                    break
                print(f"  La nota debe estar entre {NOTA_MIN} y {NOTA_MAX}")
            except ValueError:
                print("  Escribe un número")
        suma_notas += nota

    media = suma_notas / NOTAS_POR_ALUMNO

    if media >= 9:
        categoria = "Sobresaliente"
    elif media >= 7:
        categoria = "Notable"
    elif media >= NOTA_APROBADO:
        categoria = "Aprobado"
    else:
        categoria = "Suspenso"

    print(f"{nombre}: media {media:.2f} ({categoria})")

    # Acumuladores para el resumen
    suma_medias += media
    if media >= NOTA_APROBADO:
        aprobados += 1
    if media > mejor_media:
        mejor_media = media
        mejor_alumno = nombre

# --- Resumen de la clase ---
print("\n--- RESUMEN DE LA CLASE ---")
print(f"Aprobados: {aprobados}")
print(f"Suspensos: {num_alumnos - aprobados}")
print(f"Media de la clase: {suma_medias / num_alumnos:.2f}")
print(f"Mejor alumno: {mejor_alumno} ({mejor_media:.2f})")
