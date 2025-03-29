"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 17 de marzo de 2025
Descripción: Primer ejercicio de Codewars.
Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
For example:
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""

def litres(time:float)->int:
    """
    Función que calcula los litros de agua a aprtir del tiempo recorrido.
    :param time: Tiempo que ha corrido Nathan.
    :return: Los litros de agua que debe tomar.
    """
    litros = 0.5 * time
    return int(litros)

if __name__ == '__main__':
    print(litres(3))