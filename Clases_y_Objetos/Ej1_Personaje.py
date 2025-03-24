'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 12 de marzo de 2025
Descripción: Clases.
'''


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
        print(f"Posición actual: (x, y) = ({self.x}, {self.y})")




    def __str__(self):
        return f"Personaje(id: {self.id}, x: {self.x}, y: {self.y}"

def solicitar_movimiento():
    """
    Función que pide al usuario los movimientos del perosonaje.
    :return:
    """
    movimientos = input("Ingresa las órdenes de movimiento o S para salir: ").lower()
    while not movimientos.isalpha():
        movimientos = input("Intenta nuevamente: ").lower()
    return movimientos




if __name__ == '__main__':
    personaje = Personaje()
    print(personaje)

    print("-- Se solicita iterativamente las secuencias de movimiento. --")
    while True:
        movimiento = solicitar_movimiento()
        if movimiento != "s":
            personaje.moverse(movimiento)
            personaje.posicion_actual()
        else:
            personaje.posicion_actual()
            break

