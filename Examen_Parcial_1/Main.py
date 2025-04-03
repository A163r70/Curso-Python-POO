from Equipo import Equipo
from Jugador import Jugador
from Torneo import Torneo
torneo = Torneo("Champions League")


def menu()->int:
    """
    Función que nos muestra el menú.
    :return:
    """
    print("*** Bienvenido al torneo: Champions League. ***")
    print("1.- Crear nuevo jugador.")
    print("2.- Crear nuevo equipo.")
    print("3.- Ver lista de jugadores.")
    print("4.- Ver lista de equipos.")
    print("5.- Agregar jugadores a algún equipo.")
    print("6.- Eliminar jugadores de un equipo.")
    print("7.- Agregar equipos al torneo.")
    print("8.- Eliminar equipos del torneo.")
    print("9.- Anotar gol(es) a un jugador.")
    print("10.- Conocer el número total de goles de los equipos.")
    print("11.- Generar rol de juegos.")
    print("0.- Salir.")
    opcion = input("Por favor, ingrese una de las opciones anteriores: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion

if __name__ == '__main__':
    nuevos_jugadores = []# Lista donde se agregan los nuevos jugadores.
    nuevos_equipos = []# Lista donde se agregan los nuevos equipos.
    salir = 1
    while salir != 0:
        opc = menu()
        if opc == 1:#Crear nuevo jugador
            #Pedimos nombre y número del nuevo jugador y lo agregamos a la lista.
            jugador_nombre = input("Ingresa el nombre del jugador: ")
            numero = input("Ingresa el número del jugador: ")
            while not numero.isnumeric():
                numero = input("Valor no válido: ")
            numero = int(numero)
            nuevo_jugador = Jugador(jugador_nombre, numero)
            nuevos_jugadores.append(nuevo_jugador)
            print("Se agrego un jugador")
            print()

        elif opc == 2:#Crear nuevo equipo
            #Pedimos el nombre del equipo y lo agregamos a la lista.
            nombre_equipo = input("Ingresa el nombre del equipo: ")
            nuevo_equipo = Equipo(nombre_equipo)
            nuevos_equipos.append(nuevo_equipo)
            print("Se agrego un equipo.")

        elif opc == 3:#Ver lista de jugadores
            #Mostramos todos los jugadores que hay en la lista.
            if not nuevos_jugadores:
                print("No hay jugadores.")
            else:
                print("Lista de jugadores.")
                for i,jugador in enumerate(nuevos_jugadores):
                    print(f"{i+1}.- {jugador}")
                print()

        elif opc == 4:#Ver lista de equipos
            #Mostramos todos los equipos que hay en la lista.
            if not nuevos_equipos:
                print("No hay equipos todavía.")
            else:
                print("Lista de Equipos.")
                for i,equipo in enumerate(nuevos_equipos):
                    print(f"{i+1}.- {equipo.nombre}")
                print()

        elif opc == 5:#Agregar jugadores a un equipo
            #En un ciclo while mostramos los equipos que hay y le damos a elegir al usuario a cual le quiere agregar los
            #jugadores, después mostramos la lista de jugadores que hay, y el usuario ingresa los índices de los
            # jugadores que quiere agregar, si se repite un jugador en un equipo no lo agrega. El ciclo se repite si
            # el índice que ingresa no es un número.
            if len(nuevos_equipos) == 0:
                print("No hay equipos aún.")
                break
            else:
                print("Selecciona un equipo para agregarle jugadores.")
                for i, eq in enumerate(nuevos_equipos):
                    print(f"{i + 1}.- {eq.nombre}")
                equipo_elegido = input("Ingresa el número del equipo al que le va a agregar jugadores: ")
                while not equipo_elegido.isnumeric():
                    equipo_elegido = input("Intenta de nuevo: ")
                equipo_elegido = int(equipo_elegido)-1
                if equipo_elegido < 0 or equipo_elegido >= len(nuevos_equipos):
                    print("Fuera de rango.")
                else:
                    equipo = nuevos_equipos[equipo_elegido]
                if len(nuevos_jugadores) == 0:
                    print("No hay jugadores para agregar.")
                    break
                else:
                    print("Selecciona los índices de los jugadores que quiere agregar, separados por comas.")
                    for i,jugador in enumerate(nuevos_jugadores):
                        print(f"{i+1}.- {jugador.nombre}")
                    eleccion = input()
                    indices = eleccion.split(",")

                    jugadores_a_agregar = []
                    for indice in indices:
                        if indice.isnumeric():
                            numero_jugador = int(indice.strip())-1
                            if numero_jugador >= 0 and numero_jugador < len(nuevos_jugadores):
                                jugadores_a_agregar.append(nuevos_jugadores[numero_jugador])
                            else:
                                print("El índice no es válido.")
                                break
                        else:
                            print("El índice no es un número")
                            break

                for jdr in equipo.jugadores:
                    for remplazo in jugadores_a_agregar:
                        if jdr == remplazo:
                            jugadores_a_agregar.remove(remplazo)
                            print("Se elimino el jugador que ya esta en otro equipo.")

                equipo.agregar_jugadores(*jugadores_a_agregar)
                print(f"Se agregaron solo jugadores con índices correctos al equipo {equipo.nombre}.")

        elif opc == 6:#Eliminar jugadores de un equipo
            #Mostramos los equipos que existen y el usuario elije a que equipo eliminarle jugadores.
            #Si tiene jugadores le muestra los jugadores y el usuario elije el índice del que quiere eliminar.
            #Buscamos ese índice en los jugadores de el equipo elegido y lo eliminamos.
            if len(nuevos_equipos) == 0:
                print("No hay equipos aún.")
            else:
                print("Selecciona el equipo al que le eliminarás jugadores.")
                for i, eqp in enumerate(nuevos_equipos):
                    print(f"{i+1}.- {eqp.nombre}")
                equipo_elegido = input("Ingresa el número del equipo al que le va a eliminar jugadores: ")
                while not equipo_elegido.isnumeric() or int(equipo_elegido) not in range(1, len(nuevos_equipos)+1):
                    equipo_elegido = input("Intenta de nuevo: ")

                equipo = nuevos_equipos[int(equipo_elegido)-1]

            if len(equipo.jugadores) == 0:
                print("No hay jugadores para eliminar.")
            else:
                print("Selecciona los índices de los jugadores que quiere eliminar, separados por comas.")
                for i,jugador in enumerate(equipo.jugadores):
                    print(f"{i+1}.- {jugador.nombre}")
                eleccion = input()

                indices= [indi.strip() for indi in eleccion.split(",") if indi.strip().isdigit()]

                jugadores_a_eliminar = []
                for indi in indices:
                    if indi.isnumeric():
                        numero_jugador = int(indi.strip())-1
                        if 0 <= numero_jugador < len(equipo.jugadores):
                            jugadores_a_eliminar.append(equipo.jugadores[numero_jugador])
                        else:
                            print("El índice no es válido.")
                    else:
                        print("El índice no es un número")

                if jugadores_a_eliminar:
                    equipo.remover_jugadores(*jugadores_a_eliminar)
                    print(f"Se eliminaron jugadores del equipo {equipo.nombre}")

        elif opc == 7:#Agregar equipos al torneo
            #Verificamos que haya equipos.
            #Mostramos los equipos que existen y el usuario elije que equipo desea agregar al torneo.
            #Agregamos los equipos al torneo ya creado.
            if not nuevos_equipos:
                print("No hay equipos para agregar al torneo.")
            else:
                print("Selecciona los índices de los equipos que quiere agregar, separados por comas.")
                for i, equipo in enumerate(nuevos_equipos):
                    print(f"{i+1}.- {equipo.nombre}")
                eleccion = input()
                indices = eleccion.split(",")

                equipos_a_agregar = []
                for indice in indices:
                    numero_equipo = int(indice.strip()) - 1
                    if numero_equipo >= 0 and numero_equipo < len(nuevos_equipos):
                        equipos_a_agregar.append(nuevos_equipos[numero_equipo])
                    else:
                        print("El índice no es válido.")

                torneo.agregar_equipos(*equipos_a_agregar)
                print(f"Los equipos agregados al torneo son:")
                for i,equipo in enumerate(torneo.equipos):
                    print(f"{i+1}.- {equipo.nombre}")

        elif opc == 8:#Eliminar equipos del torneo
            #Verficamos que haya equipos en el torneo.
            #Mostramos los equipos que hay.
            #El usuario elije que equipos desea eliminar y los eliminamos del torneo.
            if not torneo:
                print("No hay equipos para eliminar.")
            else:
                print("Seleciona los índices de los equipos que quiere eliminar, separados por una coma.")
                for i,equipo in enumerate(torneo.equipos):
                    print(f"{i+1}.- {equipo.nombre}")
                eleccion = input()
                indices = eleccion.split(",")

                equipos_a_eliminar = []
                for indice in indices:
                    numero_equipo = int(indice.strip())-1
                    if numero_equipo >= 0 and numero_equipo < len(torneo.equipos):
                        equipos_a_eliminar = list[torneo.equipos[numero_equipo]]
                torneo.remover_equipos(*equipos_a_eliminar)
                print("Equipos eliminados correctamente.")

        elif opc == 9:#Anotar goles a un jugador
            #Verificamos que haya jugadores.
            #Mostramos los jugadores que hay y el usuario elije a que jugador anotarle goles.
            #Pedimos la cantidad de goles que le quiere anotar.
            #Le anotamos al jugador elejido los goles.
            if not nuevos_jugadores:
                print("No hay jugadores aún.")
            else:
                print("Selecciona el índice del jugador al que le quiere anotar goles.")
                for i,jugador in enumerate(nuevos_jugadores):
                    print(f"{i+1}.- {jugador.nombre}")
                jugador_indice = input("Ingrese el índice: ")
                while not jugador_indice.isnumeric():
                    jugador_indice = input("Intenta de nuevo: ")
                jugador_indice = int(jugador_indice)-1

                goles = input("Ingresa el número de goles: ")
                while not goles.isnumeric():
                    goles = input("Intenta de nuevo: ")
                goles = int(goles)

                nuevos_jugadores[jugador_indice].anotar_goles(goles)
                print(f"Se anotaron {goles} goles a {nuevos_jugadores[jugador_indice].nombre}.")

        elif opc == 10:#Conocer el número total de goles de los equipos
            #Iteramos sobre cada equipo que hay y mandamos a llamra el métod0 total_goles
            for equipo in nuevos_equipos:
                print(f"El {equipo.nombre} tiene {equipo.total_goles()} goles.")
        elif opc == 11:#General rol de juegos
            #Mandamos a llamar al métod0 general_rol
            torneo.generar_rol()
        elif opc == 0:#Saliendo
            print("Saliendo...")
            salir = 0
        else:
            print("Error.")