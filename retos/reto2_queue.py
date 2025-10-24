"""
Reto 2: Simulador de atención usando Queue (FIFO).

Clase a implementar:
    class QueueManager:
        - add_person(nombre: str, tiempo: int) -> None
        - serve_person() -> tuple[str, int]   # (nombre, tiempo)
        - state() -> list[str]                # nombres en orden FIFO

Reglas:
- 'agregar_persona' encola al final.
- 'atender_persona' desencola y retorna la tupla; si está vacía, lanza IndexError.
- 'estado' retorna los nombres en el orden actual sin mutar la cola.

Tips:
- Usa Queue de estructuras/queue.py
"""

from estructuras.queue import Queue

class QueueManager:

    def __init__ (self):
        self._cola = Queue()

    # TODO: implementar usando Queue internamente.
    def add_person(self, nombre: str, tiempo: int) -> None:
        person = (nombre, tiempo)
        self._cola.enqueue(person)

    def serve_person(self) -> tuple[str, int]:
        if self._cola.is_empty() :
            raise IndexError
        else :
            return self._cola.dequeue()
            
    def state(self) -> list[str]:
        list = []
        base = self._cola.head

        while base is not None :
            nombre, _ = base.value
            list.append(nombre)
            base =  base.next
        
        return list