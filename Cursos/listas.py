"""
Operaciones con listas
"""
# lista vacia
L = []
print(L, type(L))

L = [4,6,3,1,3,4,9]
print(L)

# Recorrer una lista:
for i in L:
    print(i)

if 3 in L:
    print("El 3 esta en la lista")   

num = 0
if num not in L:
    print(num, "no esta en la lista")     

# Recorrido de la lista con el indice:
for i in range(0, len(L)):
    print(i, L[i])
# print(L[10]) error!
L += [100]
print(L)

L = [4,6,3,1,3,[4,9]]
print(L[5][0])
print(L[-1][0])

L = list()
print(L)
L = list('hola')
print(L)

# Pruebas con Slicing: [inicio : fin-1 : salto]
L = [4,6,3,1,3,4,9]
print('Los 3 primeros: ', L[0:3])
print('Los 3 primeros: ', L[:3])
print('Quitar el primer numero', L[1:])
print('Toda la lista',L[:])
print('De dos en dos',L[::2])
print(L[::-1])
L[0] = 90
print(L)

L[3:8] = [-2,-3]
print(L)

"""
Interseccion de los Listas:
intersección: L = [5]
"""
L1 = [5,7,5,4,3,23,3]
L2 = [2,5,6,9,11]

r = []
for i in L1:
    if i in L2:
        if i not in r:
            r += [i]
print(r) 

"""
Comprobar si la lista es un palindromo.
L = [1,4,5,6,6,5,4,1]
"""
L = [1,4,5,6,0,6,5,4,1]
print('longitud: ', len(L))
print('mitad: ', len(L) // 2)

if L == L[::-1]:
    print("ok")
else:
    print('No es palindromo')

"""
Ejemplo bucle while
i = 1
while i < 5:
    print(i)
    i += 1
"""    
