from modulos.call import Call

class CallInt(Call):

    def __init__(self,importe=0.0,segundos=0.0,cuota=0.0):
        Call.__init__(self,importe,segundos)
        self.cuota=cuota
    
    def calcularImporte(self):
        return super().calcularImporte() + self.cuota