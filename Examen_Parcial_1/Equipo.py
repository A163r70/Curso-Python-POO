from Examen_Parcial_1.Jugador import Jugador

class Equipo:
    id = 1
    def __init__(self, nombre:str, *jugadores:Jugador):
        self._nombre = nombre
        self._jugadores = list(jugadores)
        self._id_equipo = Equipo.id
        Equipo.id += 1

    @property
    def nombre(self)->str:
        return self._nombre
    @nombre.setter
    def nombre(self, name):
        self._nombre = name

    @property
    def jugadores(self)->list:
        return self._jugadores

    @property
    def id_equipo(self):
        return self._id_equipo

    def agregar_jugadores(self, *jugadores:Jugador)->None:
        """
        Métod0 para agregar múltiples jugadores.
        :param jugadores: Jugadores que se agregarán.
        :return:
        """
        for jugador in jugadores:
            if jugador not in self._jugadores:
                self._jugadores.append(jugador)

    def remover_jugadores(self, *jugadores:Jugador)->None:
        """
        Métod0 para remover múltiples jugadores.
        :param jugadores: Jugadores que serán removidos.
        :return:
        """
        for jugador in self._jugadores:
            if jugador not in jugadores:
                self._jugadores = list[jugador]

    def mostrar_jugadores(self)->None:
        """
        Métod0 para mostrar la lista de jugadores.
        :return:
        """
        if not self.jugadores:
            print("No hay jugadores para mostrar.")
        else:
            print(f"Los jugadores del equipo {self.nombre} son:")
            for i,jugador in enumerate(self.jugadores):
                print(f"{i}.- {jugador.nombre}")

    def total_goles(self)->int:
        """
        Métod0 para calcular el total de goles anotados por todos los jugadores del equipo.
        :return: El total de goles.
        """
        return sum(jugador.goles for jugador in self._jugadores)

    def __str__(self):
        return f"Equipos( Nombre: {self.nombre}, Jugadores: {self.jugadores}, Num. Equipo: {self.id_equipo}"

if __name__ == '__main__':
    pass