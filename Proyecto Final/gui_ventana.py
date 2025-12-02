# gui_registro.py
import tkinter as tk
from tkinter import messagebox, ttk
from archivo_ventas import agregar_venta, guardar_venta_en_txt, obtener_ventas
from catalogo import Catalogo

def ventana_registro():
    ventana = tk.Toplevel() 
    ventana.title("Registro de Ventas")
    ventana.geometry("420x360")
    ventana.config(bg="#1e1e2f")

    lbl_style = {"bg": "#1e1e2f", "fg": "white", "font": ("Arial", 11)}
    entry_style = {"bg": "#2c2c3e", "fg": "white", "insertbackground": "white"}

    nombres_juegos = [item["nombre"] for item in Catalogo]

    tk.Label(ventana, text="Registro de Ventas", font=("Arial", 14), bg="#1e1e2f", fg="white").pack(pady=10)

    tk.Label(ventana, text="Seleccione un juego:", **lbl_style).pack(pady=5)
    combo_juegos = ttk.Combobox(ventana, values=nombres_juegos, state="readonly")
    combo_juegos.pack()

    tk.Label(ventana, text="Cantidad vendida:", **lbl_style).pack(pady=5)
    entrada_cantidad = tk.Entry(ventana, **entry_style)
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
    tk.Button(ventana, text="Regresar a Menú", command=ventana.destroy).pack(pady=5)

    ventana.mainloop()