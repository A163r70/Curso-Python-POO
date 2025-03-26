"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 20 de marzo de 2025
Descripción:
"""
from Clases_y_Objetos.ScoreBoard import ScoreBoard


class Window:
    def __init__(self,title:str,width:int,height:int,scoreboard:ScoreBoard=ScoreBoard()):
        self._title = title
        self._width = width
        self._height = height
        self._scoreboard = scoreboard

    @property
    def title(self)->str:
        return self._title
    @title.setter
    def title(self,titulo:str)->None:
        self._title = titulo

    @property
    def widht(self)->int:
        return self._width
    @widht.setter
    def widht(self, widht:int):
        self._width = widht

    @property
    def height(self)->int:
        return self._height
    @height.setter
    def height(self, height:int):
        self._height = height

    @property
    def scoreboard(self)->ScoreBoard:
        return self._scoreboard
    @scoreboard.setter
    def scoreboard(self, scoreboard:ScoreBoard):
        self._scoreboard = scoreboard


    def draw(self)->None:
        return f"Window (Titulo={self._title}"

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)


    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")
