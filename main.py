import tkinter
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from LecturaXML import *
import graphviz

lecture = None
Sistema = None
Mesag = None

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

        btnAyuda=tk.Button(root)
        btnAyuda["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnAyuda["font"] = ft
        btnAyuda["fg"] = "#000000"
        btnAyuda["justify"] = "center"
        btnAyuda["text"] = "Ayuda"
        btnAyuda.place(x=160,y=30,width=150,height=20)
        btnAyuda["command"] = self.btnAyuda

        btnGestionDrones = tk.Button(root)
        btnGestionDrones["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        btnGestionDrones["font"] = ft
        btnGestionDrones["fg"] = "#000000"
        btnGestionDrones["justify"] = "center"
        btnGestionDrones["text"] = "Gestion de Drones"
        btnGestionDrones.place(x=6, y=30, width=150, height=20)
        btnGestionDrones["command"] = self.VentanaMsjListado

        opciones = ["Listado de Mensajes","Ver Instrucciones para Mandar Mensaje"]
        self.cmbMensaje = ttk.Combobox(root,values=opciones)
        self.cmbMensaje.bind("<<ComboboxSelected>>",self.seleccionado)
        self.cmbMensaje.place(x=4,y=60)


    def seleccionado(self,event):
        seleccion = self.cmbMensaje.get()
        if seleccion == "Listado de Mensajes":
            print("Ha seleccionado la opcion de Listado de Mensajes")
            self.VentanaMsjListado()

    def VentanaMsjListado(self):
        ventanitaM = tkinter.Toplevel()
        ventanitaM.geometry("800x300")
        ventanitaM.title("Gestion Drones")
        lblIngreso = tkinter.Label(ventanitaM, text="Listado de Mensajes")
        lblIngreso.grid(row=0, column=10)
        self.txt = tk.Text(ventanitaM, width=40, height=15)
        self.txt.grid(row=1, column=5, padx=30,columnspan=60)
        btnMostrar = tkinter.Button(ventanitaM, text="Mostrar Listado", command = lambda : [self.txt.delete("1.0", tk.END),self.MostrarLstMensaje()])
        btnMostrar.place(x=140,y=270)
        lblSelecMensaje = tkinter.Label(ventanitaM,text="Ingrese el nombre del Mensaje")
        lblSelecMensaje.place(x=500,y=5)
        MensajePorMostrar = tkinter.Entry(ventanitaM,width=45)
        MensajePorMostrar.place(x=450,y=30)
        btnMostraSistemaMensaje = tkinter.Button(ventanitaM,text="Mostrar Mensaje", command = lambda : [self.BusquedaMensaje(MensajePorMostrar.get())])
        btnMostraSistemaMensaje.place(x= 545,y =60)
        self.salidaInstrucciones = tkinter.Text(ventanitaM,height=10,width=50)
        self.salidaInstrucciones.place(x=375,y=100)

    def verificacionSistema(self,TextoEnEntrada):
        lstMensajes = Mesag
        msgADesencriptar = TextoEnEntrada
        print(msgADesencriptar)

        for i in range(lstMensajes.getSize()):
            tempLst = lstMensajes.buscarID(i)
            name = tempLst.getNombreM()
            NombreDelSistema = tempLst.getNombreListaSistemas()
            ListaIntrucciones = tempLst.getInstrucciones()
            if name == msgADesencriptar:
                print("Se encontro el mensaje: ",name)
                return NombreDelSistema,ListaIntrucciones

    def BusquedaMensaje(self,TextoEntrada):

        lstMensaje = Mesag
        msgABuscar = TextoEntrada

        nombre,Lista = self.verificacionSistema(msgABuscar)
        self.salidaInstrucciones.insert(tkinter.END,"--------Sistema de Drones a utilizar: "+nombre+"--------\n")
        print (nombre,Lista)




    def MostrarLstMensaje(self):
        lstMsg = Mesag

        for i in range(lstMsg.getSize()):
            nm = lstMsg.buscarID(i)
            print(nm.getNombreM())
            print(nm.getNombreListaSistemas())
            self.txt.insert(tkinter.END,"--------Nombre del Mensaje: "+str(nm.getNombreM())+"--------\n")
            inst = nm.getInstrucciones()
            for j in range (inst.getSize()):
                actual_ins = inst.buscarID(j)
                actual_ins.getDron()
                actual_ins.getInstruccionMsg()
                self.txt.insert(tkinter.END,str("INSTRUCCIÓN: "+actual_ins.getDron())+" "+str(actual_ins.getInstruccionMsg())+"\n")



    def btnInicializar(self):
        print("Apartado de incicializacion")


    def btnCarga(self):
        global lecture
        global Sistema
        global Mesag
        print("Carga de Archivos")
        name = tkinter.filedialog.askopenfilename()
        if name:
            lectura = LecturaXML(name)
            lectura.getDrones()
            lecture = lectura.getListaDrones()
            Sistema = lectura.getListaSistemaDrones()
            Mesag = lectura.getListaMensajes()
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
        self.graficarSistemas(sistema)
        self.crearG(sistema)


    def graficarSistemas(self,ListaSistemaDrone):
        sistema = ListaSistemaDrone
        g = graphviz.Digraph('G',filename="graficaSistemas.gv")
        g.format = 'png'

        for i in range(sistema.getSize()):
            actualS = sistema.buscarID(i)
            print("Nombre Sistema: ", actualS.getNombre(), "Altura Max: ", actualS.getAlturaMax(), " Cantidad Drones: ",actualS.getCantidadD())
            contenido = actualS.getContenido()
            g.node(str(actualS.getNombre()))
            g.node(str(actualS.getAlturaMax()))
            g.node(str(actualS.getCantidadD()))
            g.edge(str(actualS.getNombre()),str(actualS.getAlturaMax()))
            g.edge(str(actualS.getNombre()),str(actualS.getCantidadD()))
            print("cantidad de Valores en Contenido: ", contenido.getSize())
            for j in range(contenido.getSize()):
                cnt = contenido.buscarID(j)
                print(cnt.getNombreDron())
                alturas = cnt.getListaAlturas()
                g.node(str(cnt.getNombreDron()))
                g.edge(str(actualS.getNombre()),str(cnt.getNombreDron()))
                for k in range(alturas.getSize()):
                    actualAltura = alturas.buscarID(k)
                    print("Valor: ", actualAltura.getNValor(), "Altura: ", actualAltura.getDatoAltura())

        g.render()

    def crearG(self,listaSistema):

        sistema = listaSistema



    def btnMensajes(self):
        print("Apartado de Gestion de Mensajes")


    def btnAyuda(self):
        print("Apartado ayuda")

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
