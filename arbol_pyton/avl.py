class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.fa=0 #fa = factor de equilibrio
        self.izq = None
        self.der = None

class avl:
    def __init__(self):
        self.raiz = None

    #metodo que devuelve la fa mayor
    def maximo(self, a1,a2):
        if a1>a2:
            return a1
        else:
            return a2

    #metodo que retorna la fa de un nodo
    def factor_equilibrio(self, nodo):
        if nodo:
            return nodo.fa
        else:
            return -1

    #metodos del arbol
    def insertar(self,dato):
        nuevo = nodo(dato)

        if self.raiz == None:
            self.raiz = nuevo
        else:
            self.raiz = self.nodo_insertar(nuevo,self.raiz)

    def nodo_insertar(self,nuevo,raiz_actual):
        if raiz_actual:
            if raiz_actual.dato > nuevo.dato:
                raiz_actual.izq = self.nodo_insertar(nuevo,raiz_actual.izq)
                ##validar fas y ver si necesita rotacion 
                if (self.factor_equilibrio(raiz_actual.der) - self.factor_equilibrio(raiz_actual.izq)==-2):
                    if nuevo.dato < raiz_actual.izq.dato:
                        raiz_actual = self.R_izq(raiz_actual)
                    else:
                        raiz_actual = self.R_izq_der(raiz_actual)

            elif raiz_actual.dato < nuevo.dato:
                raiz_actual.der = self.nodo_insertar(nuevo,raiz_actual.der)
                #validar fac y ver si necesita rotacion
                if(self.factor_equilibrio(raiz_actual.der)- self.factor_equilibrio(raiz_actual.izq) == 2):
                    if nuevo.dato > raiz_actual.der.dato:
                        raiz_actual = self.R_der(raiz_actual)
                    else:
                        raiz_actual = self.R_der_izq(raiz_actual)
                
            #retornamos la raiz_actual con la nueva fa
            print(type(raiz_actual))
            raiz_actual.fa = self.maximo(self.factor_equilibrio(raiz_actual.der),self.factor_equilibrio(raiz_actual.izq)) +1
            return raiz_actual
        else:
            raiz_actual = nuevo
            return raiz_actual


    #ROTACIONES
    def R_izq(self,nodo):
        aux = nodo.izq
        nodo.izq = aux.der
        aux.der = nodo
        nodo.fa = self.maximo(self.factor_equilibrio(nodo.der),self.factor_equilibrio(nodo.izq))+1
        aux.fa = self.maximo(self.factor_equilibrio(aux.der),nodo.fa)+1
        return aux

    def R_der(self, nodo):
        aux = nodo.der
        nodo.der = aux.izq
        aux.izq = nodo
        nodo.fa = self.maximo(self.factor_equilibrio(nodo.der),self.factor_equilibrio(nodo.izq))+1
        aux.fa = self.maximo(self.factor_equilibrio(aux.der), nodo.fa)+1
        return aux

    def R_izq_der(self, nodo):
        nodo.izq = self.R_der(nodo.izq)
        aux = self.R_izq(nodo)
        return aux

    def R_der_izq(self,nodo):
        nodo.der = self.R_izq(nodo.der)
        aux = self.R_der(nodo)
        return aux



    def inorden(self,raiz_actual):
        if raiz_actual:
            self.inorden(raiz_actual.izq)
            print(raiz_actual.dato)
            self.inorden(raiz_actual.der)

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

    def listar(self, raiz_actual):
        if raiz_actual:
            cadena = "n"+str(raiz_actual.dato)+"[label= \""+str(raiz_actual.dato)+" \n FA:"+str(raiz_actual.fa)+"\"];\n"
            cadena += self.listar(raiz_actual.izq)
            cadena += self.listar(raiz_actual.der)
            return cadena
        else:
            return ""
    
    def enlazar(self,raiz_actual):
        cadena =""
        if raiz_actual:
            if raiz_actual.izq:
                cadena+= "n"+str(raiz_actual.dato)+" -> n"+str(raiz_actual.izq.dato)+"\n"
            if raiz_actual.der:
                cadena+= "n"+str(raiz_actual.dato)+" -> n"+str(raiz_actual.der.dato)+"\n"

            cadena += self.enlazar(raiz_actual.izq)
            cadena += self.enlazar(raiz_actual.der)
        
        return cadena

arbol_avl = avl()

arbol_avl.insertar(1)
arbol_avl.insertar(3)
arbol_avl.insertar(2)

arbol_avl.inorden(arbol_avl.raiz)
arbol_avl.graficar()