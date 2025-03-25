"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 20 de marzo de 2025
Descripción: Encapsulamiento
Diagrama de clases de UML
- privado
+ publico
#_ protejido.
"""

class CuentaBancaria:
    def __init__(self, titular:str, saldo_inicial:float=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad:float)->None:
        self._saldo += cantidad

    def retirar(self,cantidad:float)->None:

        self._saldo -= cantidad

    @property
    def saldo(self)->float:
        return self._saldo

    @saldo.setter
    def saldo(self,nuevo_saldo:float)->None:
        self._saldo = nuevo_saldo

    def __str__(self):
        pass

if __name__ == '__main__':
    cuenta_guadalupe = CuentaBancaria("Guadalupe", 0)
    cuenta_guadalupe.saldo = 5
