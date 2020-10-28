def suma(a,b):
    return a+b
    
def resta(a,b):
    return a-b
    
def salir(a=0,b=0):
    exit()
    
def menu(opciones,a,b):
    print('menu')
    i=1
    for op in opciones:
        print(i,op.__name__)
        i+=1
    opcion = int(input ("ponga opcion " ))
    a= int(input ('numero 1: '))
    b= int(input ('numero 2: '))
    
    print(opciones[opcion-1](a,b))
    
    
L=[suma,resta,salir]
a1=10
b2=20
menu(L,a1,b2)
