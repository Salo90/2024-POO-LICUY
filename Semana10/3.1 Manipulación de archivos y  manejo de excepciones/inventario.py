import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    @staticmethod
    def from_string(producto_str):
        id_producto, nombre, cantidad, precio = producto_str.strip().split(",")
        return Producto(id_producto, nombre, int(cantidad), float(precio))

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Cargar productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo.")
            return

        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    producto = Producto.from_string(linea)
                    self.productos[producto.id_producto] = producto
            print(f"Inventario cargado exitosamente desde {self.archivo}.")
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo} no existe.")
        except PermissionError:
            print(f"Error: No tienes permiso para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guardar los productos actuales en el archivo de inventario."""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print(f"Inventario guardado exitosamente en {self.archivo}.")
        except PermissionError:
            print(f"Error: No tienes permiso para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """Agregar un nuevo producto al inventario."""
        if producto.id_producto in self.productos:
            print(f"Error: El producto con ID {producto.id_producto} ya existe.")
            return
        self.productos[producto.id_producto] = producto
        self.guardar_inventario()
        print(f"Producto {producto.nombre} añadido exitosamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualizar cantidad o precio de un producto existente."""
        if id_producto not in self.productos:
            print(f"Error: El producto con ID {id_producto} no existe.")
            return
        if cantidad is not None:
            self.productos[id_producto].cantidad = cantidad
        if precio is not None:
            self.productos[id_producto].precio = precio
        self.guardar_inventario()
        print(f"Producto con ID {id_producto} actualizado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Eliminar un producto del inventario."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        else:
            print(f"Error: El producto con ID {id_producto} no existe.")

    def buscar_producto_por_nombre(self, nombre):
        """Buscar productos por nombre."""
        encontrados = [producto for producto in self.productos.values() if producto.nombre.lower() == nombre.lower()]
        return encontrados

    def mostrar_productos(self):
        """Mostrar todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

def menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                id_producto = input("Ingrese ID del producto: ")
                if id_producto in inventario.productos:
                    print(f"Error: El producto con ID {id_producto} ya existe.")
                    intentar_nuevamente = input("¿Desea intentar con otro ID? (s/n): ")
                    if intentar_nuevamente.lower() != 's':
                        break
                else:
                    nombre = input("Ingrese nombre del producto: ")
                    cantidad = int(input("Ingrese cantidad del producto: "))
                    precio = float(input("Ingrese precio del producto: "))
                    producto = Producto(id_producto, nombre, cantidad, precio)
                    inventario.añadir_producto(producto)
                    confirmar = input("¿Desea agregar otro producto? (s/n): ")
                    if confirmar.lower() == 's':
                        continue  # Volver al inicio del bucle para buscar otro producto
                    break

        elif opcion == "2":
            while True:
                criterio = input("¿Desea eliminar por ID o por nombre? (Ingrese 'id' o 'nombre'): ").lower()

                if criterio == "id":
                    while True:
                        id_producto = input("Ingrese ID del producto a eliminar: ")
                        if id_producto in inventario.productos:
                            producto = inventario.productos[id_producto]
                            print(f"Producto encontrado: {producto}")
                            confirmar = input("¿Está seguro que desea eliminar este producto? (s/n): ")
                            if confirmar.lower() == 's':
                                inventario.eliminar_producto(id_producto)
                                confirmar = input("¿Desea eliminar otro producto? (s/n): ")
                                if confirmar.lower() == 's':
                                    continue  # Volver al inicio del bucle para buscar otro producto
                                break
                            else:
                                print("Eliminación cancelada.")
                            break
                        else:
                            print(
                                f"No se encontró ningún producto con ID {id_producto}. Por favor, intente nuevamente.")

                elif criterio == "nombre":
                    while True:
                        nombre = input("Ingrese nombre del producto a eliminar: ")
                        productos = inventario.buscar_producto_por_nombre(nombre)
                        if productos:
                            print("Productos encontrados:")
                            for producto in productos:
                                print(producto)
                            id_producto = input("Ingrese el ID del producto que desea eliminar: ")
                            if id_producto in inventario.productos:
                                producto_seleccionado = inventario.productos[id_producto]
                                print(f"Producto encontrado: {producto_seleccionado}")
                                confirmar = input(f"¿Está seguro que desea eliminar el producto '{producto_seleccionado.nombre}' con ID {producto_seleccionado.id_producto}? (s/n): ")
                                if confirmar.lower() == 's':
                                    inventario.eliminar_producto(id_producto)
                                    confirmar = input("¿Desea eliminar otro producto? (s/n): ")
                                    if confirmar.lower() == 's':
                                        continue  # Volver al inicio del bucle para buscar otro producto
                                    break
                                else:
                                    print("Eliminación cancelada.")
                            else:
                                print(f"No se encontró ningún producto con ID {id_producto}.")
                            break
                        else:
                            print(
                                f"No se encontraron productos con el nombre '{nombre}'. Por favor, intente nuevamente.")

                else:
                    print("Criterio no válido. Por favor, ingrese 'id' o 'nombre'.")
                    continue

                break

        elif opcion == "3":
            while True:
                criterio = input("¿Desea actualizar por ID o por nombre? (Ingrese 'id' o 'nombre'): ").lower()

                if criterio == "id":
                    while True:
                        id_producto = input("Ingrese ID del producto a actualizar: ")
                        if id_producto in inventario.productos:
                            producto = inventario.productos[id_producto]
                            print(f"Producto encontrado: {producto}")
                            cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
                            precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
                            cantidad = int(cantidad) if cantidad else None
                            precio = float(precio) if precio else None
                            inventario.actualizar_producto(id_producto, cantidad, precio)
                            confirmar = input("¿Desea actualizar otro producto? (s/n): ")
                            if confirmar.lower() == 's':
                                continue  # Volver al inicio del bucle para buscar otro producto
                            break
                        else:
                            print(
                                f"No se encontró ningún producto con ID {id_producto}. Por favor, intente nuevamente.")

                elif criterio == "nombre":
                    while True:
                        nombre = input("Ingrese nombre del producto a actualizar: ")
                        productos = inventario.buscar_producto_por_nombre(nombre)
                        if productos:
                            print("Productos encontrados:")
                            for producto in productos:
                                print(producto)
                            id_producto = input("Ingrese el ID del producto que desea actualizar: ")
                            if id_producto in inventario.productos:
                                producto_seleccionado = inventario.productos[id_producto]
                                print(f"Producto encontrado: {producto_seleccionado}")
                                cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
                                precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
                                cantidad = int(cantidad) if cantidad else None
                                precio = float(precio) if precio else None
                                inventario.actualizar_producto(id_producto, cantidad, precio)
                                confirmar = input("¿Desea actualizar otro producto? (s/n): ")
                                if confirmar.lower() == 's':
                                    continue  # Volver al inicio del bucle para buscar otro producto
                                break
                            else:
                                print(f"No se encontró ningún producto con ID {id_producto}.")
                            break
                        else:
                            print(
                                f"No se encontraron productos con el nombre '{nombre}'. Por favor, intente nuevamente.")

                else:
                    print("Criterio no válido. Por favor, ingrese 'id' o 'nombre'.")
                    continue
                break

        elif opcion == "4":
            while True:
                nombre = input("Ingrese nombre del producto a buscar: ")
                productos = inventario.buscar_producto_por_nombre(nombre)
                if productos:
                    print("Productos encontrados:")
                    for producto in productos:
                        print(producto)
                    confirmar = input("¿Desea buscar otro producto? (s/n): ")
                    if confirmar.lower() == 's':
                        continue  # Volver al inicio del bucle para buscar otro producto
                    else:
                        print("Busqueda cancelada.")
                        break
                else:
                    print(f"No se encontraron productos con el nombre '{nombre}'.")
                    confirmar = input("¿Desea intentar buscar otro nombre? (s/n): ")
                    if confirmar.lower() != 's':
                        break

        elif opcion == "5":

            while True:

                inventario.mostrar_productos()

                confirmar = input("¿Desea cerrar la ventana? (s/n): ")

                if confirmar.lower() == 's':

                    #print("¡Gracias por visitar!")

                    #return  # Sale del programa

                #else:

                    break  # Vuelve al menú principal

        elif opcion == "6":
            print("¡Gracias por visitar!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
