'''
Clase Personas prubas
'''
class Persona:
    ''''
    Clase persona
    '''
    num_instancias = 0
    
    def __init__(self,nombre='',edad=0,altura=0.0):
        '''
        constructor clase personas
        '''
        self.nombre=nombre
        
        self.edad=edad
        self.altura=altura
        Persona.num_instancias+=1
        
        
    def __str__(self):
        return self.nombre  + ' ' + str(self.edad) + ' ' + str(self.altura)
    
    def __repr__(self):
        return str(self)
    
    def __del__(self):
        Persona.num_instancias-=1
    
    def __eq__(self,otro):
        return self.nombre==otro.nombre and self.edad==otro.edad and self.altura==otro.altura
    
    def __lt__(self,otro):
        return self.nombre<otro.nombre and self.edad<otro.edad and self.altura<otro.altura
        
    def hablar(self,otro):
        print(self.nombre,' > ',otro.nombre)
        

    
if __name__=='__main__':
    
    p1=Persona('Oscar',45,1.65)
    p2=Persona('Raul',87,1.75)
    p3=Persona('Alberto',90,1.98)
    print(Persona.num_instancias)
    L=[p1,p2,p3]
    
    if p1<p2:
        print('repe')
    else:
        print('no repe')
    
    L.sort()
    #L.sort(key=lambda per: per.altura,reverse=True)    
    print(L)
    
        
    p1.hablar(p3)
    
    L2=[p.__dict__ for p in L]
    
    print(L2)
    
    L3=[('popo',34,1.87),('lola',56,1.90)]
    
    L4 = [Persona(*t) for t in L3]
    
    print(L4)
    
    print(Persona.num_instancias)
    
    p2.__del__()
    
    print(Persona.num_instancias)
    
    
   