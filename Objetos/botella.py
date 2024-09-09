"""
Enunciado:
Implementar la clase Botella que cumpla con el siguiente comportamiento:

>> botella = Botella(500)      >> botella.cargar(300)
>> print(botella)              Exception(“La botella no cuenta con capacidad suficiente”)
Botella: 0/500cc               >> botella.servir(200)
>> botella.esta_vacia()        >> print(botella)
True                           Botella: 100/500cc
>> botella.cargar(300)         >> botella.servir(200)
>> print(botella)              Exception(“La botella no cuenta con carga suficiente”)
Botella: 300/500cc
"""

class Botella:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.contenido = 0

    def esta_vacia(self):
        print(self.contenido == 0)

    def cargar(self, cantidad):
        if (cantidad + self.contenido) > self.capacidad:
            raise Exception("La botella no cuenta con capacidad suficiente")

        self.contenido += cantidad

    def servir(self, cantidad):
        if cantidad > self.contenido:
            raise Exception("La botella no cuenta con carga suficiente")

        self.contenido -= cantidad

    def __str__(self):
        return f"Botella: {self.contenido}/{self.capacidad}cc"
