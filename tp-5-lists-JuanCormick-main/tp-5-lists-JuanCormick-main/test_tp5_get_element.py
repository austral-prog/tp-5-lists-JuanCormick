import unittest
import exercise_get_element as ex


class TestGetElement(unittest.TestCase):

    def test_primer_elemento(self):
        """Test obtener primer elemento"""
        result = ex.get_element([10, 20, 30], 0)
        self.assertEqual(10, result)

    def test_elemento_medio(self):
        """Test obtener elemento del medio"""
        result = ex.get_element(['a', 'b', 'c', 'd'], 2)
        self.assertEqual('c', result)

    def test_ultimo_elemento(self):
        """Test obtener último elemento"""
        result = ex.get_element([1, 2, 3, 4, 5], 4)
        self.assertEqual(5, result)

    def test_indice_negativo(self):
        """Test con índice negativo"""
        result = ex.get_element([1, 2, 3], -1)
        self.assertEqual(3, result)

    def test_indice_fuera_de_rango_positivo(self):
        """Test con índice fuera de rango (muy grande)"""
        result = ex.get_element([1, 2, 3], 10)
        self.assertIsNone(result)

    def test_indice_fuera_de_rango_negativo(self):
        """Test con índice negativo fuera de rango"""
        result = ex.get_element([1, 2, 3], -10)
        self.assertIsNone(result)

    def test_lista_vacia(self):
        """Test con lista vacía"""
        result = ex.get_element([], 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
