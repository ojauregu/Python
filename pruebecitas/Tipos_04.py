import sys
import random
MIN = 0
MAX = 99


def pedir_numero(invitacion, minimo, maximo):

    invitacion += " entre " + str(minimo) + " y " + str(maximo) + " :"

    while True:

        num1 = input(invitacion)

        try:
            num1 = int(num1)
        except:
            print("no es un numero", file=sys.stderr)
            pass
        else:
            if minimo <= num1 <= maximo:
                break
    return num1


numero = pedir_numero("meta numero", MIN, MAX)

while True:
    intento = pedir_numero("adivine el numero", MIN, MAX)
    if intento < numero:
        print("es mas grande")
    elif intento > numero:
        print("es mas pequeño")
    else:
        print("HAS GANADO")
        break