import os

d={}

fich=(os.listdir())
for i in fich:
    if '.' in i:
        key = i.partition('.')[2]
    else:
        key = 'dir'

    if key in d:
        d[key] +=1
    else:
        d[key]=1   

for k,v in d.items():
    print (k,v)    
