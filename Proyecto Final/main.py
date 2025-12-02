# El Main... no hay más ciencia
import tkinter as tk
from gui_ventana import ventana_registro
from reporte_de_ventas import generar_reporte_ventas

def menu():
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.geometry("330x290")
    ventana.config(bg="#1e1e2f") 

    tk.Label(ventana, text="=== Menú Principal ===", font=("Arial", 14), bg="#1e1e2f", fg="white").pack(pady=20)

    btn_style = {"bg": "#4c72af", "fg": "white", "activebackground":"#3b5a8e", "activeforeground": "white", "width": 25, "pady": 5}

    tk.Button(ventana, text="1. Abrir registro de ventas", command=ventana_registro, **btn_style).pack(pady=5)
    tk.Button(ventana, text="2. Generar reporte de ventas", command=generar_reporte_ventas, **btn_style).pack(pady=5)
    tk.Button(ventana, text="3. Salir", command=ventana.destroy, **btn_style).pack(pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    menu()
