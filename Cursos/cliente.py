import socket
s = socket.socket ()
s.connect (('localhost', 9999))
print ('entro')
while True:
    mensaje = input('Mensaje ')
    if mensaje == '':
        print ('ponga algun valor')
    else:
        s.send (mensaje.encode ('utf 8'))
        recibido = s.recv(1024)
        recibido=recibido.decode ('utf 8')
        if mensaje == 'quit': break
        print('Recibido:', recibido)
          
print ('adios')

s.close ()