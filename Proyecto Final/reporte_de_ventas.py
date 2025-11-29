# Codigo que genera reporte de ventas
import pandas as pd
import matplotlib.pyplot as plt
from archivo_ventas import obtener_ventas

def generar_reporte_ventas():
    ventas = obtener_ventas()
    if not ventas:
        print("No hay ventas registradas.")
        return

    # Crear DataFrame a partir de la lista de dicts
    df = pd.DataFrame(ventas)

    # Asegurarnos que existen las columnas necesarias
    if 'juego' not in df.columns or 'cantidad' not in df.columns:
        print("Formato de datos de ventas incorrecto.")
        return

    # Agrupar por juego y sumar las cantidades
    reporte_ventas = df.groupby('juego', as_index=False)['cantidad'].sum()

    print("\n==== Resumen de Ventas: ====")
    print(reporte_ventas)

    # Graficar las ventas
    plt.figure(figsize=(10,6))
    plt.bar(reporte_ventas['juego'], reporte_ventas['cantidad'])
    plt.xlabel('Juegos')
    plt.ylabel('Cantidad Vendida')
    plt.title('Reporte de Ventas de Juegos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
