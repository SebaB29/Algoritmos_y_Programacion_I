"""
Enunciado:
Escribir una clase Cuenta que tenga el siguiente comportamiento:

>>> c = Cuenta('Pérez')              >>> d = Cuenta('López')
>>> c.acreditar(100, 'Sueldo')       >>> c.transferir(30, d)
>>> c.extraer(60, 'Shopping')        >>> c.saldo()
>>> c.saldo()                        10
40                                   >>> d.saldo()
>>> print(c)                         30
Cuenta de Pérez

>>> c.movimientos()
[('acreditación',100,'Sueldo'),('extracción',60,'Shopping'), ('extracción',30,'Cuenta de López')]
>>> d.movimientos()
[('acreditación',30,'Cuenta de Pérez')]
>>> d.extraer(100, 'Deudas')
ERROR ValueError: Fondos Insuficientes  
"""

class Cuenta:
    def __init__(self, apellido):
        self.apellido = apellido
        self.dinero_cuenta = 0
        self.movimientos_cuenta = []

    def acreditar(self, cantidad, tipo):
        self.dinero_cuenta += cantidad
        self.movimientos_cuenta.append(("acreditación", cantidad, tipo))

    def extraer(self, cantidad, tipo):
        if cantidad > self.dinero_cuenta:
            raise ValueError("Fondos Insuficioentes")
        self.dinero_cuenta -= cantidad
        self.movimientos_cuenta.append(("extracción", cantidad, tipo))

    def transferir(self, cantidad, otra_cuenta):
        if cantidad > self.dinero_cuenta:
            raise ValueError("Fondos Insuficioentes")
        self.dinero_cuenta -= cantidad
        self.movimientos_cuenta.append(("extracción", cantidad, f"Cuenta de {otra_cuenta.apellido}"))
        otra_cuenta.dinero_cuenta += cantidad
        otra_cuenta.movimientos_cuenta.append(("acreditación", cantidad, f"Cuenta de {self.apellido}"))

    def movimientos(self):
        print(self.movimientos_cuenta)

    def saldo(self):
        print(self.dinero_cuenta)

    def __str__(self):
        return f"Cuenta de {self.apellido}"
