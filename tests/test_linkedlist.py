import unittest
from retos.reto3_linkedlist import add_task, find_by_id, find_by_priority

class TestChallenge3LinkedList(unittest.TestCase):
    def test_add_and_find_by_id(self):
        add_task(1, "Probar DLL", 2)
        tarea = find_by_id(1)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea.id, 1)
        self.assertEqual(tarea.descripcion, "Probar DLL")
        self.assertEqual(tarea.prioridad, 2)

    # TODO: agrega más casos:
    # - eliminar por id (cuando implementes remove)
    # - find_by_priority devuelve múltiples tareas
    def test_find_by_priority(self):
        tarea = find_by_priority(2)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea[0].prioridad, 2)
        
    # - find_by_id inexistente -> None
    def test_find_by_id_inexistente(self):
        tarea = find_by_id(5)
        self.assertIsNone(tarea)

if __name__ == "__main__":
    unittest.main()
