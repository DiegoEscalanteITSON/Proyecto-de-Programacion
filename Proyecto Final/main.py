# El Main... no hay más ciencia
import tkinter as tk
from colorama import init, Fore
from gui_ventana import ventana_registro
from reporte_de_ventas import generar_reporte_ventas

def menu():
    root = tk.Tk()
    root.title("Menú Principal")
    root.geometry("300x200")

    tk.Label(root, text="=== Menú Principal ===", font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="1. Abrir registro de ventas", command=ventana_registro, width=25).pack(pady=10)
    tk.Button(root, text="2. Generar reporte de ventas", command=generar_reporte_ventas, width=25).pack(pady=10)
    tk.Button(root, text="3. Salir", command=root.destroy, width=25).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    menu()