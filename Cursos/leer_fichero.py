

def lecturaFichero(path):
    '''
    Leer fichero de texto por linea
    '''
    f = None
    try:
        f=open(path,'r')
        while True:
            linea=f.readline()
            if not linea:break
            print(linea.strip('\n'))
            print(f.tell())
            
    except Exception as e:
        
        print(e)
    finally:
        if f != None:
            f.close()

def escrituraConsola(path):
    '''
    Graba fichero de texto
    '''
    f = None
    try:
        f=open(path,'a')
        while True:
            s=input('dame cadena ')
            if s.lower()=='fin':break
            f.write(s)
            f.write('\n')

            
    except Exception as e:
        
        print(e)
    finally:
        if f != None:
            f.close()
    
def partirFichero(path,NumPart):
    f = None
    
    try:
        
        f=open(path,'r')
        linea=f.read()
        lon=(len(linea))
        tam= lon // NumPart
        print(tam)
        index=0
        
        for i in range(numParticiones):
    
            print (fichSal)
            f_out = open(fichSal,'w')
            f_out.write(linea[index:index+tam])
            index+=tam
            
            

            
            
    except Exception as e:
        
        print(e)
        
    finally:
        if f != None:
            f.close()

  
if __name__ == "__main__":
    
    file='C:\\Users\\n64258\\Documents\\Cursos\\fichero\\oscar.txt'
    lecturaFichero(file)
    file2='C:\\Users\\n64258\\Documents\\Cursos\\fichero\\oscar2.txt'
    #escrituraConsola(file2)
    numParticiones=7
    #partirFichero(file,numParticiones)
    
    