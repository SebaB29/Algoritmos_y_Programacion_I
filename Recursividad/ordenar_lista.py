"""
Enunciado:
Hacer una función recursiva que recibe una lista L y una función f, y devuelve una nueva lista que contiene al principio todos los elementos de L para los que f devuelve True, y al final el resto de los elementos. No es necesario mantener el orden relativo de los elementos en cada grupo.
Ejemplo: particionar([7,8,3,5,2], es_par) → [8,2,5,3,7]
"""

def es_par(n):
    return n % 2 == 0

def _ordenar_lista(lista, funcion, indice, nueva_lista):
    if indice == len(lista):
        return nueva_lista
    if funcion(lista[indice]):
        nueva_lista.insert(0, lista[indice])
    else:
        nueva_lista.append(lista[indice])
    return _ordenar_lista(lista, funcion, indice+1, nueva_lista)


def ordenar_lista(lista, funcion):
    """
    Ordena la lista segun el criterio de la funcion.
    Los que den True del lado izquierdo de la lista y del lado
    derehco los False.
    """
    return _ordenar_lista(lista, funcion, 0, [])
