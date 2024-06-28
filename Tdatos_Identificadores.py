"""
Este programa gestiona un registro básico de ventas. Permite agregar ventas,
calcular el total de ventas y mostrar el historial de ventas.
"""

# Definimos una lista para almacenar las ventas
registro_ventas = []

#Agrega una venta al registro.
def agregar_venta(fecha, articulo, cantidad, precio_unitario):

    venta = {
        'fecha': fecha,
        'articulo': articulo,
        'cantidad': cantidad,
        'precio_unitario': precio_unitario,
        'total': cantidad * precio_unitario
    }
    registro_ventas.append(venta)
    print(f"Venta agregada: {venta}")

#Calcula el total de todas las ventas registradas.
def calcular_total_ventas():
    total_ventas = sum(venta['total'] for venta in registro_ventas)
    return total_ventas

#Muestra el historial de ventas.
def mostrar_historial_ventas():

    for venta in registro_ventas:
        print(f"Fecha: {venta['fecha']}, Artículo: {venta['articulo']}, "
              f"Cantidad: {venta['cantidad']}, Precio Unitario: {venta['precio_unitario']}, "
              f"Total: {venta['total']}")

#Permite ingresar una venta a través de la consola.
def ingresar_venta_por_consola():
    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    articulo = input("Ingrese el nombre del artículo: ")
    cantidad = int(input("Ingrese la cantidad de artículos vendidos: "))
    precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
    agregar_venta(fecha, articulo, cantidad, precio_unitario)

# Ejemplo de uso del programa
while True:
    print("\nMenú:")
    print("1. Agregar venta")
    print("2. Mostrar historial de ventas")
    print("3. Calcular total de ventas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        ingresar_venta_por_consola()
    elif opcion == '2':
        print("\nHistorial de Ventas:")
        mostrar_historial_ventas()
    elif opcion == '3':
        total = calcular_total_ventas()
        print(f"\nTotal de Ventas: ${total:.2f}")
    elif opcion == '4':
        print("Registro finalizada..")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")