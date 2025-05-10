"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
You have managed to intercept an important message and you are trying to read it.
You realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.
You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.
Create a function that will instantly decode any of these messages

You can assume no punctuation or capitals, only lower case letters, but remember spaces!
"""
from operator import index


def decode(message):
    """
    Función que decodifica una cadena de caracteres cambiando la letra por su contraparte en el abecedario cuando
    esta inverso.
    :param message: Mensaje que se va a decodificar.
    :return: Mensaje decodificado.
    """
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    abecedario_invertido = ''
    for i in range(len(abecedario) - 1, -1, -1):
        abecedario_invertido += abecedario[i]
    mensaje = ''
    for letra in message:
        if letra == ' ':
            mensaje += ' '
        else:
            indice = abecedario.index(letra)
            mensaje += abecedario_invertido[indice]

    return mensaje

if __name__ == '__main__':
    print(decode("sr"))
    print(decode("svool"))
    print(decode("r slkv mlylwb wvxlwvh gsrh nvhhztv"))
    print(decode("qzezxirkg rh z srts ovevo wbmznrx fmgbkvw zmw rmgvikivgvw kiltiznnrmt ozmtfztv rg szh yvvm hgzmwziwravw rm gsv vxnzxirkg ozmtfztv hkvxrurxzgrlm zolmthrwv sgno zmw xhh rg rh lmv lu gsv gsivv vhhvmgrzo gvxsmloltrvh lu dliow drwv dvy xlmgvmg kilwfxgrlm gsv nzqlirgb lu dvyhrgvh vnkolb rg zmw rg rh hfkkligvw yb zoo nlwvim dvy yildhvih drgslfg koftrmh"))
    print(decode("gsv vrtsgs hbnkslmb dzh qvzm hryvorfh urmzo nzqli xlnklhrgrlmzo kilqvxg lxxfkbrmt srn rmgvinrggvmgob"))
    print(decode("husbands ask repeated resolved but laughter debating"))
    print(decode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(decode(" "))
    print(decode(""))
    print(decode("thelastrandomsentence"))