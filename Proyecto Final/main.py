# El Main... no hay más ciencia
from colorama import init, Fore
from tkinter import Tk
from gui_ventana import adrir_gui
from reporte_de_ventas import generar_reporte_ventas

init(autoreset=True)

def menu():
    ventana = Tk()
    ventana.title("Menú Principal")
    ventana.withdraw()

    while True:
        print(Fore.CYAN + "\n=== Menú Principal ===")
        print("1. Abrir registro de ventas")
        print("2. Generar reporte de ventas")
        print("3. Salir")

if __name__ == "__main__":
    adrir_gui()