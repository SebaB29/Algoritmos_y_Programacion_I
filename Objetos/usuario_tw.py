"""
Enunciado:
Se pide implementar la clase TwitterUser con los siguientes métodos:
__init__(): recibe como parámetro el nombre del usuario.
tweet(): recibe como parámetro un mensaje (se debe validar que no sobrepase los 280 caracteres) y lo agrega —con la fecha actual— a la lista de tuits del usuario. (Para obtener la fecha actual, se puede importar el módulo datetime, e invocar datetime.datetime.now())
follow(): recibe como parámetro otro usuario (de tipo TwitterUser) y lo guarda como un usuario al que se está siguiendo.
get_timeline(): devuelve una lista con los mensajes que tuitearon los usuarios a los que se está siguiendo. Debe ser una lista de tuplas tal que: (fecha, nombre_usuario, mensaje). Este método no toma parámetros, y la lista devuelta debe estar ordenada por fecha.
"""

import datetime

class TwitterUser:
    def __init__(self, usuario):
        self.nombre_usuario = usuario
        self.seguidos = []
        self.tuits = []

    def tweet(self, mensaje):
        if len(mensaje) > 280:
            raise Exception("Sobrepasa el limite de caracteres")
        self.tuits.append((datetime.datetime.now(), mensaje))

    def follow(self, otro_usuario):
        if not otro_usuario in self.seguidos:
            self.seguidos.append(otro_usuario)

    def get_timeline(self):
        tuits = []
        for usuario in self.seguidos:
            for tuit in usuario.tuits:
                tuits.append(tuit)

        return tuits
