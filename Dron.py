
class Dron:

    def __init__(self,nombre, Alturas = None):
        self.nombre = nombre
        self.Alturas = Alturas

    def getNombre(self):
        return self.nombre

    def getAlturas(self):
        return self.Alturas