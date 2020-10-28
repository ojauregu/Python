import sqlite3 as dbapi
from os.path import isfile

#print(dbapi.apilevel)
#print(dbapi.threadsafety)
#print(dbapi.paramstyle)
class Empleado:
    
    def __init__(self,dni='',nom='',dpo=''):
        
        self.dni=dni
        self.nom=nom
        self.dpo=dpo
    
    def __str__(self):
        
        return self.dni + ' ' + self.nom + ' ' + self.dpo

    def getTuple(self):
        
        return self.dni,self.nom,self.dpo

    
class EmpleadoDB:
    
    def __init__(self,path):
        self.path=path
        if not isfile(path):
            raise Exception ("No existe fichero " + path)
        
        self.con  = dbapi.connect(path)
    
    def create(self,emp):
        try:
            cur=self.con.cursor()
            sql='insert into empleados values(?,?,?)'
            cur.execute(sql, emp.getTuple())
            self.con.commit()
            return True
            
        except Exception as e:
            self.con.rollback()
            raise e
        
        finally:
            if cur:
                cur.close()
            
    
    def update(self,emp):
        pass
    
    def delete(self,dni):
        pass
    
    def read(self,dni):
        
        try:
            cur=self.con.cursor()            
            sql="Select * from empleados where dni=?"
            cur.execute(sql, (dni,))
            t = cur.fetchone()
           
            if t == None:
                raise Exception("El emp" + dni +" no existe")
            else:
                return t
        
        except Exception as e:
            raise e
        
        finally:
            if cur:
                cur.close()
    
    def select(self,dpo=''):
        try:
            cur=self.con.cursor()
            L= []

            if dpo:
                sql='Select * from empleados where departamento=?'
                cur.execute(sql, (dpo,))
            else:
                sql='Select * from empleados'
                cur.execute(sql)
            for t in cur.fetchall():
                L.append(Empleado(*t))
            return L
        
        except Exception as e:
            raise e
        
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if self.con:
            self.con.close()
           

if __name__ == "__main__":
    
    empDB=EmpleadoDB('C:\\Users\\n64258\\Documents\\Python Basico\\practicas\\intermedio I\\bbdd.dat')
    emp=Empleado('33516268-Y','Ana Perez','Seguridad')
    '''
    try:
        L=empDB.select()
        for i in L:
            print(i)
            
            
    except Exception as e:
        print(e)
    '''
    try:
        i=empDB.select()
        for t in i:
            print(t)

    except Exception as e:
        print(e)

