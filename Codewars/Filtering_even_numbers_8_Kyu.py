"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de marzo de 2025
Descripción:
The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.
However, there is a bug in the method that needs to be resolved.
"""
def kata_13_december(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            lst.pop(i)
        else:
            i += 1
    return lst

if __name__ == '__main__':
    print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]))
    print(kata_13_december([1, 2, 2, 2, 4, 3, 4]))