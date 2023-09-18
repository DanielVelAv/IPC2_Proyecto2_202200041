import xml.etree.ElementTree as ET
from ListaDoble import ListaDoble
from Dron import *

class LecturaXML():

    def __init__(self,path):
        self.raiz = ET.parse(path).getroot()
        self.ListasD = ListaDoble()

    def getDrones(self):

        Drones = self.ListasD

        for i in self.raiz.findall('listaDrones'):
            drones = ListaDoble()
            for k in i.findall('dron'):
                nuevoDron = Dron(k.text)
                Drones.agregar(nuevoDron)


        Drones.recorrer()





archiv = LecturaXML('C:/Users/dolyaD/Documents/GitHub/IPC2_Proyecto2_202200041/entradaV3.xml')
archiv.getDrones()

