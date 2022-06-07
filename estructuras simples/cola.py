class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.sig = None

class cola:
    def __init__(self):
        self.frente = None
    
    def encolar(self, nuevoValor):
        nuevoNodo = nodo(nuevoValor)

        if(self.frente==None):
            self.frente = nuevoNodo
        else:
            pivote = self.frente
            while pivote:
                if(pivote.sig == None):
                    pivote.sig = nuevoNodo
                    break
                pivote = pivote.sig

    def descolar(self):
        if(self.frente != None):
            pivote = self.frente
            self.frente = self.frente.sig
            print("descolar -> "+ str(pivote.dato))
        else:
            print("La cola estavacia")
        

nuevaCola = cola()

nuevaCola.encolar(10)
nuevaCola.encolar(1)
nuevaCola.encolar(6)
nuevaCola.encolar(5)

nuevaCola.descolar()
nuevaCola.descolar()
nuevaCola.descolar()
nuevaCola.descolar()
nuevaCola.descolar()