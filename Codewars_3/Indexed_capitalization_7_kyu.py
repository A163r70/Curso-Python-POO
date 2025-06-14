"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 6 de junio de 2025
Descripción:
Given a string of lowercase letters and an array of integer indices, capitalize all letters at the given indices.
If an index is beyond the string, it should be ignored.
"""

def capitalize(s, ind):
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    for i in range(len(s)):
        if i in ind:
            for j in range(26):
                if s[i] == minusculas[j]:
                    resultado += mayusculas[j]
                    break
        else:
            resultado += s[i]

    return resultado

if __name__ == '__main__':
    print(capitalize("abcdef",[1,2,5]))
    print(capitalize("abcdef",[1,2,5,100]))
    print(capitalize("codewars",[1,3,5,50]))
    print(capitalize("abracadabra",[2,6,9,10]))