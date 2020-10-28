'''
pruebas con dict
'''

d = {'ana':123,'jose':345,'gema':678}
'''
print(list(d.items()))
print(list(d.keys()))
print(list(d.values()))

l = list(d.values())
'''
ext = 123
'''
if ext in l:
    print ('existe')
else:
    print('no existe')
'''
d2 = {'ana':999,'pepe':876}

print(d)

d.update(d2)

print(d)

d3=d.copy()

print(d3)

d['olga']=745

print(d3)
print(d)