import sys,io,os

def getPath():
    dir_path= os.path.dirname(os.path.realpath(__file__))
    return dir_path

print(sys.argv)

if len(sys.argv) == 1:
    print ('falta parametro')
else:
    fichero=sys.argv[1]
    path=getPath()
    print(path)
    print(fichero)
    l=list(fichero.partition('.'))
    print (l[0])
    fichero_sal=''
    fichero_sal=l[0]+'_copia'+l[1]+l[2]
    print(fichero_sal)
    