"""
Enunciado:
Se tiene implementada la clase Tatuaje(nombre,area,dolor) cuya área y dolor son enteros mayores a 0. Implementar las clases Tatuador(nombre) y Brazo(area, aguante), que se comporten de la siguiente forma:

>>> tatuaje_dragon = Tatuaje("Dragón",10,30)    >>> tatuador.tatuar(brazo2, tatuaje_panda)
>>> tatuaje_panda = Tatuaje("Panda",10,10)      ValueError: Ya no te queda más lugar
>>> brazo1 = Brazo(20, 10)                      >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> brazo2 = Brazo(10, 100)                     >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> tatuador = Tatuador("Miguel")               >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> tatuador.tatuar(brazo1, tatuaje_dragon)     ValueError: Ya no te queda más lugar
ValueError: No te lo vas a bancar               >>> print(tatuador)
>>> tatuador.tatuar(brazo2, tatuaje_dragon)     Miguel: 3 tatuajes realizados
"""

class Tatuaje:
    def __init__(self, nombre, area, dolor):
        self.nombre = nombre
        self.area = area
        self.dolor = dolor

class Tatuador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tatuajes_realizados = 0

    def tatuar(self, zona_cuerpo, tatuaje):
        if tatuaje.area > zona_cuerpo.area:
            raise ValueError("Ya no te queda más lugar")
        elif tatuaje.dolor > zona_cuerpo.aguante:
            raise ValueError("No te la bancas")

        zona_cuerpo.area -= tatuaje.area
        self.tatuajes_realizados += 1

    def __str__(self):
        return f"{self.nombre}: {self.tatuajes_realizados} tatuajes realizados"

class ZonaCuerpo:
    def __init__(self, area, aguante):
        self.area = area
        self.aguante = aguante
