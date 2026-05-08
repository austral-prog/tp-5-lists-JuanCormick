import unittest
import exercise_check_lists as ex


class TestCheckLists(unittest.TestCase):

    def test_mismo_tercer_elemento(self):
        """Test cuando ambas listas tienen el mismo tercer elemento"""
        lista1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
        lista2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
        result = ex.check_lists(lista1, lista2)
        self.assertTrue(result)

    def test_diferente_tercer_elemento(self):
        """Test cuando las listas tienen diferente tercer elemento"""
        lista1 = ['Black', 'Pink', 'Green', 'White']
        lista2 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
        result = ex.check_lists(lista1, lista2)
        self.assertFalse(result)

    def test_primera_lista_corta(self):
        """Test cuando la primera lista no tiene tercer elemento"""
        lista1 = ['Black', 'Pink']
        lista2 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
        result = ex.check_lists(lista1, lista2)
        self.assertFalse(result)

    def test_segunda_lista_corta(self):
        """Test cuando la segunda lista no tiene tercer elemento"""
        lista1 = ['Black', 'Pink', 'Green', 'White']
        lista2 = ['Red']
        result = ex.check_lists(lista1, lista2)
        self.assertFalse(result)

    def test_ambas_listas_cortas(self):
        """Test cuando ambas listas no tienen tercer elemento"""
        lista1 = ['Black']
        lista2 = ['Red', 'Green']
        result = ex.check_lists(lista1, lista2)
        self.assertFalse(result)

    def test_listas_vacias(self):
        """Test con ambas listas vacías"""
        result = ex.check_lists([], [])
        self.assertFalse(result)

    def test_mismo_tercer_elemento_numeros(self):
        """Test con listas de números"""
        lista1 = [1, 2, 10, 4]
        lista2 = [5, 6, 10, 8]
        result = ex.check_lists(lista1, lista2)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
