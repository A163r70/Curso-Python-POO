"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 20 de marzo de 2025
Descripción:
"""

class ScoreBoard:
    def __init__(self, points:int=0, text_color:tuple[int,int,int]=(0,0,0), font:str="Kimono", size:float=48):
        self._points = points
        self._text_color = text_color
        self._font = font
        self._size = size

    #Point
    @property
    def points(self)->int:
        return self._points
    #Point
    @points.setter
    def points(self,puntos:int)->None:
        self._points = puntos

    @property
    def text_color(self)->tuple:
        return self._text_color
    @text_color.setter
    def text_color(self, texto_color:tuple[int]):
        self._text_color = texto_color

    @property
    def font(self)->str:
        return self._font
    @font.setter
    def font(self, fuente:str):
        self._font = fuente

    @property
    def size(self)->float:
        return self._size
    @size.setter
    def size(self, tamano:float):
        self._size = tamano

    def draw(self)->None:
        print(f"Score = {self.points}")

    def __str__(self):
        return f"ScoreBoard (Points ={self._points},Text_color={self._text_color},Font={self.font},Size={self.size})"

if __name__ == '__main__':
    """ %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
    if __name__ == "__main__":
        # Se crean objetos de la clase y se imprime.
        print("  -- Se crean objetos de la clase Scoreboard.")

        print()
        print("Se crea un objeto sin argumentos:")
        marcador1 = ScoreBoard()
        print(f"marcador1 = {marcador1}")

        print()
        print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
        marcador2 = ScoreBoard(10, font="Arial", text_color=(127, 127, 127))
        print(f"marcador2 = {marcador2}")

        print()
        print("Se prueba el método draw() en ambos objetos:")
        marcador1.draw()
        marcador2.draw()