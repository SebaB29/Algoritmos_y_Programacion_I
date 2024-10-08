"""
Implementación de:
- Lista Enlazada
- Pila
- Cola
- Cola Enlazada
"""

class _Nodo:
    def __init__(self, dato=None, proximo=None):
        self.dato = dato
        self.proximo = proximo
    
    def __str__(self):
        return f"{self.dato}"


class _IteradorListaEnlazada:
    def __init__(self, primero):
        self.actual = primero
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration()

        dato = self.actual.dato
        self.actual = self.actual.proximo
        return dato


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.longitud = 0

    def insert(self, i, elemento):
        if i < 0 or i > self.longitud:
            raise IndexError("Posición inválida")

        nuevo = _Nodo(elemento)
        if i == 0:
            nuevo.proximo = self.primero
            self.primero = nuevo
        else:
            nodo_anterior = self.primero
            for _ in range(1, i):
                nodo_anterior = nodo_anterior.proximo

            nuevo.proximo = nodo_anterior.proximo
            nodo_anterior.proximo = nuevo

        self.longitud += 1
    
    def append(self, elemento):
        nuevo = _Nodo(elemento)
        if not self.primero:
            self.primero = nuevo
            return
        
        actual = self.primero
        while actual.proximo:
            actual = actual.proximo
        
        actual.proximo = nuevo
        self.longitud += 1

    def extender(self, lista):
        if lista.esta_vacia():
            return
        
        actual = self.primero
        while actual and actual.proximo:
            actual = actual.proximo

        actual_lista = lista.primero
        if not actual:
            nuevo = _Nodo(actual_lista.dato)
            self.primero = nuevo
            actual_lista = actual_lista.proximo
        
        while actual_lista:
            nuevo = _Nodo(actual_lista.dato)
            actual.proximo = nuevo
            actual = nuevo
            actual_lista = actual_lista.proximo

    def remove(self, elemento):
        if self.longitud == 0:
            raise ValueError("Lista Vacía")

        elif self.primero.dato == elemento:
            self.primero = self.primero.proximo
        
        else:
            nodo_anterior = self.primero
            nodo_actual = nodo_anterior.proximo
            while nodo_actual is not None and nodo_actual.dato != elemento:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_anterior.proximo
            
            if nodo_actual == None:
                raise ValueError("El valor no está en la lista")

            nodo_anterior.proximo = nodo_actual.proximo
        
        self.longitud -= 1
    
    def pop(self, i=None):
        if i is None:
            i = self.longitud - 1

        elif i < 0 or i > self.longitud:
            raise IndexError("Índice fuera de rango")

        elif i == 0:
            dato = self.primero.dato
            self.primero = self.primero.prox

        else:
            nodo_anterior = self.primero
            nodo_actual = nodo_anterior.proximo
            for posicion in range(1, i):
                nodo_anterior = self.primero
                nodo_actual = nodo_anterior.proximo

            dato = nodo_actual.dato
            nodo_anterior = nodo_actual.proximo
        
        self.longitud -= 1
        return dato
    
    def invertir(self):
        pila = Pila()
        actual = self.primero
        while actual:
            pila.apilar(actual)
            actual = actual.proximo
        anterior = pila.desapilar()
        self.primero = anterior
        while not pila.esta_vacia():
            siguiente = pila.desapilar()
            anterior.proximo = siguiente
            anterior = siguiente
        anterior.proximo = None
    
    def esta_vacia(self):
        return self.longitud == 0

    def map(self, funcion):
        actual = self.primero
        resultado = ListaEnlazada()
        ultimo_nodo = None
        while actual:
            dato = actual.dato
            nuevo_nodo = _Nodo(funcion(dato))
            if ultimo_nodo:
                ultimo_nodo.prox = nuevo_nodo
            else:
                resultado.primero = nuevo_nodo
            ultimo_nodo = nuevo_nodo
            actual = actual.proximo
        return resultado

    def __iter__(self):
        return _IteradorListaEnlazada(self.primero)
    
    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.proximo
        return " -> ".join(elementos)

class Pila:
    def __init__(self):
        self.pila = []
    
    def apilar(self, elemento):
        self.pila.append(elemento)
    
    def desapilar(self):
        if self.esta_vacia():
            raise ValueError("La pila está vacía")
        return self.pila.pop()
    
    def esta_vacia(self):
        return len(self.pila) == 0

    def ver_tope(self):
        return self.pila[-1]

    def __str__(self):
        elementos = []
        for elemento in self.pila:
            elementos.append(str(elemento))
        return "|| " + ", ".join(elementos) + " >"

class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, elemento):
        self.items.append(elemento)
    
    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        return self.items.pop(0)
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def __str__(self):
        elementos = []
        for elemento in self.items:
            elementos.append(str(elemento))
        return "< " + ", ".join(elementos) + " >"

class ColaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def encolar(self, elemento):
        nuevo = _Nodo(elemento)
        if self.ultimo:
            self.ultimo.proximo = nuevo
            self.ultimo = nuevo
        else:
            self.primero = nuevo
            self.ultimo = nuevo
    
    def desencolar(self):
        if self.primero is None:
            raise ValueError("La cola está vacía")
        valor = self.primero.dato
        self.primero = self.primero.proximo
        if not self.primero:
            self.ultimo = None
        return valor
    
    def esta_vacia(self):
        return self.primero is None

