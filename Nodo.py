class Nodo():
    def __init__(self,dato = None,siguiente = None,anterior = None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

    def getDato(self):
        return self.dato

    def getSiguiente(self):
        return self.siguiente

    def getAnterior(self):
        return self.anterior


    def setDato(self,dato):
        self.dato = dato

    def setSiguiente(self,siguiente):
        self.siguiente = siguiente

    def setAnterior(self,anterior):
        self.anterior = anterior