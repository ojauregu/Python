def division(a,b):
    return a/b
def calcula():
    division(1,0)

def prueba2(ini,fin):
    if fin <= ini:
        raise Exception('Errorrrrrr Fin menor que Ini')
'''
try:        
    calcula()
    
except Exception as e:
    print(e.__class__.__name__)
    print('division por cero')
'''    
try:
    prueba2(12,10)   
except Exception as e:
    print(e.__class__.__name__)
    print(e)
