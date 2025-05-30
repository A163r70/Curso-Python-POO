
class Jugador:
    def __init__(self, nombre:str, numero:int, goles:int = 0):
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    @property
    def nombre(self)->str:
        return self._nombre
    @nombre.setter
    def nombre(self, name:str):
        self._nombre = name

    @property
    def numero(self)->int:
        return self._numero
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def goles(self)->int:
        return self._goles
    @goles.setter
    def goles(self, goles):
        self._goles = goles

    def anotar_goles(self, no_goles:int)->None:
        """
        Métod0 para incrementar la cantidad de goles.
        :param no_goles:
        :return:
        """
        self.goles += no_goles

    def __str__(self):# Métod0 para mostrar la información del jugador.
        return f"Jugador( Nombre = {self.nombre}, Número = {self.numero}, Goles = {self.goles})"

if __name__ == '__main__':
    pass
