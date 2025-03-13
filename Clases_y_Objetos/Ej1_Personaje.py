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
        for i in ordenes:
            if i == "a" and self.y < 10:
                self.y += 1
            elif i == "r" and self.y > 0:
                self.y -= 1
            elif i == "d" and self.x < 10:
                self.x += 1
            elif i == "i" and self.x > 0:
                self.x -= 1
            else:
                print("Error")


    def posicion_actual(self)->None:
        pass




    def __str__(self):
        return f"Personaje(id: {self.id}, x: {self.x}, y: {self.y}"

def solicitar_movimiento():
    salir = True
    print("Se solicita iterativamente las secuencias de movimiento.")
    while salir:
        movimientos = input("Ingresa las órdenes de movimiento o S para salir: ").lower()
        if movimientos == "s":
            break
        else:
            self.moverse(movimientos)




if __name__ == '__main__':
    personaje = Personaje()
    print(personaje)

    movimiento = solicitar_movimiento()
    while movimiento != "s":
        pass
