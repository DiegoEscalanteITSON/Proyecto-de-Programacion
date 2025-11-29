# Codigo que genera reporte de ventas
import pandas as pd
import matplotlib.pyplot as plt
from archivo_ventas import obtener_ventas

def generar_reporte_ventas():
    print("\nGenerando reporte de ventas...")
    ventas = obtener_ventas()
    if not ventas:
        print("No hay ventas registradas.")
        return

    # Crear DataFrame a partir de la lista de dicts
    df = pd.DataFrame(ventas)
    # Asegurarnos que existen las columnas necesarias
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors='coerce').fillna(0).astype(int)
    df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors='coerce').fillna(0.0).astype(float)
    # Agrupar por juego y sumar las cantidades
    df["total"] = df["cantidad"] * df["precio_unitario"]
    reporte = df.groupby("juego").agg({"cantidad": "sum", "total": "sum"}).reset_index()

    print("\n==== Resumen de Ventas: ====")
    print(reporte)

    # Graficar las ventas
    plt.figure(figsize=(10,6))
    plt.bar(reporte['juego'], reporte['cantidad'])
    plt.xlabel('Juegos')
    plt.ylabel('Cantidad Vendida')
    plt.title('Reporte de Ventas de Juegos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10,6))
    plt.bar(reporte['juego'], reporte['total'], color='orange')
    plt.xlabel('Juegos')
    plt.ylabel('Total de Ventas ($)')
    plt.title('Total de Ventas por Juego')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()