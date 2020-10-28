"""
Operaciones con conjuntos 
"""
c2 = {'a','b','c'}
print(c2, type(c2))

# Quitar repetidos de una lista:
L = [7,6,5,3,4,3,3,2,1,1,1,2,4]
c = set(L)
print(c, type(c))


L2 = list(set(L))
print(L)
print(L2)

for n in c:
    print(n)

# Error no puedo acceder a una posición del Conjunto:
#print("posicion 0: ", c[0])   

c1={'oscar','pedro','ana','fer'}
c2={'antonio','juan','jose','fer'}
c3={'raul','lola','fer','pere'}
c4=c1|c2
print (c4)
print(c4.issuperset(c2))
