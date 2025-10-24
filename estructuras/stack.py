"""
Stack (Pila) implementado con lista enlazada simple.

TODO:
- Implementa Node (valor, next)
- Implementa Stack con operaciones: push, pop, peek, is_empty, size
- Garantiza que push y pop sean O(1)

Sugerencia:
- Mantén referencia a la "cabeza" (top) y un contador de tamaño.
"""

class Node:
    # TODO: implementar nodo simple
    def __init__ (self, valor: str, next: None):
        self.valor = valor
        self.next = next

class Stack:
    # TODO: implementar pila enlazada
    def __init__(self) :
        self.top = None
        self.size = 0

    def push(self, value):
        """Inserta en el tope. O(1)"""
        tope = Node(value, self.top)
        self.top = tope
        self.size += 1

    def pop(self):
        """Extrae y retorna el tope. O(1). Debe lanzar IndexError si está vacía."""
        if self.size == 0:
            return IndexError
        else :
            tope = self.top
            self.top = tope.next
            self.size -= 1
            return tope.valor

    def peek(self):
        """Retorna el tope sin extraer. O(1). IndexError si vacía."""
        if self.size == 0:
            return IndexError
        else :
            return self.top

    def is_empty(self):
        """True si no hay elementos. O(1)"""
        return self.size == 0

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self.size
