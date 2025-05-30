"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""

def remove_exclamation_marks(s):
    """
    Función que remueve los signos de exclamación de una cadena.
    :param s: Cadena a la que se le eliminarán los signos de exclamación.
    :return: Cadena sin signos de exclamación.
    """
    list = ""
    for sign in s:
        if sign != '!':
            list += sign
    return list

if __name__ == '__main__':
    print(remove_exclamation_marks("Hello World!"))
    print(remove_exclamation_marks("Hello World!!!"))
    print(remove_exclamation_marks("Hi! Hello!"))
    print(remove_exclamation_marks(""))
    print(remove_exclamation_marks("Oh, no!!!"))