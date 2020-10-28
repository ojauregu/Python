import re

html='<p>Nombre</p><pi>Jorge</pi>'

etiqueta='p'

patron="<" + etiqueta + ">(.+)</" + etiqueta + ">"
print(patron)
obj = re.match(patron,html)

if obj:
    print(obj.group())
    print(obj.groups())
else:
    print('nada')