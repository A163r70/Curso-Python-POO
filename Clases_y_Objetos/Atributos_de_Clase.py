'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de marzo de 2025
Descripción: Atributos de clase.
'''

class Empleado:
    #__no_id__:int atributo d clase
    no_id = 1
    def __init__(self, nombre:str,sueldo:float):
        self.nombre = nombre
        self.sueldo = sueldo
        self.id = Empleado.no_id
        Empleado.no_id +=1 #generaor de id automaico, o contador

    def aumentar_sueldo(self,porcentaje:float)->None:
        pass

    def __str__(self)->str:
        return f"Empleado( id= {self.id}, nombre= {self.nombre}, suelo= {self.sueldo})"

if __name__ == '__main__':
    empleado1 = Empleado("Addi", 150)
    empleado2 = Empleado("Héctor", 150)
