import re

def cumplePatron(patron,cadena):
    if re.match (patron, cadena):
        return True
    else:
        return False
    
    
def validaMatricula(matricula):
    #patron='[0-9]{4}[BCDFGHJKLMNPRSTVWXYZ]{3}'
    patron='\d{4}[BCDFGHJKLMNPRSTVWXYZ]{3}$'
    
    return cumplePatron(patron,matricula)

def validaCodigo(codigo):
    #patron='[0-9]{4}[BCDFGHJKLMNPRSTVWXYZ]{3}'
    patron= r'(COD|S/N)_[AEIOU]{3}_[1-9]\d{5}$'
    
    return cumplePatron(patron,codigo)




'''
print (cumplePatron("abc","abc"))
print (cumplePatron(".bc","abc"))
print (cumplePatron("abc",".bc"))
print (cumplePatron("abc","abc9999"))
print (cumplePatron("abc8","abc9999"))
print (cumplePatron("...\.","123."))

print (cumplePatron("abc|bbc|vbv","bbc9999"))
'''
L=['33516268R', '33516267U','a12345678']

patron = ("[0-9]" *8) + "[A-Z]"

L2 = [ (cumplePatron(patron,i)) for i in L]

print(L)
print(L2)

L3=['76541nAD', '8888JJJ','124RKD','4123KKKF']

L4 = [ (validaMatricula(i)) for i in L3]

print(L3)
print(L4)



L5=['COD_AEE_800999', 'S/N_UOO_123456','S/N_UOO_1234564','SIN_UOO_123456','S/N_UOO_023456','COD_UOO_023456','COD_UOO_1233456']

#L6 = [ (validaCodigo(i)) for i in L5]

for i in L5:
    print(i,validaCodigo(i))

patron= r'(COD|S/N)_[AEIOU]{3}_[1-9]\d{5}'
s="EL apara COD_AEE_800999 es valido"
print(s, re.search(patron,s))