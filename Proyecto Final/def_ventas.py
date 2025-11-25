# Def que llamara a las funciones de ventas
# ventas.py

ventas = []   # lista global

def agregar_venta(juego):
    ventas.append(juego)

def obtener_ventas():
    return ventas
