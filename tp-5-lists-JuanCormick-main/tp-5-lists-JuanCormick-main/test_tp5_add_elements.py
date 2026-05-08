import unittest
import exercise_add_elements as ex


class TestAddElements(unittest.TestCase):

    def test_lista_normal(self):
        """Test agregar elementos a lista normal"""
        lista = ['Red', 'Green', 'White', 'Black']
        result = ex.add_elements(lista)
        expected = ['Pink', 'Red', 'Green', 'White', 'Black', 'Yellow']
        self.assertEqual(expected, result)

    def test_lista_vacia(self):
        """Test agregar elementos a lista vacía"""
        lista = []
        result = ex.add_elements(lista)
        expected = ['Pink', 'Yellow']
        self.assertEqual(expected, result)

    def test_lista_numeros(self):
        """Test agregar elementos a lista de números"""
        lista = [0, 1, 2]
        result = ex.add_elements(lista)
        expected = ['Pink', 0, 1, 2, 'Yellow']
        self.assertEqual(expected, result)

    def test_lista_un_elemento(self):
        """Test agregar elementos a lista con un elemento"""
        lista = ['Middle']
        result = ex.add_elements(lista)
        expected = ['Pink', 'Middle', 'Yellow']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
