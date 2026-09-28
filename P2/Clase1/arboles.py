class Nodo:
    def __init__(self):
        self.info = 0
        self.izq = None
        self.der = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.valores = []

    def insertar(self, info):
        nuevo = Nodo()
        nuevo.info = info
        nuevo.izq = None
        nuevo.der = None

        if self.raiz is None:
            self.raiz = nuevo
            self.valores.append(info)
            return

        actual = self.raiz
        anterior = None

        while actual is not None:
            anterior = actual

            if info < actual.info:
                actual = actual.izq
            elif info > actual.info:
                actual = actual.der
            else:
                return

        if info < anterior.info:
            anterior.izq = nuevo
        else:
            anterior.der = nuevo

        self.valores.append(info)

    def imprimir(self):
        for valor in self.valores:
            print(valor, end=" ")

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.info, end=" ")
            self.preorden(nodo.izq)
            self.preorden(nodo.der)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izq)
            print(nodo.info, end=" ")
            self.inorden(nodo.der)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.info, end=" ")


arbol = ArbolBinario()

arbol.insertar(14)
arbol.insertar(15)
arbol.insertar(4)
arbol.insertar(9)
arbol.insertar(7)
arbol.insertar(18)
arbol.insertar(3)
arbol.insertar(5)
arbol.insertar(16)
arbol.insertar(4)
arbol.insertar(20)
arbol.insertar(17)
arbol.insertar(9)
arbol.insertar(14)
arbol.insertar(5)

print("Árbol:")
arbol.imprimir()

print("\nPreorden:")
arbol.preorden(arbol.raiz)

print("\nInorden:")
arbol.inorden(arbol.raiz)

print("\nPostorden:")
arbol.postorden(arbol.raiz)