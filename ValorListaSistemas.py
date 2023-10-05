
class ValorListaSistemas:
    def __init__(self, NValor, datoAltura = None):
        self.NValor = NValor
        self.datoAltura = datoAltura

    def getNValor(self):
        return self.NValor

    def getDatoAltura(self):
        return self.datoAltura


class TiempoLuz():
    def __init__(self,dron,estado,tiempoLuz):
        self.dron = dron
        self.estado = estado
        self.tiempoLuz = tiempoLuz

    def getDron(self):
        return self.dron

    def estado(self):
        return self.altura

    def tiempoLuz(self):
        return self.tiempoLuz()