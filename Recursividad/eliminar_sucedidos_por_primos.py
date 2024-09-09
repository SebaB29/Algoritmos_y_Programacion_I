"""
Enunciado:
Realizar una función recursiva que reciba una lista de Python de números y devuelva una nueva lista eliminando los dígitos que son sucedidos por un número primo, devolviendo una lista igual a la recibida por parámetro pero sin los dígitos que cumplan la condición especificada. Nota: la función es_primo() ya se encuentra implementada.

Ejemplo: eliminar_sucedidos_primo([4,7,6,11,13]) → [7,13]
"""

def es_primo(n):
    for num in range(2, n):
        if n % num == 0:
            return False
        return True

def _eliminar_sucedidos_por_primos(lista, indice, nueva_lista):
    if indice == len(lista)-1:
        nueva_lista.append(lista[indice])
        return nueva_lista

    if not es_primo(lista[indice+1]):
        nueva_lista.append(lista[indice])
    return _eliminar_sucedidos_por_primos(lista, indice+1, nueva_lista)

def eliminar_sucedidos_por_primos(lista):
    return _eliminar_sucedidos_por_primos(lista, 0, [])
