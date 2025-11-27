# Archivo que abrira la ventana GUI para registra ventas
import tkinter as tk
from tkinter import messagebox, ttk
from archivo_ventas import guardar_venta_en_txt
from def_ventas import agregar_venta

def ventana_registro_ventas(ventana_principal):
    ventana_registro_ventas = tk.Toplevel(ventana_principal)
    ventana_registro_ventas.title("Registro de Ventas")
    ventana_registro_ventas.geometry("400x300")

    