"""
Queue (Cola) implementada con lista doblemente enlazada.

TODO:
- Implementa DoubleNode (value, prev, next)
- Implementa Queue con operaciones: enqueue, dequeue, peek, is_empty, size
- Enqueue al final (tail) y dequeue al inicio (head) para O(1)

Sugerencia:
- Mantén punteros a head y tail, más un contador.
"""

class DoubleNode:
    # TODO: implementar nodo doble
    def __init__(self, nombre: str, tiempo: int, prev: None, next: None) :
        self.value = (nombre, tiempo)
        self.prev = prev
        self.next = next

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # TODO: implementar cola enlazada doble
    def enqueue(self, value):
        """Inserta al final. O(1)"""
        nodo = DoubleNode(value[0], value[1], None, None)

        if self.size == 0 :
            self.head = nodo
            self.tail = nodo
        else :
            nodo.prev = self.tail
            self.tail.next = nodo
            self.tail = nodo

        self.size += 1

    def dequeue(self):
        """Extrae el primero. O(1). Debe lanzar IndexError si está vacía."""
        if self.size == 0 :
            raise IndexError
        else :
            nombre, tiempo = self.head.value
            tupla = (nombre, tiempo)

            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            
            self.size -= 1
            return tupla

    def peek(self):
        """Retorna el primero sin extraer. O(1). IndexError si vacía."""
        if self.is_empty :
            return IndexError
        else :
            valor = self.head.value
            return valor

    def is_empty(self):
        """True si la cola está vacía. O(1)"""
        return self.size == 0

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self.size

