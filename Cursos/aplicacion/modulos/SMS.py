from modulos.servicio import Servicio

class SMS(Servicio):
    
    def __init__(self,importe=0.0):
        Servicio.__init__(self,importe)
        
    def calcularImporte(self):
        return self.importe
    