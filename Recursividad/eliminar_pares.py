"""
Enunciado:
Realizar una función recursiva que elimine los números pares de una lista de Python que contiene únicamente números.
"""

def eliminar_pares(lista, indice):
    if indice == len(lista):
        return lista
    if lista[indice] % 2 == 0:
        lista.remove(lista[indice])
    return eliminar_pares(lista, indice+1)
