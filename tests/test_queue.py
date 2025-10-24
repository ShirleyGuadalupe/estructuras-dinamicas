import unittest
from retos.reto2_queue import QueueManager

class TestChallenge2Queue(unittest.TestCase):
    def test_serve_in_fifo_order(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)

        nombre, tiempo = gestor.serve_person()
        self.assertEqual(nombre, "Ana")
        self.assertEqual(tiempo, 5)

    # TODO: agrega más casos:
    # - atender_persona en cola vacía -> IndexError
    def test_serve_in_empty_queue(self):
        gestor = QueueManager()
        with self.assertRaises(IndexError):
            gestor.serve_person()

    # - estado() refleja el orden actual
    def test_actual_state(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)

        self.assertEqual([("Ana"), ("Luis")], gestor.state())

    # - mezcla de agregar/atender repetidas veces
    def test_add_and_serve(self):
        gestor = QueueManager()
        gestor.add_person("Ruth", 4)
        gestor.add_person("Carlos", 3)
        gestor.add_person("Carlitos", 2)
        gestor.add_person("Lupe", 1)
        self.assertEqual([("Ruth"), ("Carlos"), ("Carlitos"), ("Lupe")], gestor.state())
        gestor.serve_person()  
        gestor.serve_person()  
        self.assertEqual([("Carlitos"), ("Lupe")], gestor.state())
        self.assertEqual(len(gestor.state()), 2)


if __name__ == "__main__":
    unittest.main()
