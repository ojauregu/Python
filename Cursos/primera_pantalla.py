from tkinter import *

raiz=Tk()
raiz.title('Ventana de pruebas')

raiz.resizable(True,True)

raiz.config(bg='cyan')

miFrame=Frame()

miFrame.pack()



miFrame.config(bd=35,bg='red',relief='sunken',cursor='pirate')

miFrame.config(width='650',height='350')


raiz.mainloop()