"""
Fecha: 24/06/25
Nombre: Jesus Alberto Ramirez Salinas
Descripcion:
Write a function that will take in any array and reverse it.
"""

def reverse(seq):
    left = 0
    right = len(seq) - 1

    while left < right:
        temp = seq[left]
        seq[left] = seq[right]
        seq[right] = temp

        left += 1
        right -= 1

if __name__ == '__main__':
    ...