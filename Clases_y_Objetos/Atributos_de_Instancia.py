
class Estudiante:
    def __init__(self,nombre):
        self.nombre = nombre
        self.temas_aprendidos = []

        def aprender_tema(tema:str)->None:
            self.temas_aprendidos.append(tema)
            print(f"{self.nombre} aprendió {tema}")

class Profesor:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.temas_dominados = []

        def dominar_tema(tema:str):
            self.temas_dominados.append(tema)
            print(f"{self.nombre} domina el tema {tema}")

        def ensenar_tema(no_tema: int)->str:
            tema_ensenar = self.temas_dominados[no_tema]
            return tema_ensenar