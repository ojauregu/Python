
class HoraExcep(Exception):
    def __init__(self,mensaje=''):
        self.mensaje=mensaje
        
    def __str__(self):
        return self.mensaje

class Hora:
    '''
    operaciones con horas
    '''
   

    def __init__(self,h=0,m=0):
        self.h=h
        self.m=m
        if h <0 or h > 23:
            raise HoraExcep('las horas estan mal')
        
    def __str__(self):
        return '%02d' '%02d' %(self.h ,self.m)
    
    def __len__(self):
        return 14
    
    def __add__(self,otro):
       
        if self.m+otro.m > 60:
            self.h=self.h+1
            self.m=self.m-60
            
        return self.h+otro.h , self.m+otro.m
        


if __name__ == "__main__":
    
    try:
        h1=Hora(m=50)

        
        h2=Hora(-1,50)
    
        print(h1,h2)
        suma = h1 + h2
        
        print(suma)
        
        print(h1,h2)
        
        print(len(h1))
        
    except Exception as e:
        print('nombre de la clase ', e.__class__.__name__)
        print(e)
        
    