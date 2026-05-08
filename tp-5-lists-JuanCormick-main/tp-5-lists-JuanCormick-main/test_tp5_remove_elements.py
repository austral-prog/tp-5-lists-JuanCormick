import unittest
import exercise_remove_elements as ex


class TestRemoveElements(unittest.TestCase):

    def test_lista_seis_elementos(self):
        """Test remover de lista con 6 elementos"""
        lista = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        result = ex.remove_elements(lista)
        expected = ['Green', 'White', 'Black']
        self.assertEqual(expected, result)

    def test_lista_cuatro_elementos(self):
        """Test remover de lista con 4 elementos (menos que los índices a remover)"""
        lista = ['Audi', 'BMW', 'Porsche', 'Aston Martin']
        result = ex.remove_elements(lista)
        expected = ['BMW', 'Porsche', 'Aston Martin']
        self.assertEqual(expected, result)

    def test_lista_vacia(self):
        """Test con lista vacía"""
        lista = []
        result = ex.remove_elements(lista)
        expected = []
        self.assertEqual(expected, result)

    def test_lista_un_elemento(self):
        """Test con lista de un elemento"""
        lista = ['Solo']
        result = ex.remove_elements(lista)
        expected = []
        self.assertEqual(expected, result)

    def test_lista_grande(self):
        """Test con lista más grande"""
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = ex.remove_elements(lista)
        expected = [2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
