'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 10 de enero de 2025
Descripción: Clases.
'''
class Estudiante:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_tema(self,tema:str)->None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

    def __str__(self)->str:
        return f"Estudiante(nombre: {self.nombre}, temas_aprendidos:{self.temas_aprendidos})"

class Profesor:
    def __init__(self, nombre:str, temas_dominados:list[str]):
        self.nombre = nombre
        self.temas_dominados = temas_dominados

    def dominar_tema(self,tema:str):
        self.temas_dominados.append(tema)
        print(f"{self.nombre} domina el tema {tema}")

    def ensenar_tema(self,no_tema: int)->str:
        if no_tema < len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango."

    def __str__(self)->str:
        return f"Profesor(nombre: {self.nombre}, temas_enseñar:{self.temas_dominados})"

if __name__ == '__main__':
    alberto = Estudiante("Alberto")
    addi = Estudiante("Addi")
    alberto.aprender_tema("Evolución sitio web")
    addi.aprender_tema("I o T")
    print(alberto)
    print(addi)
    profesor = Profesor("Héctor", ["Programación", "Álgebra", "Diseño Web"])
    tema = profesor.ensenar_tema(2)
    print(tema)
    #el profesor le enseña al alumno
    #1ra forma
    tema1 = profesor.ensenar_tema(1)
    alberto.aprender_tema(tema1)
    addi.aprender_tema(tema1)
    #sgunda forma, enseñar el tema 2 al estudiante 2
    addi.aprender_tema(profesor.ensenar_tema(2))
    print(alberto)
    print(addi)