"""
Enunciado:
Implementar el algoritmo de búsqueda binaria de manera recursiva.
"""

def _busqueda_binaria(lista, elemento, desde, hasta):
    if desde > hasta:
        return -1
    medio = (hasta + desde) // 2
    if lista[medio] == elemento:
        return medio
    if elemento < lista[medio]:
        return _busqueda_binaria(lista, elemento, desde, medio - 1)
    return _busqueda_binaria(lista, elemento, medio + 1, hasta)

def busqueda_binaria(lista, elemento):
    return _busqueda_binaria(lista, elemento, 0, len(lista) - 1)
