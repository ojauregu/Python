"""
Ejemplos con tuplas
"""
t1 = (1,2,3)
t2 = 1,2,3
print(t1, type(t1))
print(t2, type(t2))

# Asignar variables utilizando la expansión de tuplas:
a,b,c = t1
print(a,b,c)

# Solucion larga:
L = [('a',1), ('b',2), ('c',3)]
for i in L:
    k = i[0]
    v = i[1]
    print(i, type(i), k, v)

# Mejor solucion:
L = [['a',1], ['b',2], ['c',3]]
for k, v in L:
    print(k, v)  

# La tupla es INMUTABLE, NO SE PUEDE MODIFICAR
#t1[0] = 90
#print(t1)    

# Select * from clientes where pais=?
# OJO TUPLAS DE 1 ELEMENTO
t1 = 7,
print(type(t1)) 

t = tuple('hola')
print(t)

# Conversion de Lista a Tupla
L = [3,4,5,1,2]
t2 = tuple(L)
print(t2)

# A la inversa:
t = (9,4,5,2,3, 2, 1)
print(list(t))


