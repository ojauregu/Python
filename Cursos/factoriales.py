def factR(n):
    '''
    crea factorial recusrsivo
    '''
    return 1 if n==1 else n*factR(n-1)

def fact(n):
    '''
    crea factorial iterativo
    '''
    resul=1
    for i in range(1,n+1):
        resul *=i
    return resul

if __name__ == "__main__":
    
    print (fact(5))
    print(factR(5))
    
    
