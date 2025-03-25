"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 20 de marzo de 2025
Descripción:
"""
from Clases_y_Objetos.ScoreBoard import ScoreBoard


class Window:
    def __init__(self,text:str,width:int,height:int,scoreboard:ScoreBoard=ScoreBoard()):
        self.te