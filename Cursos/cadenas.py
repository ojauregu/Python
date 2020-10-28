"""
Pruebas con cadenas:

# Cadena raw - anula el efecto de los caracteres especiales

s = r"hola\tadios"
print(s)
s = 'hola\tadios'
print(s)
s = 'hola\nadios'
print(s)
s = "C:\\mis documentos\\cv.pdf"
print(s)
print("\"hola\"")


# La \ me permite partir lineas de codigo
texto = "Cadena raw - anula el" + \
    "efecto de los caracteres especiales"

# Buscar subcadenas:
path = "C:\mis documentos\hoja1.xlsx"
if 'documentos' in path:
    print('Existe documentos')


L = ['doc1.doc','CV.doc','tabla.xls','programa.exe']
print("Ficheros de Word:")
for f in L:
    # Si terminan en .doc
    if f[-4:]=='.doc':
        print(f)
'''


cad1='hola que tal'
cad2='que'
'''
print(cad1.find(cad2))


print(cad1.find('a'))
print(cad1.rfind('a'))

print(cad1.find('x'))

print(cad1.index('a'))
print(cad1.index('x'))

linea = "po;lo;ño;lk"
L = linea.split(';')
print(L)
s = 'pp||'.join(L)
print(s)

s = "C:\\mis documentos\\cv.pdf"

print(s.partition('.'))

s = "C:\\mis documentos\\cv.pdf"
L = ['doc1.doc','CV.docx','tabla.xls','programa.exe','pppp.pdf']
ex=('doc','docx','pdf')
for i in L:
    if i.partition('.')[2] in ex:
        print(i)
        
s=s.upper()
print(s)
 """
 
L=[1,2,3,4]
L2=[11,31,21,41]

L.append(9)

L.insert(1,99)

L.extend(L2)

print(L.index(31,4))
print(L)

L.sort(reverse=True)

print(L)
