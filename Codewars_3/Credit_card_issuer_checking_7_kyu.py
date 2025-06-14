"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 6 de junio de 2025
Descripción:
Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given
card number. If the number cannot be matched then the function should return the string Unknown.
"""
def get_issuer(card_number):
    card_number = str(card_number)
    length = len(card_number)
    first_digit = card_number[0]
    first_two = card_number[:2]
    first_four = card_number[:4]

    if length == 15 and (first_two == '34' or first_two == '37'):
        return "AMEX"
    elif length == 16 and first_four == '6011':
        return "Discover"
    elif length == 16 and first_two in ['51', '52', '53', '54', '55']:
        return "Mastercard"
    elif (length == 13 or length == 16) and first_digit == '4':
        return "VISA"
    else:
        return "Unknown"


if __name__ == '__main__':
    ...