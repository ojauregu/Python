
from modulos.SMS import SMS
from modulos.call import Call
from modulos.callint import CallInt



if __name__=='__main__':   
    
    
    
    L=[SMS(0.01),Call(0.05,10),Call(0.02,20),CallInt(0.10,20,30)]    
    print('Servicio: ')
    for i in L:
        print(i.__class__.__name__ , i.calcularImporte())
    
    
    
   
        