from tkinter import *

ventana = Tk()

ventana.geometry("1000x500")
ventana.title("APLICACION DE RECETAS")
ventana.config(background="Black")
frame1 = Frame(ventana,width=860,height=190, background="CadetBlue").pack()



menubar = Menu(ventana)
ventana.config(menu=menubar)

def enviar(entry1,entry2,entry3):
    listaBox.insert(END,'INGREDIENTES : ', entry1)
    listaBox.insert(END,'PREPARACION : ', entry2)
    listaBox.insert(END,'RECOMENDACIONES : ', entry3)
    listaBox.insert(END,'---------------------------------------------------------------------------- ')






entry1 = StringVar()
entry2 = StringVar()
entry3 = StringVar()










menubar.add_cascade(label="opcion1" )
menubar.add_cascade(label="opcion2")
menubar.add_cascade(label="opcion3")



Label(ventana,text='RECETARIO').place(x=439,y=25,width=100,height=20)
Label(ventana, text='Ingredientes').place(x=100,y=100,width=100,height=20)
Label(ventana, text='Preparacion').place(x=130,y=130,width=100,height=20)
Label(ventana, text='Recomendaciones').place(x=160,y=160,width=100,height=20)

# ----
botonCrear = Button(ventana,text="CREAR",command= lambda:enviar(entry1.get(),entry2.get(),
entry3.get()),background="CadetBlue")
botonCrear.place(x=700,y=120,width=100,height=40)

cuadro_entry1 = Entry(ventana, textvariable= entry1)
cuadro_entry1.place(x=268,y=100,width=400,height=20)
cuadro_entry2 = Entry(ventana,textvariable= entry2)
cuadro_entry2.place(x=268,y=130,width=400,height=20)
cuadro_entry3 = Entry(ventana,textvariable= entry3)
cuadro_entry3.place(x=268,y=160,width=400,height=20)

#-----


botonVer = Button(ventana,text="VER",command="",background="CadetBlue")
botonVer.place(x=840,y=98,width=80,height=20)

botonEditar = Button(ventana,text="EDITAR",command="",background="CadetBlue")
botonEditar.place(x=840,y=120,width=80,height=20)

botonBuscar = Button(ventana,text="BUSCAR",command="",background="CadetBlue")
botonBuscar.place(x=840,y=142,width=80,height=20)


#CUADRO DE TXT


listaBox = Listbox(ventana)
listaBox.place(relx=0.07,rely=0.4,relwidth=0.8,relheight=0.5)

Barra = Scrollbar(ventana, command=listaBox.yview)
Barra.place(relx=0.91, rely= 0.4,relwidth=0.02, relheight=0.5)

listaBox.config(yscrollcommand=Barra)





# imagenes 
image1 = PhotoImage(file="imag1.png")
lbl_img = Label(ventana, image=image1)
lbl_img.place(x=100,y=10,width=120,height=60)


image2 = PhotoImage(file="imag2.png")
lbl_img = Label(ventana, image=image2)
lbl_img.place(x=800,y=10,width=120,height=60)


# frame










ventana.mainloop()