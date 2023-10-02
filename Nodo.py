class Nodo():
    def __init__(self,id,dato):
        self.id = id
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

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