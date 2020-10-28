class Empleado:
    
    def __init__(self,empresa='',sueldo=0.0):
        self.empresa=empresa
        self.sueldo=sueldo
        
    def __str__(self):
        return self.empresa + ' ' + str(self.sueldo)