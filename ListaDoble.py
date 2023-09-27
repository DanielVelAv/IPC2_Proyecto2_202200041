from Nodo import Nodo

class ListaDoble():
    id = 0
    def __init__(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

    def getInicio(self):
        return self.nodoInicio

    def getSize(self):
        return self.size

    def estaVacia(self):
        return self.nodoInicio == None

    def agregar(self,dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            nuevo.setAnterior(self.nodoFinal)
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size += 1

    def recorrer(self):
        if self.nodoInicio is None:
            return
        actual = self.nodoInicio
        print("Nombre_Dron",actual.dato.nombre)
        while actual.siguiente:
            actual = actual.siguiente
            print("Nombre_Dron",actual.dato.nombre)

    def buscar(self, dato):
        actual = self.nodoInicio
        anterior = None
        no_encontrado = False

        while actual and actual.dato.nombre != dato:
            anterior = actual
            actual = actual.siguiente

            if actual == self.nodoInicio:
                no_encontrado = True
                print("No encontrado")
            break

        if not no_encontrado:
            print("nombre",actual.dato.nombre)

    def buscarID(self, dato):
        tmp = self.nodoInicio
        while tmp:
            if tmp.getId() == dato:
                return tmp.getDato()
            tmp = tmp.getSiguiente()
        return None

