"""
Enunciado:
Implementar la clase CajaFuerte que reproduzca el siguiente comportamiento:

>>> caja = CajaFuerte(9158)
>>> caja.esta_abierta()
False
>>> caja.guardar("pulsera")
Exception: La caja fuerte está cerrada
>>> caja.abrir(1234)
Exception: La clave es inválida
>>> caja.abrir(9158)
>>> caja.esta_abierta()
True
>>> caja.guardar("pulsera")
>>> caja.guardar("reloj de oro")
Exception: No se puede guardar más de una cosa
>>> caja.cerrar()
>>> caja.sacar()
Exception: La caja fuerte está cerrada
>>> caja.abrir(9158)
>>> caja.sacar()
'pulsera'
>>> caja.sacar()
Exception: No hay nada para sacar
"""

class CajaFuerte:
    def __init__(self, codigo):
        self.codigo = codigo
        self.caja_esta_abierta = False
        self.objetos_guardados = []

    def esta_abierta(self):
        print(self.caja_esta_abierta)

    def abrir(self, codigo):
        if codigo != self.codigo:
            raise Exception("La clave es inválida")
        self.caja_esta_abierta = True

    def cerrar(self):
        self.caja_esta_abierta = False

    def guardar(self, objeto):
        if not self.caja_esta_abierta:
            raise Exception("La caja fuerte está cerrada")
        elif self.objetos_guardados:
            raise Exception("No se puede guardar más de una cosa")
        self.objetos_guardados.append(objeto)

    def sacar(self):
        if not self.caja_esta_abierta:
            raise Exception("La caja fuerte está cerrada")
        elif not self.objetos_guardados:
            raise Exception("No hay nada para sacar")
        print(self.objetos_guardados.pop())

    def __str__(self):
        return f"Código: {self.codigo}  /   Esta abierta: {self.caja_esta_abierta}   /   Objetos: {''.join(self.objetos_guardados)}"
