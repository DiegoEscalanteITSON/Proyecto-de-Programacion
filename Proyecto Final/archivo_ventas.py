# Archivo que guarda las ventas en txt
# Modulo que maneja la logica de las ventas

ventas = []   # lista global de ventas

def agregar_venta(juego, cantidad, precio_unitario=None):
    """Agrega una venta a la lista de ventas."""
    total = None
    if precio_unitario is not None:
        try:
            total = float(precio_unitario) * int(cantidad)
        except (ValueError, TypeError):
            total = None

    venta = {
        "juego": juego,
        "cantidad": int(cantidad),
        "precio_unitario": precio_unitario,
        "total": total
    }
    ventas.append(venta)
    print(f"✔ Venta agregada: {juego} - Cantidad: {cantidad} - Precio unitario: {precio_unitario} - Total: {total}")

def obtener_ventas():
    """Devuelve la lista actual de ventas (referencia directa)."""
    return ventas

def guardar_venta_en_txt(ventas_list):
    """Guarda todas las ventas en un archivo de texto (sobrescribe)."""
    if not ventas_list:
        print("No hay ventas para guardar.")
        return

    try:
        with open("ventas.txt", "w", encoding="utf-8") as archivo:
            for venta in ventas_list:
                line = f"{venta['juego']} - Cantidad: {venta['cantidad']}"
                if venta.get('precio_unitario') is not None:
                    line += f" - Precio unitario: ${venta['precio_unitario']} - Total: ${venta['total']}"
                archivo.write(line + "\n")
        print("✔ Archivo 'ventas.txt' actualizado correctamente.")
    except Exception as e:
        print(f"Error al guardar ventas en archivo: {e}")