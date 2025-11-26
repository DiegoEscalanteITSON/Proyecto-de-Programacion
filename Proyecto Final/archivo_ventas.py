# Archivo que guarda la ventas en txt

def guardar_venta_en_txt(ventas):
    with open("ventas.txt", "w", encoding="utf-8") as archivo:
        for venta in ventas:
            archivo.write(f"{venta['nombre']} - ${venta['precio']}\n")
            print(f"Venta guardada: {venta['nombre']} - ${venta['precio']}")
            print("✔ Archivo ventas de registradas actualizado correctamente.")