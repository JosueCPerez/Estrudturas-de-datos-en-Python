class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.sig = None

class pila:
    def __init__(self):
        self.tope = None

    def push(self,valorNuevo):
        nuevoNodo = nodo(valorNuevo)

        if(self.tope== None):
            self.tope = nuevoNodo
        else:
            nuevoNodo.sig = self.tope
            self.tope = nuevoNodo

    def pop(self):
        if(self.tope != None):
            pivote = self.tope
            self.tope = self.tope.sig
            print("POP -> "+ str(pivote.dato))
        else:
            print("la pila esta vacia")


nuevaPila = pila()

nuevaPila.push(5)
nuevaPila.push(1)
nuevaPila.push(6)
nuevaPila.push(8)

nuevaPila.pop()
nuevaPila.pop()
nuevaPila.pop()
nuevaPila.pop()
nuevaPila.pop()