"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
You will be given two inputs: a string of words and a letter. For each string, return the alphabetic
character after every instance of letter(case insensitive).

If there is a number, punctuation or underscore following the letter, it should not be returned.
"""

def comes_after(st, l):
    """
    Función que recibe una caden y un caracter, y devuelve los caracteres que hay después del caracter recibido dentro
    de la cadena.
    :param st: Cadena de caracteres.
    :param l: Caracter que se va a ocupar.
    :return: Caracteres después de l
    """
    after = ''
    l = l.lower()
    for i in range(len(st)-1):
        if st[i].lower() == l:
            siguiente = st[i+1]
            if siguiente.isalpha():
                after += siguiente
    return after

if __name__ == '__main__':
    print(comes_after("Pirates say arrrrrrrrr.", 'r'))
    print(comes_after("Free coffee for all office workers!", 'F'))
    print(comes_after("king kUnta is the sickest rap song ever kNown k!", 'k'))
    print(comes_after("p8tice makes pottery p0rfect!", 'p'))
    print(comes_after("d8u d._ rly 2d1s", 'D'))
    print(comes_after("nothing to be found here", 'z'))