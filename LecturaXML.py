import xml.etree.ElementTree as ET
from ListaDoble import ListaDoble
from Dron import *
from ValorListaSistemas import *
from dronSistema import *
from SistemaD import *

class LecturaXML():
    def __init__(self,path):
        self.raiz = ET.parse(path).getroot()
        self.ListasD = ListaDoble()
        self.ListaSistemasDrones = ListaDoble()
        self.ListaMensajes = ListaDoble()
        self.ListaContenidoSistema = ListaDoble()

    def getDrones(self):

        Drones = self.ListasD
        SistemasDrones = self.ListaSistemasDrones

        for i in self.raiz.findall('listaDrones'):
            drones = Drones
            for k in i.findall('dron'):
                nuevoDron = Dron(k.text)
                drones.agregar(nuevoDron)

            drones.recorrer()

        for j in self.raiz.findall('listaSistemasDrones'): #para ingresar a los datos
            for k in j.findall('sistemaDrones'):    #por cada uno de los SistemasDrones guardara
                nombre = k.get('nombre') #obtiene el nombre del sistema
                mH = "" #variables que contendran Altura Maxima
                cD = "" #cantidad Drones
                print("Sistema Drones ",nombre)
                for l in k.findall('alturaMaxima'):
                    mH = l.text
                    print("AlturaMaxima"," ",mH)
                for m in k.findall('cantidadDrones'):
                    cD = m.text
                    print("CantidadDrones"," ",cD)
                ListaContenido = ListaDoble()
                for o in k.findall('contenido'):
                    Dn = "" #aqui hay diferentes valores para el sistema (parecido a dato de senales)
                    for op in o.findall('dron'): #El nombre del dron dentro de sistema drones
                        Dn = op.text
                        print("Dron: ",Dn)
                    valorA = ListaDoble()
                    for opq in o.findall('alturas'):
                        for idk in range(1,int(mH) + 1 ):
                            for opqr in opq.findall('altura'):
                                if int(opqr.attrib['valor']) == idk:
                                    nuevoV = ValorListaSistemas(opqr.get('valor'),opqr.text)
                                    valorA.agregar(nuevoV)
                    dronS = DronSistema(Dn,valorA) #contiene el nombre y la lista de alturas
                    ListaContenido.agregar(dronS)
                    print("prueba Dron",Dn,"contiene nombre y lista de alturas 'ListaContenido guarda'",ListaContenido.getSize())
                #aqui deberia de estar la lista para guardar_todo el sistemaDron
                sistemaDrones = SistemaD(nombre,mH,cD,ListaContenido) #nombre sistema, altura max, cantidad drones
                SistemasDrones.agregar(sistemaDrones)
                print(nombre,mH,cD,SistemasDrones, "Cantidad de SistemaDrones", SistemasDrones.getSize())

        for k in self.raiz.findall('listaMensajes'):
                for kl in k.findall('Mensaje'):
                    msg = kl.get('nombre')
                    print("Mensaje: ",msg)
                    for klm in kl.findall('sistemaDrones'):
                        sistDrones = klm.text
                        print("Sistema Drones:", sistDrones)
                    for klm in kl.findall('instrucciones'):
                        for klmn in klm.findall('instruccion'):
                            dron = klmn.get('dron')
                            drn = klmn.text
                            print("dron: ",dron," instruccion: ",drn)

        #aqui se guardar la lista con las 3 sublistas :3


    def getListaDrones(self):
        return self.ListasD

    def getListaSistemaDrones(self):
        return self.ListaSistemasDrones

'''archiv = LecturaXML('C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto2_202200041/entradaV3.xml')
archiv.getDrones()'''

