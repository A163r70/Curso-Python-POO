"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de marzo de 2025
Descripción:
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
"""
def find_average(numbers)->int:
    """
    Función que calcula y devuelve el promedio de una lista de números.
    :param numbers: Lista de números.
    :return: El promedio.
    """
    if [] == numbers:
        return 0
    else:
        return (sum(numbers)/len(numbers))

if __name__ == '__main__':
    print(find_average([1, 2, 3]))
    print(find_average([]))
    print(find_average([1, 2]))
    print(find_average([2, 8, 12, 47]))