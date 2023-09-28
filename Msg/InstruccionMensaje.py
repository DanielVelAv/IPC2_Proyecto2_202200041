
class InstruccionMensaje:

    def __init__(self,dron,Instruccion):
        self.dron = dron
        self.instruccion = Instruccion

    def getDron(self):
        return self.dron

    def getInstruccionMsg(self):
        return self.instruccion