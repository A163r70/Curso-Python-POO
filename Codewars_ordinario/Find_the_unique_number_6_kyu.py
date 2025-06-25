"""
Fecha: 24/06/25
Nombre: Jesus Alberto Ramirez Salinas
Descripcion:
There is an array with some numbers. All numbers are equal except for one. Try to find it!
"""
def find_uniq(arr):
    if arr[0] == arr[1]:
        repetido = arr[0]
    elif arr[0] == arr[2]:
        repetido = arr[0]
    else:
        return arr[0]

    for num in arr:
        if num != repetido:
            return num

if __name__ == '__main__':
    print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
    print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
    print(find_uniq([ 3, 10, 3, 3, 3 ]))