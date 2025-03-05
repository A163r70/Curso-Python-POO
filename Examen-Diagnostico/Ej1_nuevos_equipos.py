"""
Alumno: Jesús Alberto Ramírez Salinas
Fecha: 04 de marzo de 2025
Descripción: Ejercicio del examen diagnóstico.
"""


alumnos = ["Hector", "Alberto", "Addi", "Tania", "Patricia", "Rebeca", "Jamileth", "Bryan", "Rosalinda",
           "Galilea", "Jennifer", "Juan"]

cantidad = len(alumnos)

equipos_formados = []

for i in range(0,12,2):
    if i +1 < len(alumnos):
        equipos_formados.append((alumnos[i], alumnos[i+1]))

for equipo in equipos_formados:
    print(equipo)

