"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 20 de marzo de 2025
Descripción:
Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2".
"""

def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "" and b != "":
        return b
    elif a != "" and b == "":
        return a
    elif a != "" and b != "":
        a = int(a)
        b = int(b)
        return str(a + b)

if __name__ == '__main__':
    print(sum_str("9",""))
    print(sum_str("","9"))
    print(sum_str("",""))
    print(sum_str("628537", "604788"))
    print(sum_str("-1","-3"))