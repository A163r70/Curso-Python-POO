"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Write a function that returns a sequence (index begins with 1) of all the even characters from a string.
If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".
"""

def even_chars(st):
    """
    Función que recibe una cadena y devuelve todos los caracteres pares expecto si la cadena es menor
    de dos caracteres o mayo a 100.
    :param st: Cadena que se recibe
    :return: Cadena de solo caracteres pares.
    """
    new_st = []
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    else:
        for i in range(len(st)):
            if i % 2 == 1:
                new_st.append(st[i])
    return new_st

if __name__ == '__main__':
    print(even_chars("a"))
    print(even_chars("abcdefghijklm"))
    print(even_chars("aBc_e9g*i-k$m"))