from tkinter import *



def codigoBoton():
    print('boton')
    miNombre.set('Juan')
    
    




raiz=Tk()

miframe=Frame(raiz,width=500, height=400)

miframe.pack()

miNombre=StringVar()

miLabel= Label(miframe,textvariable=miNombre,text='Hola campeon',fg='red', font=('Comic Sans MS',24)).grid(row=0,column=0,sticky='w',padx=10,pady=10)
cuadroTexto=Entry(miframe,fg='green',bg='blue', font=('Comic Sans MS',24)).grid(row=0,column=1)

miLabel= Label(miframe,text='Hola ',fg='yellow', font=('Comic Sans MS',24)).grid(row=1,column=0,sticky='w',padx=10,pady=10)
cuadroTexto=Entry(miframe,fg='green',bg='red', font=('Comic Sans MS',24),justify='center').grid(row=1,column=1)

miLabel= Label(miframe,text='Hola perdedor',fg='yellow', font=('Comic Sans MS',24)).grid(row=0,column=2,sticky='w',padx=10,pady=10)
cuadroTexto=Entry(miframe,fg='green',bg='red', font=('Comic Sans MS',24),show='*').grid(row=0,column=4)

miLabel= Label(miframe,text='Hola ',fg='yellow', font=('Comic Sans MS',24)).grid(row=1,column=2,sticky='w',padx=10,pady=10)
cuadroTexto=Entry(miframe,fg='green',bg='red', font=('Comic Sans MS',24)).grid(row=1,column=4)





miLabel= Label(miframe,text='Comentarios  ',fg='black', font=('Comic Sans MS',24)).grid(row=2,column=0,sticky='w',padx=10,pady=10)
textoComentario=Text(miframe,width=20,height=5,fg='green',bg='red', font=('Comic Sans MS',24)).grid(row=2,column=1)

#scrollVert=Scrollbar(miframe,command=textoComentario.yview)

scrollVert=Scrollbar(miframe, command=textoComentario).grid(row=2,column=2,sticky='nsew')

botonEnvio=Button(raiz,text='Enviar',command=codigoBoton)

botonEnvio.pack()

raiz.mainloop()