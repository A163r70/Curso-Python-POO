"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
This method, which is supposed to return the result of dividing its first
argument by its second, isn't always returning correct values. Fix it.
"""

def divide_numbers(x,y)->float:
    """
    Función que devuleve el resultado correcto de la división del primer número con el segundo.
    :param x: Primer número.
    :param y: Segundo número.
    :return: Resultado de la división.
    """
    return x / y

if __name__ == '__main__':
    print(divide_numbers(1, 100))