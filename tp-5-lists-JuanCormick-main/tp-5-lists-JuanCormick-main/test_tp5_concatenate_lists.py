import unittest
import exercise_concatenate_lists as ex


class TestConcatenateLists(unittest.TestCase):

    def test_dos_listas_normales(self):
        """Test concatenar dos listas normales"""
        result = ex.concatenate_lists([1, 2, 3], [4, 5, 6])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected, result)

    def test_primera_lista_vacia(self):
        """Test con primera lista vacía"""
        result = ex.concatenate_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(expected, result)

    def test_segunda_lista_vacia(self):
        """Test con segunda lista vacía"""
        result = ex.concatenate_lists([1, 2, 3], [])
        expected = [1, 2, 3]
        self.assertEqual(expected, result)

    def test_ambas_listas_vacias(self):
        """Test con ambas listas vacías"""
        result = ex.concatenate_lists([], [])
        expected = []
        self.assertEqual(expected, result)

    def test_listas_diferentes_tipos(self):
        """Test concatenar listas de diferentes tipos"""
        result = ex.concatenate_lists([1, 2], ['a', 'b'])
        expected = [1, 2, 'a', 'b']
        self.assertEqual(expected, result)

    def test_listas_strings(self):
        """Test concatenar listas de strings"""
        result = ex.concatenate_lists(['Hello', 'World'], ['Python', 'Rocks'])
        expected = ['Hello', 'World', 'Python', 'Rocks']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
