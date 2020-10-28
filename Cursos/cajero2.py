def cajero(importe):
    
    tipos_billete = [200,100,50,20,10]
    billetes = dict()

    for b in tipos_billete:
        if importe >= b:
            billetes[b] = importe // b
            importe = importe % b
        if importe == 0: break
        
    return(billetes)

if __name__ == "__main__":
    
    cantidad = int(input("Teclear importe: "))
    
    for k,i in cajero(cantidad).items():
        if i == 1:
            print(i,' billete de ', k, ' Euros')    
        else:    
            print(i,' billetes de ', k, ' Euros')       