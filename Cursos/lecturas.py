"""
En este modulo vamos a leer datos de teclado y realizar conversiones
"""

print("Introduce mensaje:")
mensaje = input()
print(mensaje, type(mensaje))

mensaje2 = input('Dame numero: ')
num = int(mensaje2)
print("num: ", num, type(num))

def imprimir():
    print("Hola")


print(imprimir())

con = None
print(con, type(con))
