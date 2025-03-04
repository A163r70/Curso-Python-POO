"""
Alumno: Jesús Alberto Ramírez Salinas
Fecha: 04 de marzo de 2025
Descripción: Ejercici del examen diagnóstico.
"""
from random import choice

equipos = {'Los_Algoritmos_Anarquistas':{"Hector", "Alberto", "Addi",},
           'Los_Hackers_de_Cafe':{"Tania", "Patricia", "Rebeca"},
           'Los_Codificadores_nocturnos':{"Jamileth", "Bryan", "Rosalinda"},
           'Los_Ctrl+Z':{"Galilea", "Jennifer", "Juan"}}

alumnos = ["Hector", "Alberto", "Addi", "Tania", "Patricia", "Rebeca", "Jamileth", "Bryan", "Rosalinda",
           "Galilea", "Jennifer", "Juan"]
equipo1 = []
equipo2 = []
equipo3 = []
equipo4 = []
equipo5 = []
equipo6 = []

for i in range(6):
    for j in range(2):
        alumno1 = choice(alumnos)


