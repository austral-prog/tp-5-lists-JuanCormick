# Ejercicio 3: Agregar elementos al principio y final

def add_elements(lista):
    """
    Agrega 'Pink' al principio y 'Yellow' al final de la lista.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista modificada con los elementos agregados
    """
    lista.insert(0,'Pink')
    lista.append('Yellow')
    return lista

