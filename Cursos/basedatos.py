import sqlite3 as dbapi
from os.path import isfile

#print(dbapi.apilevel)
#print(dbapi.threadsafety)
#print(dbapi.paramstyle)








def testConexion(path,query):
    con = None
    cur=None
    try:
        if not isfile(path):
            raise Exception ("No existe fichero " + path)
        con = dbapi.connect(path)
        cur = con.cursor()
        dpo=input('Depart: ')
        #cur.execute(query)
        cur.execute(query,(dpo,))

        cols=(t for t in cur.description)

        for i in cols:
            print(i[0])
            
        for empl in cur.fetchall ():
            print (empl)
        
    
    except Exception as e:
        print ('Error ', e, e.__class__.__name__)
        
    
    finally:
        
        if cur !=None:
            cur.close()        
        if con !=None:
            con.close()
            

if __name__ == "__main__":
    
    
    query="select * from Empleados where departamento =  ?"
    #query="select * from Empleados"
    
    path='C:\\Users\\n64258\\Documents\\Python Basico\\practicas\\intermedio I\\bbdd.dat'
    #testConexion(path,query)
    
    testConexion(path,query)
    
    
    




''''
bbdd=dbapi.connect('C:\\Users\\n64258\\Documents\\Cursos\\bbdd\\prueba.db')
bbdd=dbapi.connect('C:\\Users\\n64258\\Documents\\Python Basico\\practicas\\intermedio I\\bbdd.dat')
cursor=bbdd.cursor()

cursor.execute("insert into empleados values ('12345678-A','Manuel Gil','Contabilidad'")

bbdd.commit()


cursor.execute("select * from Empleados")

for tupla in cursor.fetchall ():
    print (tupla)

cursor.close()
bbdd.close()
'''