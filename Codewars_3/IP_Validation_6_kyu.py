"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 6 de junio de 2025
Descripción:
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
"""


def is_valid_IP(strng):
    partes = strng.split('.')

    if len(partes) != 4:
        return False

    for num in partes:
        if not num.isdigit():
            return False

        if len(num) > 1 and num[0] == '0':
            return False  # cero a la izquierda

        num = int(num)
        if num < 0 or num > 255:
            return False

    return True