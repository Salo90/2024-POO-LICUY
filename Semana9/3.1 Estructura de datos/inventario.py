from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}
    # Añade un nuevo producto al inventario si el ID es único.
    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto añadido exitosamente.")

    # Elimina un producto del inventario por su ID.
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

# Actualiza la cantidad y/o el precio de un producto por su ID.
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

    # Busca producto por nombre
    def buscar_producto_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        return encontrados

    # Muestra todos los productos en el inventario.
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(producto)