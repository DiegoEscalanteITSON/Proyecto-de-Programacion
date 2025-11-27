# Codigo que genera reporte de ventas
import pandas as pd
import matplotlib.pyplot as plt
from def_ventas import obtener_ventas
from archivo_ventas import guardar_venta_en_txt

def generar_reporte_ventas(juego, cantidad):
    ventas = generar_reporte_ventas()
    if not ventas:
        print("No hay ventas registradas.")
        return
    
    # DataFrame para el reporte
    df = pd.DataFrame(ventas, columns=['Juego', 'Cantidad'])
    reporte_ventas = df.groupby('Producto').sum().reset_index()
    
    print("\n==== Resumen de Ventas: ====")
    print(reporte_ventas)
    
    # Graficar las ventas
    plt.figure(figsize=(10,6))
    plt.bar(reporte_ventas['Juego'], reporte_ventas['Cantidad'], color='blue')
    plt.xlabel('Juegos')
    plt.ylabel('Cantidad Vendida')
    plt.title('Reporte de Ventas de Juegos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()