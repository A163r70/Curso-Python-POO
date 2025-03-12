'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 12 de marzo de 2025
Descripción: Clases.
'''

class Personaje:
    contador_id= 1
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.contador_id = Personaje.contador_id
        Personaje.contador_id += 1

    def moverse(self,ordenes:str)->None:
        pass

    def posicion_actual(self)->None:
        pass


    def __str__(self):
        return f"Personaje(id: {Personaje.contador_id}, x: {Personaje.x}, y: {Personaje.y})"
def solicitar_moviemiento(self):
    movimientos = []
    print("Se solicita iterativamente las secuencias de movimiento.")
    movimientos = input("Ingresa las órdenes de movimiento: ")
    print(movimientos)

if __name__ == '__main__':
    solicitar_movimientos()
