
class Persona:
    def __init__(self,nombre:str,edad:int,altura:float,peso:float):
        #atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    #Métodos
    def caminar(self)->None:
        print(f"{self.nombre} está caminando para bajar sus {self.peso} kgs.")

    def comer(self)->None:
        print(f"{self.nombre} está comiendo en el comedor.")

    def jugar(self)->None:
        print(f"{self.nombre} está juando COD.")

    def dormir(self)->None:
        print(f"{self.nombre} está durmiendo placidamente.")

if __name__ == '__main__':
    alberto = Persona("Alberto Ramírez", 20, 1.67, 160)
    addi = Persona("Addi Toro", 19, 1.70, 70)
    #acceder a las caracterísicas
    print(alberto.nombre)
    print(alberto.edad)
    print(alberto.altura)
    print(alberto.peso)
    #acceder a los metodos
    print()
    alberto.caminar()
    alberto.comer()
    alberto.jugar()
    alberto.dormir()
    print()
    addi.caminar()
    addi.comer()
    addi.jugar()
    addi.dormir()
    print()
    alberto.peso = 65
    alberto.edad = 19
    alberto.caminar()
    print(alberto.nombre)