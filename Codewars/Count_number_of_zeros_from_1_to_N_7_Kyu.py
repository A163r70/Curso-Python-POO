"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de marzo de 2025
Descripción:
Create an algorithm to count the number of zeros that appear between 1 and N.
"""
def count_zeros(x)->int:
    """
    Función que calcula el número de ceros del 1 hasta x.
    :param x: Número final.
    :return: Cantidad de ceros encontrados.
    """
    contador = 0
    for i in range(1,x+1):
            contador += str(i).count("0")
    return contador

if __name__ == '__main__':
    print(count_zeros(10))
    print(count_zeros(20))
    print(count_zeros(100))
    print(count_zeros(200))