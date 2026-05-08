import unittest
import exercise_list_of_lists as ex


class TestListOfLists(unittest.TestCase):

    def test_ejemplo_basico(self):
        """Test con el ejemplo básico de la consigna"""
        lista = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
        result = ex.list_of_lists(lista)
        expected = [[1, 2], [5, 6, 7], [11, 12]]
        self.assertEqual(expected, result)

    def test_primera_lista_vacia(self):
        """Test cuando la primera lista está vacía"""
        lista = [[], [4, 5, 6], [10, 11, 12]]
        result = ex.list_of_lists(lista)
        expected = [[], [5, 6], [11, 12]]
        self.assertEqual(expected, result)

    def test_segunda_lista_vacia(self):
        """Test cuando la segunda lista está vacía"""
        lista = [[1, 2], [], [12]]
        result = ex.list_of_lists(lista)
        expected = [[1, 2], [], [12]]
        self.assertEqual(expected, result)

    def test_tercera_lista_vacia(self):
        """Test cuando la tercera lista está vacía"""
        lista = [[1], [4], []]
        result = ex.list_of_lists(lista)
        expected = [[1], [], []]
        self.assertEqual(expected, result)

    def test_listas_exactas(self):
        """Test cuando las listas tienen exactamente el tamaño necesario"""
        lista = [[1, 2], [4, 5, 6, 7], [11, 12]]
        result = ex.list_of_lists(lista)
        expected = [[1, 2], [5, 6, 7], [11, 12]]
        self.assertEqual(expected, result)

    def test_primera_lista_un_elemento(self):
        """Test cuando la primera lista tiene solo un elemento"""
        lista = [[1], [4, 5, 6], [10, 11, 12]]
        result = ex.list_of_lists(lista)
        expected = [[1], [5, 6], [11, 12]]
        self.assertEqual(expected, result)

    def test_listas_strings(self):
        """Test con listas de strings"""
        lista = [['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i', 'j']]
        result = ex.list_of_lists(lista)
        expected = [['a', 'b'], ['e', 'f', 'g'], ['i', 'j']]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
