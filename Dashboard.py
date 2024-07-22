import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    unidades = {
        '1': 'Semana2/1.1 Tarea Semana 2/Tarea-semana2POO.py',
        '2': 'Semana3/1.1 Tarea Semana 3/Tarea-Semana3-POO-Temp-Tradicional.py'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú principal
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidades '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break

        eleccion_unidades = eleccion_unidad.split(',')
        eleccion_unidades = [unidad.strip() for unidad in eleccion_unidades]

        for eleccion_unidad in eleccion_unidades:
            if eleccion_unidad in unidades:
                ruta_script = os.path.join(ruta_base, unidades[eleccion_unidad])
                codigo = mostrar_codigo(ruta_script)
                if codigo:
                    ejecutar = input(f"¿Desea ejecutar el script de la unidad {eleccion_unidad}? (1: Sí, 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    elif ejecutar == '0':
                        print(f"No se ejecutó el script de la unidad {eleccion_unidad}.")
                    else:
                        print("Opción no válida.")
            else:
                print(f"Opción {eleccion_unidad} no válida.")
        input("\nPresiona Enter para volver al menú principal.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
