class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def __str__(self):
        return f"{self.titulo} por {self.autor}, publicado en {self.año_publicacion}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

if __name__ == "__main__":
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)

    biblioteca = Biblioteca()
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    biblioteca.mostrar_libros()