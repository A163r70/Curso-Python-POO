"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Write a function that checks whether a credit card number is correct or not, using the Luhn algorithm.
"""

def valid_card(card)->bool:
    """
    Función que revisa si una tarjeta de crédito es válida o no
    :param card: Números de la tarjeta a revisar.
    :return: True si es válida y False en caso contrario.
    """
    total = 0
    tarjeta = card.replace(" ",'')
    lista = []
    for i in tarjeta:
        numero = int(i)
        lista.append(numero)

    longitud = len(lista)

    for i in range(longitud):
        digitos = lista[longitud-1-i]
        if i % 2 == 1:
            digitos *= 2
            if digitos > 9:
                digitos -= 9
        total += digitos
    if total % 10 == 0:
        return True

    return False

if __name__ == '__main__':
    print(valid_card("5457 6238 9823 4311"))
    print(valid_card("8895 6238 9323 4311"))
    print(valid_card("5457 6238 5568 4311"))
    print(valid_card("5457 6238 9323 4311"))
    print(valid_card("2222 2222 2222 2224"))
    print(valid_card("5457 1125 9323 4311"))
    print(valid_card("1252 6238 9323 4311"))
    print(valid_card("9999 9999 9999 9995"))
    print(valid_card("0000 0300 0000 0000"))
    print(valid_card("4444 4444 4444 4448"))
    print(valid_card("5457 6238 9323 1252"))
    print(valid_card("5457 6238 1251 4311"))
    print(valid_card("3333 3333 3333 3331"))
    print(valid_card("6666 6666 6666 6664"))
    print(valid_card("5457 6238 0254 4311"))
    print(valid_card("0000 0000 0000 0000"))
    print(valid_card("5457 1111 9323 4311"))
    print(valid_card("5457 6238 9823 4311"))
    print(valid_card("1145 6238 9323 4311"))
    print(valid_card("8888 8888 8888 8888"))
    print(valid_card("0025 2521 9323 4311"))
    print(valid_card("5457 6238 9323 4311"))
    print(valid_card("1111 1111 1111 1117"))
    print(valid_card("1234 5678 9012 3452"))
    print(valid_card("5458 4444 9323 4311"))
    print(valid_card("5457 6238 3333 4311"))
    print(valid_card("0123 4567 8901 2345"))
    print(valid_card("5555 5555 5555 5557"))