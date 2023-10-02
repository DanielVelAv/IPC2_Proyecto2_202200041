
class Config:
    def __init__(self,listaDrones, ListaSistemas,ListaMensajes):
        self.listaDrones = listaDrones
        self.ListaSistemas = ListaSistemas
        self.ListaMensajes = ListaMensajes

    def getListaDrones(self):
        return self.listaDrones

    def getListaSistemas(self):
        return self.ListaSistemas

    def getListaMensajes(self):
        return self.ListaMensajes