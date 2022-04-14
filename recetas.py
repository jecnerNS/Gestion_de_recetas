from tkinter import *

ventana = Tk()
ventana.geometry("1000x500")
ventana.config(background="Blue")

menubar = Menu(ventana)
ventana.config(menu=menubar)


menubar.add_cascade(label="opcion1" )
menubar.add_cascade(label="opcion2")
menubar.add_cascade(label="opcion3")

Label(ventana, text='RECETARIO').place(x=439,y=25,width=100,height=20)

botonCrear = Button(ventana,text="CREAR",command="",background="CadetBlue")
botonCrear.place(x=100,y=140,width=100,height=40)

botonVer = Button(ventana,text="VER",command="",background="CadetBlue")
botonVer.place(x=300,y=140,width=100,height=40)

botonEditar = Button(ventana,text="EDITAR",command="",background="CadetBlue")
botonEditar.place(x=600,y=140,width=100,height=40)

botonBuscar = Button(ventana,text="BUSCAR",command="",background="CadetBlue")
botonBuscar.place(x=820,y=140,width=100,height=40)


#CUADRO DE TXT


listaBox = Listbox(ventana)
listaBox.place(relx=0.10,rely=0.4,relwidth=0.7,relheight=0.7)

Barra = Scrollbar(ventana, command=Listbox.yview)
Barra.place(relx=0.9, rely= 0.5, relheight=0.5)

listaBox.config(yscrollcommand=Barra)





# imagenes 
image1 = PhotoImage(file="imag1.png")
lbl_img = Label(ventana, image=image1)
lbl_img.place(x=100,y=40,width=120,height=60)


image2 = PhotoImage(file="imag2.png")
lbl_img = Label(ventana, image=image2)
lbl_img.place(x=800,y=40,width=120,height=60)










ventana.mainloop()