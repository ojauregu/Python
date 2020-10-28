import abc

class Servicio(abc.ABC):
        
    def __init__(self,importe=0):
        self.importe=importe    
    
    @abc.abstractmethod
    def calcularImporte(self):
        pass
    
