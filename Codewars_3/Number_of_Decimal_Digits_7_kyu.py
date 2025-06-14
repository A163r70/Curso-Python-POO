"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 6 de junio de 2025
Descripción:
Determine the total number of digits in the integer (n>=0) given as input to the function.
For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

All inputs will be valid.
"""
def digits(n):
    n_lista = str(n)
    c = 0
    for i in n_lista:
        c += 1
    return c

if __name__ == '__main__':
    print(digits(5))
    print(digits(12345))
    print(digits(9876543210))