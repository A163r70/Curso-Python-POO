"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 19 de marzo de 2025
Descripción: Relaciones entre objetos.
"""



class Empleado:
    no_id = 1
    def __init__(self, nombre:str,sueldo:float):
        self.nombre = nombre
        self.sueldo = sueldo
        self.id = Empleado.no_id
        Empleado.no_id +=1 #generaor de id automaico, o contador

    def aumentar_sueldo(self,porcentaje:float)->None:
        """
        Se utiliza para aumentar el sueldo de acuerdo con un porcentaje.
        :param porcentaje: Porcentaje a incrementar el sueldo.
        """
        if porcentaje > 0:
            self.sueldo += self.sueldo * (porcentaje / 100)
            print(f"El sueldo de {self.nombre} ahora es de {self.sueldo:,.2f}")

        else:
            print("No se aplicó ningún cambio, ya que por Ley, el sueldo no puede disminuir.")

    def __str__(self)->str:
        return f"Empleado( id= {self.id}, nombre= {self.nombre}, sueldo= {self.sueldo})"

class Empresa:
    def __init__(self, nombre:str, *empleados:Empleado):
        self.nombre = nombre
        self.empleados = list(empleados)

    def agregar_empleados(self, *nuevos_empleados:Empleado)->None:
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)

    def remover_empleados(self, *empleados_a_remover:Empleado)->None:
        """
        Se utiliza para remover un empleado de la empresa.
        :param empleados_a_remover: Empleado a remover de la empresa.
        """
        for empleado in empleados_a_remover:
            if empleado in self.empleados:
                self.empleados.remove(empleado)

            else:
                print(f"El empleado {empleado} no forma parte de {self.nombre}.")

    def aumentar_sueldo_empleados(self, porcentaje:int)->None:
        """
        Se utiliza para aumentar el sueldo a todos los empleados de acuerdo con un porcentaje.
        :param porcentaje: Porcentaje a incrementar el sueldo.
        """
        for empleado in self.empleados:
            empleado.aumentar_sueldo(porcentaje=porcentaje)

    def mostrar_empleados(self)->None:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        print(f"*** Lista de empleados de {self.nombre} ***")

        for empleado in self.empleados:
            print(empleado)

    def __str__(self)->str:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"



if __name__ == '__main__':
    empleado1 = Empleado("Alberto", 300)
    empleado2 = Empleado("Addi", 150)
    print(empleado1)
    print(empleado2)
    unsij = Empresa("UNSIJ", empleado1, empleado2)
    unsij.agregar_empleados(empleado1, empleado2)
    unsij.mostrar_empleados()
    print(unsij)
    print(empleado1)
    empleado1.nombre = "Jesus Alberto"
    print(empleado1)
    #get(nombre) para leer el nombre
    #set(nombre) para cambiarlo
