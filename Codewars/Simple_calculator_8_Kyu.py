"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 19 de marzo de 2025
Descripción:
You are required to create a simple calculator that returns the result of addition, subtraction,
multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the list above a message "unknown value"
must be returned.
"""
def calculator(x, y, op)->float | str:
    """
    Función que realiza una operación matemática con dos números, dependiendo de la operación que se ingrese.
    :param x: Primer número.
    :param y: Segundo número.
    :param op: Operación que se realizará.
    :return: El resultado de la operación o un mensaje de error.
    """
    x = cadena_a_flotante(str(x))
    y = cadena_a_flotante(str(y))
    while x is None or y is None:
        return "unknown value"
    if op == "+":
        return  x + y
    elif op == "-":
        return  x - y
    elif op == "*":
        return  x * y
    elif op == "/":
        if y == 0:
            return "unknown value"
        return x / y
    else:
        return "unknown value"


def cadena_a_flotante(cadena: str) -> float | None:
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena a convertir.
    :return: El número flotante o nada.
    """
    if cadena.count(".") > 1 or cadena.count("-") > 1 or (cadena.startswith("-") and "-" in cadena[1:]):
        return None

    if cadena.replace(".", "", 1).replace("-", "", 1).isdigit():
        return float(cadena)

    return None

if __name__ == '__main__':
    print(calculator(6, 2, '+'))
    print(calculator(4, 3, '-'))
    print(calculator(5, 5, '*'))
    print(calculator(5, 4, '/'))
    print(calculator(6, 2, '&'))
    print(calculator(6, "2", '&'))