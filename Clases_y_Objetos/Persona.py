
class Persona:
    def __init__(self,nombre:str,edad:int,altura:float,peso:float):
        #atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def caminar(self)->None:
        print("Estoy caminando")

    def comer(self)->None:
        print("Estoy comiendo")

    def jugar(self)->None:
        print("Estoy jugando")

    def dormir(self)->None:
        print("Estoy durmiendo")

if __name__ == '__main__':
    alberto = Persona("Alberto Ramírez", 20, 1.67, 160)
    #acceder a las caracterísicas
    print(alberto.nombre)
    print(alberto.edad)
    print(alberto.altura)
    print(alberto.peso)
    #acceder a los metodos
    alberto.caminar()