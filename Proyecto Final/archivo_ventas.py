# Archivo que guarda la ventas en txt
# Modulo que maneja la logica de las ventas

ventas = []   # lista global

def agregar_venta(juego, cantidad):
    """Agrega una venta a la lista de ventas.  """
    ventas.append({"nombre": juego, "cantidad": cantidad})
    print(f"✔ Venta agregada: {juego} - Cantidad: {cantidad}")

def obtener_ventas():
    return ventas

def guardar_venta_en_txt(ventas):
    """Guarda las ventas en un archivo de texto."""
    if not ventas:
        print("No hay ventas para guardar.")
        return
    with open("ventas.txt", "w", encoding="utf-8") as archivo:
        for venta in ventas:
            archivo.write(f"{venta['nombre']} - ${venta['precio']}\n")
            print(f"Venta guardada: {venta['nombre']} - ${venta['precio']}")

print("✔ Archivo ventas de registradas actualizado correctamente.")
