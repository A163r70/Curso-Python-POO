"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Now you have to write a function that takes an argument and returns the square of it.
"""

def square(n)->int:
    """
    Función que calcula el cuadrado de un número dado.
    :param n: Número al que se le va a calcular el cuadrado.
    :return: El cuadrado del número n.
    """
    return n**2

if __name__ == '__main__':
    print(square(2))
    print(square(50))
    print(square(1))