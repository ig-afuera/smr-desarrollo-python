"""Ficha de un viaje en coche.

Pide los datos de un viaje y muestra su coste, el reparto entre los
pasajeros, la velocidad media y las emisiones de CO2.

Autor: (solución de referencia)
"""

PRECIO_LITRO = 1.65          # euros por litro de gasolina
EMISION_CO2_LITRO = 2.31     # kg de CO2 por litro de gasolina
UMBRAL_VIAJE_LARGO = 300     # km a partir de los cuales el viaje es largo
UMBRAL_ECONOMICO = 10        # euros por persona

# --- Entrada de datos ---
destino = input("Destino: ")
distancia = float(input("Distancia (km): "))
consumo = float(input("Consumo del coche (litros/100 km): "))
personas = int(input("Número de personas: "))
horas = int(input("Duración: horas: "))
minutos = int(input("Duración: minutos: "))

# --- Cálculos ---
litros = distancia * consumo / 100
coste = litros * PRECIO_LITRO
coste_por_persona = coste / personas
duracion_minutos = horas * 60 + minutos
velocidad_media = distancia / (duracion_minutos / 60)
co2 = litros * EMISION_CO2_LITRO

# --- Valores lógicos ---
viaje_largo = distancia > UMBRAL_VIAJE_LARGO
viaje_economico = coste_por_persona < UMBRAL_ECONOMICO

# --- Salida ---
print()
print(f"FICHA DEL VIAJE A {destino}")
print("=" * 36)
print(f"{'Distancia:':<22}{distancia:>10.1f} km")
print(f"{'Combustible:':<22}{litros:>10.2f} l")
print(f"{'Coste total:':<22}{coste:>10.2f} €")
print(f"{'Coste por persona:':<22}{coste_por_persona:>10.2f} €")
print(f"{'Duración:':<22}{horas:>6} h {minutos:02d} min")
print(f"{'Velocidad media:':<22}{velocidad_media:>10.1f} km/h")
print(f"{'Emisiones de CO2:':<22}{co2:>10.2f} kg")
print("=" * 36)
print("¿Viaje largo (más de 300 km)?", viaje_largo)
print("¿Viaje económico (menos de 10 € por persona)?", viaje_economico)
print("Tipo de 'personas':", type(personas))
print("Tipo de 'distancia':", type(distancia))
print("Tipo de 'destino':", type(destino))
