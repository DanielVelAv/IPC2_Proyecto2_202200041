import tkinter as tk
import tkinter.font as tkFont

#hola aux :)
class Menu:
    def __init__(self, root):
        root.title("Menu Principal")
        width=600
        height=500
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
        btnInicializar.place(x=190,y=90,width=216,height=30)
        btnInicializar["command"] = self.btnInicializar

        btnCarga=tk.Button(root)
        btnCarga["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnCarga["font"] = ft
        btnCarga["fg"] = "#000000"
        btnCarga["justify"] = "center"
        btnCarga["text"] = "Cargar Archivo XML"
        btnCarga.place(x=190,y=130,width=216,height=30)
        btnCarga["command"] = self.btnCarga

        btnGenerar=tk.Button(root)
        btnGenerar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnGenerar["font"] = ft
        btnGenerar["fg"] = "#000000"
        btnGenerar["justify"] = "center"
        btnGenerar["text"] = "Generar archivo XML"
        btnGenerar.place(x=190,y=170,width=217,height=30)
        btnGenerar["command"] = self.btnGenerar

        btnGestionD=tk.Button(root)
        btnGestionD["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnGestionD["font"] = ft
        btnGestionD["fg"] = "#000000"
        btnGestionD["justify"] = "center"
        btnGestionD["text"] = "Gestión de drones"
        btnGestionD.place(x=190,y=210,width=215,height=30)
        btnGestionD["command"] = self.btnGestionD

        btnGestionS=tk.Button(root)
        btnGestionS["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnGestionS["font"] = ft
        btnGestionS["fg"] = "#000000"
        btnGestionS["justify"] = "center"
        btnGestionS["text"] = "Gestion de Sistemas de Drones"
        btnGestionS.place(x=190,y=250,width=215,height=30)
        btnGestionS["command"] = self.btnGestionS

        btnMensajes=tk.Button(root)
        btnMensajes["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnMensajes["font"] = ft
        btnMensajes["fg"] = "#000000"
        btnMensajes["justify"] = "center"
        btnMensajes["text"] = "Gestión de Mensajes"
        btnMensajes.place(x=190,y=290,width=215,height=30)
        btnMensajes["command"] = self.btnMensajes

        btnAyuda=tk.Button(root)
        btnAyuda["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnAyuda["font"] = ft
        btnAyuda["fg"] = "#000000"
        btnAyuda["justify"] = "center"
        btnAyuda["text"] = "Ayuda"
        btnAyuda.place(x=190,y=330,width=214,height=30)
        btnAyuda["command"] = self.btnAyuda

        lblMenu=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        lblMenu["font"] = ft
        lblMenu["fg"] = "#333333"
        lblMenu["justify"] = "center"
        lblMenu["text"] = "Menu Principal"
        lblMenu.place(x=200,y=30,width=199,height=35)

    def btnInicializar(self):
        print("Apartado de incicializacion")


    def btnCarga(self):
        print("Carga de Archivos")


    def btnGenerar(self):
        print("Apartado de generar")


    def btnGestionD(self):
        print("Apartado Gestion Drones")


    def btnGestionS(self):
        print("Apartado Gestion Sistema de drones")


    def btnMensajes(self):
        print("Apartado de Gestion de Mensajes")


    def btnAyuda(self):
        print("Apartado ayuda")

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
