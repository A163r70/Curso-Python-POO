"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 17 de marzo de 2025
Descripción: Primer ejercicio de Codewars.
Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
For example:
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""
def cadena_a_flotante(cadena: str)-> float | None:
    """
    Función que convierte una cadena a un número flotante con validación.
    :param cadena: {Es la cadena a convertir a flotante}
    :return:
    """
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "0")
    if revisar_cadena.isnumeric() and no_puntos in (0,1) and no_guiones in (0,1):
        return float(cadena)
    else:
        return None

def recibir_tiempo()->float:
    horas = input("Ingresa el tiempo recorrido: ")
    tiempo = cadena_a_flotante(horas)
    while tiempo is None:
        horas = input("Opción no válida. Intente nuevamente: ")
        tiempo = cadena_a_flotante(horas)
    return tiempo

def litres(time:float)->int:
    litros = 0.5 * time
    return int(litros)

if __name__ == '__main__':
    tiempo = recibir_tiempo()
    litros = litres(tiempo)
    print(f"time = {tiempo} -----> litres = {litros}")