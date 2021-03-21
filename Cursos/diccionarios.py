"""
Pruebas con diccionarios
"""

# Crear diccionario vacio:
d = dict()
print(d, type(d))

d2 = {"uno":"uno","dos":"dos","tres":"tres"}
print(d2)

d2["cuatro"] = "cuatro"

print(d2["cuatro"])

# Buscar una clave:
if "cuatro" in d2:
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



