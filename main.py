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
        btnGenerar["command"] = self.salida

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
        btnGestionDrones["text"] = "Gestion de Mensajes"
        btnGestionDrones.place(x=6, y=30, width=150, height=20)
        btnGestionDrones["command"] = self.VentanaMsjListado




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
                return NombreDelSistema,ListaIntrucciones


    #funcion princpal Para Desencriptado de Mensaje
    def BusquedaMensaje(self,TextoEntrada):
        lstDrones = lecture
        lstMensaje = Mesag
        msgABuscar = TextoEntrada
        contador = 0

        #obtiene el nombre del Sistema a usar y La lista completa con las instrucciones
        nombreSistemaDrone,ListaInstrucciones = self.verificacionSistema(msgABuscar)
        # se inserta a el txt el sistema
        self.salidaInstrucciones.insert(tkinter.END,"--------Sistema de Drones a utilizar: "+nombreSistemaDrone+"--------\n")
        # a partir del nombre obtenido anteriormente se obtiene la lista con todos los datos
        ListaSistemaCompleto = self.RegresarDatosSistema(nombreSistemaDrone)
        #aqui se imprime el nombre del sistema, altura, y cantidad de drones dentro de
        print(ListaSistemaCompleto.getNombre(),ListaSistemaCompleto.getAlturaMax(),ListaSistemaCompleto.getCantidadD(),"todo se ve bien jefe")
        tmp = ListaSistemaCompleto.getContenido()
        mensaje = ""
        #primer intento de obtener el mensaje, problemas con el orden y los comandos
        while not ListaInstrucciones.estaVacia():
            tmpLst = ListaInstrucciones.getInicio()
            segCont = 0
            #por cada for unicamente un dron hara una iteracion
            for i in range(0,int(ListaSistemaCompleto.getCantidadD())):
                temp = tmp.buscarID(i)
                conta = i
                if contador == 0:
                    alturaAct = temp.setAlturaActual(temp.getListaAlturas().getInicio())
                    alturaA = temp.getAlturaActual()
                    altura = temp.getListaAlturas().getInicio()
                    print(temp.getNombreDron(),"Subir")
                else:
                    print(temp.getNombreDron())
                    if temp.getNombreDron() == tmpLst.getDato().getDron():
                        if temp.getAlturaActual().getDato().getNValor() < tmpLst.getDato().getInstruccionMsg():
                            temp.setAlturaActual(temp.getAlturaActual().getSiguiente())
                            print("----",temp.getNombreDron(), " subir----")
                            self.salidaInstrucciones.insert(tkinter.END, f"{temp.getNombreDron()} subir\n")
                            instruccion = TiempoLuz(temp.getNombreDron(),"Subir",contador)
                        elif temp.getAlturaActual().getDato().getNValor() > tmpLst.getDato().getInstruccionMsg():
                            temp.setAlturaActual(temp.getAlturaActual().getAnterior())
                            print(temp.getNombreDron(), " bajar")
                            self.salidaInstrucciones.insert(tkinter.END, f"{temp.getNombreDron()} Bajar\n")
                        elif temp.getAlturaActual().getDato().getNValor() == tmpLst.getDato().getInstruccionMsg():
                            mensaje += temp.getListaAlturas().buscarID(int(tmpLst.getDato().getInstruccionMsg())-1).getDatoAltura()
                            self.salidaInstrucciones.insert(tkinter.END, f"{temp.getNombreDron()} Emitiendo Luz\n")
                            print(temp.getNombreDron(),"Emitir Luz")
                            ListaInstrucciones.eliminar(0)
            contador += 1
            print("El contador va: ",contador)
        print("El mensaje es: ",mensaje)
        self.salidaInstrucciones.insert(tkinter.END,"El Mensaje es: " + mensaje + "\n")
        self.salidaInstrucciones.insert(tkinter.END, "El tiempo es: " + str(contador) + "\n")

        '''while not ListaInstrucciones.estaVacia():
            if contador == 1:
                for j in range(int(ListaSistemaCompleto.getCantidadD())):
                    pass
            else:'''


        '''while not ListaInstrucciones.estaVacia():
            inst = ListaInstrucciones.getInicio()
            dron = ListaInstrucciones.getInicio().getDato().getDron()
            print("institucion ",inst.getDato().getInstruccionMsg(),"drone", dron)
            ListaInstrucciones.eliminar(0)'''


        #este ciclo es para cada uno de los sistemas
        '''for i in range(int(ListaSistemaCompleto.getCantidadD())): # aqui ejecuta el sistema
            temp = tmp.buscarID(i)
            print(temp.getNombreDron())
            #ciclo para las intrucciones
            altura = temp.getListaAlturas().getInicio()

            while not ListaInstrucciones.estaVacia():
                tmpLst = ListaInstrucciones.getInicio()
                if temp.getNombreDron() == tmpLst.getDato().getDron():
                    print("se encontro coinidicencia en el dron: ", temp.getNombreDron())

                    if altura.getDato().getNValor() == tmpLst.getDato().getInstruccionMsg():
                        print("encontrado y guardado", altura.getDato().getDatoAltura())
                        ListaInstrucciones.eliminar(0)
                    if altura.getDato().getNValor() < tmpLst.getDato().getInstruccionMsg():
                        print("Es menor")
                        altura = altura.getSiguiente()
                    if altura.getDato().getNValor() > tmpLst.getDato().getInstruccionMsg():
                        print("Es mayor")
                else:
                    print("debe ir a: ",tmpLst.getDato().getInstruccionMsg(),tmpLst.getDato().getDron(),altura.getDato().getNValor(),altura.getDato().getDatoAltura())'''



        '''still,indice = self.comprobacion(temp.getNombreDron(),ListaInstrucciones)
        if still == True:
            pass
        elif still == False:
            break'''
        '''for l in range(ListaInstrucciones.getSize()):
            u = tmpTT.getDato().getDron()
            print(u)
            if tmpTT.getDato().getDron() == temp.getNombreDron():
            tmpTT = tmpTT.getSiguiente()'''


            #debo quitar el ciclo o de lo contraio se reiniciara
        '''for p in range(ListaInstrucciones.getSize()):
            tmpLstI = ListaInstrucciones.buscarID(p)
            #print(tmpLstI.getDron())
            lstA = temp.getListaAlturas()
            lstAA = lstA.getInicio()
            #si se encuentra el dron en las instrucciones
            if temp.getNombreDron() == tmpLstI.getDron():
                # se verifica si el dron esta en el mensaje
                print(f"El {temp.getNombreDron()} se encuentra en la lista de instrucciones, su instruccion es ir a altura {tmpLstI.getInstruccionMsg()}")

                #se empieza a recorrer la lista de la lista sistema
                #el uso de ciclos puede causar problemas, se deben recorrer nodos
                #para aplicar las condicionales
                while tmpLstI:
                    print(lstAA.getDato().getNValor(),lstAA.getDato().getDatoAltura())
                    if int(tmpLstI.getInstruccionMsg()) > int(lstAA.getDato().getNValor()):
                        print("La altura esta mas arriba")
                        lstAA = lstAA.getSiguiente()
                    elif tmpLstI.getInstruccionMsg() < lstAA.getDato().getNValor():
                        print("La altura esta mas abajo")
                        lstAA =  lstAA.getAnterior()
                    elif tmpLstI.getInstruccionMsg() == lstAA.getDato().getNValor():
                        print("Esta en la altura deseada")
                        break'''
        '''print(lst)'''
        '''for l in range(lstA.getSize()):
            tmpAlt = lstA.buscarID(l)
            #se imprime la altura y el dato en esa altura
            print(tmpAlt.getNValor(),tmpAlt.getDatoAltura())
            #condicion en caso que se encuentre en esa altura
            if tmpLstI.getInstruccionMsg() == tmpAlt.getNValor():
                print("Se encuentra en la posicion Adecuada, altura ",tmpAlt.getNValor())
                mensaje += tmpAlt.getDatoAltura()
                break'''
    print("El mensaje obtenido es: ")

        #necesito recorrer par saber si en las instrucciones se encuentra el primer dron y las instrucciones que ejecutara

    def comprobarLista(self,nombreDron,ListaInstrucciones):

        DronEnInstruccion = False

        for i in range(ListaInstrucciones.getSize()):
            tmp = ListaInstrucciones.buscarID(i)
            if tmp is not None:

                tmpA = tmp.getDron()
                if nombreDron == tmpA:
                    DronEnInstruccion = True
                else:
                    DronEnInstruccion = False
        return DronEnInstruccion

    def comprobacion(self,nombreDron,ListaInstrucciones):
        StillDron = False
        index = 0
        lstI = ListaInstrucciones.getInicio()
        for i in range(ListaInstrucciones.getSize()):
            lstI.getDato().getDron()
            print(lstI.getDato().getDron())
            if lstI.getDato().getDron() == nombreDron:
                index = i
                print(index)
                StillDron = True
                return StillDron, index
            else:
                StillDron = False
            lstI = lstI.getSiguiente()
        return StillDron


    def RegresarDatosSistema(self,nombreSistemaBuscado):
        sistemaPorBuscar = nombreSistemaBuscado
        ListaSistemas = Sistema

        for i in range(ListaSistemas.getSize()):
            tempLst = ListaSistemas.buscarID(i)
            tempLst.getNombre()
            if sistemaPorBuscar == tempLst.getNombre():
                return tempLst


    def MostrarLstMensaje(self):
        lstMsg = Mesag

        for i in range(lstMsg.getSize()):
            nm = lstMsg.buscarID(i)
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
        self.graficacion(sistema)


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

    def graficacion(self,listaSistemas):
        sistema = listaSistemas
        g = graphviz.Digraph('G',filename="SistemasDrones")
        g.format = "jpg"
        for i in range(sistema.getSize()):
            actualS = sistema.buscarID(i)
            g.node(str(actualS.getNombre()))
        g.render()

    def crearG(self,listaSistema):

        sistema = listaSistema

        g = graphviz.Digraph()
        g.format = "jpg"


        g.node('tabla', shape='plaintext', label='''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'''
            '''<TR>
                <TD>Prueba</TD> 
                <TD>Prueba</TD>
                <TD>Prueba</TD>
            </TR>
        </TABLE>>''')



        g.render()


    def salida(self):
        lstMensaje = Mesag

        salida = '<?xml version="1.0" encoding="UTF-8"?>\n'
        salida += '<respuesta>\n'
        salida += '\t<listaMensajes>\n'
        for i in range(lstMensaje.getSize()):
            tmpMsg = lstMensaje.buscarID(i)
            salida += f'\t\t<mensaje nombre="{tmpMsg.getNombreM()}">\n'
            salida += f'\t\t\t<sistemaDrones>{tmpMsg.getNombreListaSistemas()}</sistemaDrones>\n'
            salida += f'\t\t\t\t<tiempoOptimo>{None}</tiempoOptimo>\n'
            salida += f'\t\t\t\t<mensajeRecibido>{None}</mensajeRecibido>\n'
            salida += '\t\t\t\t<instrucciones>\n'
            salida += f'\t\t\t\t\t<tiempo valor = {None}>\n'

            salida += '\t\t\t\t\t</tiempo>\n'
            salida += '\t\t\t\t</instrucciones>\n'
            salida += '\t\t</mensaje>\n'
        salida += '\t</listaMensajes>\n'
        salida += '</respuesta>'

        name = tkinter.filedialog.asksaveasfilename(defaultextension=".xml")

        with open(name, "w") as archivo:
            archivo.write(salida)

    def btnMensajes(self):
        print("Apartado de Gestion de Mensajes")


    def btnAyuda(self):
        ventanaAyuda = tk.Toplevel()
        ventanaAyuda.geometry("400x325")
        ventanaAyuda.title("Gestion Drones")
        lblListadoDron = tk.Label(ventanaAyuda, text="Nombre: Daniel Eduardo Velásquez Avila\n Curso: Introducción a la Programación y Computación \n Seccion: N \nCarnet: 202200041 \n CUI: 3596985220101")
        lblListadoDron.place(x=50, y=50)
        txtDoc = tk.Text(ventanaAyuda,height=2,width=40)
        txtDoc.place(x=40,y=150)
        txtDoc.insert(tkinter.END,"https://github.com/DanielVelAv/IPC2_Proyecto2_202200041.git")

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
