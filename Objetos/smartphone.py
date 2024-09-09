"""
Enunciado:
Modelar en python:

Una clase App que permita crear aplicaciones con su nombre y una lista de sistemas operativos soportados.
Una clase Smartphone que permita crear smartphones con su nombre de modelo y su nombre de sistema operativo, además de permitir instalar apps (debe poder almacenar la instancia de la App).
Los objetos instanciados de dichas clases deberán cumplir con el siguiente comportamiento:

>>> app_fb = App("Facebook", ["ios", "android"])    >>> nexus.instalar(app_itunes)
>>> app_tw = App("Twitter", ["ios", "android"])     Exception(“La app no es compatible
>>> app_itunes = App("iTunes", ["ios"])             con el sistema operativo”)
>>> nexus = Smartphone("Nexus 6P", "android")       >>> iphone.instalar(app_itunes)
>>> iphone = Smartphone("iPhone 7", "ios")          >>> iphone.instalar(app_tw)
>>> nexus.instalar(app_fb)                          >>> print(nexus)
>>> nexus.instalar(app_fb)                          Nexus 6P (android). Apps: Facebook
Exception(“La app ya está instalada”)               >>> print(iphone)
                                                    iPhone 7 (ios). Apps: Itunes, Twitter
"""

class App:
    def __init__(self, nombre, sistemas_operativos):
        self.nombre_app = nombre
        self.os_soportados = sistemas_operativos

class Smartphone:
    def __init__(self, modelo, sistema_operativo):
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.Apps = []

    def instalar(self, aplicacion):
        if aplicacion.nombre_app in self.Apps:
            print("La app ya está instalada")
        elif not self.sistema_operativo in aplicacion.os_soportados:
            print("La app no es compatible")
        else:
            self.Apps.append(aplicacion.nombre_app)

    def __str__(self):
        return f"{self.modelo} ({self.sistema_operativo}). Apps: {', '.join(self.Apps)}"
