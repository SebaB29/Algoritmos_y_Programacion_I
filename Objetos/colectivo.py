"""
Enunciado:
Asumiendo que ya existe una clase Pasajero(destino) cuyo destino es una cadena, implementar la clase Colectivo con los siguientes métodos:

Un constructor, que crea un Colectivo vacío.
Un método subir, que recibe un destino (en forma de cadena) y un pasajero lo agrega al colectivo.
Un método bajar, que recibe un destino, saca del colectivo a los pasajeros que tienen dicho destino asignado, devolviéndolos en una lista.
"""

class Pasajero:
    def __init__(self, destino):
        self.destino = destino

class Colectivo:
    def __init__(self):
        self.asientos = []

    def subir(self, pasajero):
        self.asientos.append(pasajero)

    def bajar(self, destino):
        for pasajero in self.asientos:
            if pasajero.destino == destino:
                self.asientos.remove(pasajero)

    def __str__(self):
        return f"Asientos: {self.asientos}"
