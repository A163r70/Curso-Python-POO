"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de marzo de 2025
Descripción:
Aliens from Kepler 27b have immigrated to Earth! They have learned English and go to our stores,
eat our food, dress like us, ride Ubers, use Google, etc. However, they speak English a little differently.
Can you write a program that converts our English to their Alien English?

Task:
Write a function that receives a lowercase string and converts it from our English to Alien English.
They tend to speak the letter a like o and o like a u.

"hello" ---> "hellu"
"codewars" ---> "cudewors"
"""
def convert(st):
    nl = ""
    for letra in st:
        if letra == 'a':
            nl += 'o'
        elif letra == 'o':
            nl += 'u'
        else:
            nl += letra
    return nl


if __name__ == '__main__':
    print(convert('codewars'))
    print(convert('hello'))