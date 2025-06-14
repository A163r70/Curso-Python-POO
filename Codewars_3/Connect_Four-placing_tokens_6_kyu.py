"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 6 de junio de 2025
Descripción:
INPUT
A list of integers representing the columns (from 0 to 6) where tokens are dropped, in order.
The first player is yellow (Y), followed by red (R), alternating turns.

OUTPUT
The final state of the board after all tokens have been placed. Empty cells are marked with -.

ASSUMPTIONS
The board has 7 columns and 6 rows (standard Connect Four size).
Tokens fall to the lowest available position in the chosen column.
All input values are valid and within the allowed range.
The input list must not be modified.
Output format: rows are listed from top to bottom, with the top row first and the bottom row last.
"""

def connect_four_place(columns):
    tablero = []
    for i in range(6):
        fila = []
        for j in range(7):
            fila.append('-')
        tablero.append(fila)

    usuario = 'Y'

    for move in columns:
        col = move
        for fila in range(5, -1, -1):
            if tablero[fila][col] == '-':
                tablero[fila][col] = usuario
                break

        if usuario == 'Y':
            usuario = 'R'
        else:
            usuario = 'Y'

    return tablero

if __name__ == '__main__':
    print(connect_four_place([0,1,0,1,0,1]))