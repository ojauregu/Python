def prueba(a=1,b=2,c=3):
    print(a,b,c)
          

def prueba2(p1,p2,o1=0,o2=0,*args):
    print(p1,p2)
    print(o1,o2)
    print (args)
     
'''
prueba2(1,2)
print()
prueba2(1,2,3,4)
print()
prueba2(1,2,3,4,5,6,7,8)
print()
'''

def prueba3(**kwargs):
    for k,i in kwargs.items():
        print (k,i)

prueba3(a=1,b=2,c=3)