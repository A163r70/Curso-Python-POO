"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.
"""

def distinct(seq):
    """
    Función que remueve números repetidos de una lista, manteniendo el orden que tiene.
    :param seq: Lista de números.
    :return: Lista sin números repetidos.
    """
    new_seq = []
    for i in seq:
        if i not in new_seq:
            new_seq.append(i)
    return new_seq

if __name__ == '__main__':
    print(distinct([1]))
    print(distinct([1, 2]))
    print(distinct([1, 1, 2]))
    print(distinct([1, 1, 1, 2, 3, 4, 5]))
    print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))