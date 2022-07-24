from tkinter import *
from tkinter import messagebox






lista = []

def guardar():
    nom = nombre.get()
    ape = apellido.get()
    co = correo.get()
    tel = telefono.get()
    lista.append(nom+"$"+ape+"$"+tel+"$"+co)
    ing_contacto()
    nom = nombre.set(" ")
    ape = apellido.set("")
    co = correo.set("")
    tel = telefono.set("")
    consulta()

def eliminar():
    eliminados.get()   
    removido = False
    for element in lista:
        arreglo = element.split("$")
        if eliminados.get()==arreglo[2]:
            lista.remove(element)
            removido= True
    ing_contacto()
    consulta()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado"+ " "+ eliminados.get())


def consulta():
    re = Text(root, width=80, height=15)
    lista.sort()
    valor=[]
    re.insert(INSERT,"Nombre\tApellido\t\tTelefono\t\tCorreo\n")
    for element in lista:
        arreglo = element.split("$")
        valor.append(arreglo[2])
        re.insert(INSERT,arreglo[0]+"\t"+arreglo[1]+"\t"+arreglo[2]+"\t"+arreglo[3])
        re.place(x=20, y=230)
        spinTelefono = Spinbox(root, value=(valor), textvariable=eliminados)
        spinTelefono.place(x=450, y=50)
    if lista == []:
         spinTelefono=Spinbox(root, value=(valor))
         spinTelefono.place(x=450, y=50)
    re.config(state=DISABLED)    

def inarchivo():
    txt_archivo =open("BD_py.txt", "a")
    txt_archivo.close()

def cargar():
    txt_archivo = open("BD_py.txt", "r")
    linea = txt_archivo.readline()
    if linea:
        while linea:
            if linea[-1]=="\n":
                linea=linea[:-1]
            lista.append(linea)
            linea = txt_archivo.readline()
    txt_archivo.close()

def ing_contacto():
        txt_archivo = open("BD_py.txt", "w")
        lista.sort()
        for element in lista:
            txt_archivo.write(element+"\n")
        txt_archivo.close()


root = Tk()
root.title("Agenda")
root.geometry("700x500")
colorfondo="#006"
colorletra="#FFF"
root.configure(background=colorfondo)
nombre = StringVar()
apellido = StringVar()
correo = StringVar()
telefono = StringVar()
#eliminar = StringVar()
eliminados = StringVar()
inarchivo()
cargar()
consulta()



tituloetiqueta = Label(root, text='Agenda Privada', fg=colorletra, bg=colorfondo)
tituloetiqueta.place(x=270, y=10)

nombreetiqueta =Label(root, text= 'Nombre', fg=colorletra, bg=colorfondo)
nombreetiqueta.place(x=50,y=50)

entrda1=Entry(root, textvariable=nombre)
entrda1.place(x=150, y=50)


apellidoetiqueta =Label(root, text= 'Apellido', fg=colorletra, bg=colorfondo)
apellidoetiqueta.place(x=50,y=80)


entrda2=Entry(root, textvariable=apellido)
entrda2.place(x=150, y=80)

telefonoetiqueta =Label(root, text= 'Telefono', fg=colorletra, bg=colorfondo)
telefonoetiqueta.place(x=50,y=110)


entrda3=Entry(root, textvariable=telefono)
entrda3.place(x=150, y=110)

correoetiqueta =Label(root, text= 'Correo', fg=colorletra, bg=colorfondo)
correoetiqueta.place(x=50,y=140)


entrda4=Entry(root, textvariable=correo)
entrda4.place(x=150, y=140)


eliminaretiqueta =Label(root, text= 'Eliminar', fg=colorletra, bg=colorfondo)
eliminaretiqueta.place(x=370,y=50)


spintelefono=Spinbox(root, text=eliminar)
spintelefono.place(x=470, y=50)

botonguardar=Button(root, text='Guardar', command=guardar, fg=colorletra, bg=colorfondo)
botonguardar.place(x=190, y=170)

botonEliminar=Button(root, text='Eliminar', command=eliminar, fg=colorletra, bg=colorfondo)
botonEliminar.place(x=520,y=80)


root.mainloop()