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
    def __init__ (self, id: int, descripcion: str, prioridad: int, prev: DoubleNode, next: DoubleNode) :
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    # TODO: implementar DLL
    def __init__ (self) :
        self.head = DoubleNode(None, None, None, None, None, None)
        self.tail = DoubleNode(None, None, None, None, None, None)
        self.size = 0
        
    def append(self, task):
        """Inserta al final. O(1)"""
        if (self.size == 0) :
            tarea = DoubleNode(task.id, task.descripcion, task.prioridad, None, task)
            self.head = tarea
            self.tail = tarea
            self.size += 1
        else :
            tarea = DoubleNode(task.id, task.descripcion, task.prioridad, self.tail, None)
            self.tail.next = task
            self.tail = tarea
            self.size += 1
      
    def prepend(self, task):
        """Inserta al inicio. O(1)"""
        raise NotImplementedError

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""
        raise NotImplementedError

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
        raise NotImplementedError

    def iter_forward(self):
        """Generador hacia adelante."""
        raise NotImplementedError

    def iter_backward(self):
        """Generador hacia atrás."""
        raise NotImplementedError

    def size(self):
        return self.size
