"""
Enunciado:
Se pide implementar la clase Boleteria, que recibe en su constructor un evento y la cantidad de localidades para el mismo; de modo tal que cumpla el siguiente comportamiento:

>>> b = Boleteria("Rush",500)                       >>> b.localidades_agotadas()
>>> print(b)                                        False
Evento: Rush - Localidades vendidas: 0 de 500       >>> b.vender_localidades(100)
>>> b.vender_localidades(400)                       >>> b.localidades_agotadas()
>>> b.vender_localidades(200)                       True
Traceback (most recent call last):                  >>> print(b)
...                                                 Evento: Rush - Localidades vendidas: 500 de 500
ValueError: No hay localidades suficientes
"""

class Boleteria:
    def __init__(self, evento, asientos):
        self.evento = evento
        self.asientos = asientos
        self.asientos_vendidos = 0

    def vender_asientos(self, cantidad):
        if (self.asientos_vendidos + cantidad) > self.asientos:
            raise ValueError("No hay asientos suficientes")
        self.asientos_vendidos += cantidad

    def asientos_agotados(self):
        print(self.asientos == self.asientos_vendidos)

    def __str__(self):
        return f"Evento: {self.evento}  -  Asientos vendidos: {self.asientos_vendidos} de {self.asientos}"
