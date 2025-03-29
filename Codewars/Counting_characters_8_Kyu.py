"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de marzo de 2025
Descripción:
Define a method named countCharOccurrences or count_char_occurrences that accepts a string and a char as inputs
and returns the number of times the char occurs in the string as an int.
"""

def count_char_occurrences(strng, char)->int:
    """
    Función que cuneta el número de veces que aparece una letra en una cadena.
    :param strng: Cadena de letras.
    :param char: Letra a buscar en la cadena.
    :return: Número de veces que aparece la leta en la cadena.
    """
    cont = 0
    for i in strng:
        if i == char:
            cont += 1
    return cont

if __name__ == '__main__':
    print(count_char_occurrences("missippi", 'i'))
    print(count_char_occurrences("feed", 'e'))
    print(count_char_occurrences("aaaaaaaa", 'a'))
    print(count_char_occurrences("quicksilver", 'z'))