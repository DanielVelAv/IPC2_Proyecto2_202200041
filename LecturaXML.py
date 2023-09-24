import xml.etree.ElementTree as ET
from ListaDoble import ListaDoble
from Dron import *

class LecturaXML():

    def __init__(self,path):
        self.raiz = ET.parse(path).getroot()
        self.ListasD = ListaDoble()
        self.ListaSistemasDrones = ListaDoble()
        self.ListaMensajes = ListaDoble()

    def getDrones(self):

        Drones = self.ListasD

        for i in self.raiz.findall('listaDrones'):
            drones = ListaDoble()
            for k in i.findall('dron'):
                nuevoDron = Dron(k.text)
                Drones.agregar(nuevoDron)

        Drones.recorrer()

        for j in self.raiz.findall('listaSistemasDrones'):
            print(j)
            for k in j.findall('sistemaDrones'):
                nombre = k.get('nombre')
                print(k," ",nombre)
                for l in k.findall('alturaMaxima'):
                    mH = l.text
                    print("AlturaMaxima"," ",mH)
                for m in k.findall('cantidadDrones'):
                    cD = m.text
                    print("CantidadDrones"," ",cD)
                for o in k.findall('contenido'):
                    print(o)
                    for op in o.findall('dron'):
                        Dn = op.text
                        print("Dron: ",Dn)
                    for opq in o.findall('alturas'):
                        for opqr in opq.findall('altura'):
                            alt = opqr.text
                            valor = opqr.get('valor')
                            print("Valor: ",valor,"Altura: ",alt)

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

archiv = LecturaXML('C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto2_202200041/entradaV3.xml')
archiv.getDrones()

