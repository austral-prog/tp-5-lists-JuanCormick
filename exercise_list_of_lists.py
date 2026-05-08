# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas

    Returns:
        La lista de listas modificada según las reglas
    """
    lista_de_listas[0]=lista_de_listas[0][0:2]
    lista_de_listas[1]=lista_de_listas[1] [1:4]
    lista_de_listas[2]= lista_de_listas[2] [-2:]
    return lista_de_listas
