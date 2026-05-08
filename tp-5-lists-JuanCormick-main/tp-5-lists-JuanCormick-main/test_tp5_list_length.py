import unittest
import exercise_list_length as ex


class TestListLength(unittest.TestCase):

    def test_lista_vacia(self):
        """Test con lista vacía"""
        result = ex.list_length([])
        self.assertEqual(0, result)

    def test_lista_un_elemento(self):
        """Test con lista de un elemento"""
        result = ex.list_length([5])
        self.assertEqual(1, result)

    def test_lista_varios_elementos(self):
        """Test con lista de varios elementos"""
        result = ex.list_length([1, 2, 3, 4, 5])
        self.assertEqual(5, result)

    def test_lista_strings(self):
        """Test con lista de strings"""
        result = ex.list_length(['Red', 'Green', 'Blue'])
        self.assertEqual(3, result)

    def test_lista_mixta(self):
        """Test con lista de tipos mixtos"""
        result = ex.list_length([1, 'hello', 3.14, True, None])
        self.assertEqual(5, result)


if __name__ == '__main__':
    unittest.main()
