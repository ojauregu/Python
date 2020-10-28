'''
Pruebas fucnione
'''
import Practica1

def sumar(a,b,c):
    ''' 
    suma tres cosas
    '''
    return a+b+c

print (sumar(5,3,2))

def sumar_restar(a,b):
    ''' 
    suma y resta tres cosas
    '''
    return a+b , a-b

print (sumar_restar(5,3))

print (Practica1.generarAlf())