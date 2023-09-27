import tkinter
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from LecturaXML import *

lecture = None
Sistema = None

class Menu:
    def __init__(self, root):
        root.title("Menu Principal")
        width=820
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        btnInicializar=tk.Button(root)
        btnInicializar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnInicializar["font"] = ft
        btnInicializar["fg"] = "#000000"
        btnInicializar["justify"] = "center"
        btnInicializar["text"] = "Inicializar Sistema"
        btnInicializar["border"] = "1px"
        btnInicializar.place(x=5,y=5,width=150,height=20)
        btnInicializar["command"] = self.btnInicializar

        btnCarga=tk.Button(root)
        btnCarga["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnCarga["font"] = ft
        btnCarga["fg"] = "#000000"
        btnCarga["justify"] = "center"
        btnCarga["text"] = "Cargar Archivo XML"
        btnCarga.place(x=160,y=5,width=150,height=20)
        btnCarga["command"] = self.btnCarga

        btnGenerar=tk.Button(root)
        btnGenerar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnGenerar["font"] = ft
        btnGenerar["fg"] = "#000000"
        btnGenerar["justify"] = "center"
        btnGenerar["text"] = "Generar archivo XML"
        btnGenerar.place(x=315,y=5,width=150,height=20)
        btnGenerar["command"] = self.btnGenerar

        btnGestionD=tk.Button(root)
        btnGestionD["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnGestionD["font"] = ft
        btnGestionD["fg"] = "#000000"
        btnGestionD["justify"] = "center"
        btnGestionD["text"] = "Gestión de drones"
        btnGestionD.place(x=470,y=5,width=150,height=20)
        btnGestionD["command"] = self.btnGestionD

        btnGestionS=tk.Button(root)
        btnGestionS["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnGestionS["font"] = ft
        btnGestionS["fg"] = "#000000"
        btnGestionS["justify"] = "center"
        btnGestionS["text"] = "Gestion de Sistemas de Drones"
        btnGestionS.place(x=625,y=5,width=180,height=20)
        btnGestionS["command"] = self.btnGestionS

        btnMensajes=tk.Button(root)
        btnMensajes["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnMensajes["font"] = ft
        btnMensajes["fg"] = "#000000"
        btnMensajes["justify"] = "center"
        btnMensajes["text"] = "Gestión de Mensajes"
        btnMensajes.place(x=5,y=30,width=150,height=20)
        btnMensajes["command"] = self.btnMensajes

        btnAyuda=tk.Button(root)
        btnAyuda["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnAyuda["font"] = ft
        btnAyuda["fg"] = "#000000"
        btnAyuda["justify"] = "center"
        btnAyuda["text"] = "Ayuda"
        btnAyuda.place(x=160,y=30,width=150,height=20)
        btnAyuda["command"] = self.btnAyuda


    def btnInicializar(self):
        print("Apartado de incicializacion")


    def btnCarga(self):
        global lecture
        global Sistema
        print("Carga de Archivos")
        name = tkinter.filedialog.askopenfilename()
        if name:
            lectura = LecturaXML(name)
            lectura.getDrones()
            lecture = lectura.getListaDrones()
            Sistema = lectura.getListaSistemaDrones()
            print(lecture)



    def btnGenerar(self):
        print("Apartado de generar")


    def recorrido(self,dron):
        dr = dron.getInicio()
        txt = dr.getDato().getNombre() + "\n"
        while dr.getSiguiente():
            dr = dr.getSiguiente()
            txt += dr.getDato().getNombre() + "\n"
        return txt

    def dronAgr(self,nombreD):
        global lecture
        dron = lecture
        nombre = nombreD
        nombreDron = Dron(nombre)
        dron.agregar(nombreDron)


    def btnGestionD(self):
        global lecture
        dron = lecture
        print("Apartado Gestion Drones")
        ventanita = tk.Toplevel()
        ventanita.geometry("400x325")
        ventanita.title("Gestion Drones")
        lblListadoDron = tk.Label(ventanita, text="Listado de Drones Actuales")
        lblListadoDron.grid(row=0, column=0)
        txt = tk.Text(ventanita,width=20,height=15)
        txt.grid(row=1,column=0,padx=10)
        btnMostrar = tk.Button(ventanita, text="Mostrar",
        command=lambda: [txt.delete("1.0", tk.END), txt.insert("1.0", self.recorrido(dron))])
        btnMostrar.grid(row=2, column=0)

        lblNDron = tk.Label(ventanita,text="Ingrese el Nombre del dron a Agregar\n (El Nombre debe ser diferente)")
        lblNDron.grid(row=0, column=2,pady=10)
        txtDirec = tkinter.Entry(ventanita)
        txtDirec.grid(row=1, column=2, pady=1)
        btnAceptar = tkinter.Button(ventanita, text="Aceptar", command = lambda : self.dronAgr(txtDirec.get()))
        btnAceptar.grid(row=2, column=2, pady=1)









    def btnGestionS(self):
        global Sistema
        print("Apartado Gestion Sistema de drones")

        sistema = Sistema

        for i in range(sistema.getSize()):
            actualS = sistema.buscarID(i)
            print("Nombre Sistema: ",actualS.getNombre(),"Altura Max: ",actualS.getAlturaMax()," Cantidad Drones: ",actualS.getCantidadD())
            contenido = actualS.getContenido()
            print("cantidad de Valores en Contenido: ", contenido.getSize())
            for j in range(contenido.getSize()):
                cnt = contenido.buscarID(j)
                print(cnt.getNombreDron())
                alturas = cnt.getListaAlturas()
                for k in range(alturas.getSize()):
                    actualAltura = alturas.buscarID(k)
                    print("Valor: ",actualAltura.getNValor(),"Altura: ",actualAltura.getDatoAltura())



    def btnMensajes(self):
        print("Apartado de Gestion de Mensajes")


    def btnAyuda(self):
        print("Apartado ayuda")

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
