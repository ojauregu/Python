"""
Prueba con operadores.
"""

numero1 = 10
numero2 = 3

# Division con decimales:
resul = numero1 / numero2
print(resul, type(resul))

# Division entera
resul = numero1 // numero2
print(resul, type(resul))

resul = "a"
print(resul, type(resul))
#exit()

# Operador modulo: el resto de la div. entera.
resul = numero1 % numero2
print("Resto: ", resul)

resul = -resul
print(resul)

x = 2
print(x**10)

# Operadores relacionales:
a = 12
b = 9
if a == b:
    print(a, "y", b, "son iguales") 

elif a < b:
    print(a, "<",b)

else:
    print(a,">",b)

print("fin")

# Me permite dejar vacio un bloque 
if a == b:
    pass

# Operadores a nivel de Bits:
"""
a: 1001 1000: 0x98
b: 1011 1010: 0xBA
------------
&: 1001 1000
|: 1011 1010
^: 0010 0010
"""
a = 0x98
b = 0xBA
print(bin(a))
print(bin(b))
"""
Rotaciones de Bits: << 
1000 0100 << 1 
0000 1000
Rot. >>
0001 0000 = 16
0000 1000 = 8
"""
# Comprobar si un numero esta demtro de un rango:
numero = 20 # Comprobar si esta entre 10 y 30
if numero >= 10 and numero <= 30:
    print("Dentro del rango")
else:
    print("Fuera del rango")

var = numero >= 10 and numero <= 30
print(var, type(var))

