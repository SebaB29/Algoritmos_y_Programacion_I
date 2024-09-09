"""
Enunciado:
Escribir una clase Item, que recibe en su constructor el nombre del objeto y su peso. Escribir también una clase Caja, que recibe en su constructor la capacidad de la misma (o sea, cuánto peso puede cargar). Además, esta clase debe tener los siguientes métodos:

* guardar_item, que recibe un Item y lo guarda en su interior, siempre y cuando tenga capacidad. Si no tiene capcidad, debe lanzar una excepción.

* obtener_mas_pesado y obtener_mas_liviano, que devuelven el Item con mayor y menor peso, respectivamente. En ambos casos devuelve None si no hay items guardados, y si hay más de uno con el mismo peso devuelve cualquiera de ellos.
"""

class Item:
    def __init__(self, objeto, peso):
        self.nombre_objeto = objeto
        self.peso_objeto = peso

class CajaLlena(Exception):
        pass

class Caja:
    def __init__(self, capacidad):
        self.almacenamiento = []
        self.capacidad = capacidad

    def guardar_item(self, item):
        if self.capacidad >= item.peso_objeto:
            self.capacidad -= item.peso_objeto
            self.almacenamiento.append((item.nombre_objeto, item.peso_objeto))
        else:
            raise CajaLlena("LA CAJA ESTÁ LLENA")

    def obtener_mas_pesado(self):
        objeto_mas_pesado, mayor_peso = None, 0
        for objeto, peso in self.almacenamiento:
            if peso > mayor_peso:
                objeto_mas_pesado, mayor_peso = objeto, peso

        return objeto_mas_pesado

    def obtener_mas_liviano(self):
        objeto_mas_liviano, menor_peso = None, self.capacidad
        for objeto, peso in self.almacenamiento:
            if peso < menor_peso:
                objeto_mas_liviano, menor_peso = objeto, peso

        return objeto_mas_liviano


    def __str__(self):
        objetos = []
        for objeto, peso in self.almacenamiento:
            objetos.append(objeto)
        return f"Objetos: {', '.join(objetos)}"
