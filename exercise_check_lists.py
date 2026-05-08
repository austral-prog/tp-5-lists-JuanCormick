# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2):
    """
    Verifica si ambas listas tienen el mismo elemento en la tercera posición.
    Si alguna de las listas no tiene un tercer elemento, retorna False.

    Args:
        lista1: Primera lista
        lista2: Segunda lista

    Returns:
        True si ambas listas tienen el mismo tercer elemento, False en caso contrario
    """
    len1=len(lista1)
    len2=len(lista2)
    if len1>=3 and len2>=3:
        if lista1[2]==lista2[2]:
            return True
    else:
        return False


