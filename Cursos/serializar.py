try:
    import cPickle as pickle
except ImportError:
    import pickle
import shelve

# Crear diccionario vacio:
d = dict()
print(d, type(d))

d2 = {1:"uno",2:"dos",3:"tres"}
print(d2)

d2[4] = "cuatro"

# Buscar una clave:
if 4 in d2:
    print("el 4 esta")

# Recorrer el diccionario:
for k, v in d2.items():
    print(k, v)

"""
Leer una frase de teclado: hola que tal
'a':2
' ':2
'h':1
...
"""
frase = input("Teclear una frase: ")
h = dict()
for i in frase:
    if i in h:
        # La clave ya existe suma uno mas.
        h[i] += 1
    else:
        # Crea la clave para la letra
        h[i] = 1


L=list(h.items()) 
L.sort(key=lambda t:t[1],reverse=True)
print (L)
for letra, cont in L:

    print(letra, cont)     


fichero = open('datos.bin','wb')


pickle.dump(h,fichero,2)
animales= ['piton','cobra','gallo']


pickle.dump(animales,fichero,2)



fichero.close()

fichero = open('datos.bin','rb')

animales2 = pickle.load (fichero)
print('-----------------')
print(animales2,type(animales2))
print('-----------------')

animales2 = pickle.load (fichero)
print('-----------------')
print(animales2,type(animales2))
print ('-----------------')


