"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 6 de junio de 2025
Descripción:
"""
import math
def heron(a, b, c):
    s = (a+b+c)/2
    h = math.sqrt(s*(s-a)*(s-b)*(s-c))

    return h


if __name__ == '__main__':
    print(heron(3,4,5))
    print(heron(4,4,4))