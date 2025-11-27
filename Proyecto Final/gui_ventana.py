# Archivo que abrira la ventana GUI para registra ventas
import tkinter as tk
from tkinter import messagebox, ttk
from archivo_ventas import guardar_venta_en_txt
from def_ventas import agregar_venta

def adrir_gui():
    ventana = tk.Tk()
    ventana.title("Registro de Ventas")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Productos:").pack()
    entrada_producto = tk.Entry(ventana)
    entrada_producto.pack()

    tk.Label(ventana, text="Precio:").pack()
    entrada_precio = tk.Entry(ventana)
    entrada_precio.pack()

    def registrar_venta():
        producto = entrada_producto.get()
        precio = entrada_precio.get()

        if not producto or not precio:
            messagebox.showerror("Error", "Por favor, vuelva a internar.")
            return
        
        agregar_venta(producto)
        guardar_venta_en_txt(producto, precio)
        messagebox.showinfo("Venta registrada")

    tk.Button(ventana, text="Registrar Venta", command=registrar_venta).pack(pady=10)
    ventana.mainloop()