"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!
"""

def better_than_average(class_points, your_points)->bool:
    """
    Función que calcula si el estudiante es mejor que el promedio de su clase, calculando la media y comparando
    el resultado con su resultado.
    :param class_points: Lista con los puntos de la clase.
    :param your_points: Puntos del estudiante.
    :return: True si es mejor que el promedio de la clase, False si no.
    """
    media = sum(class_points)/len(class_points)
    if media < your_points:
        return True
    else:
        return False

if __name__ == '__main__':
    print(better_than_average([2, 3], 5))
    print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
    print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
    print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))
    print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21))
    print(better_than_average([100, 90, 80], 85))
    print(better_than_average([50, 50, 50], 50))