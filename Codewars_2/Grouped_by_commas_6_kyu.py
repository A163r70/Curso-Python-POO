"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Finish the solution so that it takes an input n (integer) and returns a string that is the decimal
representation of the number grouped by commas after every 3 digits.
"""
def group_by_commas(n):
    """
    Función que recibe números y coloca una coma cada tres dígitos, devolviendo la cadena con las comas.
    :param n: Números a los que se les colocarán las comas.
    :return: La cadena de números con las comas en sus lugares correspondientes.
    """
    num_str = str(n)
    resultado = ''
    contador = 0

    for i in range(len(num_str) - 1, -1, -1):
        resultado = num_str[i] + resultado
        contador += 1
        if contador == 3 and i != 0:
            resultado = ',' + resultado
            contador = 0

    return resultado

if __name__ == '__main__':
    print(group_by_commas(1))
    print(group_by_commas(12))
    print(group_by_commas(123))
    print(group_by_commas(1234))
    print(group_by_commas(12345))
    print(group_by_commas(123456))
    print(group_by_commas(1234567))
    print(group_by_commas(12345678))
    print(group_by_commas(123456789))
    print(group_by_commas(1234567890))
    print(group_by_commas(2147483647))
    print(group_by_commas(0))