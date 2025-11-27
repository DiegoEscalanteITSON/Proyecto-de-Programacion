# Def que llamara a las funciones de ventas
# ventas.py

ventas = []   # lista global

def agregar_venta(juego, cantidad):
    ventas.append((juego, cantidad))
    print(f"Venta agregada: {juego} - Cantidad: {cantidad}")

def obtener_ventas():
    return ventas
