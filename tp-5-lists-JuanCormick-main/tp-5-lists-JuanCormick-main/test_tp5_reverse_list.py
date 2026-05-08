import unittest
import exercise_reverse_list as ex


class TestReverseList(unittest.TestCase):

    def test_lista_numeros(self):
        """Test invertir lista de números"""
        result = ex.reverse_list([1, 2, 3, 4, 5])
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(expected, result)

    def test_lista_strings(self):
        """Test invertir lista de strings"""
        result = ex.reverse_list(['a', 'b', 'c', 'd'])
        expected = ['d', 'c', 'b', 'a']
        self.assertEqual(expected, result)

    def test_lista_un_elemento(self):
        """Test invertir lista de un elemento"""
        result = ex.reverse_list([42])
        expected = [42]
        self.assertEqual(expected, result)

    def test_lista_dos_elementos(self):
        """Test invertir lista de dos elementos"""
        result = ex.reverse_list([1, 2])
        expected = [2, 1]
        self.assertEqual(expected, result)

    def test_lista_vacia(self):
        """Test invertir lista vacía"""
        result = ex.reverse_list([])
        expected = []
        self.assertEqual(expected, result)

    def test_lista_mixta(self):
        """Test invertir lista con tipos mixtos"""
        result = ex.reverse_list([1, 'hello', 3.14, True])
        expected = [True, 3.14, 'hello', 1]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
