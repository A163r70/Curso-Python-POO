"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 6 de junio de 2025
Descripción:
Triangular numbers are so called because of the equilateral triangular shape that they occupy when
laid out as dots. i.e.
You need to return the nth triangular number. You should return 0 for out of range values.
"""
def triangular(n):
    if n <= 0:
        return 0
    return n * (n + 1) // 2  # Usamos división entera

if __name__ == '__main__':
    print(triangular(0))
    print(triangular(2))
    print(triangular(3))
    print(triangular(4))
    print(triangular(9))