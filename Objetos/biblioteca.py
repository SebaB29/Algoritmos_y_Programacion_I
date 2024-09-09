"""
Enunciado:
Sabiendo que la clase Libro tiene los métodos obtener_autor y obtener_titulo que devuelven cadenas de caracteres, escribir la clase Biblioteca con los métodos:

* agregar_libro que recibe un Libro y lo agrega a la colección.
* sacar_libro que recibe el nombre de un título y el de un autor y lo saca de la biblioteca, devolviéndolo o levantando una excepción en caso de que los datos no correspondan con los de algún libro agregado.
* contiene_libro que recibe el nombre de un título y el de un autor y devuelve True o False de acuerdo a si está en la colección o no.
"""

class Libro:
    def __init__(self, titulo, autor):
        """..."""
        self.titulo = titulo
        self.autor = autor
    
    def obtener_titulo(self):
        """..."""
        return str(self.titulo)
    
    def obtener_autor(self):
        """..."""
        return str(self.autor)

class Biblioteca:
    def __init__(self):
        """..."""
        self.coleccion = set()
    
    def agregar_libro(self, libro):
        """..."""
        self.coleccion.add((libro.titulo, libro.autor))
    
    def sacar_libro(self, titulo, autor):
        """..."""
        if not (titulo, autor) in self.coleccion:
            raise Exception("El libro no esta en la colección")
        self.coleccion.remove((titulo, autor))
        return f"Libro: {titulo}, Autor: {autor}"
    
    def contiene_libro(self, titulo, autor):
        """..."""
        return (titulo, autor) in self.coleccion
