"""
Implementar un cajero para el desglose de billetes:
Leer una cantidad que tiene que ser multiplo de 10, si no, se rechaza
Dar la cantidad de cada billete: Por ejemplo: 320 --> 3 de 100, 1 de 20.
"""
# Validacion:
while True:
    cantidad = int(input("Teclear importe: "))
    if cantidad % 10 == 0:
        break

# Calcular el desglose:    
tipos_billete = [500,200,100, 50, 20, 10]
billetes = dict()

for b in tipos_billete:
    if cantidad >= b:
        billetes[b] = cantidad // b
        cantidad = cantidad % b
    

    if cantidad == 0: break
    
    
for k,i in billetes.items():
    if i == 1:
        print(i,' billete de ', k, ' Euros')    
    else:    
        print(i,' billetes de ', k, ' Euros')       

"""
d2 = {100:0, 50:0, 20:0, 10:0}
cantidad = 340
for b, cont in d2.items():
    numBilletes = cantidad // b
    print(cantidad,b,numBilletes)
"""

