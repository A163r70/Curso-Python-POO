from Examen_Parcial_1.Jugador import Jugador


class Equipo:
    id = 1
    def __init__(self, nombre:str, *jugadores:tuple[Jugador]):
        self._nombre = nombre
        self._jugadores = jugadores
        self._id_equipo = Equipo.id
        Equipo.id += 1

    @property
    def nombre(self)->str:
        return self._nombre
    @nombre.setter
    def nombre(self, name):
        self._nombre = name

    @property
    def jugadores(self)->tuple:
        return self._jugadores
    @jugadores.setter
    def jugadores(self, jugadores):
        self._jugadores

    def agregar_jugadores(self, *jugadores:tuple[Jugador])->None:
        pass

    def remover_jugadores(self, *jugadores:tuple[Jugador])->None:
        pass

    def mostrar_jugadores(self)->None:
        pass

    def total_goles(self)->int:
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    pass