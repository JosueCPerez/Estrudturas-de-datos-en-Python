class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.izq = None
        self.der = None

class arbol:
    def __init__(self):
         self.raiz = None

    #metodos sobre el arbol

    def insertar(self, dato):
        nuevo = nodo(dato)
        if(self.raiz == None):
            self.raiz = nuevo
        else:
           self.raiz = self.insertar_nodo(nuevo,self.raiz)
    
    def insertar_nodo(self,nuevo_nodo,raiz):
        if raiz != None:
            if raiz.dato > nuevo_nodo.dato:
                raiz.izq = self.insertar_nodo(nuevo_nodo,raiz.izq)
                return raiz
            elif raiz.dato < nuevo_nodo.dato:
                raiz.der = self.insertar_nodo(nuevo_nodo,raiz.der)
                return raiz
        else:
            raiz = nuevo_nodo
            return raiz
        
    def preorden(self,raiz):
        if raiz:
            print(raiz.dato)
            self.preorden(raiz.izq)
            self.preorden(raiz.der)

    def inorden(self,raiz):
        if raiz:
            self.preorden(raiz.izq)
            print(raiz.dato)
            self.preorden(raiz.der)


    def graficar(self):
        cadena = "digraph arbol {\n"
        if(self.raiz != None):
            cadena += self.listar(self.raiz)
            cadena += "\n"
            cadena += self.enlazar(self.raiz)
        cadena += "}"
        Archivo = open("ejemplo.dot","w+")
        Archivo.write(cadena)
        Archivo.close()

    def listar(self, raiz):
        if(raiz != None):
            cadena = "n" +str(raiz.dato)+ " [label = \"" + str(raiz.dato) + "\"];\n"
            cadena += self.listar(raiz.izq)
            cadena += self.listar(raiz.der)
            return cadena
        return ""
    
    def enlazar(self,raiz):
        cadena=""
        if raiz:
            if raiz.izq:
                cadena+="n"+str(raiz.dato)+"-> n"+str(raiz.izq.dato)+"\n"
            if raiz.der:
                cadena+="n"+str(raiz.dato)+"-> n"+str(raiz.der.dato)+"\n"

            cadena += self.enlazar(raiz.izq)
            cadena += self.enlazar(raiz.der)
            return cadena
        
        return cadena


#main 
nuevo = arbol()
nuevo.insertar(5)
nuevo.insertar(10)
nuevo.insertar(2)
nuevo.insertar(20)
nuevo.insertar(12)
nuevo.insertar(9)

#print(nuevo.raiz.dato)
print("#### recorrido preorden")
nuevo.preorden(nuevo.raiz)
print("#### recorrido inorden")
nuevo.inorden(nuevo.raiz)

nuevo.graficar()