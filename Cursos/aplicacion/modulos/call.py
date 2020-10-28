from modulos.servicio import Servicio

class Call(Servicio):

    def __init__(self,importe=0.0,segundos=0.0):
        Servicio.__init__(self,importe)
        self.segundos=segundos
    
    def calcularImporte(self):
        return self.segundos * self.importe
