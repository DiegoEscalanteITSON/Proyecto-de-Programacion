# gui_registro.py
import tkinter as tk
from tkinter import messagebox, ttk
from archivo_ventas import agregar_venta, guardar_venta_en_txt, obtener_ventas
from catalogo import Catalogo


def ventana_registro():
    ventana = tk.Tk()
    ventana.title("Registro de Ventas")
    ventana.geometry("360x260")

    # Lista de nombres para el Combobox
    nombres_juegos = [j["nombre"] for j in Catalogo]

    tk.Label(ventana, text="Seleccione un juego:").pack(pady=5)
    combo_juegos = ttk.Combobox(ventana, values=nombres_juegos, state="readonly")
    combo_juegos.pack()

    tk.Label(ventana, text="Cantidad vendida:").pack(pady=5)
    entrada_cantidad = tk.Entry(ventana)
    entrada_cantidad.pack()

    def registrar():
        juego = combo_juegos.get()
        cantidad_text = entrada_cantidad.get().strip()

        if not juego:
            messagebox.showerror("Error", "Seleccione un juego.")
            return

        if not cantidad_text:
            messagebox.showerror("Error", "Ingrese la cantidad.")
            return

        try:
            cantidad = int(cantidad_text)
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero positivo.")
            return

        # Buscar el precio en el catálogo
        precio = next((item["precio"] for item in Catalogo if item["nombre"] == juego), None)

        # Registrar la venta (pasa el precio unitario)
        agregar_venta(juego, cantidad, precio)

        # Guardar ventas actuales en archivo
        ventas_actuales = obtener_ventas()
        guardar_venta_en_txt(ventas_actuales)

        messagebox.showinfo("Éxito", f"Venta de '{juego}' registrada.")

        # Limpiar
        entrada_cantidad.delete(0, tk.END)
        combo_juegos.set("")

    tk.Button(ventana, text="Registrar venta", command=registrar).pack(pady=15)

    ventana.mainloop()