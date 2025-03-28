from Examen_Parcial_1.Equipo import Equipo


class Torneo:
    def __init__(self, nombre:str, *equipos:tuple[Equipo]):
        self._nombre = nombre
        self._equipos = list[Equipo]

    def agregar_equipos(self, *equipos:tuple[Equipo])->None:
        pass

    def remover_equipos(self, *jugadores:tuple[Equipo])->None:
        pass

    def mostrar_equipos(self)->None:
        pass

    def generar_rol(self)->None:
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    pass