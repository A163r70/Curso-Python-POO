"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de marzo de 2025
Descripción:
Write a function that accepts a non-negative integer n and a string s as parameters,
and returns a string of s repeated exactly n times.

6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""
def repeat_str(repeat, string)->str:
    """
    Función que regresa una cadena con las veces que el usuario quiere que se repita una letra o cadena.
    :param repeat: Número de veces que se va a repetir.
    :param string: Cadena que se va a repetir.
    :return: Cadena repetida.
    """
    if repeat == 0 or string == "":
        return ""
    else:
        return repeat*string

if __name__ == '__main__':
    print(repeat_str(4, 'a'))
    print(repeat_str(3, 'hello '))
    print(repeat_str(2, 'abc'))
    print(repeat_str(0, ''))
    print(repeat_str(0, 'I'))
    print(repeat_str(5, ''))
    print(repeat_str(6, 'I'))
