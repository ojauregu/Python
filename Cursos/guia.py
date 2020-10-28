from persona import Persona
from empleado import Empleado

class Guia(Persona,Empleado):
    

    def __init__(self,nombre='',edad=0,altura=0.0,idiomas=[],nacion='',empresa='',sueldo=0.0):
        '''
        constructor clase gui
        '''
        Persona.__init__(self,nombre,edad,altura)
        Empleado.__init__(self,empresa,sueldo)
        self.idiomas=idiomas
        self.nacion=nacion             

    def __str__(self): 
        return Persona.__str__(self) + ' ' + Empleado.__str__(self) + ' , '.join(self.idiomas) + ' ' + self.nacion


if __name__=='__main__':
    
    g1=Guia('Oscar',45,1.65,['ingles]'],'españa','IBM',100.00)
    g2=Guia('Raul',87,1.75)
    g3=Guia('Alberto',90,1.98)
    L=[g1,g2,g3]
    print(L)
    
    
    p1=Persona('Oscar',45,1.65)
    p2=Persona('Raul',87,1.75)
    p3=Persona('Alberto',90,1.98)
    L1=[p1,p2,p3]
    print(L1)
    
    print(isinstance(p1,Guia))
    print(Persona.__subclasses__())
    