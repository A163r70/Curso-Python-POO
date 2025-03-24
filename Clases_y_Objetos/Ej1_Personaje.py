"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 12 de marzo de 2025
Descripción:
Crea una clase llamada Personaje que simule los movimientos de un personaje de videojuegos en una ventana.

1.- El personaje se moverá por una ventana de tamaño máximo (x, y) = (10, 10)
y podrá realizar los siguientes movimientos si no supera el límite de la ventana:
      * Avanzar (caracteres 'A' o 'a'): aumenta en 1 la posición en y,
      * Retroceder (caracteres 'R' o 'r'): disminuye en 1 la posición en y,
      * Derecha (caracteres 'D' o 'd'): aumenta en 1 la posición en x,
      * Izquierda (caracteres 'I' o 'i'): disminuye en 1 la posición en x.

2.- El personaje tendrá los siguientes métodos (además de los métodos mágicos):
      * moverse() que recibe la orden como parámetro,
      * posicion_actual() que muestra en consola la posición en (x,y).

3.- Se debe llevar un registro del ID de los personajes creados, por lo que se debe utilizar un atributo de clase.

4.- Al crear los objetos de la clase, inicialmente deben establecerse en el origen (x, y) = (0, 0).

5.- Se debe solicitar iterativamente la secuencia de movimientos e indicar la posición final de la secuencia.

6.- El programa se detendrá con los caracteres 'S' o 's'.
"""


class Personaje:
    contador_id= 1
    def __init__(self):
        self.x = x=0
        self.y = y=0
        self.id = Personaje.contador_id
        Personaje.contador_id += 1

    def moverse(self,ordenes:str)->None:
        """
        Función que mueve al personaj en el taler 10 x 10
        :param ordenes:
        :return:
        """
        for i in ordenes:
            if i == "a" and self.y < 10:
                self.y += 1
            elif i == "r" and self.y > 0:
                self.y -= 1
            elif i == "d" and self.x < 10:
                self.x += 1
            elif i == "i" and self.x > 0:
                self.x -= 1


    def posicion_actual(self)->None:
        """
        Función que muestra la posicón actual del personaje.
        :return:
        """
        print()
        print(f"Posición actual: (x, y) = ({self.x}, {self.y})")
        print()

    def __str__(self):
        return f"Personaje(id: {self.id}, x: {self.x}, y: {self.y})"

def solicitar_movimiento():
    """
    Función que pide al usuario los movimientos del perosonaje.
    :return:
    """
    print("Avanzar (caracteres 'A' o 'a')")
    print("Retroceder (caracteres 'R' o 'r')")
    print("Derecha caracteres ('D' o 'd')")
    print("Izquierda caracteres ('I' o 'i')")
    print()
    movimientos = input("Ingresa las órdenes o S para salir: ").lower()
    while not movimientos.isalpha():
        movimientos = input("Intenta nuevamente: ").lower()
    return movimientos




if __name__ == '__main__':
    personaje = Personaje()
    print(personaje)

    print("-- Se solicita iterativamente las secuencias de movimiento. --")
    print()
    while True:
        movimiento = solicitar_movimiento()
        if movimiento != "s":
            personaje.moverse(movimiento)
            personaje.posicion_actual()
        else:
            personaje.posicion_actual()
            break