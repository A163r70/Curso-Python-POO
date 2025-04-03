from Examen_Parcial_1.Equipo import Equipo

class Torneo:
    def __init__(self, nombre:str, *equipos:Equipo):
        self._nombre = nombre
        self._equipos = list(equipos)

    @property
    def nombre(self)->str:
        return self._nombre
    @nombre.setter
    def nombre(self, name:str):
        self._nombre = name

    @property
    def equipos(self)->list:
        return self._equipos


    def agregar_equipos(self, *equipos:Equipo)->None:
        """
        Métod0 para agregar múltiples equipos.
        :param equipos: Lista de equipos que serán agregados.
        :return:
        """
        for equipo in equipos:
            if equipo not in self._equipos:
                self._equipos.append(equipo)

    def remover_equipos(self, *equipos:Equipo)->None:
        """
        Métod0 para remover múltiples equipos.
        :param equipos: Lista de equipos que serán removidos.
        :return:
        """
        for equipo in self._equipos:
            if equipo not in equipos:
                self._equipos = list[equipo]

    def mostrar_equipos(self)->None:
        """
        Métod0 para mostrar la lista de equipos.
        :return:
        """
        if not self._equipos:
            print("No hay equipos para mostrar.")
        else:
            print("Los equipos del torneo son los siguientes:")
            for equipo in self.equipos:
                print(f"Equipo{equipo.id_equipo}: {equipo.nombre}")

    def generar_rol(self)->None:
        """
        Métod0 para generar un rol de partidos estilo "todos contra todos" organizado por jornadas,
        en donde se incluyen a todos los equipos del torneo.
        :return:
        """
        if len(self.equipos) < 2:
            print("No hay suficientes equipos.")
        else:
            print("El rol de partidos queda de la siguiente manera:")
            contador_equipos = 1
            for i in range(len(self.equipos)):
                for j in range(i + 1, len(self.equipos)):
                    print(f"Partido {contador_equipos}: {self.equipos[i].nombre} vs {self.equipos[j].nombre}")
                    contador_equipos += 1
        print()

    def __str__(self):
        return f"Torneo( Nombre: {self.nombre}, Equipos: {len(self.equipos)}"

if __name__ == '__main__':
    torneo = Torneo("Champions League")