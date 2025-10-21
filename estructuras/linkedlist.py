"""
Lista doblemente enlazada (DLL) para gestionar tareas.

TODO:
- Implementa DoubleNode (id, descripcion, prioridad, prev, next)
- Implementa DoublyLinkedList con: append, prepend, remove_by_id, find_by_id, find_by_prioridad, iter_forward, iter_backward, size
- Mantén head, tail y contador para O(1) en inserciones a extremos.

Nota:
- 'find' será O(n) lineal.
"""

class DoubleNode:
    # TODO: implementar nodo doble para tareas
    def __init__ (self, id: int, descripcion: str, prioridad: int, prev: None, next: None) :
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    # TODO: implementar DLL
    def __init__ (self) :
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, task):
        """Inserta al final. O(1)"""
        tarea = DoubleNode(task["id"], task["descripcion"], task["prioridad"], None, None)
        
        if (self.size == 0) :
            tarea.next = None
            self.head = tarea
            self.tail = tarea
            self.size += 1
        else :
            tarea.prev = self.tail
            self.tail.next = tarea
            self.tail = tarea
            self.size += 1
      
    def prepend(self, task):
        """Inserta al inicio. O(1)"""

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""

    def find_by_id(self, task_id):
        """Retorna la tarea o None. O(n)"""
        nodo_base = self.head
        while nodo_base is not None:
            if nodo_base.id == task_id:
                return nodo_base
            else :
                nodo_base = nodo_base.next
        return None

    def find_by_prioridad(self, prioridad):
        """Retorna lista de tareas con esa prioridad. O(n)"""
        nodo_base = self.head
        lista_tareas = []
        while nodo_base is not None:
            if nodo_base.prioridad == prioridad:
                lista_tareas.append(nodo_base)
            nodo_base = nodo_base.next
        return lista_tareas
    
    def iter_forward(self):
        """Generador hacia adelante."""


    def iter_backward(self):
        """Generador hacia atrás."""

    def size(self):
        return self.size
