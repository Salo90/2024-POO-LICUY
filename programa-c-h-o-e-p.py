#Desarrollar un programa de registro de ventas.
# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo privado
        self._precio = precio  # Atributo privado

# Creamos el metodo para obtener detalles de la venta.
    def obtener_detalles(self):
        return f"Producto: {self._nombre}, Precio: ${self._precio:.2f}"

    # Creamos el metodo para obtener precios de la venta.
    def obtener_precio(self):
        return self._precio

# Clase derivada ProductoDigital, que hereda de Producto
class ProductoDigital(Producto):
    def __init__(self, nombre, precio, tamaño_archivo):
        super().__init__(nombre, precio)
        self._tamaño_archivo = tamaño_archivo  # Atributo privado

    # Sobrescribimos el método obtener_detalles para mostrar polimorfismo
    def obtener_detalles(self):
        detalles_base = super().obtener_detalles()
        return f"{detalles_base}, Tamaño del archivo: {self._tamaño_archivo}MB"

# Clase Venta para manejar las ventas
class Venta:
    def __init__(self):
        self._ventas = []  # Lista privada para almacenar ventas

    def registrar_venta(self, producto, cantidad):
        total = producto.obtener_precio() * cantidad
        venta = {
            'producto': producto.obtener_detalles(),
            'cantidad': cantidad,
            'total': total
        }
        self._ventas.append(venta)
        return venta

    def mostrar_ventas(self):
        for venta in self._ventas:
            print(f"Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Total: ${venta['total']:.2f}")

    def obtener_total_ventas(self):
        total_general = sum(venta['total'] for venta in self._ventas)
        return total_general

# Creamos instancias y demostramos su funcionalidad

# Creando productos
producto1 = Producto("Camisa", 29.99)
producto2 = ProductoDigital("Ebook de Fisica", 9.99, 5)

# Crear instancia de Venta
registro_ventas = Venta()

# Registrar ventas
venta1 = registro_ventas.registrar_venta(producto1, 3)
venta2 = registro_ventas.registrar_venta(producto2, 2)

# Mostrar ventas registradas
registro_ventas.mostrar_ventas()

# Obtener y mostrar el total de ventas
total_ventas = registro_ventas.obtener_total_ventas()
print(f"Total de todas las ventas: ${total_ventas:.2f}")

# Salida esperada:
# Producto: Camisa, Precio: $29.99, Cantidad: 3, Total: $89.97
# Producto: Producto: Ebook de Fisica, Precio: $9.99, Tamaño del archivo: 5MB, Cantidad: 2, Total: $19.98
# Total de todas las ventas: $109.95