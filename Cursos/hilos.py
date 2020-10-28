from threading import Thread
from threading import Lock
from time import sleep
class Hilo(Thread):
    def __init__(self, id, num=5):
        Thread.__init__(self)
        self.num = num
        self.id= id
    def run(self):

        for i in range(self.num):
            print('hilo ' , self.id ,'mensaje ',i)
            sleep(1.5)
        print('termina hilo ', self.id)        

iter=1000000
contador=0

def hiloSuma():
    global contador
    

    for i in range(iter):
        contador+=1

        
def hiloResta():
    global contador
    for i in range(iter):
        contador-=1

if __name__ == "__main__":

    print ('Soy el hilo principal')
    
    hilo1 = Thread(target=hiloSuma)
    hilo2 = Thread(target=hiloResta)
    
    hilo1.start()
    hilo2.start()
    
    hilo1.join()
    hilo2.join()
    
    print ('contador ', contador)
    
    print ('Soy el hilo principal termino')
    
    ''''
    L=[]
    for i in range(0, 5):
        t = Hilo((i+1))
        t.start()
        L.append(t)
    # Ojo, si ejecutamos join, hilo a hilo hace que los hilos se ejecuten uno detrás de otro.
        for h in L:
            h.join()
    # Si no se lanza join, main termina pero los hilos continúan ejecutándose.
    '''

    