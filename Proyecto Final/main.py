# El Main... no hay más ciencia
from colorama import init, Fore
from gui_ventana import ventana_registro
from reporte_de_ventas import generar_reporte_ventas

init(autoreset=True)

def menu():
    while True:
        print(Fore.CYAN + """
              \n=== Menú Principal ===
        "1. Abrir registro de ventas"
        "2. Generar reporte de ventas"
        "3. Salir"
              """)

        opcion = input(Fore.YELLOW + "Seleccione una opción (1-3): ")
        if opcion == '1':
            ventana_registro()
        elif opcion == '2':
            generar_reporte_ventas()
        elif opcion == '3':
            print(Fore.GREEN + "Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()