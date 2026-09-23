"""Ticket de la Cafetería El Rincón.

Pide el pedido de un cliente y muestra el ticket con el IVA, el cambio
desglosado en euros y céntimos y algunos datos de control.

Autor: (solución de referencia)
"""

NOMBRE_LOCAL = "Cafetería El Rincón"
IVA = 0.10              # IVA de hostelería
PRECIO_CAFE = 1.30      # euros, sin IVA
PRECIO_BOLLO = 1.85     # euros, sin IVA

# --- Entrada de datos ---
cliente = input("Nombre del cliente: ")
cafes = int(input("Número de cafés: "))
bollos = int(input("Número de bollos: "))
entregado = float(input("Dinero entregado (€): "))

# --- Cálculos ---
importe_cafes = cafes * PRECIO_CAFE
importe_bollos = bollos * PRECIO_BOLLO
subtotal = importe_cafes + importe_bollos
importe_iva = subtotal * IVA
total = subtotal + importe_iva
cambio = entregado - total

# Desglose del cambio (se supone que el dinero entregado es suficiente)
cambio_centimos = round(cambio * 100)
cambio_euros = cambio_centimos // 100
cambio_cts = cambio_centimos % 100

# --- Valores lógicos ---
pago_suficiente = entregado >= total
pedido_grande = cafes + bollos >= 5

# --- Salida ---
etiqueta_iva = f"IVA ({IVA:.0%})"
print()
print(f"{NOMBRE_LOCAL:^34}")
print("-" * 34)
print(f"Cliente: {cliente}")
print("-" * 34)
print(f"{cafes} x Café  {PRECIO_CAFE:>5.2f} {importe_cafes:>16.2f} €")
print(f"{bollos} x Bollo {PRECIO_BOLLO:>5.2f} {importe_bollos:>16.2f} €")
print("-" * 34)
print(f"{'Subtotal':<14}{subtotal:>18.2f} €")
print(f"{etiqueta_iva:<14}{importe_iva:>18.2f} €")
print(f"{'TOTAL':<14}{total:>18.2f} €")
print(f"{'Entregado':<14}{entregado:>18.2f} €")
print(f"{'Cambio':<14}{cambio:>18.2f} €")
print("-" * 34)
print(f"Cambio a devolver: {cambio_euros} € y {cambio_cts} cts")
print()
print("Pago suficiente:", pago_suficiente)
print("Pedido grande (5 o más artículos):", pedido_grande)
print("Tipo de 'cafes':", type(cafes))
print("Tipo de 'total':", type(total))
print("Tipo de 'cliente':", type(cliente))
