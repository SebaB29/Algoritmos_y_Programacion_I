"""
Enunciado:
Realizar una función recursiva en Python que reciba un número entero y devuelva el producto de sus dígitos.
Ejemplo: producto_digital(356) → 90, pues $3 \cdot 5 \cdot 6 = 90$.
"""

def _producto_digitos(cadena, indice):
    if indice == len(cadena):
        return 1
    return int(cadena[indice]) * _producto_digitos(cadena, indice+1)

def producto_digitos(numero):
    return _producto_digitos(str(numero), 0)
