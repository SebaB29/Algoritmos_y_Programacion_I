"""
Enunciado:
Escribir una clase FacebookUser que contenga los siguientes métodos:
__init__: Recibe un nombre de usuario.
__str__: Devuelve el nombre de usuario.
publicar(post): Publica un post en el muro del usuario.
agregar_amigo(otro_usuario): Convierte al usuario actual y a otro usuario en amigos. La amistad es recíproca, si Juan agrega como amigo a José, entonces Juan está dentro de los amigos de José.
mostrar_amigos(): Devuelve una lista con los nombres de todos los amigos.
mostrar_muro(): Muestra todos los posts del usuario ordenados de mas nuevo a más viejo
"""

class FacebookUser:
    def __init__(self, usuario):
        self.nombre_usuario = usuario
        self.muro = []
        self.amigos = []

    def pubilcar(self, post):
        self.muro.append(post)

    def agregar_amigo(self, otro_usuario):
        self.amigos.append(otro_usuario.nombre_usuario)
        otro_usuario.amigos.append(self.nombre_usuario)

    def mostrar_amigos(self):
        return f"Amigos: {self.amigos}"

    def mostrar_muro(self):
        for post in range(len(self.muro)-1, -1, -1):
            print(self.muro[post])

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}"
