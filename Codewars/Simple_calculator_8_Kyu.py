"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 19 de marzo de 2025
Descripción:
You are required to create a simple calculator that returns the result of addition, subtraction,
multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the list above a message "unknown value"
must be returned.
"""
def calculator(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        print("unknown value")

if __name__ == '__main__':
    print(calculator(6, 2, '+'))
    print(calculator(4, 3, '-'))
    print(calculator(5, 5, '*'))
    print(calculator(5, 4, '/'))
    print(calculator(6, 2, '&'))