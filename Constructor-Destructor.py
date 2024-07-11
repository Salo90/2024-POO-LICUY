#Ejemplo de un programa en Python que gestiona el acceso de usuarios utilizando clases con constructores (__init__) y destructores (__del__).
class Usuario:
    def __init__(self, nombre, email):
        """
        Constructor de la clase Usuario.

        Inicializa los atributos nombre y email del objeto Usuario.
        Se llama automáticamente cuando se crea una nueva instancia de Usuario.

        :param nombre: Nombre del usuario
        :param email: Email del usuario
        """
        self.nombre = nombre
        self.email = email
        print(f"Usuario {self.nombre} creado con éxito.")

    def __del__(self):
        """
        Destructor de la clase Usuario.

        Realiza tareas de limpieza, como imprimir un mensaje indicando que el usuario ha sido eliminado.
        Se llama automáticamente cuando todas las referencias al objeto Usuario se eliminan.
        """
        print(f"Usuario {self.nombre} eliminado.")

    def mostrar_informacion(self):
        """
        Muestra la información del usuario.
        """
        print(f"Nombre: {self.nombre}, Email: {self.email}")


class SistemaAcceso:
    def __init__(self):
        """
        Constructor de la clase SistemaAcceso.

        Inicializa una lista vacía de usuarios.
        """
        self.usuarios = []
        print("Sistema de acceso inicializado.")

    def __del__(self):
        """
        Destructor de la clase SistemaAcceso.

        Realiza tareas de limpieza, como liberar la lista de usuarios.
        Se llama automáticamente cuando todas las referencias al objeto SistemaAcceso se eliminan.
        """
        print("Sistema de acceso cerrado.")

    def agregar_usuario(self, nombre, email):
        """
        Agrega un nuevo usuario al sistema de acceso.

        :param nombre: Nombre del usuario
        :param email: Email del usuario
        """
        nuevo_usuario = Usuario(nombre, email)
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario {nombre} agregado al sistema.")

    def eliminar_usuario(self, nombre):
        """
        Elimina un usuario del sistema de acceso por su nombre.

        :param nombre: Nombre del usuario a eliminar
        """
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                self.usuarios.remove(usuario)
                print(f"Usuario {nombre} eliminado del sistema.")
                break
        else:
            print(f"Usuario {nombre} no encontrado en el sistema.")

    def mostrar_usuarios(self):
        """
        Muestra todos los usuarios en el sistema de acceso.
        """
        print("Usuarios en el sistema:")
        for usuario in self.usuarios:
            usuario.mostrar_informacion()


# Demostración del uso de las clases con constructores y destructores
if __name__ == "__main__":
    # Crear una instancia del sistema de acceso
    sistema = SistemaAcceso()

    # Agregar usuarios al sistema
    sistema.agregar_usuario("Patricio Licuy", "sa.licuy@gmail.com")
    sistema.agregar_usuario("Salomón Licuy", "salo.licuy@gmail.com")
    sistema.agregar_usuario("Ana Lopez", "ana.lopez@gmail.com")

    # Mostrar todos los usuarios en el sistema
    sistema.mostrar_usuarios()

    # Eliminar un usuario del sistema
    sistema.eliminar_usuario("Salomón Licuy")

    # Mostrar todos los usuarios después de eliminar uno
    sistema.mostrar_usuarios()

    # El sistema de acceso se cerrará automáticamente al final del programa,
    # lo que activará el destructor de la clase SistemaAcceso.