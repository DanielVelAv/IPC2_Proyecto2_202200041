
class DronSistema:
    def __init__(self,nombreDron,ListaAlturas):
        self.alturaActual = None
        self.nombreDron = nombreDron
        self.ListaAlturas = ListaAlturas

    def getNombreDron(self):
        return self.nombreDron

    def getListaAlturas(self):
        return self.ListaAlturas

    def getAlturaActual(self):
        return self.alturaActual

    def setAlturaActual(self,alturaActual):
        self.alturaActual = alturaActual