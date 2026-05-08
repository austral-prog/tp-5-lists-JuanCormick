import unittest
import exercise_is_empty as ex


class TestIsEmpty(unittest.TestCase):

    def test_lista_vacia(self):
        """Test con lista vacía"""
        result = ex.is_empty([])
        self.assertTrue(result)

    def test_lista_un_elemento(self):
        """Test con lista de un elemento"""
        result = ex.is_empty([1])
        self.assertFalse(result)

    def test_lista_varios_elementos(self):
        """Test con lista de varios elementos"""
        result = ex.is_empty(['Red', 'Green', 'White', 'Black'])
        self.assertFalse(result)

    def test_lista_con_cero(self):
        """Test con lista que contiene cero"""
        result = ex.is_empty([0])
        self.assertFalse(result)

    def test_lista_con_none(self):
        """Test con lista que contiene None"""
        result = ex.is_empty([None])
        self.assertFalse(result)

    def test_lista_con_string_vacio(self):
        """Test con lista que contiene string vacío"""
        result = ex.is_empty([''])
        self.assertFalse(result)

    def test_lista_con_lista_vacia(self):
        """Test con lista que contiene lista vacía"""
        result = ex.is_empty([[]])
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
