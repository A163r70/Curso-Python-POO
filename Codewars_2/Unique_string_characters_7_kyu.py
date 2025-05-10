"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
In this Kata, you will be given two strings a and b and your task will be to return the characters that
are not common in the two strings.
"""

def solve(a,b):
    """
    Función que recibe dos cadenas y concatena las letras que hay en la cadena a pero no en la b y también las letras
    que hay en la cadena b que no hay en la cadena b
    :param a: Cadena a
    :param b: Cadena b
    :return: Cadena con letras sin repetir.
    """
    differents = ''
    for letra in a:
        if letra not in b:
            differents += letra
    for letra in b:
        if letra not in a:
            differents += letra
    return str(differents)

if __name__ == '__main__':
    print(solve("xyab","xzca"))
    print(solve("xyabb","xzca"))
    print(solve("abcd","xyz"))
    print(solve("xxx","xzca"))