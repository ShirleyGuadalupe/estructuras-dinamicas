import unittest
from retos.reto3_linkedlist import add_task, find_by_id, find_by_priority, add_task_prepend, remove, print_backward, print_forward, get_size

class TestChallenge3LinkedList(unittest.TestCase):
    def test_add_and_find_by_id(self):
        add_task(1, "Probar DLL", 2)
        tarea = find_by_id(1)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea.id, 1)
        self.assertEqual(tarea.descripcion, "Probar DLL")
        self.assertEqual(tarea.prioridad, 2)

    def test_add_preppend_and_find_by_id(self):
        add_task_prepend(2, "Probar Prepend", 2)
        tarea = find_by_id(2)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea.id, 2)
        self.assertEqual(tarea.descripcion, "Probar Prepend")
        self.assertEqual(tarea.prioridad, 2)

    # TODO: agrega más casos:
    # - find_by_priority devuelve múltiples tareas
    def test_find_by_priority(self):
        tareas = find_by_priority(2)
        self.assertIsNotNone(tareas)
        if tareas :
            for tarea in tareas :
                self.assertEqual(tarea.prioridad, 2)

     # - find_by_id inexistente -> None
    def test_find_by_id_inexistente(self):
        tarea = find_by_id(5)
        self.assertIsNone(tarea)

    def test_imprimir_adelante(self):
        list = print_forward()
        print(list)
        self.assertEqual(get_size(), 2)

    def test_imprimir_atras(self):
        list = print_backward() 
        print(list)
        self.assertEqual(get_size(), 2)

    # - eliminar por id 
    def test_remove_by_id(self):
        remover1 = remove(2)
        remover2 = remove(1)
        self.assertTrue(remover1)
        self.assertTrue(remover2)
        self.assertEqual(get_size(), 0)
   
if __name__ == "__main__":
    unittest.main()
