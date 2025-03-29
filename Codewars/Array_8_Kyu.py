"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 19 de marzo de 2025
Descripción:
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
a can contain numbers or strings. x can be either.
Return true if the array contains the value, false if not.
"""
def check(seq, elem)->bool:
    """
    Función que devuelve verdadero si un número o str se encunetra en una cadena, o falso en caso contrario.
    :param seq: Lista de números o cadenas.
    :param elem: Elemento a buscar en la lista.
    :return: Verdadero o Falso.
    """
    respuesta = True
    for x in seq:
        if x == elem:
            return True
        else:
            respuesta = False
    return respuesta


if __name__ == '__main__':
    print(check([66, 101], 66))
    print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))
    print(check([101, 45, 75, 105, 99, 107], 107))
    print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))
    print(check(['t', 'e', 's', 't'], 'e'))
    print(check(["what", "a", "great", "kata"], "kat"))
    print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups"))
    print(check(["come", "on", 110, "2500", 10, '!', 7, 15], "Come"))
    print(check(["when's", "the", "next", "Katathon?", 9, 7], "Katathon?"))
    print(check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45))
    print(check(["anyone", "want", "to", "hire", "me?"], "me?"))