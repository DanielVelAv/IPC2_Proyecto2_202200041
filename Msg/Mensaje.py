
class Mensaje:
    def __init__(self,nombre,ListaSistemas,Instrucciones):
        self.nombre = nombre
        self.NombrelistaSistemas = ListaSistemas
        self.instrucciones = Instrucciones

    def getNombreM(self):
        return self.nombre

    def getNombreListaSistemas(self):
        return self.NombrelistaSistemas

    def getInstrucciones(self):
        return self.instrucciones