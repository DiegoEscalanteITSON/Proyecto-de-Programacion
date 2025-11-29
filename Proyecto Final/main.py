# El Main... no hay más ciencia
import tkinter as tk
from gui_ventana import ventana_registro
from reporte_de_ventas import generar_reporte_ventas

def menu():
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.geometry("300x200")

    tk.Label(ventana, text="=== Menú Principal ===", font=("Arial", 14)).pack(pady=20)
    tk.Button(ventana, text="1. Abrir registro de ventas", command=ventana_registro, width=25).pack(pady=10)
    tk.Button(ventana, text="2. Generar reporte de ventas", command=generar_reporte_ventas, width=25).pack(pady=10)
    tk.Button(ventana, text="3. Salir", command=ventana.destroy, width=25).pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    menu()