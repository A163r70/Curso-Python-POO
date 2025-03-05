"""
Alumno: Jesús Alberto Ramírez Salinas
Fecha: 04 de marzo de 2025
Descripción: Ejercicio del examen diagnóstico.
"""
import random

def parejas_validas(parejas, equipos_antes):
    for equipo_antiguo in equipos_antes:
        coincidencia = 0
        for integrante in parejas:
            if integrante in equipo_antiguo:
                coincidencia += 1
        if coincidencia == 2:
            return True
    return False

def formar_equipos():
    equipos_formados = []
    random.shuffle(alumnos)
    equipos = []

    while len(equipos_formados) < 6:
        for i in range(0,12,2):
            if i +1 < len(alumnos):
                equipos = [(alumnos[i], alumnos[i+1])]

        equipo_valido = True
        for parejas in equipos:
            if parejas_validas(parejas, equipos_anteriores):
                equipo_valido = False
                break

        if equipo_valido == True:
            equipos_formados = equipos




if __name__ == '__main__':
    alumnos = ["Hector", "Alberto", "Addi", "Tania", "Patricia", "Rebeca", "Jamileth", "Bryan", "Rosalinda",
               "Galilea", "Jennifer", "Juan"]

    equipos_anteriores = [["Hector", "Alberto", "Addi"], ["Patricia", "Tania", "Rebeca"],
                          ["Juan", "Galilea", "Jennifer"], ["Jamileth", "Bryan", "Rosalinda"]]
    formar_equipos()