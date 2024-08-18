class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters y Setters
    @property
    def id_producto(self):
        return self.__id_producto

    @id_producto.setter
    def id_producto(self, value):
        self.__id_producto = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    from producto import Producto

    class Inventario:
        def __init__(self):
            self.productos = {}

        def añadir_producto(self, producto):
            if producto.id_producto in self.productos:
                print("Error: El ID del producto ya existe.")
            else:
                self.productos[producto.id_producto] = producto
                print("Producto añadido exitosamente.")

        def eliminar_producto(self, id_producto):
            if id_producto in self.productos:
                del self.productos[id_producto]
                print("Producto eliminado exitosamente.")
            else:
                print("Error: Producto no encontrado.")

        def actualizar_producto(self, id_producto, cantidad=None, precio=None):
            if id_producto in self.productos:
                producto = self.productos[id_producto]
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado exitosamente.")
            else:
                print("Error: Producto no encontrado.")

        def buscar_producto_por_nombre(self, nombre):
            encontrados = [producto for producto in self.productos.values() if
                           nombre.lower() in producto.nombre.lower()]
            return encontrados

        def mostrar_productos(self):
            if not self.productos:
                print("No hay productos en el inventario.")
            else:
                for producto in self.productos.values():
                    print(producto)

    Archivo: main.py
    python
    Copiar
    código
    from inventario import Inventario
    from producto import Producto

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
                id_producto = input("Ingrese ID del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad del producto: "))
                precio = float(input("Ingrese precio del producto: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "2":
                id_producto = input("Ingrese ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == "3":
                id_producto = input("Ingrese ID del producto a actualizar: ")
                cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
                precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "4":
                nombre = input("Ingrese nombre del producto a buscar: ")
                productos = inventario.buscar_producto_por_nombre(nombre)
                if productos:
                    for producto in productos:
                        print(producto)
                else:
                    print("No se encontraron productos con ese nombre.")

            elif opcion == "5":
                inventario.mostrar_productos()

            elif opcion == "6":
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Inténtelo de nuevo.")

    if __name__ == "__main__":
        main()