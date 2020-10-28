alfabeto='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '

def generarAlf():
    '''
    devuelve alfabeto
    '''
    alfabeto='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '
    return alfabeto

def codificarletra (letra,alfabeto,k):
    '''
    devuelve posicion de la letra
    '''
    
    return alfabeto.index(letra) + k
   

def decodificarletra(numero,alfabeto,k):
    '''
    devuelve letra asociada a numero
    '''
    return alfabeto[numero-k]
    

if __name__ == "__main__":
 
    entrada =  input ("introduzca palabra ")   
    numero=0
  
 
    codigo=[codificarletra(i,generarAlf(),5) for i in entrada]
    
    ''''
    for i in entrada:
        codigo.append(codificarletra(i,generarAlf(),5))
    '''      
    print (codigo)

    decode=[decodificarletra (i,generarAlf(),0) for i in codigo]
    '''
    for i in codigo:
        decode.append(decodificarletra (i,generarAlf(),0))
    '''
    print (decode)
    
    entrada =  input ("introduzca palabra codificada ")   
    
    codigo = [codificarletra(i,generarAlf(),-5) for i in entrada]
    
    '''
    for i in entrada:
        codigo.append(codificarletra(i,generarAlf(),-5))
    '''    
    print (codigo)

    decode = [decodificarletra (i,generarAlf(),0) for i in codigo]
    
    '''
    for i in codigo:
        decode.append(decodificarletra (i,generarAlf(),0))
    '''
    print (decode)