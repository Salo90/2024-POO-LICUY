# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Uso de tuplas para los atributos inmutables como título y autor
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"

# Clase que representa un usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para gestionar los libros prestados a cada usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def listar_libros_prestados(self):
        return self.libros_prestados

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"

# Clase que gestiona la biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar los libros disponibles con ISBN como clave
        self.libros_disponibles = {}
        # Conjunto para asegurar que los IDs de usuario sean únicos
        self.usuarios_registrados = set()
        # Diccionario para almacenar objetos Usuario con ID de usuario como clave
        self.usuarios = {}

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no está disponible.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios[id_usuario]
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Préstamo no posible: Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            libro_devuelto = None
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    libro_devuelto = libro
                    break
            if libro_devuelto:
                usuario.devolver_libro(isbn)
                self.libros_disponibles[isbn] = libro_devuelto
                print(f"Libro '{libro_devuelto.titulo}' devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (titulo and titulo.lower() in libro.titulo.lower()) or \
               (autor and autor.lower() in libro.autor.lower()) or \
               (categoria and categoria.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            return usuario.listar_libros_prestados()
        else:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return []

# Pruebas del sistema de gestión de biblioteca
biblioteca = Biblioteca()

# Crear libros (tuplas inmutables para autor y título)
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "0987654321")
libro3 = Libro("Donde los árboles cantan", "Laura Gallego", "Fantasía", "1122334455")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Registrar usuarios
usuario1 = Usuario("Ana Pérez", "U001")
usuario2 = Usuario("Carlos López", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("U001", "1234567890")  # Ana pide El Quijote
biblioteca.prestar_libro("U002", "0987654321")  # Carlos pide Cien años de soledad

# Listar libros prestados por Ana
print(f"Libros prestados por Ana: {usuario1.listar_libros_prestados()}")

# Devolver un libro
biblioteca.devolver_libro("U001", "1234567890")

# Buscar libros por título, autor o categoría
resultados_busqueda = biblioteca.buscar_libro(titulo="árboles")
print(f"Resultados de búsqueda: {resultados_busqueda}")

# Listar libros prestados por Carlos
print(f"Libros prestados por Carlos: {usuario2.listar_libros_prestados()}")

