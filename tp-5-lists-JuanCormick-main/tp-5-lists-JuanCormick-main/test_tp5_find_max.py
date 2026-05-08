import unittest
import exercise_find_max as ex


class TestFindMax(unittest.TestCase):

    def test_lista_positivos(self):
        """Test con lista de números positivos"""
        result = ex.find_max([3, 7, 2, 9, 1])
        self.assertEqual(9, result)

    def test_lista_negativos(self):
        """Test con lista de números negativos"""
        result = ex.find_max([-5, -2, -8, -1, -10])
        self.assertEqual(-1, result)

    def test_lista_mixta(self):
        """Test con lista de números positivos y negativos"""
        result = ex.find_max([-5, 10, -3, 25, 0])
        self.assertEqual(25, result)

    def test_lista_un_elemento(self):
        """Test con lista de un elemento"""
        result = ex.find_max([42])
        self.assertEqual(42, result)

    def test_lista_todos_iguales(self):
        """Test con lista donde todos los elementos son iguales"""
        result = ex.find_max([5, 5, 5, 5])
        self.assertEqual(5, result)

    def test_lista_vacia(self):
        """Test con lista vacía"""
        result = ex.find_max([])
        self.assertIsNone(result)

    def test_lista_decimales(self):
        """Test con lista de decimales"""
        result = ex.find_max([3.14, 2.71, 9.99, 1.41])
        self.assertEqual(9.99, result)


if __name__ == '__main__':
    unittest.main()
