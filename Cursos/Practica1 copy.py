'''

def geneAlf():
    alf = "".join(chr(i)+chr(i+32) for i in range(65,65+26))
    return alf

print(geneAlf())
'''
'''
L = [1, 2,3,4,5,6,7]
L2 = list (filter (lambda n: n % 2.0 == 0 , L))
print (L2)

L=[('pepe',80,1.79), ('juan',98,1.50),('pedro',56,1.80),('raul',76,1.98)]
print (L)
L.sort(key=lambda t:t[2],reverse=True)
print(L)


l2 = (n ** 2 for n in range(10))
print(l2)
for i in l2:
    print(i)

'''

def gen1(ini,fin,sal=1):
    
    def esPrimo(numero):
        for i in range(2,numero):
            if numero % i == 0:
                return False
        return True
    
    i=ini
    
    while i<fin:
        if esPrimo(i):
            yield i
        i += sal
    
    
    
print('Primos')
for i in gen1(1,100):
    print(i,end=' ' )