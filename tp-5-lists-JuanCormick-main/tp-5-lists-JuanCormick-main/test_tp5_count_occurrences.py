import unittest
import exercise_count_occurrences as ex


class TestCountOccurrences(unittest.TestCase):

    def test_elemento_presente_una_vez(self):
        """Test elemento presente una vez"""
        result = ex.count_occurrences([1, 2, 3, 4, 5], 3)
        self.assertEqual(1, result)

    def test_elemento_presente_varias_veces(self):
        """Test elemento presente múltiples veces"""
        result = ex.count_occurrences([1, 2, 2, 3, 2, 4], 2)
        self.assertEqual(3, result)

    def test_elemento_no_presente(self):
        """Test elemento no presente"""
        result = ex.count_occurrences([1, 2, 3, 4, 5], 10)
        self.assertEqual(0, result)

    def test_lista_vacia(self):
        """Test con lista vacía"""
        result = ex.count_occurrences([], 5)
        self.assertEqual(0, result)

    def test_todos_iguales(self):
        """Test donde todos los elementos son el buscado"""
        result = ex.count_occurrences([7, 7, 7, 7], 7)
        self.assertEqual(4, result)

    def test_strings(self):
        """Test con lista de strings"""
        result = ex.count_occurrences(['red', 'blue', 'red', 'green', 'red'], 'red')
        self.assertEqual(3, result)

    def test_elemento_cero(self):
        """Test buscando el número cero"""
        result = ex.count_occurrences([0, 1, 0, 2, 0], 0)
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()
