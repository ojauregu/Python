import random

def cuadrado(x):
    return x **2


L=list(range(1,11))
print(L)

L2=list(map(cuadrado,L))
print(L2)

L2=[cuadrado(i) for i in L]
print(L2)

d2={i:i**2 for i in range(1,11)}
print (d2)

L=[random.randint(1,100) for i in range(25)]
print (L)

L3 = [(i,2**i) for i in range(1,11)]
print(L3)