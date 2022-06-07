class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.sig = None

class lista:
    def __init__(self):
        self.primero = None

    def insertar(self,valor):
        nuevo = nodo(valor)

        if(self.primero == None):
            self.primero = nuevo
        else:
            aux = self.primero
            while aux:
                if(aux.sig ==None):
                    aux.sig = nuevo
                    break
                aux = aux.sig
        
    def imprimir(self):
        aux = self.primero
        while(aux):
            print(aux.dato)
            aux = aux.sig


lista_simple = lista()
lista_simple.insertar(5)
lista_simple.insertar(7)
lista_simple.insertar(2)
lista_simple.insertar(1)
lista_simple.imprimir()
