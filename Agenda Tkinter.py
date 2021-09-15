from tkinter import *
from tkinter import messagebox

lista =  []


# A partir de aqui las funciones y procesos lógicos se inician


def save():
	n = nombre.get()
	ap = Ap.get()
	am = SegundoAp.get()
	c = Correo.get()
	t = Telefono.get()
	lista.append(n+"$"+ap+"$"+am+"$"+c+"$"+t)
	escribirContacto()
	messagebox.showinfo("Guardado", "El contacto ha sido guardado en la agenda")
	nombre.set("")
	Ap.set("")
	SegundoAp.set("")
	Telefono.set("")
	Correo.set("")
	consultar()


def delete():
	eliminado = conteliminar.get()
	removido = False
	for elemento in lista:
		arreglo = elemento.split("$")
		if conteliminar.get() == arreglo[3]:
			lista.remove(elemento)
			removido = True
	escribirContacto()
	consultar()
	if removido:
		messagebox.showinfo("Eliminado","El contacto fue eliminado con éxito: "+ eliminado)


def consultar():
	r = Text(ventana, width=85, height=15)
	lista.sort()
	valores = []
	r.insert(INSERT, "  Nombre\t\tApellido\t\tSegundo Ap\t\tCorreo\t\t    Telefono\t \n\n" )
	for elemento in lista:
		arreglo = elemento.split("$")
		valores.append(arreglo[3])
		r.insert(INSERT, "  " + arreglo[0]+ "\t\t" + arreglo[1] + "\t\t" + arreglo[2] + "\t"+ "   " + arreglo[3] + "\t\t"+ "    " + arreglo[4] + "\t\n")

	r.place(x=20,y=230)
	spinTelefono = Spinbox(ventana, value=(valores), textvariable=conteliminar).place(x=450, y=50)
	if lista==[]:
		spinTelefono = Spinbox(ventana, value=(valores)).place(x=450, y=50)

	r.config(state=DISABLED)	


def IniciarArchivo():
	archivo = open("ag.txt", "a")
	archivo.close()


def cargar():
	archivo = open("ag.txt", "r")
	linea = archivo.readline()
	if linea:
		while linea:
			if linea[-1] == '\n':
				linea = linea[:-1]
			lista.append(linea)
			linea = archivo.readline()
	archivo.close()


def escribirContacto():
	archivo = open("ag.txt", "w")
	lista.sort()
	for elemento in lista:
		archivo.write(elemento+"\n")
	archivo.close()


ventana = Tk()
nombre = StringVar()
Ap = StringVar()
SegundoAp = StringVar()
Correo = StringVar()
Telefono = StringVar()
conteliminar = StringVar()
ColordeFondo = "#571845"
ColorLetra = "#FFF"
IniciarArchivo()
cargar()
consultar()
ventana.geometry("725x500")
ventana.title("Agenda")
ventana.configure(background=ColordeFondo)
etiquetaTitulo = Label(ventana, text="Agenda de Contactos", bg=ColordeFondo, fg=ColorLetra, font=("Narkisim", 20)).place(x=250,y=10)
etiqueta_nombre = Label(ventana, text="Nombre: ", bg=ColordeFondo, fg=ColorLetra).place(x=50,y=50)
CajaN = Entry(ventana, textvariable=nombre).place(x=150,y=50)

# Apellido
etiqueta_apellido = Label(ventana, text="Apellido: ", bg=ColordeFondo, fg=ColorLetra).place(x=50,y=80)
CajaAp = Entry(ventana, textvariable=Ap).place(x=150,y=80)

# Apellido 2
etiqueta_segundoap = Label(ventana, text="Segundo Apellido: ", bg=ColordeFondo, fg=ColorLetra).place(x=50,y=110)
CajaSAp = Entry(ventana, textvariable=SegundoAp).place(x=150,y=110)

# Numero Telefonico
etiqueta_Telefono = Label(ventana, text="Nro. Telefonico: ", bg=ColordeFondo, fg=ColorLetra).place(x=50,y=140)
CajaT = Entry(ventana, textvariable=Telefono).place(x=150,y=140)

# Correo Electronico
etiqueta_Correo = Label(ventana, text="E-mail: ", bg=ColordeFondo, fg=ColorLetra).place(x=50,y=170)
CajaC = Entry(ventana, textvariable=Correo).place(x=150,y=170)

etiqueta_Eliminar = Label(ventana, text="Telefono: ", bg=ColordeFondo, fg=ColorLetra).place(x=370,y=50)
# Comienzo del spinbox
spinTelefono = Spinbox(ventana, textvariable=conteliminar).place(x=450,y=50)

# Botones 
botonGuardar = Button(ventana, text="Guardar", command=save, bg="#900c3e", fg="white").place(x=180,y=200)
botonElimininar = Button(ventana, text="Eliminar", command=delete, bg="#900c3e", fg="white").place(x=470,y=80)

ventana.mainloop()
