import socket


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('localhost',9999))
s.listen(1)
sc, addr = s.accept()
print('fuera bucle while')

while True:
    print ('entro')
    recibido = sc.recv (1024)
    recibido=recibido.decode('utf 8')
    if recibido == 'quit': break
    print('Recibido:', recibido.upper())
      
    sc.send(recibido.encode('utf 8'))
    print ('salgo')

print('fin comunicacion')
           
sc.close()
s.close()